import random,os
from time import sleep
try:
	import pyfiglet
except ModuleNotFoundError:
	os.system('pip install pyfiglet')

text_logo = ("""
       ###    #####   ##### ###### ######  
      ## ##  ##   ## ##   ##  ##     ##    
     ##   ## ##      ##       ##     ##    
     ##   ##  #####  ##       ##     ##    
     #######      ## ##       ##     ##    
     ##   ## ##   ## ##   ##  ##     ##    
     ##   ##  #####   ##### ###### ###### 
================================================
           ORIGINAL CODE BY QAISER
================================================""")
def caseher():
	os.system('clear');print(text_logo)
	print('[01] Convert Text To Multi-ASCII [290+FONTS] ')
	print('[02] Convert Text To Single-ASCII [Random-FONT] ')
	print('[00] Exit/Close Program')
	print("================================================")
	select_kar=input("[•] Select : ")
	if select_kar in ["01","1"]:
		generator_qaiser_multi()
	if select_kar in ["02","2"]:
		generator_qaiser_single()
	if select_kar in ["00","0"]:
		exit('Thanks For Your Time ❤')
	else:
		print("Select Valid Option ! ")
		input('Press Enter To Run Again ');caseher()

def generator_qaiser_multi():
	os.system('clear');print(text_logo)
	extra = input(" ENTER YOUR TEXT : ")
	if extra=='':
		print('Dont Remain Empty');sleep(2)
		caseher()
	_file=open('/sdcard/logo.txt','w')
	for i in range(292):
		abbas = random.choice(['1943____', '3-d', '3x5', '4x4_offr', '5lineoblique', '5x7', '5x8', '64f1____', '6x10', '6x9', 'a_zooloo', 'acrobatic', 'advenger', 'alligator', 'alligator2', 'alphabet', 'aquaplan', 'arrows', 'asc_____', 'ascii___', 'assalt_m', 'asslt__m', 'atc_____', 'atc_gran', 'avatar', 'b_m__200', 'banner', 'banner3-D', 'banner3', 'banner4', 'barbwire', 'basic', 'battle_s', 'battlesh', 'baz__bil', 'beer_pub', 'bell', 'big', 'bigchief', 'binary', 'block', 'brite', 'briteb', 'britebi', 'britei', 'broadway', 'bubble', 'bubble__', 'bubble_b', 'bulbhead', 'c1______', 'c2______', 'c_ascii_', 'c_consen', 'calgphy2', 'caligraphy', 'catwalk', 'caus_in_', 'char1___', 'char2___', 'char3___', 'char4___', 'charact1', 'charact2', 'charact3', 'charact4', 'charact5', 'charact6', 'characte', 'charset_', 'chartr', 'chartri', 'chunky', 'clb6x10', 'clb8x10', 'clb8x8', 'cli8x8', 'clr4x6', 'clr5x10', 'clr5x6', 'clr5x8', 'clr6x10', 'clr6x6', 'clr6x8', 'clr7x10', 'clr7x8', 'clr8x10', 'clr8x8', 'coil_cop', 'coinstak', 'colossal', 'com_sen_', 'computer', 'contessa', 'contrast', 'convoy__', 'cosmic', 'cosmike', 'cour', 'courb', 'courbi', 'couri', 'crawford', 'cricket', 'cursive', 'cyberlarge', 'cybermedium', 'cybersmall', 'd_dragon', 'dcs_bfmo', 'decimal', 'deep_str', 'defleppard', 'demo_1__', 'demo_2__', 'demo_m__', 'devilish', 'diamond', 'digital', 'doh', 'doom', 'dotmatrix', 'double', 'drpepper', 'druid___', 'dwhistled', 'e__fist_', 'ebbs_1__', 'ebbs_2__', 'eca_____', 'eftichess', 'eftifont', 'eftipiti', 'eftirobot', 'eftitalic', 'eftiwall', 'eftiwater', 'epic', 'etcrvs__', 'f15_____', 'faces_of', 'fair_mea', 'fairligh', 'fantasy_', 'fbr12___', 'fbr1____', 'fbr2____', 'fbr_stri', 'fbr_tilt', 'fender', 'finalass', 'fireing_', 'flyn_sh', 'fourtops', 'fp1_____', 'fp2_____', 'fraktur', 'funky_dr', 'future_1', 'future_2', 'future_3', 'future_4', 'future_5', 'future_6', 'future_7', 'future_8', 'fuzzy', 'gauntlet', 'ghost_bo', 'goofy', 'gothic', 'gothic__', 'graceful', 'gradient', 'graffiti', 'grand_pr', 'greek', 'green_be', 'hades___', 'heavy_me', 'helv', 'helvb', 'helvbi', 'helvi', 'heroboti', 'hex', 'high_noo', 'hills___', 'hollywood', 'home_pak', 'house_of', 'hypa_bal', 'hyper___', 'inc_raw_', 'invita', 'isometric1', 'isometric2', 'isometric3', 'isometric4', 'italic', 'italics_', 'ivrit', 'jazmine', 'jerusalem', 'joust___', 'katakana', 'kban', 'kgames_i', 'kik_star', 'krak_out', 'larry3d', 'lazy_jon', 'lcd', 'letterw3', 'lexible_', 'lockergnome', 'madrid', 'marquee', 'mayhem_d', 'mcg_____', 'mike', 'mini', 'mirror', 'mnemonic', 'modern__', 'morse', 'mshebrew210', 'nancyj-underlined', 'nancyj', 'new_asci', 'nfi1____', 'nipples', 'npn_____', 'nvscript', 'ogre', 'os2', 'p_s_h_m_', 'p_skateb', 'pacos_pe', 'pawn_ins', 'pawp', 'peaks', 'pebbles', 'pod_____', 'poison', 'rad_____', 'rally_sp', 'rampage_', 'rastan__', 'rci_____', 'rectangles', 'relief2', 'rev', 'road_rai', 'rockbox_', 'roman', 'roman___', 'rounded', 'rowancap', 'runyc', 'sans', 'sansbi', 'sansi', 'sbookb', 'sbooki', 'script__', 'serifcap', 'shimrod', 'short', 'skate_ro', 'skateord', 'sketch_s', 'slant', 'slide', 'slscript', 'small', 'smkeyboard', 'smscript', 'smshadow', 'smslant', 'smtengwar', 'space_op', 'stampatello', 'standard', 'star_war', 'starwars', 'stellar', 'stencil1', 'stencil2', 'stop', 'street_s', 'subteran', 'tanja', 'tav1____', 'taxi____', 'thin', 'threepoint', 'ticksslant', 'tiles', 'tombstone', 'trek', 'tsalagi', 'tsn_base', 'twin_cob', 'unarmed_', 'univers', 'usa_____', 'usaflag', 'utopia', 'utopiab', 'war_of_w', 'wavy', 'whimsy', 'xbriteb', 'xbritebi', 'xbritei', 'xchartr', 'xcour', 'xcourb', 'xcouri', 'xhelvb', 'xhelvbi', 'xhelvi', 'xsans', 'xsansb', 'xsansbi', 'xsansi', 'xsbook', 'xsbookb', 'xsbookbi', 'xtimes', 'yie-ar__', 'z-pilot_', 'lean', 'letter_w', 'letters', 'linux', 'mad_nurs', 'magic_ma', 'master_o', 'maxfour', 'mig_ally', 'moscow', 'nancyj-fancy', 'notie_ca', 'ntgreek', 'o8', 'octal', 'odel_lak', 'ok_beer_', 'outrun__', 'panther_', 'pepper', 'phonix__', 'platoon2', 'platoon_', 'puffy', 'pyramid', 'r2-d2___', 'rad_phan', 'radical_', 'rainbow_', 'rally_s2', 'raw_recu', 'relief', 'ripper!_', 'rok_____', 'rot13', 'rozzo', 'runic', 'sansb', 'sblood', 'sbook', 'sbookbi', 'script', 'shadow', 'skateroc', 'sm______', 'smisome1', 'spc_demo', 'speed', 'stacey', 'stealth_', 'straight', 'super_te', 't__of_ap', 'tec1____', 'tec_7000', 'tecrvs__', 'tengwar', 'term', 'thick', 'ti_pan__', 'ticks', 'times', 'timesofl', 'tinker-toy', 'tomahawk', 'top_duck', 'trashman', 'triad_st', 'ts1_____', 'tsm_____', 'tty', 'ttyb', 'tubular', 'twopoint', 'type_set', 'ucf_fan_', 'ugalympi', 'usa_pq__', 'utopiabi', 'utopiai', 'vortron_', 'weird', 'xbrite', 'xchartri', 'xcourbi', 'xhelv', 'xsbooki', 'xtty', 'xttyb', 'yie_ar_k', 'zig_zag_', 'zone7___'])
		gen_qsr = pyfiglet.figlet_format(extra,font=abbas)
		_file.write(f"\t\t\t NO : {i} \n================================================\n{gen_qsr}================================================\n")
	print(" Generating Fonts ........");sleep(2.5)
	print(f"\033[1;92m Completed Fonts Saved in File \033[0m: /sdcard/logo.txt")
	ope=input(" Do You Want To Open File y/n ? ")
	if ope in ['n','N','no','No']:
		caseher()
	if ope in ['y','Yes','Y','yes']:
		os.system('termux-open /sdcard/logo.txt')
		input(" \tPress Enter To Go Back ")
		caseher()
	else:
		os.system('termux-open /sdcard/logo.txt')

def generator_qaiser_single():
	os.system('clear');print(text_logo)
	extra = input(" ENTER YOUR TEXT : ")
	abbas = random.choice(['1943____', '3-d', '3x5', '4x4_offr', '5lineoblique', '5x7', '5x8', '64f1____', '6x10', '6x9', 'a_zooloo', 'acrobatic', 'advenger', 'alligator', 'alligator2', 'alphabet', 'aquaplan', 'arrows', 'asc_____', 'ascii___', 'assalt_m', 'asslt__m', 'atc_____', 'atc_gran', 'avatar', 'b_m__200', 'banner', 'banner3-D', 'banner3', 'banner4', 'barbwire', 'basic', 'battle_s', 'battlesh', 'baz__bil', 'beer_pub', 'bell', 'big', 'bigchief', 'binary', 'block', 'brite', 'briteb', 'britebi', 'britei', 'broadway', 'bubble', 'bubble__', 'bubble_b', 'bulbhead', 'c1______', 'c2______', 'c_ascii_', 'c_consen', 'calgphy2', 'caligraphy', 'catwalk', 'caus_in_', 'char1___', 'char2___', 'char3___', 'char4___', 'charact1', 'charact2', 'charact3', 'charact4', 'charact5', 'charact6', 'characte', 'charset_', 'chartr', 'chartri', 'chunky', 'clb6x10', 'clb8x10', 'clb8x8', 'cli8x8', 'clr4x6', 'clr5x10', 'clr5x6', 'clr5x8', 'clr6x10', 'clr6x6', 'clr6x8', 'clr7x10', 'clr7x8', 'clr8x10', 'clr8x8', 'coil_cop', 'coinstak', 'colossal', 'com_sen_', 'computer', 'contessa', 'contrast', 'convoy__', 'cosmic', 'cosmike', 'cour', 'courb', 'courbi', 'couri', 'crawford', 'cricket', 'cursive', 'cyberlarge', 'cybermedium', 'cybersmall', 'd_dragon', 'dcs_bfmo', 'decimal', 'deep_str', 'defleppard', 'demo_1__', 'demo_2__', 'demo_m__', 'devilish', 'diamond', 'digital', 'doh', 'doom', 'dotmatrix', 'double', 'drpepper', 'druid___', 'dwhistled', 'e__fist_', 'ebbs_1__', 'ebbs_2__', 'eca_____', 'eftichess', 'eftifont', 'eftipiti', 'eftirobot', 'eftitalic', 'eftiwall', 'eftiwater', 'epic', 'etcrvs__', 'f15_____', 'faces_of', 'fair_mea', 'fairligh', 'fantasy_', 'fbr12___', 'fbr1____', 'fbr2____', 'fbr_stri', 'fbr_tilt', 'fender', 'finalass', 'fireing_', 'flyn_sh', 'fourtops', 'fp1_____', 'fp2_____', 'fraktur', 'funky_dr', 'future_1', 'future_2', 'future_3', 'future_4', 'future_5', 'future_6', 'future_7', 'future_8', 'fuzzy', 'gauntlet', 'ghost_bo', 'goofy', 'gothic', 'gothic__', 'graceful', 'gradient', 'graffiti', 'grand_pr', 'greek', 'green_be', 'hades___', 'heavy_me', 'helv', 'helvb', 'helvbi', 'helvi', 'heroboti', 'hex', 'high_noo', 'hills___', 'hollywood', 'home_pak', 'house_of', 'hypa_bal', 'hyper___', 'inc_raw_', 'invita', 'isometric1', 'isometric2', 'isometric3', 'isometric4', 'italic', 'italics_', 'ivrit', 'jazmine', 'jerusalem', 'joust___', 'katakana', 'kban', 'kgames_i', 'kik_star', 'krak_out', 'larry3d', 'lazy_jon', 'lcd', 'letterw3', 'lexible_', 'lockergnome', 'madrid', 'marquee', 'mayhem_d', 'mcg_____', 'mike', 'mini', 'mirror', 'mnemonic', 'modern__', 'morse', 'mshebrew210', 'nancyj-underlined', 'nancyj', 'new_asci', 'nfi1____', 'nipples', 'npn_____', 'nvscript', 'ogre', 'os2', 'p_s_h_m_', 'p_skateb', 'pacos_pe', 'pawn_ins', 'pawp', 'peaks', 'pebbles', 'pod_____', 'poison', 'rad_____', 'rally_sp', 'rampage_', 'rastan__', 'rci_____', 'rectangles', 'relief2', 'rev', 'road_rai', 'rockbox_', 'roman', 'roman___', 'rounded', 'rowancap', 'runyc', 'sans', 'sansbi', 'sansi', 'sbookb', 'sbooki', 'script__', 'serifcap', 'shimrod', 'short', 'skate_ro', 'skateord', 'sketch_s', 'slant', 'slide', 'slscript', 'small', 'smkeyboard', 'smscript', 'smshadow', 'smslant', 'smtengwar', 'space_op', 'stampatello', 'standard', 'star_war', 'starwars', 'stellar', 'stencil1', 'stencil2', 'stop', 'street_s', 'subteran', 'tanja', 'tav1____', 'taxi____', 'thin', 'threepoint', 'ticksslant', 'tiles', 'tombstone', 'trek', 'tsalagi', 'tsn_base', 'twin_cob', 'unarmed_', 'univers', 'usa_____', 'usaflag', 'utopia', 'utopiab', 'war_of_w', 'wavy', 'whimsy', 'xbriteb', 'xbritebi', 'xbritei', 'xchartr', 'xcour', 'xcourb', 'xcouri', 'xhelvb', 'xhelvbi', 'xhelvi', 'xsans', 'xsansb', 'xsansbi', 'xsansi', 'xsbook', 'xsbookb', 'xsbookbi', 'xtimes', 'yie-ar__', 'z-pilot_', 'lean', 'letter_w', 'letters', 'linux', 'mad_nurs', 'magic_ma', 'master_o', 'maxfour', 'mig_ally', 'moscow', 'nancyj-fancy', 'notie_ca', 'ntgreek', 'o8', 'octal', 'odel_lak', 'ok_beer_', 'outrun__', 'panther_', 'pepper', 'phonix__', 'platoon2', 'platoon_', 'puffy', 'pyramid', 'r2-d2___', 'rad_phan', 'radical_', 'rainbow_', 'rally_s2', 'raw_recu', 'relief', 'ripper!_', 'rok_____', 'rot13', 'rozzo', 'runic', 'sansb', 'sblood', 'sbook', 'sbookbi', 'script', 'shadow', 'skateroc', 'sm______', 'smisome1', 'spc_demo', 'speed', 'stacey', 'stealth_', 'straight', 'super_te', 't__of_ap', 'tec1____', 'tec_7000', 'tecrvs__', 'tengwar', 'term', 'thick', 'ti_pan__', 'ticks', 'times', 'timesofl', 'tinker-toy', 'tomahawk', 'top_duck', 'trashman', 'triad_st', 'ts1_____', 'tsm_____', 'tty', 'ttyb', 'tubular', 'twopoint', 'type_set', 'ucf_fan_', 'ugalympi', 'usa_pq__', 'utopiabi', 'utopiai', 'vortron_', 'weird', 'xbrite', 'xchartri', 'xcourbi', 'xhelv', 'xsbooki', 'xtty', 'xttyb', 'yie_ar_k', 'zig_zag_', 'zone7___'])
	gen_qsr = pyfiglet.figlet_format(extra,font=abbas)
	print(f"\n{gen_qsr}\n")
	input(" \tPress Enter To Go Back ")
	caseher()


caseher()