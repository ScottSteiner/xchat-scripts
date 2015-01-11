#########################################################################################
# Name                  steiner:dragon
# Description           Dragon bot 
# Version               1.0 (2015-01-04)
# Contact               ScottSteiner@irc.rizon.net
# Website               https://github.com/ScottSteiner
# Copyright             2012-2015, ScottSteiner <nothingfinerthanscottsteiner@gmail.com>
# License               GPL version 3 or any later version; http://www.gnu.org/copyleft/gpl.html
#########################################################################################

import xchat, re, string
from time import sleep

__module_name__ = "steiner:dragon"
__module_version__ = "1.0"
__module_description__ = "Slay the dragon"	

def dragon(text, text_eol, userdata):
	reStart = "Welcome back.*{}".format(xchat.get_info("nick"))
	reDefeated = "{} rolled the die.*You defeated".format(xchat.get_info("nick"))
	if re.search(reStart, text[1]) or re.search(reDefeated, text[1]):
		output = "!roll"
	else: return
	
	if output:
		xchat.get_context().command("say {}".format(output))
#		return xchat.EAT_XCHAT

xchat.hook_print("Channel Msg Hilight", dragon)
print("\00309{} {} has been loaded: {}\003".format(__module_name__, __module_version__, __module_description__))