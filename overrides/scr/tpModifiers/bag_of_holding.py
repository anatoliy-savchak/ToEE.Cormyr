import toee, templeplus.pymod, tpdp, debug, sys, traceback

###################################################

def GetConditionName():
	return "Bag_Of_Holding"

print("Registering " + GetConditionName())
###################################################

def items_get(npc, unwield_all = 1):
	assert isinstance(npc, toee.PyObjHandle)
	otype = npc.type
	invenField = 0
	invenNumField = 0
	if ((otype == toee.obj_t_npc) or (otype == toee.obj_t_pc)):
		invenField = toee.obj_f_critter_inventory_list_idx
		invenNumField = toee.obj_f_critter_inventory_num
	elif ((otype == toee.obj_t_container) or (otype == toee.obj_t_bag)):
		invenField = toee.obj_f_container_inventory_list_idx
		invenNumField = toee.obj_f_container_inventory_num
	else:
		invenField = toee.obj_f_critter_inventory_list_idx
		invenNumField = toee.obj_f_critter_inventory_num
	numItems = npc.obj_get_int(invenNumField)
	result = list()
	print("numItems: {}".format(numItems))
	if (numItems > 0):
		#debugg.breakp("numItems")
		if (unwield_all):
			for i in range(toee.item_wear_helmet, toee.item_wear_lockpicks):
				npc.item_worn_unwield(i, 0)

		for i in range(0, 199):
			item = npc.inventory_item(i)
			if (item):
				print(item)
				result.append(item)
				numItems -= 1
			if (numItems <=0): break
	print(result)
	return result

def item_clear_all(npc):
	assert isinstance(npc, toee.PyObjHandle)
	#breakp("inventory clear_all")
	item_unwield_all(npc)
	otype = npc.type
	invenField = 0
	invenNumField = 0
	if ((otype == toee.obj_t_npc) or (otype == toee.obj_t_pc)):
		invenField = toee.obj_f_critter_inventory_list_idx
		invenNumField = toee.obj_f_critter_inventory_num
	elif ((otype == toee.obj_t_container) or (otype == toee.obj_t_bag)):
		invenField = toee.obj_f_container_inventory_list_idx
		invenNumField = toee.obj_f_container_inventory_num
	else:
		invenField = toee.obj_f_critter_inventory_list_idx
		invenNumField = toee.obj_f_critter_inventory_num

	#print("invenField: {}, invenNumField: {}".format(invenField, invenNumField))
	numItems = npc.obj_get_int(invenNumField)
	#print("Inventory count {} for obj {}".format(numItems, npc))
	if (numItems > 0):
		for i in range(0, 199):
			#itemProto = npc.obj_get_idx_obj(invenField, i)
			#item = npc.item_find(4077)
			item = npc.inventory_item(i)
			#print("Item at {}: {}".format(i, item))
			if (item != toee.OBJ_HANDLE_NULL):
				numItems = numItems - 1
				item.destroy()
			if (numItems <=0): break

	return numItems

Bag_Of_Holding_Support = "Bag_Of_Holding_Support"

def Bag_Of_Holding_OnBuildRadialMenuEntry(attachee, args, evt_obj):
	radial_parent = tpdp.RadialMenuEntryParent("Bag of Holding")
	radial_parent_id = radial_parent.add_child_to_standard(attachee, tpdp.RadialMenuStandardNode.Items)

	radial_action = tpdp.RadialMenuEntryPythonAction("Inventory", toee.D20A_PYTHON_ACTION, 3006, 0, "TAG_INTERFACE_HELP")
	#assert isinstance(radial_action, tpdp.RadialMenuEntryParent)
	radial_action.add_as_child(attachee, radial_parent_id)
	#radial_action.add_child_to_standard(attachee, tpdp.RadialMenuStandardNode.Items)

	radial_action = tpdp.RadialMenuEntryPythonAction("Examine bodies", toee.D20A_PYTHON_ACTION, 3007, 0, "TAG_INTERFACE_HELP")
	#assert isinstance(radial_action, tpdp.RadialMenuEntryParent)
	#radial_action.add_child_to_standard(attachee, tpdp.RadialMenuStandardNode.Items)
	radial_action.add_as_child(attachee, radial_parent_id)

	radial_action = tpdp.RadialMenuEntryPythonAction("Transfer from bodies", toee.D20A_PYTHON_ACTION, 3008, 0, "TAG_INTERFACE_HELP")
	#assert isinstance(radial_action, tpdp.RadialMenuEntryParent)
	#radial_action.add_child_to_standard(attachee, tpdp.RadialMenuStandardNode.Items)
	radial_action.add_as_child(attachee, radial_parent_id)

	radial_action = tpdp.RadialMenuEntryPythonAction("List contents", toee.D20A_PYTHON_ACTION, 3009, 0, "TAG_INTERFACE_HELP")
	#assert isinstance(radial_action, tpdp.RadialMenuEntryParent)
	#radial_action.add_child_to_standard(attachee, tpdp.RadialMenuStandardNode.Items)
	radial_action.add_as_child(attachee, radial_parent_id)
	return 0

def Bag_Of_Holding_OnD20PythonActionPerform_3006(attachee, args, evt_obj):
	assert isinstance(attachee, toee.PyObjHandle)
	assert isinstance(args, tpdp.EventArgs)
	assert isinstance(evt_obj, tpdp.EventObjD20Action)
	#debug.breakp("Lodged_Quills_OnD20PythonActionPerform start")
	try:
		#debug.breakp("Bag_Of_Holding_OnD20PythonActionPerform")
		for pc in toee.game.party:
			pc.condition_add(Bag_Of_Holding_Support)

		prev_chest = FindChest()
		if (prev_chest): prev_chest.destroy()
		bag = toee.game.obj_create(1300, attachee.location)
		do_invisible = "anim_goal_use_object" in dir(attachee)
		#do_invisible = 0
		if (do_invisible):
			bag.object_flag_set(toee.OF_DONTDRAW)
			bag.move(attachee.location)
			attachee.anim_goal_use_object(bag)
			#attachee.container_open_ui(bag)
	except Exception, e:
		print "Bag_Of_Holding_OnD20PythonActionPerform:"
		print '-'*60
		traceback.print_exc(file=sys.stdout)
		print '-'*60		
	return 1

def Bag_Of_Holding_OnD20PythonActionPerform_3007(attachee, args, evt_obj):
	assert isinstance(attachee, toee.PyObjHandle)
	assert isinstance(args, tpdp.EventArgs)
	assert isinstance(evt_obj, tpdp.EventObjD20Action)
	#debug.breakp("Lodged_Quills_OnD20PythonActionPerform start")
	try:
		print("Bag_Of_Holding_OnD20PythonActionPerform_3007")
		for body in toee.game.obj_list_range(attachee.location, 20, toee.OLC_NPC):
			hp = body.stat_level_get(toee.stat_hp_current)
			print("{} hp in {}".format(hp, body))
			if (hp >= 0): continue
			if (not attachee.can_see(body)): continue
			items = items_get(body)
			#items = body.inventory_items()
			print("items: {}".format(len(items)))
			if (items):
				for item in items:
					assert isinstance(item, toee.PyObjHandle)
					text = item.description
					print("{}: {}".format(text, body))
					color = toee.tf_yellow
					tpe = item.type
					if ((tpe >= toee.obj_t_weapon) and (tpe <= toee.obj_t_armor)):
						if (item.item_flags_get() & toee.OIF_IS_MAGICAL): 
							color = toee.tf_blue
					elif ((tpe == toee.obj_t_food) or (tpe == toee.obj_t_scroll) or (tpe == toee.obj_t_generic)):
						color = toee.tf_green
					elif ((tpe == toee.obj_t_key) or (tpe == toee.obj_t_written)):
						color = toee.tf_light_blue
					body.float_text_line(text, color)
					weight = item.obj_get_int(toee.obj_f_item_weight)
					text = "*. {}. {} lb\n".format(text, weight)
					toee.game.create_history_freeform(text)
	except Exception, e:
		print "Bag_Of_Holding_OnD20PythonActionPerform_3007:"
		print '-'*60
		traceback.print_exc(file=sys.stdout)
		print '-'*60		
	return 1

def Bag_Of_Holding_OnD20PythonActionPerform_3008(attachee, args, evt_obj):
	assert isinstance(attachee, toee.PyObjHandle)
	assert isinstance(args, tpdp.EventArgs)
	assert isinstance(evt_obj, tpdp.EventObjD20Action)
	#debug.breakp("Lodged_Quills_OnD20PythonActionPerform start")
	try:
		#debug.breakp("Bag_Of_Holding_OnD20PythonActionPerform")
		prev_chest = FindChest()
		if (prev_chest): prev_chest.destroy()
		bag = toee.game.obj_create(1300, attachee.location)
		do_invisible = "anim_goal_use_object" in dir(attachee)
		#do_invisible = 0
		if (do_invisible):
			bag.object_flag_set(toee.OF_DONTDRAW)
			bag.move(attachee.location)

		# force load
		bag.object_script_execute(attachee, 0x01) #sn_use
		modified = 0
		for body in toee.game.obj_list_range(attachee.location, 20, toee.OLC_NPC):
			hp = body.stat_level_get(toee.stat_hp_current)
			print("{} hp in {}".format(hp, body))
			if (hp >= 0): continue
			if (not attachee.can_see(body)): continue
			items = items_get(body)
			#items = body.inventory_items()
			print("items: {}".format(len(items)))
			if (items):
				for item in items:
					assert isinstance(item, toee.PyObjHandle)
					text = item.description
					print("{}: {}".format(text, body))
					color = toee.tf_yellow
					tpe = item.type
					if ((tpe >= toee.obj_t_weapon) and (tpe <= toee.obj_t_armor)):
						if (item.item_flags_get() & toee.OIF_IS_MAGICAL): 
							color = toee.tf_blue
					elif ((tpe == toee.obj_t_food) or (tpe == toee.obj_t_scroll) or (tpe == toee.obj_t_generic)):
						color = toee.tf_green
					elif ((tpe == toee.obj_t_key) or (tpe == toee.obj_t_written)):
						color = toee.tf_light_blue
					if (not modified):
						toee.game.create_history_freeform("Transferred:\n")
					body.float_text_line(text, color)
					weight = item.obj_get_int(toee.obj_f_item_weight)
					text = "*. {}. {} lb\n".format(text, weight)
					toee.game.create_history_freeform(text)
					bag.item_get(item)
					modified = 1
		if (modified):
			toee.game.create_history_freeform("\n")
			# force save
			bag.object_script_execute(attachee, 0x20) #sn_transfer
		attachee.anim_goal_use_object(bag)
		#attachee.container_open_ui(bag)
	except Exception, e:
		print "Bag_Of_Holding_OnD20PythonActionPerform_3008:"
		print '-'*60
		traceback.print_exc(file=sys.stdout)
		print '-'*60		
	return 1

def sell_modifier():
	highest_appraise = -999
	for obj in toee.game.party:
		if obj.skill_level_get(toee.skill_appraise) > highest_appraise:
			highest_appraise = obj.skill_level_get(toee.skill_appraise)
	if highest_appraise > 19:
		return 0.97
	elif highest_appraise < -13:
		return 0
	else:
		return 0.4 + float(highest_appraise)*0.03

def Bag_Of_Holding_OnD20PythonActionPerform_3009(attachee, args, evt_obj):
	assert isinstance(attachee, toee.PyObjHandle)
	assert isinstance(args, tpdp.EventArgs)
	assert isinstance(evt_obj, tpdp.EventObjD20Action)
	#debug.breakp("Lodged_Quills_OnD20PythonActionPerform start")
	try:
		#debug.breakp("Bag_Of_Holding_OnD20PythonActionPerform")
		prev_chest = FindChest()
		if (prev_chest): prev_chest.destroy()
		bag = toee.game.obj_create(1300, attachee.location)
		do_invisible = "anim_goal_use_object" in dir(attachee)
		#do_invisible = 0
		if (do_invisible):
			bag.object_flag_set(toee.OF_DONTDRAW)
			bag.move(attachee.location)

		# force load
		bag.object_script_execute(attachee, 0x01) #sn_use
		toee.game.create_history_freeform("Bag of Holding contents:\n")
		items = items_get(bag, 0)
		num = 0
		total_lb = 0
		total_gp = 0
		sm = sell_modifier()
		total_gp_sell = 0.0
		for item in items:
			num +=1
			weight = item.obj_get_int(toee.obj_f_item_weight)
			total_lb += weight
			text = item.description
			worth = item.obj_get_int(toee.obj_f_item_worth)
			worth_gp = worth // 100
			total_gp += worth_gp
			total_gp_sell += worth_gp * sm
			x2 = ""
			x = item.obj_get_int(toee.obj_f_item_quantity)
			if (x > 1): x2 = " x{}".format(x)
			text = "{:02d}. {}{}.\n   {} lb. {} gp.\n".format(num, text, x2, weight, worth_gp)
			toee.game.create_history_freeform(text)
		if (num):
			toee.game.create_history_freeform("---------\n")
			text = "Total: {} lb, {} gp, sell: {} gp\n".format(total_lb, total_gp, int(total_gp_sell))
			toee.game.create_history_freeform(text)
		toee.game.create_history_freeform("\n")
		attachee.anim_goal_use_object(bag)
		#attachee.container_open_ui(bag)
	except Exception, e:
		print "Bag_Of_Holding_OnD20PythonActionPerform_3009:"
		print '-'*60
		traceback.print_exc(file=sys.stdout)
		print '-'*60		
	return 1

def FindChest():
	for obj in toee.game.obj_list_vicinity(toee.game.leader.location, toee.OLC_CONTAINER):
		if (obj.proto == 1300 and not obj.object_flags_get() & toee.OF_DESTROYED):
			return obj
	return None

def Bag_Of_Holding_S_Inventory_Update(attachee, args, evt_obj):
	#print("Bag_Of_Holding_S_Inventory_Update {}".format(attachee))
	#debug.breakp("Bag_Of_Holding_S_Inventory_Update")
	bag = FindChest()
	if (not bag): return 0
	#print("toee.game.char_ui_display_type: {}".format(toee.game.char_ui_display_type))
	#target = attachee #did not work
	target = toee.game.leader
	bag.object_script_execute(target, 0x20) #sn_transfer
	
	# check if Bag_Of_Holding_timed_destroy started running
	if (not bag.object_flags_get() & toee.OF_INVISIBLE):
		bag.object_flag_set(toee.OF_INVISIBLE)
		bag.object_flag_set(toee.OF_DONTDRAW)
		Bag_Of_Holding_timed_destroy(bag, 1000)
	return 0

def Bag_Of_Holding_timed_destroy(bag, time):
	assert isinstance(bag, toee.PyObjHandle)
	toee.game.timevent_add(_Bag_Of_Holding_destroy_on_timeevent, (bag), time) # 1000 = 1 second
	return

def _Bag_Of_Holding_destroy_on_timeevent(bag):
	assert isinstance(bag, toee.PyObjHandle)
	#print("_Bag_Of_Holding_destroy_on_timeevent toee.game.char_ui_display_type: {}".format(toee.game.char_ui_display_type))
	if (not bag.object_flags_get() & toee.OF_DESTROYED):
		is_invetory_screen_opened = 0
		if ("char_ui_display_type" in dir(toee.game)):
			is_invetory_screen_opened = toee.game.char_ui_display_type

		#is_invetory_screen_opened = 0
		if (not is_invetory_screen_opened):
			print("Bag_Of_Holding_S_Inventory_Update destroying bag {}".format(bag))
			bag.destroy()
		else:
			Bag_Of_Holding_timed_destroy(bag, 1000)
	return 1

modObj = templeplus.pymod.PythonModifier(GetConditionName(), 2) # 0 - type
modObj.AddHook(toee.ET_OnBuildRadialMenuEntry, toee.EK_NONE, Bag_Of_Holding_OnBuildRadialMenuEntry, ())
modObj.AddHook(toee.ET_OnD20PythonActionPerform, 3006, Bag_Of_Holding_OnD20PythonActionPerform_3006, ())
modObj.AddHook(toee.ET_OnD20PythonActionPerform, 3007, Bag_Of_Holding_OnD20PythonActionPerform_3007, ())
modObj.AddHook(toee.ET_OnD20PythonActionPerform, 3008, Bag_Of_Holding_OnD20PythonActionPerform_3008, ())
modObj.AddHook(toee.ET_OnD20PythonActionPerform, 3009, Bag_Of_Holding_OnD20PythonActionPerform_3009, ())
#modObj.AddHook(toee.ET_OnD20Signal, toee.EK_S_Inventory_Update, Bag_Of_Holding_S_Inventory_Update, ())

modObj2 = templeplus.pymod.PythonModifier(Bag_Of_Holding_Support, 2) # 
modObj2.AddHook(toee.ET_OnD20Signal, toee.EK_S_Inventory_Update, Bag_Of_Holding_S_Inventory_Update, ())