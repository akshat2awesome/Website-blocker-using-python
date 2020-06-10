#adding websites that we want to block in our list
website_list = ["facebook.com","yahoo.com"]
#start and end date should be in (dddd,m,dd) format
start_date = dt(2020,6,10)
end_date = dt(2020,6,11)
#it will give us todays date
todays_date = dt(dt.now().year,dt.now().month,dt.now().day)

while True:
#condition
    if start_date <= todays_date < end_date:
        with open(hostsPath,'r+') as file:
            content = file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
				#mapping hostnames to localhost IP 
                    file.write(redirect+" "+website+"\n")
                    print("website is blocked")
                    break
    else:
        with open(hostsPath,'r+') as file:
            content=file.readlines()
            file.seek(0)
            for line in content:
                if not any(site in line for website in website_list):
                    file.write(line)
					 #Removing hostnmes from hosts file 
            file.truncate()
        print ("website is unblocked")
    break