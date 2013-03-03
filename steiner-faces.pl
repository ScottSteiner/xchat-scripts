#########################################################################################
# Name                  steiner:faces
# Description           Unicode Faces ( ◕ ◡ ◕ )
# Version               1.0 (2013-03-03)
# Contact               ScottSteiner@irc.rizon.net
# Website               https://github.com/ScottSteiner/xchat-scripts
# Copyright             2012, ScottSteiner <nothingfinerthanscottsteiner@gmail.com>
# License               GPL version 3 or any later version; http://www.gnu.org/copyleft/gpl.html
#########################################################################################

use strict;
use warnings;
use Xchat qw( :all );

my $NAME    = 'steiner:faces';
my $VERSION = '1.0';

register($NAME, $VERSION, "steiner:faces - Unicode faces");

IRC::add_command_handler("face", "face");
IRC::add_command_handler("listfaces", "listfaces");

my %faces = (
	'3','( ¯3¯)',
	':)','¯\_(ツ)_/¯',
	':3','(◕ ‿‿‿ ◕)',
	':32','(◕ ◡◡◡ ◕)',
	'A','( ﾟдﾟ)',
	'alone','(ツ) FOREVER ALONE',
	'arab','ا مبارك̴ı̴̴̡̡̡ ̡͌l̡̡̡ ̡͌l̡*̡̡ ̴̡ı̴̴̡ ̡̡͡|̲̲̲͡͡͡ ̲▫̲͡ ̲̲̲͡͡π̲̲͡͡ ̲̲͡▫̲̲͡͡ ̲|̡̡̡ ̡ ̴̡ı̴̡̡ ̡͌l̡̡̡ أضحى',
	'blush','(4▰˘◡˘4▰)',
	'bomb','(ノ゜o゜)ノ　　　　●～*　　　　　Σ(゜д゜)',
	'butterfly','Ƹ̵̡Ӝ̵̨̄Ʒ',
	'cry','11｡･ﾟ･(ﾉД`)11･ﾟ･｡',
	'dozo','(ﾉﾟ-ﾟ)ﾉ☆ DOZO',
	'fabulous','＼(　13*¯∇¯)ノ ☆11Ｆ9Ａ13Ｂ4Ｕ10Ｌ6Ｏ12Ｕ2Ｓ～☆',
	'fry','≖_≖',
	'gun','(☞ ಥ益ಥ）☞ ︻╦̵̵͇̿̿̿̿╤──',
	'heart','( ´・‿-) ~ 4♥',
	'katto','---------ＫＡＴＴＯ---------(✂ﾟ∀ﾟ)✂',
	'love','(⊃ ´ω`)⊃♥⊂(´ω` ⊂)',
	'mad','4(╬ ಠ益ಠ)',
	'nipples',' 1,0／ 人0# 4◕0#####1‿‿0#####4 ◕0# 1人 ＼',
	'nyoro','(　´・ω・) nyoro~n',
	'o2','(  ◡  )',
	'o','( ◕ ◡ ◕ )',
	'o_o','ಠ_ಠ',
	'phone1','Σ(ﾟДﾟ )',
	'phone2','( ﾟДﾟ)3-------------------------------------Σ(ﾟДﾟ )',
	'pig','(=ﾟωﾟ)',
	'pika2','(◕ ◡◡ ◕)ﾉ',
	'pika','(◕ ◡◡ ◕)ﾉ<( PIKA PIKAAAAAAAAH)',
	'pitchfork','(゜ν`(∋─━ლ(╹◡╹ )',
	'point','(☞ﾟ∀ﾟ)☞',
	'pointback','☜(ﾟ∀ﾟ☜)',
	'retard','ಥಿ೪ಥ',
	'ribbon','( 13*=‿=13*)',
	'rko','\_____(◕ ◡◡◡ ◕)__________/',
	'scream','( ﾟ∀ﾟ)ｱﾊﾊ八八ﾉヽﾉヽﾉヽﾉ ＼ / ＼/ ＼',
	'shrug','ヽ(；´Д｀)ノ',
	'spider','_/¯¯/¯`(’·,.,·)´¯\¯¯\_',
	'star','ヾ(;☆ω☆)ノ',
	'swastika','卐',
	'table2','(ﾉಥ益ಥ）ﾉ ┻━┻',
	'table','(ﾉ `Д´)ﾉ ~┻━━━┻',
	'tea','(´ω`)っ旦~~ have a tea',
	'throwtable','(ﾉ・∀・)ﾉ　＝＝＝＝＝┻━┻))⊙Дﾟ)･∵',
	'thumbsup','(☝ﾟ∀ﾟ)☝',
	'two','ヽ(*^ｰ^)人(^ｰ^*)ノ',
	'twoleft','ヽ(*^ｰ^)ノ',
	'tworight','ヽ(^ｰ^*)ノ',
	'T_T','〒_〒',
	'U','( ﾟ∩ﾟ)',
	'umad','( ﾟ∀ﾟ)ｱ u mad',
	'unlimitedtableworks','┳━┳ ┻━┻ ┳━┳ ┻━┻ ┳━┳ ┻━┻ ┳━┳ ┻━┻~~~ヽ(\'～`；)ﾉ ~~~┻━┻ ┳━┳ ┻━┻ ┳━┳ ┻━┻ ┳━┳ ┻━┻ ┳━┳',
	'vuvezula','( `)3\')▃▃▃▅▆▇▉BZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ',
	'wat','┐(´д｀)┌',
	'wave','(〜￣▽￣)〜',
	'why','щ(ﾟДﾟщ)',
	'why_','┐（　｀ー´）┌',
	'wut','┐(-｡ｰ;)┌',
	'yatta','ヽ(\' ▽\' )ノ !',
	'_','（　｀ー´）',
	'_>','（　´_ゝ｀）',
	'_A_','ヽ(　￣д￣;)ノ'
);

sub face {
	IRC::command("/say $faces{\"@_\"}");
	return EAT_XCHAT;
}
sub listfaces {
	foreach my $key (sort keys(%faces) ) {
		IRC::print("$key = $faces{$key}");
	}
	return EAT_XCHAT;
}