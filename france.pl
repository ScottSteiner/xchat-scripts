#########################################################################################
# Name                  steiner:france
# Description           Typical French phrases for (He)XChat.
# Version               1.0 (2013-03-03)
# Contact               ScottSteiner@irc.rizon.net
# Website               https://github.com/ScottSteiner/xchat-scripts
# Copyright             2013, ScottSteiner <nothingfinerthanscottsteiner@gmail.com>
# License               GPL version 3 or any later version; http://www.gnu.org/copyleft/gpl.html
#########################################################################################

use strict;
use warnings;
use Xchat qw( :all );

my $NAME    = 'steiner:france';
my $VERSION = '1.0';

register($NAME, $VERSION, "French phrases by Scott Steiner");

IRC::add_command_handler("france", "france");
my @jobs = (
	"military attaché",
	"cultural attaché",
	"Keeper of the Seals",
	"Prime Minister",
	"National Statistician",
	"treasurer",
	"Last King of Scotland",
	"King of Arms",
	"governor",
	"mayor",
	"city manager"
);
my @colors = (
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
);
my @holidays = (
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
);
my @badshit = (
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
	"interracial rape"
);
my @countries = (
	"Iran",
	"Iraq",
	"Turkey",
	"Vietnam",
	"Panama",
	"Saudi Arabia",
	"Qatar",
	"Morocco",
	"Bahrain",
	"Omar",
	"Yemen",
	"Jordan",
	"Lebanon",
	"Syria",
	"Palestine",
	"Algeria",
	"Egypt",
	"Niger",
	"Rwanda",
	"Tunisia"
);

sub france {
	my $years = int(rand(17))+3;
	my $hearts_num = int(rand(6))+3;
	my $hearts_col = uc $colors[int rand @colors];
	my $sentence = "You son of a hag! I didn't serve as $jobs[int rand @jobs] for $years-odd years in $countries[int rand @countries], defending our precious American $holidays[int rand @holidays] and $badshit[int rand @badshit], just tew read such smart-mouthed assertions from the likes of a psycho like you! I'VE GOT $hearts_num $hearts_col HEARTS, MONSIEUR!!";
	if ($_[0]) { my $targ = $_[0]; $targ =~ s/\s+$//; $sentence = "$targ: $sentence"; };
	IRC::command("/say $sentence");
	return EAT_XCHAT;
}
