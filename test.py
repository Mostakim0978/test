import pyfiglet
import colorama
import requests
import base64
import os
import time
if os.name == 'nt':
    pass
os.system('clear')
os.system(f'''echo \'{pyfiglet.figlet_format('Tkkytrs', 'slant')}\'|lolcat''')

def timm():
    return time.strftime('%H:%M:%S')

dat3 = input(colorama.Fore.RED + '[ ' + colorama.Fore.GREEN + timm() + colorama.Fore.RED + ' ]' + colorama.Fore.WHITE + ' ENTER YOUR Authorization: ')
headers = {
    'Origin': 'https://api.hamsterkombat.io/',
    'Referer': 'https://api.hamsterkombat.io/clicker/',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    'authorization': dat3 }
body = '{"count":2000,"availableTaps":2475,"timestamp":' + str(int(time.time())) + '}'
png = requests.post('https://api.hamsterkombat.io/clicker/tap', headers = headers, data = body)
if str(png.status_code) == '200':
    os.system(f''' echo "\n• [ {timm()} ] Request To Add All Balance Successful\n• User Account: {dat3.lower().split('bearer')}\n• Encoded Data: {png.text[:15]}...\n• By: @Tkkytrsp \n[¡] Sleeping For 15 Minute" | lolcat\n        ''')
    time.sleep(10)
print(colorama.Fore.RED + f'''[ {timm()} ] Request Failed With Status {str(png.status_code)}''')