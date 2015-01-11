#########################################################################################
# Name                  steiner:spam
# Description           Some of my more annoying aliases
# Version               1.0 (2015-01-04)
# Contact               ScottSteiner@irc.rizon.net
# Website               https://github.com/ScottSteiner/xchat-scripts
# Copyright             2012-2015, ScottSteiner <nothingfinerthanscottsteiner@gmail.com>
# License               GPL version 3 or any later version; http://www.gnu.org/copyleft/gpl.html
#########################################################################################

import xchat, re, string, random, os
from urllib.parse import quote

__module_name__ = 'steiner:spam'
__module_version__ = '1.0'
__module_description__ = 'Some of my more annoying aliases'

def xcom(com):
	xchat.command(com)

def xsay(string):
	xcom('say {}'.format(string))

def multiple_replace(string, rep_dict):
    pattern = re.compile('|'.join([re.escape(k) for k in rep_dict.keys()]), re.M)
    return pattern.sub(lambda x: rep_dict[x.group(0)], string)

def alert(text, text_eol, userdata):
	if len(text) > 1: text = text_eol[1].strip()
	else: return
	for _ in range(3):
		xsay('\x0301,08\x02{0} {1} {0} \x0304{2}\x0301 {0} {1} {0}'.format('\x1F/!\\\x1F',userdata.upper(),text))
	return xchat.EAT_ALL
	
def box(text, text_eol, userdata):
	if len(text) > 1: text = text_eol[1].strip()
	else: return
	color = random.randrange(2,15)
	xsay('\x03{1},{1}\x02   {0}   '.format(text, color))
	xsay('\x0301,{1}\x02   {0}   \x0314,14 '.format(text, color))
	xsay('\x03{1},{1}\x02   {0}   \x0314,14 '.format(text, color))
	xsay(' \x0314,14\x02  {}    '.format(text))
	return xchat.EAT_ALL

def colors(text, text_eol, userdata):
	coldict = {00:'white', 1:'black', 2:'navy', 3:'green', 4:'bright red', 5:'dark red', 6:'purple', 7:'orange', 8:'yellow', 9:'light green', 10:'dark cyan', 11:'light blue', 12:'dark blue', 13:'pink', 14:'dark grey', 15:'light grey'}
	collist = []
	for value in coldict:
		collist.append('\x03{}{}'.format(value, coldict.get(value)))
	xsay(' '.join(collist))
	xsay('\x02{}'.format(' '.join(collist)))
	return xchat.EAT_ALL
	
def double(text, text_eol, userdata):
	if len(text) > 2:	
		if text[1].isdigit():
			if text[2].isdigit():
				colors = [text[1], text[2]]
				text = text_eol[3].strip()
			else:
				colors = [text[1], random.randrange(2,15)]
				text = text_eol[2].strip()
		else:
			colors = [random.randrange(2,15), random.randrange(2,15)]
			text = text_eol[1].strip()
	elif len(text) > 1:
		colors = [random.randrange(2,15), random.randrange(2,15)]
		text = text_eol[1].strip()
	else: return
	output = []
	
	for _ in range(10):
		output.append('\x03{},{} {} '.format(colors[0],colors[1],text))
		output.append('\x03{},{} {} '.format(colors[1],colors[0],text))
	xsay('\x02{}'.format(''.join(output)))
	return xchat.EAT_ALL

def flash(text, text_eol, userdata):
	if len(text) > 1: text = text_eol[1].strip()
	else: return
	colored = '\x03{1},{2} {0} \x03{2},{1} {0} '.format(text, '08', '00')
	reps = int(300 / len(colored))
	xsay('{}'.format(colored*reps))
	return xchat.EAT_ALL

def give(text, text_eol, userdata):
	if len(text) > 1: target = text_eol[1].strip()
	else: return
	lines = {
				'dick': '\x02\x030,1 8▇▇▇▇D \x0311~~a DICK for you\x038 {} \x0311~~\x02 \x030,1 8▇▇▇▇D',
				'rose': '\x0313@\x039}}\x033-,-- \x02\x0311~~ a rose for you\x038 {} \x0311~~\x02 \x0313@\x039}}\x033-,--',
				'turd': '\x037☁\x02\x0311~~ a turd for you\x038 {} \x0311~~\x037☁', 
				'eatadick': 'Hey {}, eat a \x02\x0304FAT DICK'
			}
	xsay(lines.get(userdata).format(target))
	return xchat.EAT_ALL

def leet(text, text_eol, userdata):
	if len(text) > 1: text = text_eol[1].strip()
	else: return
	leet = {'a': '4', 'e': '3', 'i': '1', 'o': '0', 't': '7'}
	xsay(multiple_replace(text,leet))
	return xchat.EAT_ALL

def megatold(text, text_eol, userdata):
	tolds = ['Told', 'Tolding@home', 'NO COUNTRY FOR TOLD MEN', 'Cash4TOLD.com', 'Avenged Seventold', 'Tolden Gate Bridge', 'Texas Told \'em', 'Knights of the Told Republic']
	xsay('☐ Not told')
	for told in tolds:
		xsay('☑ {}'.format(told))
	return xchat.EAT_ALL
	
def moki(text, text_eol, userdata):
	if len(text) > 1: text = text_eol[1].strip()
	else: return
	output = []
	for _ in range(10):
		output.append('\x03{},{} {} '.format(random.randrange(2,15),random.randrange(2,15),text))
	xsay('\x02{}'.format(''.join(output)))
	return xchat.EAT_ALL

def nicks(text, text_eol, userdata):
	command = 'say'
	limit = 300
	if len(text) > 1:
		if text[1].lower() in ['echo', 'me', 'notice', 'r', 'reverse', 'notice']:
			command = text[1]
			if command == 'r': limit = 200
			if command in ['notice','ctcp']: command = '{} {}'.format(command, xchat.get_context().get_info('channel'))
		elif text[1].lower() == 'macbot':
			command ='me Macbot:'
	
	opers	= ['killah','grimlock','wof','xaquseg','god','xxx','djahandarie','rails','blake','wintereise','nol888','steak','__roflmao__','the user formerly known as god','darkfyre','rails']
	bakas	= ['Nahu','enner','indel','taco']
	bots	= ['netsec','ircstats','irc-stats','rms','twitterbot','glock','onee-chan','internets','limitserv','quotes','trivia','stats','dgbot','dickbeef','erepublik','chanstat']
	
	ignorelist = opers + bakas + bots
	ignorelist.append(xchat.get_info('nick'))
	nicklist = []

	userlist = xchat.get_context().get_list('users')
	for user in userlist:
		if user.nick not in ignorelist:
			nicklist.append(user.nick)
			if len(', '.join(nicklist)) > limit:
				xcom('{} {}'.format(command, ', '.join(nicklist)))
				nicklist = []
	if nicklist:
		xcom('{} {}'.format(command, ', '.join(nicklist)))
	return xchat.EAT_ALL
	
def pasta(text, text_eol, userdata):
	if len(text) > 1: target = text_eol[1].strip()
	else: return
	chan = xchat.get_info('channel')
	network = xchat.get_info('network')
	line = random.choice(list(open('{}\\hexchat\\spam\\{}.txt'.format(os.getenv('APPDATA'),userdata))))
	line = multiple_replace(line,{'<user>': target, '<USER>': target.upper(), '<chan>': chan, '<CHAN>': chan.upper(), '<network>': network, '<NETWORK>': network.upper()})
	xsay(line.strip())
	return xchat.EAT_ALL

def rbe(text, text_eol, userdata):
	if len(text) > 1: text = text_eol[1].strip()
	else: return
	left = '\x034¾\x034,4 \x037¾\x034,7¾ \x038¾\x037,8¾ \x039¾\x038,9¾ \x033¾\x039,3¾ \x0312¾\x033,12¾ \x0313¾\x0312,13¾ \x036¾\x0313,6¾ \x03\x036¾ \x0313×\x02*\x02×x×\x02*\x02×x\x036 \x02'
	right = '\x02 \x0313x×\x02*\x02×x×\x02*\x02× \x034¾\x034,4 \x037¾\x034,7¾ \x038¾\x037,8¾ \x039¾\x038,9¾ \x033¾\x039,3¾ \x0312¾\x033,12¾ \x0313¾\x0312,13¾ \x036¾\x0313,6¾ \x03\x036¾'
	for spaces in [2, 1, 0, 0, 1, 2]:
		xsay('{0}{2}{1}{3}{1}{4}'.format(' '*spaces, ' '*(3-spaces),left, text, right))
	return xchat.EAT_ALL
	
def randomword(length):
	return ''.join(random.choice(string.ascii_letters) for x in range(length))

def reverse(text, text_eol, userdata):
	if len(text) > 1: text = text_eol[1].strip()
	else: return
	xsay(text[::-1])
	return xchat.EAT_ALL

def scroll(text, text_eol, userdata):
	if len(text) > 1: text = text_eol[1].strip()
	else: return
	xsay(text)
	for letter in list(text)[1:]:
		xsay(letter)
	return xchat.EAT_ALL
	
def told(text, text_eol, userdata):
	if len(text) > 1: target = text[1].strip()
	else: target = xchat.get_info('channel')
	xsay('{} status:'.format(target))
	xsay('☑  ＴＯＬＤ')
	xsay('☐  ＮＯＴ ＴＯＬＤ')
	return xchat.EAT_ALL

def zalgo(text, text_eol, userdata):
	if len(text) > 1: text = text_eol[1].strip()
	else: return
	xsay('{}'.format('҉'.join(list(text))))
	return xchat.EAT_ALL

xchat.hook_command('alert',alert, 'alert')
xchat.hook_command('attention', alert, 'attention')
xchat.hook_command('box', box)
xchat.hook_command('colors', colors)
xchat.hook_command('dick', give, 'dick')
xchat.hook_command('double', double)
xchat.hook_command('eatadick', give, 'eatadick')
xchat.hook_command('flash', flash)
xchat.hook_command('leet', leet)
xchat.hook_command('megatold', megatold)
xchat.hook_command('moki', moki)
xchat.hook_command('nicks', nicks)
xchat.hook_command('rbe', rbe)
xchat.hook_command('reverse', reverse)
xchat.hook_command('rose', give, 'rose')
xchat.hook_command('scroll', scroll)
xchat.hook_command('told', told)
xchat.hook_command('turd', give, 'turd')
xchat.hook_command('zalgo', zalgo)

xchat.hook_command('insult', pasta, 'insult')
xchat.hook_command('i', pasta, 'insult')
xchat.hook_command('girl', pasta, 'girl')
xchat.hook_command('juggalo', pasta, 'juggalo')
xchat.hook_command('myface', pasta, 'myface')
xchat.hook_command('sex', pasta, 'sex')
xchat.hook_command('wat', pasta, 'wat')



print('\00309{} {} has been loaded: {}\003'.format(__module_name__, __module_version__, __module_description__))