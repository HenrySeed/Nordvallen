from NPC import NPC, DialogNode


arry_npc = NPC("'Arry")

arry_dialog_1 = DialogNode("Hey there mate, how can I help?")
arry_dialog_2 = DialogNode("Well, I moved here when my ol Dorris passed, oh that must of been 7 years back? I couldnt stay in Noamsted, too many memories.")
arry_dialog_3 = DialogNode("Used to be quite nice... used to be")


arry_dialog_1.responses = [["How long have you lived here for?", arry_dialog_2]]
arry_dialog_2.responses = [["How did you like Noamsted?", arry_dialog_3]]

arry_npc.dialog_start = arry_dialog_1

