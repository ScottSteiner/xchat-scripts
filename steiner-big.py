#########################################################################################
# Name                  steiner:big
# Description           Big text script
# Version               1.0 (2015-01-04)
# Contact               ScottSteiner@irc.rizon.net
# Website               https://github.com/ScottSteiner
# Copyright             2012-2015, ScottSteiner <nothingfinerthanscottsteiner@gmail.com>
# License               GPL version 3 or any later version; http://www.gnu.org/copyleft/gpl.html
#########################################################################################

import xchat, string, re

__module_name__ = 'steiner:big'
__module_version__ = '1.0'
__module_description__ = 'Big text'	

offset = 0

def rainbow(text,offset):
	# Sourced from DEElekgolo's rainbow script
	
	# 0 = White, 1 = Black, 2 = Navy Blue, 3 = Green, 4 = Bright Red, 5 = Dark Red
	# 6 = Purple, 7 = Orange, 8 = Yellow, 9 = Light Green, 10 = Cyan
	# 11 = Light Blue, 12 = Dark Blue, 13 = Pink, 14 = Dark Grey, 15 = Light Grey
	colorlist = [4,7,8,9,11,12,13,6]
	rainbowed = ''

	for i in range(len(text)):
		if text[i] == ' ': offset -= 1
		# Gets the remainder of (i+offset) / len(colorlist) for strings longer than len(colorlist)
		rainbowed += '\x03{}{}'.format(colorlist[(i+offset)%len(colorlist)], text[i])
	return rainbowed

def repl(match):
	return '\x03{1},{1}{0}\x03'.format('\xa0'*len(match.group()), '{0:02d}'.format(color))

def big(text, text_eol, userdata):
	global offset
	if len(text) > 1:
		text = text_eol[1].strip()
	else: return
	if userdata == 'gay':
		text = rainbow(text,offset)
		offset += 1
	elif userdata == 'rb':
		text = rainbow(text,offset)
	if userdata == 'gaybow':
		linecolor = [4,7,8,9,6]
	else:
		linecolor = False
	if userdata == 'echo':
		command = 'echo'
	else:
		command = 'say'
	output = bigformat(text, linecolor)
	for line in output:
		xchat.command('{} {}'.format(command, line))

def bigformat(text, linecolor):
	global color
	output = []
	chars = {
		# X = filled in, . = empty
		' ': ['...', '...', '...', '...', '...'],
		'!': ['XX', 'XX', 'XX', '..', 'XX'],
		'\'': ['XX..XX', 'XX..XX', '......', '......', '......'],
		'#': ['.XX..XX.', 'XXXXXXXX', '.XX..XX.', 'XXXXXXXX', '.XX..XX.'],
		'%': ['XX..XX', '...XX.', '..XX..', '.XX...', 'XX..XX'],
		'\'': ['.XX', 'XX.', '...', '...', '...'],
		'(': ['...XX', '.XX..', 'XX...', '.XX..', '...XX'],
		')': ['XX...', '..XX.', '...XX', '..XX.', 'XX...'],
		'*': ['X.X.X.', '.XXX..', 'XXXXX.', '.XXX..', 'X.X.X.'],
		'+': ['......', '..XX..', 'XXXXXX', '..XX..', '......'],
		',': ['...', '...', 'XXX', '.XX', 'XX.', ''],
		'-': ['......', '......', 'XXXXXX', '......', '......'],
		'.': ['..', '..', '..', '..', 'XX'],
		'/': ['....XX', '...XX.', '..XX..', '.XX...', 'XX....'],
		'0': ['.XXXX.', 'XX..XX', 'XX.XXX', 'XXX.XX', '.XXXX.'],
		'1': ['.XXXX', 'XX.XX', '...XX', '...XX', '...XX'],
		'2': ['XXXXX.', '....XX', '..XX..', 'XX....', 'XXXXXX'],
		'3': ['XXXXX.', '....XX', '.XXXX.', '....XX', 'XXXXX.'],
		'4': ['XX.XX', 'XX.XX', 'XXXXX', '...XX', '...XX'],
		'5': ['XXXXX', 'XX...', 'XXXX.', '...XX', 'XXXX.'],
		'6': ['.XXXX.', 'XX....', 'XXXXX.', 'XX..XX', '.XXXX.'],
		'7': ['XXXXXX', '...XX.', '..XX..', '.XX...', 'XX....'],
		'8': ['.XXXX.', 'XX..XX', '.XXXX.', 'XX..XX', '.XXXX.'],
		'9': ['.XXXX.', 'XX..XX', '.XXXXX', '....XX', '.XXXX.'],
		':': ['..', '.X', '..', '.X', '..'],
		';': ['..', '.X', '..', '.X', 'X.'],
		'<': ['....XX', '..XX..', 'XX....', '..XX..', '....XX'],
		'=': ['......', 'XXXXXX', '......', 'XXXXXX', '......'],
		'>': ['XX....', '..XX..', '....XX', '..XX..', 'XX....'],
		'?': ['XXX.', '..XX', '.XX.', '....', '.XX.'],
		'@': ['XXXXXXXX', 'XX....XX', 'XX.XXXXX', 'XX......', 'XXXXXXXX'],
		'A': ['.XXXX.', 'XX..XX', 'XXXXXX', 'XX..XX', 'XX..XX'],
		'B': ['XXXXX.', 'XX..XX', 'XXXXX.', 'XX..XX', 'XXXXX.'],
		'C': ['.XXXX.', 'XX..XX', 'XX....', 'XX..XX', '.XXXX.'],
		'D': ['XXXXX.', 'XX..XX', 'XX..XX', 'XX..XX', 'XXXXX.'],
		'E': ['XXXXX', 'XX...', 'XXXX.', 'XX...', 'XXXXX'],
		'F': ['XXXXX', 'XX...', 'XXXX.', 'XX...', 'XX...'],
		'G': ['.XXXX.', 'XX....', 'XX.XXX', 'XX..XX', '.XXXXX'],
		'H': ['XX...XX', 'XX...XX', 'XXXXXXX', 'XX...XX', 'XX...XX'],
		'I': ['XXXX', '.XX.', '.XX.', '.XX.', 'XXXX'],
		'J': ['....XX', '....XX', '....XX', 'XX..XX', '.XXXX.'],
		'K': ['XX..XX', 'XX.XX.', 'XXXX..', 'XX.XX.', 'XX..XX'],
		'L': ['XX...', 'XX...', 'XX...', 'XX...', 'XXXXX'],
		'M': ['XX....XX', 'XXX..XXX', 'XXXXXXXX', 'XX.XX.XX', 'XX....XX'],
		'N': ['XX..XX', 'XXX.XX', 'XXXXXX', 'XX.XXX', 'XX..XX'],
		'O': ['.XXXX.', 'XX..XX', 'XX..XX', 'XX..XX', '.XXXX.'],
		'P': ['XXXXX.', 'XX..XX', 'XXXXX.', 'XX....', 'XX....'],
		'Q': ['.XXXX..', 'XX..XX.', 'XX..XX.', 'XX.XXX.', '.XXXXXX'],
		'R': ['XXXXX.', 'XX..XX', 'XXXXX.', 'XX..XX', 'XX..XX'],
		'S': ['.XXXX.', 'XX....', '.XXXX.', '....XX', 'XXXXX.'],
		'T': ['XXXXXX', '..XX..', '..XX..', '..XX..', '..XX..'],
		'U': ['XX..XX', 'XX..XX', 'XX..XX', 'XX..XX', '.XXXX.'],
		'V': ['XX....XX', 'XX....XX', '.XX..XX.', '..XXXX..', '...XX...'],
		'W': ['XX...XX', 'XX...XX', 'XX.X.XX', 'XXXXXXX', '.XX.XX.'],
		'X': ['XX...XX', '.XX.XX.', '..XXX..', '.XX.XX.', 'XX...XX'],
		'Y': ['XX..XX', 'XX..XX', '.XXXX.', '..XX..', '..XX..'],
		'Z': ['XXXXXX', '...XX.', '..XX..', '.XX...', 'XXXXXX'],
		'[': ['XXXXX', 'XX...', 'XX...', 'XX...', 'XXXXX'],
		'\\': ['XX....', '.XX...', '..XX..', '...XX.', '....XX'],
		']': ['XXXXX', '...XX', '...XX', '...XX', 'XXXXX'],
		'^': ['..XXX..', '.XX.XX.', 'XX...XX', '.......', '.......'],
		'_': ['......', '......', '......', '......', 'XXXXXX'],
		'`': ['XX.', '.XX', '...', '...', '...'],
		'|': ['.XX.', '.XX.', '.XX.', '.XX.', '.XX.'],
		'~': ['.........', '..XXX.XXX', 'XXX.XXX..', '.........', '.........']	}
	line = [[], [], [], [], []]
	
	# Searches for colour codes
	for char in re.findall('(?:\x03\d+(?:,\d+|)|.)', text):
		for i in range(5):
			if char.upper() in chars:
				line[i].append(chars.get(char.upper())[i])
			elif char.startswith('\x03'):
				line[i].append(char)
	for i in range(5):
		if linecolor:
			color = linecolor[i]
		else:
			color = 7 # Default color (orange)
		outputline = ''

		for char in line[i]:
			# If the list item contains a colour code, set the color for the next character and continue
			if char.startswith('\x03'):
				color = int(re.search('\x03(\d+)', char).group(1))
				continue
			outputline += '{}\xa0'.format(re.sub('(X+)', repl, ''.join(char).replace('.', '\xa0')))
		output.append(outputline)
	return output

xchat.hook_command('big', big)	
xchat.hook_command('biggay', big, 'gay')
xchat.hook_command('biggaybow', big, 'gaybow')
xchat.hook_command('bigrb', big, 'rb')
xchat.hook_command('bigecho', big, 'echo')

print('\00309{} {} has been loaded: {}\003'.format(__module_name__, __module_version__, __module_description__))