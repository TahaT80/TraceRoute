"""
        API count exceeded - Increase Quota with Membership
        If you encounter an error (API count exceeded - Increase Quota with Membership)   you need a VPN
        creat by Amir Hossein Tadas & TAHA
"""
import sys
import requests
from colorama import Fore
import os
def __start__():
        try:
                
                print(Fore.RED+" [!] Plase Enter Domain")
                print(Fore.RED+"\n [!] for exampel : test.com\n")
                inp = input(Fore.RED+" ┌─["+Fore.LIGHTGREEN_EX+"tahat80"+Fore.BLUE+"~"+Fore.WHITE+"@TraceRoute"+Fore.RED+"""]
 └──╼ """+Fore.WHITE+"卐 ")
                result = requests.get('https://api.hackertarget.com/mtr/?q=' + inp).text
                print(result)
                try:
                        input(Fore.RED+" [!] "+Fore.GREEN+"Back To again (Press Enter...) ")
                except:
                        print("")
                        sys.exit()  
        except:
                print("\nExit :)")
                
        
if __name__ == '__main__':
    while True:
        try:
            os.system('cls')
        except:
            os.system('clear')

        __start__()