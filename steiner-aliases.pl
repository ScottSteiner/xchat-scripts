#########################################################################################
# Name                  steiner:aliases
# Description           General aliases I find useful. 
# Version               1.0 (2013-03-03)
# Contact               ScottSteiner@irc.rizon.net
# Website               https://github.com/ScottSteiner/xchat-scripts
# Copyright             2012, ScottSteiner <nothingfinerthanscottsteiner@gmail.com>
# License               GPL version 3 or any later version; http://www.gnu.org/copyleft/gpl.html
#########################################################################################

use strict;
use warnings;
use Xchat qw( :all );
use URI::Escape;

my $NAME    = 'steiner:aliases';
my $VERSION = '1.0';

register($NAME, $VERSION, "General aliases by ScottSteiner");

IRC::add_command_handler("bing", "bing");
IRC::add_command_handler("chansetup", "channelSetup");
IRC::add_command_handler("ig", "fakeIgnoreLong");
IRC::add_command_handler("fakeignore", "fakeIgnoreShort");
IRC::add_command_handler("nicks","nicks");
IRC::add_command_handler("np","np");
IRC::add_command_handler("slap","slap");

sub bing {
	my $url = uri_escape(@_);
	command("say http://letmebingthatforyou.com/?q=$url");
	return 1;
}
sub channelSetup {
	command("cs set @_ ownermode on");
	command("cs set @_ protectmode on");
	#Edit this before using it, unless you want my bot to be an sop in your channel when you set it up
	command("cs sop @_ add rms");
	return 1;
}

sub fakeIgnoreLong {
	command("say @_: I have put you on a permanent ignore, public and private. I have found you disturbing, rude and generally not worth talking to. According to the channels you hang on, it strengtens the effect of wanting to put you on ignore because of my lack of interest in you as a person. This message is not meant to be rude to you, just to inform you that i won't see anything of what you type from now on.");
	return 1;
}

sub fakeIgnoreShort {
	command("say * Added @_!*\@* to ignore list");
	return 1;
}

sub nicks {
	my @ignore_opers	= ('killah','grimlock','wof','Xaquseg','GOD','xXx','djahandarie','rails','blake','Wintereise','Nol888','steak','__roflmao__','the user formerly known as GOD','darkfyre','rails');
	my @ignore_bakas	= ('nahu','enner','indel','taco','dr_venture','Swine','ralphie','snes9x','whalebiologist','leanpocket');
	my @ignore_bots	= ('netsec','ircstats','irc-stats','rms','twitterbot','glock','onee-chan','internets','limitserv','quotes','trivia','stats','DGbot','dickbeef','erepublik');
	my @userlist;
	my @ignorelist = (get_info("nick"),@ignore_opers,@ignore_bakas,@ignore_bots);
	my %ignorelist = map { $_ => 1 } @ignorelist;
	for my $nicklist ( get_list "users" ) {
		if (!exists $ignorelist{$nicklist->{nick}}) { push(@userlist, $nicklist->{nick}); }
	}
	command("say " . join(', ',@userlist));    
	return EAT_XCHAT;
}

sub np {
	my $filename = "$ENV{APPDATA}\\HexChat\\np.txt";
	open FILE, '<', $filename or die "Can't read file '$filename' [$!]\n"; 
	my $np = <FILE>; 
	close (FILE); 
	print $np;
	command("me $np");
	return 1;
}

sub slap {
	my $targ = $_[0];
	if ($targ) { $targ =~ s/\s+$//; } else { $targ = "you"; }
	command("me slaps $targ around a bit with a used condom");
	return 1;
}