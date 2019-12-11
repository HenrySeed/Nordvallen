from NPC import NPC, DialogNode


arry_npc = NPC("'Arry")

arry_dialog_0 = DialogNode("Anything else?")

arry_dialog_1 = DialogNode("Hey there mate, how can I help?", arry_dialog_0)
arry_dialog_2 = DialogNode("Well, I moved here when my ol Dorris passed, oh that must of been 7 years back? I couldn't stay in Noamsted, too many memories.")
arry_dialog_3 = DialogNode("Used to be quite nice... used to be", arry_dialog_0)
arry_dialog_4 = DialogNode("Well, I myself like to fish, not very good at it but helps pass the time.")
arry_dialog_5 = DialogNode("Ha Ha Ha Ha, well I definitely wouldn't know anything about that. Im all legit, 100% all import export... uh fish that is.")
arry_dialog_6 = DialogNode("Despite my appearance, I used to live a very different life. If I had realised Dorris would be caught up in it, I would have moved a long time ago.", arry_dialog_0)

arry_dialog_0.responses = [
    ["How long have you lived here for?", arry_dialog_2], 
    ["What do you do around here?", arry_dialog_4]
]
arry_dialog_2.responses = [
    ["How did you like Noamsted?", arry_dialog_3], 
    ["Im sorry to hear that, how did she pass?", arry_dialog_6]
]
arry_dialog_4.responses = [
    ["There seem to be a lot of fishermen around here, almost more than there are fishing boats, or fish for that matter", arry_dialog_5]
]
arry_dialog_5.responses = [
    ["Sure...", arry_dialog_0]
]

arry_npc.dialog_start = arry_dialog_1

