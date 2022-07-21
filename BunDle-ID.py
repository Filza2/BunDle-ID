from requests import get
from user_agent import generate_user_agent
print('''  
██████╗ ██╗   ██╗███╗   ██╗██████╗ ██╗     ███████╗    ██╗██████╗ 
██╔══██╗██║   ██║████╗  ██║██╔══██╗██║     ██╔════╝    ██║██╔══██╗
██████╔╝██║   ██║██╔██╗ ██║██║  ██║██║     █████╗█████╗██║██║  ██║
██╔══██╗██║   ██║██║╚██╗██║██║  ██║██║     ██╔══╝╚════╝██║██║  ██║
██████╔╝╚██████╔╝██║ ╚████║██████╔╝███████╗███████╗    ██║██████╔╝
╚═════╝  ╚═════╝ ╚═╝  ╚═══╝╚═════╝ ╚══════╝╚══════╝    ╚═╝╚═════╝ 
By @TweakPY  - @vv1ck                                                             
''')
#ex: com.zhiliaoapp.musically
#ex: com.burbn.instagram
#ex: com.atebits.Tweetie2
#ex: com.toyopagroup.picaboo
print('-------------------------------------')
bundleid=input('[?] Type The App Bundle ID:\n')
print('-------------------------------------')
head={
	'Host': 'itunes.apple.com',
	'Accept': '*/*',
	'User-Agent': generate_user_agent(),
	'Accept-Language': 'ar',
	'Application/json': 'Content-Type',
	'Accept-Encoding': 'gzip, deflate',
	'Connection': 'close'}
r=get(f'https://itunes.apple.com/lookup?bundleId={bundleid}&country=SA',headers=head)
print(r.text)
print('-------------------------------------')

