from toee import *
import tpactions
import debugg

def GetActionName():
	return "Lethal Shock"

def GetActionDefinitionFlags():
	return D20ADF_None
	
def GetTargetingClassification():
	return D20TC_Target0

def GetActionCostType():
	return D20ACT_Standard_Action

def AddToSequence(d20action, action_seq, tb_status):
	action_seq.add_action(d20action)
	return AEC_OK