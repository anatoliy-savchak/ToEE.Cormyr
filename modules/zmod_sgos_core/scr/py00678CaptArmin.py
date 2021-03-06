from toee import *
from utilities import *
from scripts import *
from combat_standard_routines import *
import shattered_consts


def san_dialog( attachee, triggerer ):
	attachee.turn_towards(triggerer)
	if not attachee.has_met( triggerer ):
		triggerer.begin_dialog( attachee, 1 )
	else:
		if anyone( game.leader.group_list(), "has_follower", 14957 ):
			triggerer.begin_dialog( attachee, 400 )
			return SKIP_DEFAULT			
		elif game.quests[shattered_consts.QUEST_LUMINOSITY].state == qs_accepted:
			triggerer.begin_dialog( attachee, 100 )
			return SKIP_DEFAULT
		elif game.quests[shattered_consts.QUEST_LUMINOSITY].state == qs_mentioned:
			triggerer.begin_dialog( attachee, 150 )
			return SKIP_DEFAULT
		elif game.quests[shattered_consts.QUEST_PICKING_AT_THE_SCAR].state == qs_accepted:
			triggerer.begin_dialog( attachee, 200 )                 # you have to accept the next quest once 3 is completed atm
			return SKIP_DEFAULT
		else:
			triggerer.begin_dialog( attachee, 300 )                 # indicates something went wrong
			return SKIP_DEFAULT
	return SKIP_DEFAULT

def san_first_heartbeat( attachee, triggerer ):
	if game.global_flags[12] == 1:
		attachee.object_flag_unset(OF_OFF)
		attachee.turn_towards(game.leader)
		attachee.scripts[19] = 678
		game.new_sid = 0
		return RUN_DEFAULT
	return RUN_DEFAULT

def san_dying( attachee, triggerer ):
	return RUN_DEFAULT

def san_resurrect( attachee, triggerer ):
	return RUN_DEFAULT

def san_heartbeat( attachee, triggerer ):
	for obj in game.obj_list_vicinity(attachee.location,OLC_PC):
		attachee.turn_towards(obj)
		if (is_safe_to_talk(attachee,obj)):
			obj.begin_dialog(attachee,1)
			game.new_sid = 0
			return RUN_DEFAULT
	return RUN_DEFAULT

def buttin( attachee, triggerer):
	npc = find_npc_near(attachee,14957)
	if (npc != OBJ_HANDLE_NULL):
		triggerer.begin_dialog(npc,600)
		npc.turn_towards(triggerer)
		attachee.turn_towards(npc)
	else:
		triggerer.begin_dialog(attachee,420)
	return SKIP_DEFAULT