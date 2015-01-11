#########################################################################################
# Name                  steiner:replies
# Description           There's Nothing Finer Than Scott Steiner
# Version               1.0 (2015-01-04)
# Contact               ScottSteiner@irc.rizon.net
# Website               https://github.com/ScottSteiner
# Copyright             2012-2015, ScottSteiner <nothingfinerthanscottsteiner@gmail.com>
# License               GPL version 3 or any later version; http://www.gnu.org/copyleft/gpl.html
#########################################################################################

import xchat, re, string
from time import sleep

__module_name__ = "steiner:replies"
__module_version__ = "1.0"
__module_description__ = "There's Nothing Finer Than Scott Steiner"	

steinerhook = None
steinertimer = None

def steiner(text, text_eol, userdata):
	ignore = ['swim', 'seventyNexus', 'SeventyTwo', 'Noxialis', 'ChanServ', 'cocaine', 'Ultimation_', 'roofletrain', 'Serpentine', 'hachimitsu-boy', 'whatapath', 'YourImaginaryFriend', 'RocketLauncher', 'Onee-chan', 'Fijou', 'DarkAceLaptop', 'GayServ', 'zingas', 'rpk', 'qb', 'mkillebrew', 'whoapath', 'guymann', 'Doomfag', 'maws', 'cunnelatio', 'DenSaakalte', 'martian', 'irc', 'cyberdynesystems', 'net', 'somberlain', 'PhilKenSebben', 'kyokugen', 'Erotica', 'mechanicalTurk', 'ed', 'anon__', 'E-Pain', 'thenoize', 'skew', 'StoneColdSteveAustin', 'frussif', 'Ultimation', 'charles', 'i7MUSHROOM', 'slamm', 'homo', 'Hypnotized', 'Dr_Venture', 'AoC', 'Porygon', 'axujen', 'Jax', 'Special-G', 'peopleschampion', 'LtSerge', 'Dwarf', 'pinetreegator', 'Cap', '[^_^]', 'swam', 'Clear', 'takoyaki', 'keret', 'MeanPocket', 'keref', 'hachi', 'vortmax', 'War', 'Hachi-chan', 'JediDachshund', 'BillGates', 'BTDT', 'kk', 'guy9000', 'Erzengel', 'Revived', 'BradPitt', 'Colink', 'ekOz', 'Jynweythek']
	steiner = ""
	
	nick = xchat.strip(text[0]).translate(str.maketrans("", "", "+%@&~"))
	if nick in ignore or "ScottSteiner" not in xchat.get_info("nick"): return
	if text[1] == "nothing gayer":
		steiner = "than {}".format(nick)
	elif re.search("nothin(?:g(?:'s|)|)gayer", text[1]):
		steiner = "{} is a faggot".format(nick)
	elif re.search("nothin(?:g(?:'s|)|) finer than", text[1]) or text[1] == "no one kinder than":
		steiner = "Scott Steiner"
	elif re.search("nothin(?:g(?:'s|)|) finer", text[1]) or text[1] == "no one kinder":
		steiner = "than Scott Steiner"
	elif text[1] == "nothing is finer":
		steiner = "than {} being a dumbfuck inbred retard who still can't into a simple script".format(nick)
	elif text[1] == "big poppa pump":
		steiner = "IS YOUR HOOKUP. HOLLER IF YA HEAR ME"
	
	if steiner:
		print("{0}<{1}{0}> {2}".format("\x0307", text[0],text[1]))
		xchat.get_context().command("say {}".format(steiner))
		global steinerhook, steinertimer
		xchat.unhook(steinerhook)
		steinertimer = xchat.hook_timer(60000, steinertoggle) 
		steinerhook = None
		return xchat.EAT_XCHAT
		
def steinertoggle(userdata):
	global steinerhook
	print("Enabling Steiner function")
	if steinerhook is None: steinerhook = xchat.hook_print("Channel Message", steiner)
	else: steinerhook = None
		
steinertoggle(None)
print("\00309{} {} has been loaded: {}\003".format(__module_name__, __module_version__, __module_description__))