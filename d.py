import os
import binascii
import gzip
from Crypto.Cipher import AES
from MedoEncTT import MedoEnc
try:
   import http.client;import requests;from types import SimpleNamespace;import json;from faker import Faker ;import random;import pycountry;import random;import mechanize;from bs4 import BeautifulSoup;from user_agent import generate_user_agent;from threading import *;import http.client,datetime,re ;from urllib.parse import urlencode;import time;from uuid import uuid4 ;import gzip,re;import io;import os;import requests;import base64;from uuid import uuid4;import random;from ms4 import InfoIG, RestInsta;import requests;import time;import hashlib;import uuid;import json;from secrets import token_hex;from ms4 import Instagram;import pycountry;import random;import mechanize;from bs4 import BeautifulSoup;from user_agent import generate_user_agent;import string;import json;from ms4 import UserAgentGenerator;import requests;import base64;from uuid import uuid4;import random;from ms4 import InfoIG, RestInsta;import requests;import time;import hashlib;import uuid;from secrets import token_hex;import pycountry;import random;import mechanize;from bs4 import BeautifulSoup;from user_agent import generate_user_agent;import threading;import requests;import random;import requests;import os;import uuid;from secrets import token_hex;import time;from user_agent import generate_user_agent  ;from ms4 import Instagram;from requests import get,post;from random import choice,randrange;import os,sys,uuid;import http.client;import requests;import re, uuid;import time;from time import sleep,time;from user_agent import generate_user_agent;from random import choice,randrange;from requests import get;import urllib.parse;import multiprocessing;import re;import random;import os,requests,sys,time,datetime;from MedoSigner import Argus,Gorgon, md5,Ladon
except:
   os.system("pip install ms4 mechanize bs4 uuid requests faker user_agent pycountry MedoSigner pycryptodome")
   import http.client;import requests;from types import SimpleNamespace;import json;from faker import Faker ;import random;import pycountry;import random;import mechanize;from bs4 import BeautifulSoup;from user_agent import generate_user_agent;from threading import *;import http.client,datetime,re ;from urllib.parse import urlencode;import time;from uuid import uuid4 ;import gzip,re;import io;import os;import requests;import base64;from uuid import uuid4;import random;from ms4 import InfoIG, RestInsta;import requests;import time;import hashlib;import uuid;import json;from secrets import token_hex;from ms4 import Instagram;import pycountry;import random;import mechanize;from bs4 import BeautifulSoup;from user_agent import generate_user_agent;import string;import json;from ms4 import UserAgentGenerator;import requests;import base64;from uuid import uuid4;import random;from ms4 import InfoIG, RestInsta;import requests;import time;import hashlib;import uuid;from secrets import token_hex;import pycountry;import random;import mechanize;from bs4 import BeautifulSoup;from user_agent import generate_user_agent;import threading;import requests;import random;import requests;import os;import uuid;from secrets import token_hex;import time;from user_agent import generate_user_agent  ;from ms4 import Instagram;from requests import get,post;from random import choice,randrange;import os,sys,uuid;import http.client;import requests;import re, uuid;import time;from time import sleep,time;from user_agent import generate_user_agent;from random import choice,randrange;from requests import get;import urllib.parse;import multiprocessing;import re;import random;import os,requests,sys,time,datetime;from MedoSigner import Argus,Gorgon, md5,Ladon
def sign(params, payload: str = None, sec_device_id: str = "", cookie: str or None = None, aid: int = 1233, license_id: int = 1611921764, sdk_version_str: str = "2.3.1.i18n", sdk_version: int =2, platform: int = 19, unix: int = None):
        x_ss_stub = md5(payload.encode('utf-8')).hexdigest() if payload != None else None
        data=payload
        if not unix: unix = int(time.time())
        return Gorgon(params, unix, payload, cookie).get_value() | { "x-ladon"   : Ladon.encrypt(unix, license_id, aid),"x-argus"   : Argus.get_sign(params, x_ss_stub, unix,platform        = platform,aid             = aid,license_id      = license_id,sec_device_id   = sec_device_id,sdk_version     = sdk_version_str, sdk_version_int = sdk_version)}
devices={"is_activated": True, "install_id": "7229653126709135110", "device_id": "7229652427230873093", "new_user": True, "cookie": "store-idc=maliva;store-country-code=er;store-country-code-src=did;install_id=7229653126709135110;ttreq=1$473cbda6f6482e61f74ce5f2cb61a4d037487182;", "device_info": {"iid": "7229653126709135110", "device_id": "7229652427230873093", "version_code": "290304", "os_version": "9", "app_name": "musical_ly", "channel": "googleplay", "device_platform": "android", "aid": "1233", "cdid": "ccc594ba-231b-8a1a-5afc-e39f3aa2037b", "openudid": "94f1b4c545635c10", "device_type": "sm-g991b", "device_brand": "samsung", "os_api": 27, "dpi": 240, "ssmix": "a", "region": "ER", "carrier_region": "ER", "op_region": "ER", "sys_region": "ER", "app_language": "en", "locale": "en", "language": "en", "timezone_offset": 43200, "manifest_version_code": "290304", "update_version_code": "290304", "version_name": "29.3.4", "ab_version": "29.3.4", "build_number": "29.3.4", "ac2": "wifi", "ac": "wifi", "resolution": "1080*1920"}}
ddv = (devices)
device_info = ddv["device_info"]
device_id = ddv["device_id"]
install_id = ddv["install_id"]
cdid = device_info["cdid"]
openudid = device_info["openudid"]
device_brand = device_info["device_brand"]
device_type = device_info["device_type"]
url = "https://deviceinfohw.ru/devices/uploads.php"
params = {  'platform': "PLATFORM",  'cpu': "CPU",  'brand': "BRAND",  'filter_key': "KEY",  'filter': device_type,  'submit': ""}
headers = {  'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36",  'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",  'sec-ch-ua': "\"Not-A.Brand\";v=\"99\", \"Chromium\";v=\"124\"",  'sec-ch-ua-mobile': "?1",  'sec-ch-ua-platform': "\"Android\"",  'upgrade-insecure-requests': "1",  'sec-fetch-site': "same-origin",  'sec-fetch-mode': "navigate",  'sec-fetch-user': "?1",  'sec-fetch-dest': "document",  'accept-language': "ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7"}
response = requests.get(url, params=params, headers=headers)
xxxlxx = response.text.split("<td>")[1].split(",")[0]
email = input("Enter Email : ")
m=sign(params=f"iid={install_id}&device_id={device_id}&tt_data=a&ac=WIFI&channel=googleplay&aid=1233&app_name=musical_ly&version_code=360505&version_name=36.5.5&device_platform=android&os=android&ab_version=36.5.5&ssmix=a&device_type={device_type}&device_brand={device_brand}&language=ar&os_api=34&os_version=14&openudid={openudid}&manifest_version_code=2023605050&resolution=1440%2A2969&dpi=532&update_version_code=2023605050&_rticket=1728874754703&is_pad=0&app_type=normal&sys_region=AE&last_install_time=1728874754&mcc_mnc=41820&timezone_name=Asia%2FBaghdad&carrier_region_v2=418&app_language=ar&carrier_region=IQ&ac2=wifi&uoo=0&op_region=IQ&timezone_offset=10800&build_number=36.5.5&host_abi=arm64-v8a&locale=ar&region=AE&ts=1728874754&cdid={cdid}&cronet_version=1c651b66_2024-08-30&ttnet_version=4.2.195.8-tiktok&use_store_region_cookie=1",payload="",cookie="")
conn = http.client.HTTPSConnection("log-boot.tiktokv.com")
tt_encrypt = MedoEnc()
data_to_encrypt = r'{"magic_tag":"ss_app_log","header":{"display_name":"TikTok","update_version_code":2023605050,"manifest_version_code":2023605050,"app_version_minor":"","aid":1233,"channel":"googleplay","package":"com.zhiliaoapp.musically","app_version":"36.5.5","version_code":360505,"sdk_version":"3.10.3-tiktok.1","sdk_target_version":29,"git_hash":"78b0c0b","os":"Android","os_version":"14","os_api":34,"device_model":"'+device_type+r'","device_brand":"'+device_brand+r'","device_manufacturer":"'+device_brand+r'","cpu_abi":"arm64-v8a","release_build":"a9dd7a3_20240919","density_dpi":532,"display_density":"mdpi","resolution":"2969x1440","language":"ar","timezone":3,"access":"wifi","not_request_sender":1,"carrier":"Zain 4.5G+","mcc_mnc":"41820","rom":"S928BXXS3AXHD","rom_version":"UP1A.231005.007.S928BXXS3AXHD","cdid":"'+cdid+r'","sig_hash":"e89b158e4bcf988ebd09eb83f5378e87","gaid_limited":0,"google_aid":"'+str(uuid4())+r'","openudid":"'+openudid+r'","clientudid":"'+str(uuid4())+r'","region":"AE","tz_name":"Asia\/Baghdad","tz_offset":10800,"sim_region":"iq","req_id":"'+str(uuid4())+r'","device_platform":"android","custom":{"is_kids_mode":0,"filter_warn":0,"web_ua":"Dalvik\/2.1.0 (Linux; U; Android 14; '+device_type+r' Build\/UP1A.231005.007)","is_foldable":0,"user_period":0,"screen_height_dp":938,"user_mode":-1,"priority_region":"IQ","apk_last_update_time":1728501287049,"screen_width_dp":433,"dark_mode_setting_value":1},"apk_first_install_time":'+str(int(time.time()))+r',"is_system_app":0,"sdk_flavor":"global","guest_mode":0},"_gen_time":'+str(int(time.time()))+r'}'
encrypted_data = tt_encrypt.encrypt(data_to_encrypt)
#print(bytes.fromhex(encrypted_data))
payload =bytes.fromhex(encrypted_data)# open("device_register","rb").read()
headers = {
  'User-Agent': "com.zhiliaoapp.musically/2023605050 (Linux; U; Android 14; ar_AE; "+device_type+"; Build/UP1A.231005.007; Cronet/TTNetVersion:1c651b66 2024-08-30 QuicVersion:182d68c8 2024-05-28)",
  'content-type': "application/octet-stream;tt-data=a",
  'x-argus': m["x-argus"],  'x-gorgon':m["x-gorgon"],'x-khronos': m["x-khronos"],'x-ladon':m["x-ladon"],
}
conn.request("POST", "/service/2/device_register/?tt_data=a&ac=WIFI&channel=googleplay&aid=1233&app_name=musical_ly&version_code=360505&version_name=36.5.5&device_platform=android&os=android&ab_version=36.5.5&ssmix=a&device_type={device_type}&device_brand={device_brand}&language=ar&os_api=34&os_version=14&openudid={openudid}&manifest_version_code=2023605050&resolution=1440%2A2969&dpi=532&update_version_code=2023605050&_rticket=1728874754703&is_pad=0&app_type=normal&sys_region=AE&last_install_time=1728874754&mcc_mnc=41820&timezone_name=Asia%2FBaghdad&carrier_region_v2=418&app_language=ar&carrier_region=IQ&ac2=wifi&uoo=0&op_region=IQ&timezone_offset=10800&build_number=36.5.5&host_abi=arm64-v8a&locale=ar&region=AE&ts=1728874754&cdid={cdid}&cronet_version=1c651b66_2024-08-30&ttnet_version=4.2.195.8-tiktok&use_store_region_cookie=1", payload, headers)
res = conn.getresponse()
data = res.read()
cookies = res.getheader('Set-Cookie')
dev = json.loads(data.decode("utf-8"))
install_id=dev["install_id"]
device_id=dev["device_id"]
print(install_id)
print(device_id)
m=sign(params=f"iid={install_id}&device_id={device_id}&ac=WIFI&channel=googleplay&aid=1233&app_name=musical_ly&version_code=360505&version_name=36.5.5&device_platform=android&os=android&ab_version=36.5.5&ssmix=a&device_type={device_type}&device_brand={device_brand}&language=ar&os_api=34&os_version=14&openudid={openudid}&manifest_version_code=2023605050&resolution=1440%2A2969&dpi=532&update_version_code=2023605050&_rticket=1728863462034&is_pad=0&app_type=normal&sys_region=AE&last_install_time=1728863433&mcc_mnc=41820&timezone_name=Asia%2FBaghdad&carrier_region_v2=418&app_language=ar&carrier_region=IQ&ac2=wifi&uoo=0&op_region=IQ&timezone_offset=10800&build_number=36.5.5&host_abi=arm64-v8a&locale=ar&region=AE&ts=1728863461&cdid={cdid}&support_webview=1&reg_store_region=iq&user_selected_region=0&cronet_version=1c651b66_2024-08-30&ttnet_version=4.2.195.8-tiktok&use_store_region_cookie=1",payload="",cookie="")
conn = http.client.HTTPSConnection("api16-normal-c-alisg.tiktokv.com")
payload = "hashed_id=55a5b9f463e3ea3c04100ed7cc17a6895dab675ee3ba5f989b7e6250e8721cb2&type=2"
headers = {
  'User-Agent': "com.zhiliaoapp.musically/2023605050 (Linux; U; Android 14; ar_AE; "+device_type+"; Build/UP1A.231005.007; Cronet/TTNetVersion:1c651b66 2024-08-30 QuicVersion:182d68c8 2024-05-28)",
  'content-type': "application/x-www-form-urlencoded; charset=UTF-8",
  'x-argus': m["x-argus"],  'x-gorgon':m["x-gorgon"],'x-khronos': m["x-khronos"],'x-ladon':m["x-ladon"],
  'Cookie': cookies
}
conn.request("POST", f"/passport/app/region/?iid={install_id}&device_id={device_id}&ac=WIFI&channel=googleplay&aid=1233&app_name=musical_ly&version_code=360505&version_name=36.5.5&device_platform=android&os=android&ab_version=36.5.5&ssmix=a&device_type={device_type}&device_brand={device_brand}&language=ar&os_api=34&os_version=14&openudid={openudid}&manifest_version_code=2023605050&resolution=1440%2A2969&dpi=532&update_version_code=2023605050&_rticket=1728863462034&is_pad=0&app_type=normal&sys_region=AE&last_install_time=1728863433&mcc_mnc=41820&timezone_name=Asia%2FBaghdad&carrier_region_v2=418&app_language=ar&carrier_region=IQ&ac2=wifi&uoo=0&op_region=IQ&timezone_offset=10800&build_number=36.5.5&host_abi=arm64-v8a&locale=ar&region=AE&ts=1728863461&cdid={cdid}&support_webview=1&reg_store_region=iq&user_selected_region=0&cronet_version=1c651b66_2024-08-30&ttnet_version=4.2.195.8-tiktok&use_store_region_cookie=1", payload, headers)
res = conn.getresponse()
data = res.read()
cookies = res.getheader('Set-Cookie')
print(data.decode("utf-8"))
m=sign(params=f"passport-sdk-version=6030790&iid={install_id}&device_id={device_id}&ac=WIFI&channel=googleplay&aid=1233&app_name=musical_ly&version_code=360505&version_name=36.5.5&device_platform=android&os=android&ab_version=36.5.5&ssmix=a&device_type={device_type}&device_brand={device_brand}&language=ar&os_api=34&os_version=14&openudid={openudid}&manifest_version_code=2023605050&resolution=1440%2A2969&dpi=532&update_version_code=2023605050&_rticket=1728863462019&is_pad=0&app_type=normal&sys_region=AE&last_install_time=1728863433&mcc_mnc=41820&timezone_name=Asia%2FBaghdad&carrier_region_v2=418&app_language=ar&carrier_region=IQ&ac2=wifi&uoo=0&op_region=IQ&timezone_offset=10800&build_number=36.5.5&host_abi=arm64-v8a&locale=ar&region=AE&ts=1728863461&cdid={cdid}&support_webview=1&reg_store_region=iq&user_selected_region=0&cronet_version=1c651b66_2024-08-30&ttnet_version=4.2.195.8-tiktok&use_store_region_cookie=1",payload="",cookie="")
conn = http.client.HTTPSConnection("api16-normal-c-alisg.tiktokv.com")
payload = f"account_sdk_source=app&multi_login=1&email={email}&mix_mode=1"
headers = {
  'User-Agent': "com.zhiliaoapp.musically/2023605050 (Linux; U; Android 14; ar_AE; "+device_type+"; Build/UP1A.231005.007; Cronet/TTNetVersion:1c651b66 2024-08-30 QuicVersion:182d68c8 2024-05-28)",
  'content-type': "application/x-www-form-urlencoded; charset=UTF-8",
  'x-argus': m["x-argus"],  'x-gorgon':m["x-gorgon"],'x-khronos': m["x-khronos"],'x-ladon':m["x-ladon"],
  'Cookie': cookies
}
conn.request("POST", f"/passport/user/check_email_registered?passport-sdk-version=6030790&iid={install_id}&device_id={device_id}&ac=WIFI&channel=googleplay&aid=1233&app_name=musical_ly&version_code=360505&version_name=36.5.5&device_platform=android&os=android&ab_version=36.5.5&ssmix=a&device_type={device_type}&device_brand={device_brand}&language=ar&os_api=34&os_version=14&openudid={openudid}&manifest_version_code=2023605050&resolution=1440%2A2969&dpi=532&update_version_code=2023605050&_rticket=1728863481835&is_pad=0&app_type=normal&sys_region=AE&last_install_time=1728863433&mcc_mnc=41820&timezone_name=Asia%2FBaghdad&carrier_region_v2=418&app_language=ar&carrier_region=IQ&ac2=wifi&uoo=0&op_region=IQ&timezone_offset=10800&build_number=36.5.5&host_abi=arm64-v8a&locale=ar&region=AE&ts=1728863481&cdid={cdid}&support_webview=1&reg_store_region=iq&user_selected_region=0&cronet_version=1c651b66_2024-08-30&ttnet_version=4.2.195.8-tiktok&use_store_region_cookie=1", payload, headers)
res = conn.getresponse()
data = res.read()
cookies = res.getheader('Set-Cookie')
print(data.decode("utf-8"))
email = ''.join([hex(int(x ^ 5))[2:] for x in email.encode('utf-8')])
conn = http.client.HTTPSConnection("api16-normal-c-alisg.tiktokv.com")
payload = f"birthday=1998-10-19&rules_version=v2&password=4860616a3c3d3c454545&fixed_mix_mode=1&account_sdk_source=app&mix_mode=1&multi_signup=0&multi_login=1&email={email}"
headers = {
  'User-Agent': "com.zhiliaoapp.musically/2023605050 (Linux; U; Android 14; ar_AE; "+device_type+"; Build/UP1A.231005.007; Cronet/TTNetVersion:1c651b66 2024-08-30 QuicVersion:182d68c8 2024-05-28)",
  'content-type': "application/x-www-form-urlencoded; charset=UTF-8",
    'x-argus': m["x-argus"],  'x-gorgon':m["x-gorgon"],'x-khronos': m["x-khronos"],'x-ladon':m["x-ladon"],
  'Cookie': cookies
}
conn.request("POST", f"/passport/email/register/v2/?passport-sdk-version=6030790&iid={install_id}&device_id={device_id}&ac=WIFI&channel=googleplay&aid=1233&app_name=musical_ly&version_code=360505&version_name=36.5.5&device_platform=android&os=android&ab_version=36.5.5&ssmix=a&device_type={device_type}&device_brand={device_brand}&language=ar&os_api=34&os_version=14&openudid={openudid}&manifest_version_code=2023605050&resolution=1440%2A2969&dpi=532&update_version_code=2023605050&_rticket=1728863481835&is_pad=0&app_type=normal&sys_region=AE&last_install_time=1728863433&mcc_mnc=41820&timezone_name=Asia%2FBaghdad&carrier_region_v2=418&app_language=ar&carrier_region=IQ&ac2=wifi&uoo=0&op_region=IQ&timezone_offset=10800&build_number=36.5.5&host_abi=arm64-v8a&locale=ar&region=AE&ts=1728863481&cdid={cdid}&support_webview=1&reg_store_region=iq&user_selected_region=0&cronet_version=1c651b66_2024-08-30&ttnet_version=4.2.195.8-tiktok&use_store_region_cookie=1", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))
sesion = data.decode("utf-8").split('"session_key":"')[1].split('"')[0]
print(sesion)
with open("sessionid.txt","a") as f:
    f.write(f"{sesion}\n")
