#########################################################################################
# Name                  steiner:france
# Description           Typical French phrases for (He)XChat.
# Version               1.1 (2015-01-11)
# Contact               ScottSteiner@irc.rizon.net
# Website               https://github.com/ScottSteiner/xchat-scripts
# Copyright             2013-15, ScottSteiner <nothingfinerthanscottsteiner@gmail.com>
# License               GPL version 3 or any later version; http://www.gnu.org/copyleft/gpl.html
#########################################################################################

import xchat, random

__module_name__ = 'steiner:france'
__module_version__ = '1.1'
__module_description__ = 'Typical French phrases for (He)XChat'


def france(text, text_eol, userdata):
	if len(text) > 1: target = '{}: '.format(text_eol[1].strip())
	else: target = ''
	
	xchat.command("say You son of a hag! I didn't serve as {} for {}-odd years in {}, defending our precious American {} and {}, just tew read such smart-mouthed assertions from the likes of a psycho like you! I'VE GOT {} {} HEARTS, MONSIEUR!!".format(random.choice(jobs), random.randint(3,20), random.choice(countries), random.choice(holidays), random.choice(badshit), random.randint(3,9), random.choice(colors).upper()))
	return xchat.EAT_ALL

xchat.hook_command('france', france)

print('\x0309{} {} has been loaded: {}\003'.format(__module_name__, __module_version__, __module_description__))

jobs = [
	"military attach",
	"cultural attach",
	"Keeper of the Seals",
	"Prime Minister",
	"National Statistician",
	"treasurer",
	"Last King of Scotland",
	"King of Arms",
	"governor",
	"mayor",
	"city manager"
]
colors = [
	"blue",
	"red",
	"yellow",
	"purple",
	"orange",
	"green",
	"beige",
	"brown",
	"black",
	"white",
	"apricot",
	"amber",
	"auburn",
	"burgundy",
	"celadon",
	"cerulean",
	"cinnabar",
	"cobalt",
	"copper",
	"crimson",
	"cyan",
	"emerald",
	"fuchsia",
	"grey",
	"indigo",
	"ivory",
	"jade",
	"lavender",
	"lemon",
	"lilac",
	"magenta",
	"maroon",
	"mauve",
	"mustard",
	"olive",
	"peach",
	"ping",
	"pumpkin",
	"rose",
	"ruby",
	"rust",
	"saffron",
	"sapphire",
	"tan",
	"tangerine",
	"vermilion",
	"violet",
	"wisteria"
]
holidays = [
	"the Fourth of July",
	"President's Day",
	"Memorial Day",
	"Labor Day",
	"Columbus Day",
	"Veteran's Day",
	"Thanksgiving",
	"Christmas",
	"Valentine's Day",
	"St Patrick's Day",
	"Halloween",
	"September the Eleventh",
	"9/11"
]
badshit = [
	"slavery",
	"segregation",
	"lynching",
	"internment camps",
	"Trail of Tears",
	"genocide",
	"GRIDS",
	"KKK",
	"Neo Nazis",
	"white slavery",
	"child prostitution",
	"nuclear holocaust",
	"unprovoked wars",
	"illegal wars",
	"assassination of civil rights leaders",
	"interspecies rape",
	"interracial rape",
	"drone attacks"
]
countries = [
	"Afghanistan",
	"Algeria", 
	"Bangladesh",
	"Bahrain",
	"Chechnya",
	"Congo",
	"Djibouti",
	"Egypt",
	"Iran",
	"Iraq",
	"Jordan",
	"Lebanon",
	"Libya",
	"Mali",
	"Morocco",
	"Niger",
	"Oman",
	"Pakistan",
	"Palestine",
	"Qatar",
	"Saudi Arabia",
	"Senegal",
	"Somalia",
	"Sudan",
	"Syria",
	"Tunisia",
	"Turkey",
	"Uzbekistan",
	"Yemen",
	"Bosnia",
	"Cuba",
	"Grenada",
	"Haiti",
	"Nicaragua",
	"North Korea",
	"Panama",
	"Rwanda",
	"Vietnam",
	"Yugoslavia"
]