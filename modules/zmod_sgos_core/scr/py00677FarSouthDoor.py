import toee, utils_npc, shattered_consts, startup_zmod

def san_use(attachee, triggerer):
	assert isinstance(attachee, toee.PyObjHandle)
	assert isinstance(triggerer, toee.PyObjHandle)

	npc = toee.game.obj_create(14026, triggerer.location)
	triggerer.turn_towards(attachee)
	triggerer.begin_dialog(npc, 1)
	return toee.SKIP_DEFAULT

def san_dialog( attachee, triggerer ):
	assert isinstance(attachee, toee.PyObjHandle)
	assert isinstance(triggerer, toee.PyObjHandle)

	startup_zmod.zmod_templeplus_config_apply()
	triggerer.begin_dialog(npc, 1)
	return toee.SKIP_DEFAULT

def distance_sumbertone_to_shattered_lab_sec():
	miles = 50
	total_hours = utils_npc.travel_hours_to_day_hours(utils_npc.pc_travel_time_calc_hours(miles))
	total_seconds = (int)(total_hours * 60*60)
	return total_seconds

def distance_sumbertone_to_shattered_temple_sec():
	miles = 140
	total_hours = utils_npc.travel_hours_to_day_hours(utils_npc.pc_travel_time_calc_hours(miles))
	total_seconds = (int)(total_hours * 60*60)
	return total_seconds

def distance_sumbertone_to_shattered_armory_sec():
	miles = 250
	total_hours = utils_npc.travel_hours_to_day_hours(utils_npc.pc_travel_time_calc_hours(miles))
	total_seconds = (int)(total_hours * 60*60)
	return total_seconds