import data

def plotdata(stars,pos,count):

	if count==1:
		print("\033[34m    {}   ".format(data.header))
		print("\033[1;37m¯¯¯¯{}¯¯¯¯".format('¯'*len(data.header)),end="\n")
		print('''\033[1;37m{}
\033[1;37m|-----\033[1;32m{} (@{})
\033[1;37m|  |
\033[1;37m|  |--\033[1;32mTotal Repsitories :: \033[1;37m{}
\033[1;37m|  |--\033[1;32mTotal Stars       :: \033[1;37m{}
\033[1;37m|  |--\033[1;32mTotal Followers   :: \033[1;37m{}
\033[1;37m|  |--\033[1;32mTotal Following   :: \033[1;37m{}
\033[1;37m|  |--\033[1;32mUser Email        :: \033[1;37m{}
\033[1;37m|  |--\033[1;32mUser Organization :: \033[1;37m{}
\033[1;37m|  |--\033[1;32mUser Location     :: \033[1;37m{}
\033[1;37m|'''
.format("|",data.name_list[pos],data.username_list[pos],data.repo_list[pos].strip(),data.star_list[pos].strip(),data.followers_list[pos].strip(),data.following_list[pos].strip(),data.email_list[pos].strip(),data.company_list[pos],data.location_list[pos]))


	elif(count>1 and count<=stars):
		print('----',len(data.name_list), len(data.username_list), len(data.repo_list), len(data.star_list), len(data.followers_list),len(data.following_list),len(data.email_list),len(data.company_list),len(data.location_list))
		# print(data.name_list, data.username_list, data.repo_list, data.star_list, data.followers_list,data.following_list,data.email_list,data.company_list,data.location_list)
		print('''\033[1;37m{}
\033[1;37m|-----\033[1;32m{} (@{})
\033[1;37m|  |
\033[1;37m|  |--\033[1;32mTotal Repsitories :: \033[1;37m{}
\033[1;37m|  |--\033[1;32mTotal Stars       :: \033[1;37m{}
\033[1;37m|  |--\033[1;32mTotal Followers   :: \033[1;37m{}
\033[1;37m|  |--\033[1;32mTotal Following   :: \033[1;37m{}
\033[1;37m|  |--\033[1;32mUser Email        :: \033[1;37m{}
\033[1;37m|  |--\033[1;32mUser Organization :: \033[1;37m{}
\033[1;37m|  |--\033[1;32mUser Location     :: \033[1;37m{}
\033[1;37m|'''
.format("|",data.name_list[pos],data.username_list[pos],data.repo_list[pos].strip(),data.star_list[pos].strip(),data.followers_list[pos].strip(),data.following_list[pos].strip(),data.email_list[pos].strip(),data.company_list[pos],data.location_list[pos]))


	elif count==stars:
		print('''\033[1;37m{}
\033[1;37m|-----\033[1;32m{} (@{})
\033[1;37m|  |
\033[1;37m|  |--\033[1;32mTotal Repsitories :: \033[1;37m{}
\033[1;37m|  |--\033[1;32mTotal Stars       :: \033[1;37m{}
\033[1;37m|  |--\033[1;32mTotal Followers   :: \033[1;37m{}
\033[1;37m|  |--\033[1;32mTotal Following   :: \033[1;37m{}
\033[1;37m|  |--\033[1;32mUser Email        :: \033[1;37m{}
\033[1;37m|  |--\033[1;32mUser Organization :: \033[1;37m{}
\033[1;37m|  |--\033[1;32mUser Location     :: \033[1;37m{}
\033[1;37m|'''
.format("|",data.name_list[pos],data.username_list[pos],data.repo_list[pos].strip(),data.star_list[pos].strip(),data.followers_list[pos].strip(),data.following_list[pos].strip(),data.email_list[pos].strip(),data.company_list[pos],data.location_list[pos]))


def save(stars):
	file = data.header + '.csv'
	# if os.path.exists(file):
	# 	os.remove(file)
	with open(file, 'a') as f:
		f.write('name,repo,star,followers,following,email,company,location\n')
		for i in range(stars):
			f.write(str(data.username_list[i]) + ',' +
				str(data.repo_list[i].strip()) + ',' +
				str(data.star_list[i].strip()) + ',' +
				str(data.followers_list[i].strip()) + ',' +
				str(data.following_list[i].strip()) + ',' +
				str(data.email_list[i].strip()) + ',' +
				str(data.company_list[i].replace(',',' ')) + ',' +
				str(data.location_list[i].replace(',',' ')) + '\n')
	print("saved file!")


def save_list(stars,pos,count):
	print('----',len(data.name_list), len(data.username_list), len(data.repo_list), len(data.star_list), len(data.followers_list),len(data.following_list),len(data.email_list),len(data.company_list),len(data.location_list))
	file = data.header + '.csv'
	with open(file, 'a') as f:
		if count==1:
			f.write('name,repo,star,followers,following,email,company,location\n')
		f.write(str(data.username_list[pos]) + ',' +
				str(data.repo_list[pos].strip()) + ',' +
				str(data.star_list[pos].strip()) + ',' +
				str(data.followers_list[pos].strip()) + ',' +
				str(data.following_list[pos].strip()) + ',' +
				str(data.email_list[pos].strip()) + ',' +
				str(data.company_list[pos].replace(',',' ')) + ',' +
				str(data.location_list[pos].replace(',',' ')) + '\n')
	print("saved file:",count)