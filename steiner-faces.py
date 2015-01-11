#########################################################################################
# Name                  steiner:faces
# Description           Unicode Faces ( ◕ ◡ ◕ )
# Version               1.1 (2015-01-10)
# Contact               ScottSteiner@irc.rizon.net
# Website               https://github.com/ScottSteiner/xchat-scripts
# Copyright             2012-2015, ScottSteiner <nothingfinerthanscottsteiner@gmail.com>
# License               GPL version 3 or any later version; http://www.gnu.org/copyleft/gpl.html
#########################################################################################

import xchat

__module_name__ = 'steiner:faces'
__module_version__ = '1.1'
__module_description__ = 'Unicode faces'

faces = {
	'3'						: '( ¯3¯)',
	':)'					: '¯\_(ツ)_/¯',
	':3'					: '(◕ ‿‿‿ ◕)',
	':32'					: '(◕ ◡◡◡ ◕)',
	'A'						: '( ﾟдﾟ)',
	'alone'					: '(ツ) FOREVER ALONE',
	'arab'					: 'ا مبارك̴ı̴̴̡̡̡ ̡͌l̡̡̡ ̡͌l̡*̡̡ ̴̡ı̴̴̡ ̡̡͡|̲̲̲͡͡͡ ̲▫̲͡ ̲̲̲͡͡π̲̲͡͡ ̲̲͡▫̲̲͡͡ ̲|̡̡̡ ̡ ̴̡ı̴̡̡ ̡͌l̡̡̡ أضحى',
	'blush'					: '(\x034▰\x03˘◡˘\x034▰\x03)',
	'bomb'					: '(ノ゜o゜)ノ　　　　●～*　　　　　Σ(゜д゜)',
	'butterfly'				: 'Ƹ̵̡Ӝ̵̨̄Ʒ',
	'cry'					: '\x0311｡･ﾟ･\x03(ﾉД`)\x0311･ﾟ･｡\x03',
	'dozo'					: '(ﾉﾟ-ﾟ)ﾉ☆ DOZO',
	'fabulous'				: '＼( \x0313*\x03¯∇¯)ノ ☆\x0311Ｆ\x03\x039Ａ\x03\x0313Ｂ\x03\x034Ｕ\x03\x0310Ｌ\x03\x036Ｏ\x03\x0312Ｕ\x03\x032Ｓ\x03～☆',
	'fry'					: '≖_≖',
	'gun'					: '(☞ ಥ益ಥ）☞ ︻╦̵̵͇̿̿̿̿╤──',
	'heart'					: '( ´・‿-) ~ \x034♥',
	'katto'					: '---------ＫＡＴＴＯ---------(✂ﾟ∀ﾟ)✂',
	'love'					: '(⊃ ´ω`)⊃♥⊂(´ω` ⊂)',
	'mad'					: '\x034(╬ ಠ益ಠ)\x03',
	'nipples'				: ' \x031,0／ 人\x030# \x034◕\x030#####\x031‿‿\x030#####\x034 ◕\x030# \x031人 ＼',
	'nyoro'					: '(　´・ω・) nyoro~n',
	'o2'					: '(  ◡  )',
	'o'						: '( ◕ ◡ ◕ )',
	'o_o'					: 'ಠ_ಠ',
	'phone1'				: 'Σ(ﾟДﾟ )',
	'phone2'				: '( ﾟДﾟ)3-------------------------------------Σ(ﾟДﾟ )',
	'pig'					: '(=ﾟωﾟ)',
	'pika2'					: '(◕ ◡◡ ◕)ﾉ',
	'pika'					: '(◕ ◡◡ ◕)ﾉ<( PIKA PIKAAAAAAAAH)',
	'pitchfork'				: '(゜ν`(∋─━ლ(╹◡╹ )',
	'point'					: '(☞ﾟ∀ﾟ)☞',
	'pointback'				: '☜(ﾟ∀ﾟ☜)',
	'retard'				: 'ಥಿ೪ಥ',
	'ribbon'				: '( \x0313*\x03=‿=\x0313*\x03)',
	'rko'					: '\_____(◕ ◡◡◡ ◕)__________/',
	'scream'				: '( ﾟ∀ﾟ)ｱﾊﾊ八八ﾉヽﾉヽﾉヽﾉ ＼ / ＼/ ＼',
	'shrug'					: 'ヽ(；´Д｀)ノ',
	'spider'				: '_/¯¯/¯`(’·,.,·)´¯\¯¯\_',
	'star'					: 'ヾ(;☆ω☆)ノ',
	'swastika'				: '卐',
	'table2'				: '(ﾉಥ益ಥ）ﾉ ┻━┻',
	'table'					: '(ﾉ `Д´)ﾉ ~┻━━━┻',
	'tea'					: '(´ω`)っ旦~~ have a tea',
	'throwtable'			: '(ﾉ・∀・)ﾉ　＝＝＝＝＝┻━┻))⊙Дﾟ)･∵',
	'thumbsup'				: '(☝ﾟ∀ﾟ)☝',
	'two'					: 'ヽ(*^ｰ^)人(^ｰ^*)ノ',
	'twoleft'				: 'ヽ(*^ｰ^)ノ',
	'tworight'				: 'ヽ(^ｰ^*)ノ',
	'T_T'					: '〒_〒',
	'U'						: '( ﾟ∩ﾟ)',
	'umad'					: '( ﾟ∀ﾟ)ｱ u mad',
	'unlimitedtableworks'	: '┳━┳ ┻━┻ ┳━┳ ┻━┻ ┳━┳ ┻━┻ ┳━┳ ┻━┻~~~ヽ(\'～`；)ﾉ ~~~┻━┻ ┳━┳ ┻━┻ ┳━┳ ┻━┻ ┳━┳ ┻━┻ ┳━┳',
	'vuvezula'				: '( `)3\')▃▃▃▅▆▇▉BZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ',
	'wat'					: '┐(´д｀)┌',
	'wave'					: '(〜￣▽￣)〜',
	'why'					: 'щ(ﾟДﾟщ)',
	'why_'					: '┐（　｀ー´）┌',
	'wut'					: '┐(-｡ｰ;)┌',
	'yatta'					: 'ヽ(\' ▽\' )ノ !',
	'_'						: '（　｀ー´）',
	'_>'					: '（　´_ゝ｀）',
	'_A_'					: 'ヽ(　￣д￣;)ノ'
}

def face(text, text_eol, userdata):
	global faces
	try:
		xchat.command("say {}".format(faces[text[1]]))
	except IndexError:
		listfaces()
	return xchat.EAT_ALL

def listfaces():
	global faces
	for face in sorted(faces):
		print("{}: {}".format(face, faces[face]))
	return xchat.EAT_ALL
	
xchat.hook_command('face', face)
xchat.hook_command('listfaces', listfaces)

print('\00309{} {} has been loaded: {}\003'.format(__module_name__, __module_version__, __module_description__))