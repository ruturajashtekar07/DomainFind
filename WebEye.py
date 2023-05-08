import socket
import requests
import pyfiglet

subDomainName = ['www.','edu.','drive.','mail.','news.','books.','store.','docs.','info.']
mainDomainName = ['.com','.eu','.in','.org','.info','.edu','.net','.biz','.site','.xyz']

print(pyfiglet.figlet_format('WebEye',font='standard'))
print('[i] This is a tool to check the status of every domain of company.')
while True:
    var0 = input('[~] Input(name):> ')
    print('\n[1] Domain','\n[2] Subdomain','\n[3] All type of scan','\n[q] Quit the tool')
    userIn = input('\n[~] Enter the option(Option): ')
    if 'q' == userIn and 'q' in var0 :
        break
    var0 = var0.replace(" ","")
    try:
        userIn = int(userIn)
        if 1 == userIn:
            print("\n[.] this is a main_domain-search...")
            for x in mainDomainName:
                attr = var0 + x 
                s = requests.session()
                try:
                    r = s.get(f'https://www.{attr}')
                    print(f'[ACTIVE] "www.{attr}" is UP! at {socket.gethostbyname(f"www.{attr}")} (CODE = 200)')
                except requests.ConnectionError as e:
                    pass
            print("\n[~] scan done!...")
        elif 2 == userIn:
            print("\n[.] this is a subdomain-search...")
            for i in subDomainName:
                try:
                    attr = i + var0
                    r = requests.get(f'https://{attr}.com')
                    print(f'[ACTIVE]"{attr}.com" is UP! at {socket.gethostbyname(f"{attr}.com")} (CODE = 200)')
                except requests.ConnectionError as e :
                    pass
            print("\n[-] scan done!...")
        elif 3 == userIn:
            print('-'*12)
            print("[^]this is a all type of search")
            print("[>]this is a sub_domain-search...\n")
            for x in mainDomainName:
                attr = var0 + x 
                try:
                    r = requests.get(f'https://www.{attr}')
                    print(f'[ACTIVE] "www.{attr}" is UP! at {socket.gethostbyname(f"www.{attr}")} (CODE = 200)')
                except requests.ConnectionError as e:
                    pass
            print('\n[1] Main-Domain scan done ')
            print("\n[>] this is a main_domain-search...")
            for i in subDomainName:
                attr = i + var0 
                try:
                    r = requests.get(f'https://{attr}.com')
                    print(f'[ACTIVE] "{attr}.com" is UP! at {socket.gethostbyname(f"{attr}.com")} (CODE = 200)')
                except requests.ConnectionError as e :
                    pass
            print('\n [2] Sub-Domain Scan Done')
            print("\n[-] both-scans are done!...")        
        else:
            print("Enter the valid option")
    except Exception as e:
        print('''error : invalid parameters given...
        enter the number''')
print('bye')