import random , os ,requests
import json
import socket
import urllib.parse
import emoji
import  u_a


urls_BVB="https://indab0x.nl.eu.org/"

vversion="M_M0P  MAC+NO AND CHEAP_VPN-UP * V2"
telegram_tokens_bot=["0","5036803152:AAGs0ES1OmEdy86MNJDp7mp19BB5IQhcVHU","5099462819:AAEndTxvXaSqBQ6E_EpiCN02a81ROGPMgr0","5001651751:AAGzzbUfJXWHZz-FKJyLSUxzg-JiRMO5v-Q","5041058138:AAFRher-cMwnRI476iW24tT6Kt8lvC0bmLc","5051743922:AAEOHJTRzv2WIxZ8bR-VrVYNA6io6qB1Ltw"]
hostname_os=socket.getfqdn()
visible_v=0

if "LOOKE3" in hostname_os:
	print(hostname_os)
	visible_v=1


def get_tokens():
	bot_name=hostname_os_val()
	# print(bot_name)
	tokens=telegram_tokens_bot[5]
	if "1" in bot_name:
		tokens=telegram_tokens_bot[1]
	if "2" in bot_name:
		tokens=telegram_tokens_bot[2]
	if "3" in bot_name:
		tokens=telegram_tokens_bot[3]
	if "4" in bot_name:
		tokens=telegram_tokens_bot[4]
	if "5" in bot_name:
		tokens=telegram_tokens_bot[5]
	print(tokens)
	return tokens


##############################################################################################
# print(str(len(user_agent_list)))

def hostname_os_val():
	hostname_os=socket.getfqdn()
	# print(hostname_os[-1])
	b_v=hostname_os[-1]
	return b_v

############################# VPN ##################################""
pwd = os.path.dirname(os.path.realpath( __file__ ))
p_vpn_g=pwd+"/CHEAP_VPN/"
file_vpn_dead=pwd+"/DEAD_CONFIG_TCP/"
# 	p_vpn_g=pwd+"/N0RD/WORKING_CONFIG/"
p_vpn_dead=pwd+"/N0RD/DEAD_CONFIG_TCP/"
#CHEAP_VPN



vpn_type="N"
total_l0g=[]
# def send_msg(text):

# 	msg_telegram="[ "+hostname_os +" ]"+text
# 	token = "2137513961:AAGENlwIUQnfvbKZX64-fZ72R_oStto8oFo"
# 	chat_id = "-643828126"
# 	url_req = "https://api.telegram.org/bot" + token + "/sendMessage" + "?chat_id=" + chat_id + "&text=" + msg_telegram 
# 	results = requests.get(url_req)
# 	# print(results.json())

def send_msg(text):

	msg_telegram="[ "+hostname_os +" ] [ "+vversion+" ] \n"+text+"\n [ "+urls_BVB+" ]"
	# token = "2137513961:AAGENlwIUQnfvbKZX64-fZ72R_oStto8oFo"
	#-609247805
	token="5086890807:AAEEM2OhQaR9mB7KUZvwkE60mHvoSY4BhOQ"
	# token="5035848854:AAG9a-7bHDYTOXiNEdjXRsnM-gbkdw9TCfE"
	chat_id = "-609247805"
	# chat_id = "-1001616252735"
	url_req = "https://api.telegram.org/bot" + token + "/sendMessage" + "?chat_id=" + chat_id + "&text=" + msg_telegram
	# url_req = "https://api.telegram.org/bot" + token + "/sendMessage" + "?chat_id=" + chat_id + "&text=" + msg_telegram 

	results = requests.get(url_req)
	# print(results.json())

# send_msg("text")


def alias_send_msg(text):
	pol=emoji.emojize(""':man_genie:')
	mp=emoji.emojize(" "'  :dizzy:'+"[ "+hostname_os +" ] "':dizzy:'+" \n"''+pol+"  [ "+vversion+" ] "'')
	msg_telegram=mp+" \n"+pol+" [ "+text+" ] \n "#+pol+" [  ] \n "+pol
	# token = "2137513961:AAGENlwIUQnfvbKZX64-fZ72R_oStto8oFo"
	#-609247805
	token=get_tokens()
	# token="5086890807:AAEEM2OhQaR9mB7KUZvwkE60mHvoSY4BhOQ"
	# token="5035848854:AAG9a-7bHDYTOXiNEdjXRsnM-gbkdw9TCfE"
	chat_id = "-615987943"
	# chat_id = "-1001616252735"
	url_req = "https://api.telegram.org/bot" + token + "/sendMessage" + "?chat_id=" + chat_id + "&text=" + msg_telegram
	# url_req = "https://api.telegram.org/bot" + token + "/sendMessage" + "?chat_id=" + chat_id + "&text=" + msg_telegram 

	results = requests.get(url_req)
	# print(results.json())




# alias_send_msg("text")










def testt():
	print("this is imported def")



########################################################################################################################################
def iip ():
	try:
		# pass
		#sourceee="ipecho.net"
		os.system("curl -s ipinfo.io > ipifo.json")
		f = open ('ipifo.json', "r")
		data = json.loads(f.read())
		#r = requests.get(sourceee)
		ip=data['ip']
		tz=data['timezone']
		loc=data['loc']
		country=data['country']
		print(" [ "+ip + " ] ["+tz+" ] [ "+loc+" ]")
	except Exception as e:
		iip ()
		ip=""
		tz="OKEurope/Paris"
		loc=""
	return ip,tz ,loc


def randomm():
	random_vpn=random.choice(os.listdir(p_vpn_g))
	final_vpn=p_vpn_g+random_vpn
	return final_vpn,random_vpn


#final_vpn,random_vpn=randomm()


#######################  DISPLAY ##############################
# display_aary=['1366x768','2560x1700','1366x768','2560x1600','2560x1440','1921x1080','2560x1440','1366x768','1440x900','1280x800','2560x1600','1440x900','1680x1050','2880x1800','1920x1200','1080x1920','768x1280','2160x4096','768x1366','1366x768','3840x2160','1600x900','1920x1080','2560x1440','1920x1200','2560x1440','2560x1600','1920x1080','1366x768','2560x1440','1366x768','3000x2000','2160x3840','768x1280','2304x1440','1366x768','1440x900','2560x1600','2880x1800','4096x2304','5120x2880','3840x2160','1920x1080','1280x800','1920x1080','1920x1080','1366x768','1920x1080','720x1280','480x800','1280x720','2560x1440','480x800','480x800','480x800','1080x1920','1080x1920','1080x1920','1080x1920','768x1280','1080x1920','1440x2560','1440x2560','1440x2560','768x1280','720x1280','1080x1920','480x854','540x960','540x960','540x960','1440x2560','1440x2560','1440x2560','720x1280','540x960','1080x1920','1080x1920','1080x1920','720x1280','800x1280','720x1280','480x800','480x800','480x800','720x1280','1080x1920','480x800','720x1280','720x1280','720x1280','1440x2560','1440x2560','1440x2560','1080x1920','1440x2560','1080x1920','1280x720','1920x1080','1080x1920','1080x1920','720x1280','1080x1920','1080x1920','1080x1920','540x960','1280x720','1920x1080','1920x1080','1920x1080','1920x1080','1280x720','1280x720','1280x720','1280x720','854x480','1920x1080','1920x1080','800x480','1920x1080','1920x1080','1920x1080','2560x1440','1920x1080','1920x1080','960x540','1920x1080','1920x1080','720x720','768x1280','960x540','1280x768','1440x1440','1280x720','1280x720','480x360','320x480','640x960','640x1136','750x1334','750x1334','1080x1920','750x1334','1080x1920','480x800','768x1280','480x800','480x800','480x800','480x800','768x1280','768x1280','1440x2560','1280x720','1440x2560','1440x2560','1080x1920','1080x1920','1440x2560','1600x1200','2048x1536','1280x800','768x1280','1280x800','1024x600','2048x1536','600x1024','800x1280','1200x1920','1280x720','800x1280','1200x1920','1200x1920','600x800','1024x600','1024x600','1280x800','1920x1080','1920x1080','800x1280','600x1024','800x1280','2048x1536','1280x800','800x1280','1280x800','1280x800','1024x600','1024x600','1280x800','1024x600','768x1024','1536x2048','768x1024','900x1600','1080x1920','1080x1920','1280x800','1280x800','1024x600','1280x800','1280x800','1280x800','1280x800','2048x1536','1920x1200','2560x1600','2560x1600','2048x1536','2048x1536','2732x2048','2048x1536','2048x1536','1280x800','2160x1440','2736x1824','2736x1824','2960x1440','2960x1440','750x1334','1080x1920','1125x2436','828x1792','1125x2436','1242x2688','640x1136','828x1792','1125x2436','1242x2688','1080x2400','1080x2310','1080x2400','1080x2340','1080x2340','1080x2340','1080x2340','1080x2400','1080x2400','1080x2400','1080x2340','1080x2340','1080x2340','1440x2560','1440x2560','1440x3200','1440x3088','1440x3200','1440x3040','1080x2400','1080x2280','1080x1920','1080x1920','2224x1668','2360x1640','2160x1620','2388x1668','2732x2048','2048x1536','2224x1668','1170x2532','1080x2340','1170x2532','1284x2778']
def resolution_func():

	# display_aary=['1366x768','2560x1700','1366x768','2560x1600','2560x1440','1921x1080','2560x1440','1366x768','1440x900','1280x800','2560x1600','1440x900','1680x1050','2880x1800','1920x1200','1080x1920','768x1280','2160x4096','768x1366','1366x768','3840x2160','1600x900','1920x1080','2560x1440','1920x1200','2560x1440','2560x1600','1920x1080','1366x768','2560x1440','1366x768','3000x2000','2160x3840','768x1280','2304x1440','1366x768','1440x900','2560x1600','2880x1800','4096x2304','5120x2880','3840x2160','1920x1080','1280x800','1920x1080','1920x1080','1366x768','1920x1080','720x1280','1280x720','2560x1440','1080x1920','768x1280','1080x1920','1440x2560','1440x2560','1440x2560','1080x1920','1440x2560','1440x2560','1440x2560','720x1280','1080x1920','1080x1920','1080x1920','720x1280','800x1280','720x1280','480x800','480x800','480x800','720x1280','1080x1920','480x800','720x1280','720x1280','720x1280','1440x2560','1440x2560','1440x2560','1080x1920','1440x2560','1080x1920','1280x720','1920x1080','1080x1920','1080x1920','720x1280','1080x1920','1080x1920','1080x1920','540x960','1280x720','1920x1080','1920x1080','1920x1080','1920x1080','1280x720','1280x720','1280x720','1280x720','854x480','1920x1080','1920x1080','800x480','1920x1080','1920x1080','1920x1080','2560x1440','1920x1080','1920x1080','960x540','1920x1080','1920x1080','720x720','768x1280','960x540','1280x768','1440x1440','1280x720','1280x720','480x360','320x480','640x960','640x1136','750x1334','750x1334','1080x1920','750x1334','1080x1920','480x800','768x1280','480x800','480x800','480x800','480x800','768x1280','768x1280','1440x2560','1280x720','1440x2560','1440x2560','1080x1920','1080x1920','1440x2560','1600x1200','2048x1536','1280x800','768x1280','1280x800','1024x600','2048x1536','600x1024','800x1280','1200x1920','1280x720','800x1280','1200x1920','1200x1920','600x800','1024x600','1024x600','1280x800','1920x1080','1920x1080','800x1280','600x1024','800x1280','2048x1536','1280x800','800x1280','1280x800','1280x800','1024x600','1024x600','1280x800','1024x600','768x1024','1536x2048','768x1024','900x1600','1080x1920','1080x1920','1280x800','1280x800','1024x600','1280x800','2048x1536','1920x1200','2560x1600','2560x1600','2048x1536','2048x1536','2732x2048','2048x1536','2048x1536','1280x800','2160x1440','2736x1824','2736x1824','2960x1440','2960x1440','750x1334','1080x1920','1125x2436','1125x2436','1242x2688','828x1792','1125x2436','1242x2688','1080x2400','1080x2310','1080x2400','1080x2340','1080x2340','1080x2340','1080x2340','1080x2400','1080x2400','1080x2400','1080x2340','1080x2340','1080x2340','1440x2560','1440x2560','1440x3200','1440x3088','1440x3200','1440x3040','1080x2400','1080x2280','1080x1920','1080x1920','2224x1668','2360x1640','2160x1620','2388x1668','2732x2048','2048x1536','2224x1668','1170x2532','1080x2340','1170x2532','1284x2778']
	display_aary=['1366x768','2560x1700','1366x768','2560x1600','2560x1440','1921x1080','2560x1440','1366x768','1440x900','1280x1024','2560x1600','1440x900','1680x1050','2880x1800','1920x1200','1080x1920','2160x4096','1366x768','3840x2160','1600x900','1920x1080','2560x1440','1920x1200','2560x1440','2560x1600','1920x1080','1366x768','2560x1440','1366x768','3000x2000','2160x3840','2304x1440','1366x768','1440x900','2560x1600','2880x1800','4096x2304','5120x2880','3840x2160','1920x1080','1280x1024','1920x1080','1920x1080','1366x768','1920x1080' ,'1280x720','2560x1440','1080x1920','1080x1920','1440x2560','1440x2560','1440x2560','1080x1920','1440x2560','1440x2560','1440x2560' ,'1080x1920','1080x1920','1080x1920' ,'1080x1920','1440x2560','1440x2560','1440x2560','1080x1920','1440x2560','1080x1920','1280x720','1920x1080','1080x1920','1080x1920' ,'1080x1920','1080x1920','1080x1920' ,'1280x720','1920x1080','1920x1080','1920x1080','1920x1080','1280x720','1280x720','1280x720','1280x720','1920x1080','1920x1080','1920x1080','1920x1080','1920x1080','2560x1440','1920x1080','1920x1080','1920x1080','1920x1080','1280x768','1440x1440','1280x720','1280x720',  '1080x1920', '1080x1920','1440x2560','1280x720','1440x2560','1440x2560','1080x1920','1080x1920','1440x2560','1600x1200','2048x1536','1280x1024','1280x1024','2048x1536' ,'1200x1920','1280x720' ,'1200x1920','1200x1920','1280x1024','1920x1080','1920x1080'  ,'2048x1536','1280x1024' ,'1280x1024','1280x1024','1280x1024' ,'1536x2048' ,'1080x1920','1080x1920','1280x1024','1280x1024','1280x1024','2048x1536','1920x1200','2560x1600','2560x1600','2048x1536','2048x1536','2732x2048','2048x1536','2048x1536','1280x1024','2160x1440','2736x1824','2736x1824','2960x1440','2960x1440','1080x1920','1125x2436','1125x2436','1242x2688','1125x2436','1242x2688','1080x2400','1080x2310','1080x2400','1080x2340','1080x2340','1080x2340','1080x2340','1080x2400','1080x2400','1080x2400','1080x2340','1080x2340','1080x2340','1440x2560','1440x2560','1440x3200','1440x3088','1440x3200','1440x3040','1080x2400','1080x2280','1080x1920','1080x1920','2224x1668','2360x1640','2160x1620','2388x1668','2732x2048','2048x1536','2224x1668','1170x2532','1080x2340','1170x2532','1284x2778']
	# display_aary=['1366x768']

	random_display_chose=random.choice(display_aary)

	display=random_display_chose.split(sep="x")
	width=display[0]
	height=display[1]
	return width ,height


#########      URLS     ######################



user_agent = u_a.user_agent


##URLS 
#firefox_options_binary = "/root/EXTRA/firefox-49.0b9/firefox/firefox"
# new_driver_path = '/usr/bin/geckodriver13'
# new_driver_path = '/usr/bin/geckodriver22'
new_driver_path = '/usr/bin/geckodriver_15'
# new_binary_path = '/root/EXTRA/firefox-53.0b9/firefox/firefox'

########################
#new_binary_path = '/root/EXTRAT/firefox/firefox'
#new_binary_path = '/root/EXTRA/firefox-53.0b9/firefox/firefox'
# new_driver_path = '/usr/bin/geckodriver222'


def random_fir():
	# firefox_version=['53.0.2','53.0b9']
	firefox_version=['49.0b9']
	# firefox_version=['57.0.1','58.0.1','59.0b9','60.0.1esr']
	random_firefox_version=random.choice(firefox_version)
	print("[ "+random_firefox_version +" ]", end=" ")
	new_binary_path="/root/EXTRAT/firefox-"+random_firefox_version+"/firefox/firefox"
	return new_binary_path








































