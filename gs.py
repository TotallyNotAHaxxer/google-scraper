import os
import time 
import colorama 
import GoogleNews
from GoogleNews import GoogleNews
from colorama import Fore

os.system(' clear ')
print(" ENJOY :D !!!!! ")
time.sleep(1)
os.system(' clear ')
time.sleep(0.1)
print(Fore.CYAN+"`mMMMMMMMMMMMNmmdhy-")
time.sleep(0.1)
print(Fore.CYAN+" dMMMMMMMMMMMMMMMMMMs`")
time.sleep(0.1)
print(Fore.CYAN+" +MMsohNMMMMMMMMMMMMMm/")
time.sleep(0.1)
print(Fore.CYAN+" .My   .+dMMMMMMMMMMMMMh.")
time.sleep(0.1)
print(Fore.CYAN+"  +       :NMMMMMMMMMMMMNo")
time.sleep(0.1)
print(Fore.CYAN+"           `yMMMMMMMMMMMMMm:")
time.sleep(0.1)
print(Fore.CYAN+"             /NMMMMMMMMMMMMMy`")
time.sleep(0.1)
print(Fore.CYAN+"              .hMMMMMMMMMMMMMN+")
time.sleep(0.1)
print(Fore.CYAN+"                  ``-NMMMMMMMMMd-")
time.sleep(0.1)
print(Fore.CYAN+"                     /MMMMMMMMMMMs`")
time.sleep(0.1)
print(Fore.CYAN+"                      mMMMMMMMsyNMN/")
time.sleep(0.1)
print(Fore.CYAN+"                      +MMMMMMMo  :sNh.")
time.sleep(0.1)
print(Fore.CYAN+"                      `NMMMMMMm     -o/")
time.sleep(0.1)
print(Fore.CYAN+"                       oMMMMMMM.")
time.sleep(0.1)
print(Fore.CYAN+"                       `NMMMMMM+")
time.sleep(0.1)
print(Fore.CYAN+"                        +MMd/NMh")
time.sleep(0.1)
print(Fore.CYAN+"                         mMm -mN`")
time.sleep(0.1)
print(Fore.CYAN+"                         /MM  `h:")
time.sleep(0.1)
print(Fore.CYAN+"                          dM`   .")
time.sleep(0.1)
print(Fore.CYAN+"                          :M-")
time.sleep(0.1)
print(Fore.CYAN+"                           d:")
time.sleep(0.1)
print(Fore.CYAN+"                           -+")
time.sleep(0.1)
print(Fore.CYAN+"                            -")
time.sleep(0.1)
print(Fore.CYAN+" ==================SCRAPING NEWS=================== ")
googlenews = GoogleNews()
googlenews = GoogleNews(period='7d')
googlenews.search('USA')
result=googlenews.result()
for x in result:
   print("-"*50)
   print("Title--", x['title'])
   print("Date/Time--", x['date'])
   print("Description--", x['desc'])
   print("Link--", x['link'])
