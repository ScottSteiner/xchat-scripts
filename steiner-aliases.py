#########################################################################################
# Name                  steiner:aliases
# Description           Various aliases I find useful. 
# Version               1.1 (2015-01-04)
# Contact               ScottSteiner@irc.rizon.net
# Website               https://github.com/ScottSteiner/xchat-scripts
# Copyright             2012-2015, ScottSteiner <nothingfinerthanscottsteiner@gmail.com>
# License               GPL version 3 or any later version; http://www.gnu.org/copyleft/gpl.html
#########################################################################################

import xchat, re, string
from urllib.parse import quote

__module_name__ = 'steiner:aliases'
__module_version__ = '1.1'
__module_description__ = 'Various aliases I find useful.'

def xcom(com):
	xchat.command(com)

def xsay(string):
	xcom('say {}'.format(string))
	
def bing(text, text_eol, userdata):
	xsay('http://letmebingthatforyou.com/?q={}'.format(quote(' '.join(text[1:]))))
	return xchat.EAT_ALL

def channelSetup(text, text_eol, userdata):
	if len(text) > 1: channel = text_eol[1].strip()
	else: return
	xcom('cs set {} ownermode on'.format(channel))
	xcom('cs set {} protectmode on'.format(channel))
	#Edit this before using it, unless you want my bot to be an sop in your channel when you set it up
	xcom('cs sop {} add rms'.format(channel))
	return xchat.EAT_ALL
	
def cold(text, text_eol, userdata):
	xsay('.w Verkhoyansk')
	return xchat.EAT_ALL
	
def fakeIgnoreLong(text, text_eol, userdata):
	if len(text) > 1: target = text_eol[1].strip()
	else: return
	xsay('{}: I have put you on a permanent ignore, public and private. I have found you disturbing, rude and generally not worth talking to. According to the channels you hang on, it strengtens the effect of wanting to put you on ignore because of my lack of interest in you as a person. This message is not meant to be rude to you, just to inform you that i won\'t see anything of what you type from now on.'.format(target))
	return xchat.EAT_ALL

def fakeIgnoreShort(text, text_eol, userdata):
	if len(text) > 1: target = text_eol[1].strip()
	else: return
	xsay('* Added {}!*@* to ignore list'.format(target))
	return xchat.EAT_ALL
	
def mypower(text, text_eol, userdata):
	count, total, channelcount = 0, 0, 0
	
	windows = xchat.get_list('channels')
	for window in windows:
		if window.type == 2:
			channelcount += 1
			userlist = window.context.get_list('users')
			for user in userlist:
				if user.nick == xchat.get_info('nick'):
					if user.prefix in ['~','&','@','%', '!']:
						count += len(userlist)
					break
			total += len(userlist)
	percentage = round(((count / total) * 100),2)
	xsay('I have power over {}/{} people ({}%) in {} channels.'.format(count, total, percentage, channelcount))
	return xchat.EAT_ALL	
	
def myWeather(text, text_eol, userdata):
	xsay('.w 02893')
	return xchat.EAT_ALL

def slap(text, text_eol, userdata):
	if len(text) > 1: target = text_eol[1].strip()
	else: target = 'you'
	xcom('me slaps {} around a bit with a used condom'.format(target))
	return xchat.EAT_ALL

xchat.hook_command('bing', bing)
xchat.hook_command('chansetup', channelSetup)
xchat.hook_command('cold', cold)
xchat.hook_command('ig', fakeIgnoreLong)
xchat.hook_command('fakeignore', fakeIgnoreShort)
xchat.hook_command('mypower', mypower)
xchat.hook_command('power', mypower)
#xchat.hook_command('np', np)
xchat.hook_command('slap', slap)
xchat.hook_command('w', myWeather)

print('\00309{} {} has been loaded: {}\003'.format(__module_name__, __module_version__, __module_description__))