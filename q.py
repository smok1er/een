import os

try:
    import requests
except ImportError:
    os.system("pip install requests")
import requests
from time import sleep
import re

ig_did = ''
csrftoken = ''
sessionid = ''
post_id = ''
done = 0
wait = 0
error = 0
r1 = requests.session()
hashtag = 'sexygay'

def welcome():
    print("""

             _______  _______  _______  _______  _______  _       _________   ______   _______ _________
            (  ____ \(  ___  )(       )(       )(  ____ \( (    /|\__   __/  (  ___ \ (  ___  )\__   __/
            | (    \/| (   ) || () () || () () || (    \/|  \  ( |   ) (     | (   ) )| (   ) |   ) (   
            | |      | |   | || || || || || || || (__    |   \ | |   | |     | (__/ / | |   | |   | |   
            | |      | |   | || |(_)| || |(_)| ||  __)   | (\ \) |   | |@88.bq     |  | |   | |   | |
            | |      | |   | || |   | || |   | || (      | | \   |   | |     | (  \ \ | |   | |   | |   
            | (____/\| (___) || )   ( || )   ( || (____/\| )  \  |   | |     | )___) )| (___) |   | |   
            (_______/(_______)|/     \||/     \|(_______/|/    )_)   )_(     |/ \___/ (_______)   )_(   

    """)
    print("Programmed By #Koky/@88.bq")


welcome()

def close_bot():
    input("Enter To Close..")
    exit(0)


def login():
    global ig_did, csrftoken, sessionid
    username = ("xc26.zp")
    password = ('qqqq1111')
    login_url = 'https://www.instagram.com/accounts/login/ajax/'
    login_headers = {
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.9',
        'content-length': '272',
        'content-type': 'application/x-www-form-urlencoded',
        'cookie': 'ig_did=EDC7FE1B-9EAA-4086-9FB9-CE9CC4891AA1; mid=X7-grwAEAAHIBy6aN0s2Pfinqt78; ig_nrcb=1; shbid=19915; shbts=1607523548.4707706; rur=NAO; csrftoken=Di8FaJuVuyTeahnVvSDanFdNQEJfy7wl; urlgen="{\"142.93.176.154\"',
        'origin': 'https://www.instagram.com',
        'referer': 'https://www.instagram.com/',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36',
        'x-csrftoken': 'Di8FaJuVuyTeahnVvSDanFdNQEJfy7wl',
        'x-ig-app-id': '936619743392459',
        'x-ig-www-claim': 'hmac.AR23xIF4vqkna9vUUPdTH-tcaUhsYyRw5KN7GvmcfVI0SrE0',
        'x-instagram-ajax': '923d197144b7',
        'x-requested-with': 'XMLHttpRequest'
    }
    login_data = {
        'username': f'{username}',
        'enc_password': f'#PWD_INSTAGRAM_BROWSER:10:1607586932:{password}',
        'queryParams': '{}',
        'optIntoOneTap': 'false'
    }
    login_to_acc = r1.post(login_url, data=login_data, headers=login_headers)
    print(login_to_acc.content)
    if login_to_acc.content == b'{"user": false, "authenticated": false, "status": "ok"}':
        print("[!] Check Your Username And Try Again")
        close_bot()
    if login_to_acc.content == b'{"user": true, "authenticated": false, "status": "ok"}':
        print("[!] Check Yo Password And Try Again")
        close_bot()
    if ('{"message": "checkpoint_required"') in login_to_acc.text:
        print("[!] Checkpoint")
        close_bot()
    if 'userId' in login_to_acc.text:
        print("[+] Login Done")
    else:
        print("[!] Check Your Acc And Try Again")
        close_bot()
    ig_did = login_to_acc.cookies['ds_user_id']
    csrftoken = login_to_acc.cookies['csrftoken']
    sessionid = login_to_acc.cookies['sessionid']

login()
url = 'https://www.instagram.com/explore/tags/zxc/?__a=1'
x = r1.get(url).json()
x = x['graphql']['hashtag']['edge_hashtag_to_media']['edges']
v = []
for i in x:
    if len(v) == 10:
        break
    else:
        url1 = f"https://www.instagram.com/web/comments/{i['node']['id']}/add/"
        head1 = {
            'accept': '*/*',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-US,en;q=0.9',
            'content-length': '38',
            'content-type': 'application/x-www-form-urlencoded',
            'cookie': 'ig_did=EDC7FE1B-9EAA-4086-9FB9-CE9CC4891AA1; mid=X7-grwAEAAHIBy6aN0s2Pfinqt78; ig_nrcb=1; ds_user_id=43979535073; csrftoken=w8o85Yg3ZdvumwfPPTbUjX5KCouol1os; sessionid=43979535073%3AFCewAplGNTlIjG%3A17; shbid=19915; shbts=1607523548.4707706; rur=NAO; urlgen="{\"142.93.176.154\"',
            'origin': 'https://www.instagram.com',
            'referer': 'https://www.instagram.com/p/CIk_sHmFPOV/',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36',
            'x-csrftoken': 'w8o85Yg3ZdvumwfPPTbUjX5KCouol1os',
            'x-ig-app-id': '936619743392459',
            'x-ig-www-claim': 'hmac.AR23xIF4vqkna9vUUPdTH-tcaUhsYyRw5KN7GvmcfVI0SrE0',
            'x-instagram-ajax': '7e63b708ea25',
            'x-requested-with': 'XMLHttpRequest'
        }
        data = {
            'comment_text': 'hi',
            'replied_to_comment_id': ''
        }
        r1.post(url = url1, headers=head1, data = data)
        sleep(30)
        url = f"https://www.instagram.com/web/likes/{i['node']['id']}/like/"
        head = {
            'accept': '*/*',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-US,en;q=0.9',
            'content-length': '0',
            'content-type': 'application/x-www-form-urlencoded',
            'cookie': 'ig_did=EDC7FE1B-9EAA-4086-9FB9-CE9CC4891AA1; mid=X7-grwAEAAHIBy6aN0s2Pfinqt78; ig_nrcb=1; ds_user_id=43979535073; csrftoken=w8o85Yg3ZdvumwfPPTbUjX5KCouol1os; sessionid=43979535073%3AFCewAplGNTlIjG%3A17; shbid=19915; shbts=1607523548.4707706; rur=NAO; urlgen="{\"142.93.176.154\": 14061}:1kn0Jy:HBU7WVbyf1Xn9AVcdiUGoEAwcts"',
            'origin': 'https://www.instagram.com',
            'referer': 'https://www.instagram.com/p/CIk_sHmFPOV/',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36',
            'x-csrftoken': 'w8o85Yg3ZdvumwfPPTbUjX5KCouol1os',
            'x-ig-app-id': '936619743392459',
            'x-ig-www-claim': 'hmac.AR23xIF4vqkna9vUUPdTH-tcaUhsYyRw5KN7GvmcfVI0SrE0',
            'x-instagram-ajax': '7e63b708ea25',
            'x-requested-with': 'XMLHttpRequest'
        }
        print(r1.post(url = url, headers=head).text)
        v.append(1)
        sleep(20)
        
    
