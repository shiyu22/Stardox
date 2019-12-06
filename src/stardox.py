# Importing modules
import sys
import colors
import Logo
import argparse
import time

# Getting the name of the repository.
def getting_header(soup_text):
    title=soup_text.title.get_text()
    start=title.find('/')
    stop=title.find(':')
    return title[start+1:stop]

# Function to make sure all the Url passed is made in particualr format.
def format_url(url):
    if url.startswith('http://'):
        url=url.replace('http','https')
    elif url.startswith('www.'):
        url=url.replace('www.','https://')
    elif url.startswith('https://') or url.startswith('https://www.'):
        pass
    else:
        colors.error("Enter the repositories url in given format [ https://github.com/username/repository_name ]")
        sys.exit(1)
    return url

# Function to verify that the page URL given is pointing to some repository or not.
def verify_url(page_data):
    data=str(page_data)
    if "Popular repositories" in data:
        return False
    elif "Page not found" in data:
        return False
    else:
        return True

# Function returning email of the stargazer
def get_latest_commit(repo_name,username):
    email= ""
    commit_data = requests.get("https://github.com/{}/{}/commits?author={}".format(username,repo_name,username)).text
    soup = BeautifulSoup(commit_data,"lxml")
    a_tags = soup.findAll("a")
    for a_tag in a_tags:
        URL = a_tag.get("href")
        if URL.startswith("/{}/{}/commit/".format(username,repo_name)):
            label = str(a_tag.get("aria-label"))
            if "Merge" not in label and label != "None":
                patch_data = requests.get("https://github.com{}{}".format(URL,".patch")).text
                try:
                    start=patch_data.index("<")
                    stop=patch_data.index(">")
                    email = patch_data[start+1:stop]
                except ValueError:
                    return "Not enough information."
                break
    if email != "":
        return email
    else:
        return "Not enough information."

if __name__ == '__main__':
    try:
        Logo.header()         # For Displaying Logo

        parser = argparse.ArgumentParser()
        parser.add_argument('repositoryURL',help = " Path to repository.")
        parser.add_argument('-v','--verbose',help="Verbose",required=False,default=True,action='store_false')
        try:
            import requests
            from bs4 import BeautifulSoup
        except ImportError:
            colors.error('Error importing requests module.')
            sys.exit(1)
        if len(sys.argv) == 1:
            repository_link = input("\033[37mEnter the repository address :: \x1b[0m")    # Getting repository Address
            print("\n")
            verbose = True
        elif len(sys.argv) == 2:
            if sys.argv[1] == '-v':
                repository_link = input("\033[37mEnter the repository address :: \x1b[0m")    # Getting repository Address
                verbose = False
            else:
                args = parser.parse_args()
                repository_link = args.repositoryURL
                verbose = True
        else:
            args = parser.parse_args()
            verbose = args.verbose
            repository_link = args.repositoryURL

        repository_link = format_url(repository_link)       # Assuring that URL starts with https://

        try:
            html = requests.get(repository_link,timeout=8).text       # Getting HTML page of repository
        except:
            colors.error("Enter the repositories url in given format [ https://github.com/username/repository_name ]")
            sys.exit(1)
        result=verify_url(html)                             # Checking if the url given is of a repository or not.
        if result:
            colors.success("Got the repository data ",verbose)
        else:
            colors.error("Please enter the correct URL ")
            sys.exit(0)
        soup1=BeautifulSoup(html,"lxml")                    # Parsing the html data using BeautifulSoup
        try:
            import data
        except ImportError:
            colors.error('Error importing data module')
            sys.exit(1)
        title=getting_header(soup1)                         # Getting the title of the page
        data.header=title                                   # Storing title of the page as Project Title
        colors.success("Repository Title : "+title,verbose)
        star_value = watch_value = fork_value = 0
        a_tags=soup1.findAll("a")                           # Finding all the 'a' tags in response html data.
        for a_tag in a_tags:                                # Finding total stargazers of the repository
            string=a_tag.get("href")
            if(string.endswith("/watchers")):               # Finding total watchers
                watch_value=(a_tag.get_text()).strip()
                colors.success("Total watchers : "+watch_value,verbose)
            if(string.endswith("/stargazers")):             # Finding total stargazers
                star_value=(a_tag.get_text()).strip()
                colors.success("Total stargazers : "+star_value,verbose)
            if(string.endswith("/members")):                # Finding total members
                fork_value=(a_tag.get_text()).strip()
                colors.success("Total Forks : "+fork_value,verbose)
                break
        stargazer_link=repository_link+"/stargazers"
        colors.process("Fetching stargazers list",verbose)
        while (stargazer_link!=None):                                   # Getting list of all the stargazers
            # time.sleep(5)
            # print("stargazer_link_start:", stargazer_link)
            stargazer_html=requests.get(stargazer_link).text
            soup2=BeautifulSoup(stargazer_html,"lxml")
            a_next = soup2.findAll("a")
            for a in a_next:
                # if stargazer_link == 'https://github.com/milvus-io/milvus/stargazers?after=Y3Vyc29yOnYyOpO0MjAxOS0xMS0wNVQwNjoxMzo0MVoAzguFbj4%3D':
                #     print(a.get_text())
                if a.get_text() == 'Contact Support':
                    time.sleep(5)
                    break
                if a.get_text() == "Next":
                    stargazer_link = a.get('href')
                    break
                else:
                    stargazer_link = None
            # print("end-----------------:", stargazer_link)
            follow_names=soup2.findAll("h3",{"class":"follow-list-name"})
            for name in follow_names:
                a_tag=name.findAll("a")
                data.name_list.append(a_tag[0].get_text())
                username=a_tag[0].get("href")
                data.username_list.append(username[1:])
        count=1
        pos=0
        colors.process("Doxing started ...\n",verbose)
        print(colors.red+"{0}".format("-")*75,colors.green,end="\n\n")
        print("len(data):", len(data.username_list))
        while(count<=len(data.username_list)):                                         # Fetching details of stargazers one by one.
            starer_url="https://github.com/"+data.username_list[pos]
            user_html=requests.get(starer_url).text
            soup3=BeautifulSoup(user_html,"lxml")
            repo_data = requests.get("https://github.com/{}?tab=repositories&type=source".format(data.username_list[pos])).text
            repo_soup = BeautifulSoup(repo_data,"lxml")
            a_tags = repo_soup.findAll("a")
            repositories_list = []
            for a_tag in a_tags:
                if a_tag.get("itemprop") == "name codeRepository":
                    repositories_list.append(a_tag.get_text().strip())
            if len(repositories_list) > 0:
                email = get_latest_commit(repositories_list[0],data.username_list[pos])         # Getting email of the stargazer
                data.email_list.append(str(email))
            else:
                data.email_list.append("Not enough information.")
            if(user_html!=None):
                items=soup3.findAll("a",{"class":"UnderlineNav-item"})
                for item in items[1:]:
                    if item.get("href").endswith("repositories")==True:                         # Getting total repositories of the stargazer
                        a_tag=item.findAll("span")
                        repo_count=a_tag[0].get_text()
                        data.repo_list.append(repo_count)
                    elif item.get("href").endswith("stars")==True:                              # Getting total stars by the stargazer
                        a_tag=item.findAll("span")
                        star_count=a_tag[0].get_text()
                        data.star_list.append(star_count)
                    elif item.get("href").endswith("followers")==True:                          # Getting total followers of the stargazers
                        a_tag=item.findAll("span")
                        followers_count=a_tag[0].get_text()
                        data.followers_list.append(followers_count)
                    elif item.get("href").endswith("following")==True:                          # Getting following list of the stargazers
                        a_tag=item.findAll("span")
                        following_count=a_tag[0].get_text()
                        data.following_list.append(following_count)
                try:
                    import structer
                    structer.plotdata(len(data.username_list),pos,count)                                      # Plotting the tree structer of the fetched details
                except ImportError:
                    colors.error("Error importing structer module.")
                    sys.exit(1)
            count+=1
            pos+=1
        print("\n",colors.green+"{0}".format("-")*75,colors.green,end="\n\n")
    except KeyboardInterrupt:
        print("\n\nYou're Great..!\nThanks for using :)")
        sys.exit(0)
