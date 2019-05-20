import time
import sys
import textwrap
import os
import colorama
from colorama import Fore,Style
import random

#Default printing function
def nicePrint(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)

#Printing function for menacing situtaions
def nicePrintMenacing(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.07)
#Red printing function
def nicePrintRed(text):
    for char in text:
        sys.stdout.write(Fore.RED + char +Style.RESET_ALL)
        sys.stdout.flush()
        time.sleep(0.05)
#Green printing fucntion    
def nicePrintGreen(text):
    for char in text:
        sys.stdout.write(Fore.GREEN + char +Style.RESET_ALL)
        sys.stdout.flush()
        time.sleep(0.05)


#Inventory object used for storing items in the game, with starting items
items = {"lock pick": """not much more than a piece of metal but very useful for opening
locks not meant to be opened by you, it will break after one use.""",
         "dagger": """useful for slitting ropes and thorats, it will not be effective as a combat weapon""",
         "prize": """not sure what it is, it's shape is of a small ball,
you think it's made out of copper and silver,
decorated by very detailed carvings, it looks like it could probbably be opened.
It is warm to the touch!!!
Or is it just your cold hands?!?""",
        "traveling papers":"""on first glance these could pass as a real Imperial document,
but for a keen eye nothing but a forgery.""",
"20 schillings":"enough to buy a couple of beers but not enough to get you out of any real trouble"}

#Function that implements the inventory mechanism
def inventory(itmes, caller_text):
    manipulatable_items=["prize", "20 schillings", "fish and hook", "pipe", "hook", "rope" ]
    print()
    print("Your inventory contains : ")
    for item in items:
        print(f"--{item}")
    print()
    choice = input("More DETAILS on an item, MANIPULATE an item or CLOSE inventory : ")
    if choice.lower() == "details":
        item_detail = input("More info on an item : ")
        if item_detail in items:
            nicePrint(items.get(item_detail))
            print()
            inventory(items, caller_text)
        else:
            nicePrint("No such item.")
            print()
            inventory(items, caller_text)
    elif choice.lower() == "manipulate":
        item = input("Which item :")
        if item in manipulatable_items:
            if item == "prize":
                nicePrint("You try to find a way to open it but with no effect, maybe with adecvate tools.")
            elif item == "fish and hook":
                nicePrint("You remove the fish from a hook and you have a fish and a hook.")
                del items["fish and hook"]
                items.update({"hook":"a heavy hook, not very sharp, it has a metal circle for attaching a rope, it could be used as makeshift weapon"})
                items.update({"fish":"a fish, dead but still fresh, you don't know what kind of a fish it is."})
                inventory(items, caller_text)
            elif item == "20 schillings":
                nicePrint("You count the money and it is still 20.")
                inventory(items, caller_text)
            elif item == "pipe":
                nicePrint("""You take a smoke from the pipe, the tobacco is cheap and bad, 
the best you had in days. The pipe glows with embers.""")
                inventory(items, caller_text)
            elif item == "rope":
                if "hook" in items:
                    nicePrint("You tie the rope on the hooks ring and make a grappling hook")
                    del items["hook"]
                    del items["rope"]
                    items.update({"grappling hook":"rope with a hook at the end, in skillful hands it could be used to scale walls, your hands are skillful."})
                else:
                    nicePrint ("You unroll the rope, there is enough to reach the roof of the outpost.")
                inventory(items, caller_text)
            elif item == "hook" :
                if "rope" in items:
                    nicePrint("You tie the rope on the hooks ring and make a grappling hook")
                    del items["hook"]
                    del items["rope"]
                    items.update({"grappling hook":"rope with a hook at the end, in skillful hands it could be used to scale walls, your hands are skillful."})
                else:
                    nicePrint ("The hook is large enough to be used as weapon, you swing a couple of times to get the feel.")
                inventory(items, caller_text)
        else:
            nicePrint("You can't manipulate that object.")
            inventory(items, caller_text)
    elif choice.lower() == "close":
        print(caller_text)
        pass
    else:
        nicePrint("You can't do that.")
        print()
        inventory(items, caller_text)

#Function that implements the options choosing mechanism
def getcmd(cmd_list):

    cmd = input("What do you do : \n")
    if cmd in cmd_list:
        return cmd
    elif cmd.lower() == "help":
        print("""\n How to play : type your input + enter, 
        sometimes you can enter commands that are not on the menu.
        Use your imagination and have fun! 
        'inventory' to view your inventory or 'q' to quit
        You can always type 'help' for help""")
        return getcmd(cmd_list)
    elif cmd.lower() == "inventory":
        if combat :
            nicePrint("You can not open inventory with enemies nearby.\n")
            return getcmd(cmd_list)
        else:
            inventory(items, caller_text)
            return getcmd(cmd_list)
    elif cmd.lower() == "credits":
        print("""Scenario by Radoš, Rastko, Nik, tehnical advice by Mrki\n""")
        return getcmd(cmd_list)
    elif cmd.lower() == "quit" or cmd.lower() =="q":
        nicePrint("You leave your fate in Sigmar's hands")
        print()
        nicePrint("Auf wiederzhn!.\n")
        time.sleep(3)
        sys.exit(1)
    else:
        print("You can not do that, try something else.")
        return getcmd(cmd_list)



#If the Wardens on the front are permanently eliminated
wardens_eliminated = False
#How many times the player has been on the first location, if > 3 the Wardens return
start_counter = 0
#If the starting location has been searched
start_searched = False

#Starting location
def start(items):

    def start_search( ):
        global start_searched
        if "stone" in items:
            nicePrint("You already have a stone.")
            start(items)
        else:
            nicePrint("""You search your surroundings and find a fist sized stone in the wet ground.""")
            print()
            nicePrint("Take it?")
            print()
            print("1. Yes.")
            print("2. No.")
            cmd_list = ["1", "2", "yes", "no"]
            cmd = getcmd(cmd_list)

            if cmd.lower()=="1" or cmd.lower()=="yes":
                nicePrint("You pick up the stone.")
                start_searched = True
                items.update({"stone":"a fist sized stone, nothing special about it."})
            elif cmd.lower()=="2" or cmd.lower()=="no":
                nicePrint("You leave the stone on the ground.")
                
            else:
                print("You can not do that, try something else.")
                getcmd(cmd_list)
            start(items)

    global combat
    combat = False
    global start_counter
    global caller_text
    global start_searched
    global porch_emptied
    global empty_porch_counter
    global wardens_return
    global fire
    global wardens_eliminated
    

    if wardens_eliminated or fire:
        print()
        nicePrint("""You are on the road leading into the outpost,
        there is no need to hide here anymore.\n""")
        print("""1. Move to the front of the outpost.
2. Go to the river.
3. Go around to the back of the outpost.\n""")
        
        cmd_list = ["1", "2","3"]
        cmd = getcmd(cmd_list)

        if cmd=="1":
            nicePrint("You go to the front of the outpost.\n")
            empty_porch(items)
        elif cmd=="2":
            nicePrint("You move to the river.\n")
            sneak_around(items)
        elif cmd=="3":
            nicePrint("You go to the back of the outpost.\n")
            sneak_backyard(items)
        else:
            nicePrint("You can not do that, try something else.")
            getcmd(cmd_list)



    if fire or wardens_eliminated:
        pass
    else:
        if empty_porch_counter > 3 :
            wardens_return=True
            porch_emptied=False

    if "crossbow" in items:
        
        if porch_emptied or wardens_eliminated :
            pass
        else : 
            print()
            nicePrint("""With the crossbow you can take out one of the Wardens on the front porch
            and using the element of surprise engage the other.
            This way you might have a chance to eliminate them both
            and live to tell the tale.\n""")
            input("Press enter.\n")
            nicePrint("You decide to : \n")
            time.sleep(2)
            nicePrint("""1. Use the crossbow and fight.
    2. Not now.\n""")
            
            cmd_list = ["1", "2"]
            cmd = getcmd(cmd_list)
            
            if cmd=="1":
                nicePrint("""You cock the crossbow and place the bolt on it.
                Sneaking through the bushes you find a good shooting spot.
                You steady your breathing and take aim
                and say a quick prayer to Ranald
                with the wind and the rain you're going to need it.\n""")
                time.sleep(2)
                input("Press enter.\n")
                nicePrint("""You pull the trigger
                the bolt flies through the rain\n""")
                time.sleep(2)
                nicePrint("""and hits one of the Wardens square in the chest
                he falls down from his chair and through the rain 
                you can hear quiet scream of pain.
                You drop the crossbow and charge from the bushes.\n""")
                del items["crossbow"]
                time.sleep(2)
                if "hook" in items:
                    nicePrint("""You simultaneously draw your dagger and the hook
                    and run at the other Warden on the porch.
                    Your sneak attack was completely successful, 
                    the other Warden is distracted enough not to see you coming.\n""")
                    time.sleep(2)
                    nicePrint("""The tied dog is barking frantically
                    the Warden turns around spear in hand but it's too late.
                    Your last step is a jump, you leap at the Warden
                    and drive the dagger and the hook into his neck and chest.\n""")
                    input("Press enter.\n")
                    nicePrint("""You both fall on the porch floor
                    the Warden stares blankly at you.
                    The porch is now drenched in blood
                    the dog is still barking.
                    You pull the dagger and the hook out of the body 
                    wipe them and take a couple of deep breaths to calm yourself.\n""")
                    time.sleep(2)
                    wardens_eliminated=True
                    porch_emptied=True
                    nicePrint("""You have eliminated the Wardens on the front porch.\n""")
                    empty_porch(items)
                elif "club" in items:
                    nicePrint("""You prepare the club
                    and run at the other Warden on the porch.
                    Your sneak attack was completely successful, 
                    the other Warden is distracted enough not to see you coming.\n""")
                    time.sleep(2)
                    nicePrint("""The tied dog is barking frantically
                    the Warden turns around spear in hand but it's too late.
                    Your run as fast as you can and swing the club at the Warden.\n""")
                    input("Press enter.\n")
                    nicePrint("""He's face becomes a bloody mush and his head almost turns around
                    fnally he slumps to the floor.
                    The porch is now drenched in blood
                    the dog is still barking.
                    You take a couple of deep breaths to calm yourself.\n""")
                    time.sleep(2)
                    wardens_eliminated=True
                    porch_emptied=True
                    nicePrint("""You have eliminated the Wardens on the front porch.\n""")
                    empty_porch(items)
                else:
                    nicePrint("""You draw your dagger 
                    and run at the other Warden on the porch.
                    Your sneak attack was completely successful, 
                    the other Warden is distracted enough not to see you coming.\n""")
                    time.sleep(2)
                    nicePrint("""The tied dog is barking frantically
                    the Warden turns around spear in hand but it's too late.
                    Your last step is a jump, you leap at the Warden
                    and drive the dagger into his chest.\n""")
                    input("Press enter.\n")
                    nicePrint("""You both fall on the porch floor
                    the Warden stares blankly at you.
                    The porch is now drenched in blood
                    the dog is still barking.
                    You pull the dagger  
                    wipe it and take a couple of deep breaths to calm yourself.\n""")
                    time.sleep(2)
                    wardens_eliminated=True
                    porch_emptied=True
                    nicePrint("""You have eliminated the Wardens on the front porch.\n""")
                    empty_porch(items)
            elif cmd=="2":
                nicePrint("Maybe it's better to try some other approach.\n")
                pass
        

    if guard_alert:

        porch_emptied = False
        print()

        nicePrint("""Hiding in the bushes you pause to think.
        The guards are alert to you now, 
        maybe it whould be better to stay clear of them.\n""")
        
        nicePrint("What do you do : ")
        
        if backyard and river :
            print()
            print("""1. Approach the Warden's outpost directly, even though it will end badly .
2. Sneak to the river bank.
3. Sneak around to the back of the outpost, on the right.\n""")

            caller_text = """ 1. Approach the Warden's outpost directly, even though it will end badly .
2. Sneak to the river bank.
3. Sneak around to the back of the outpost, on the right.\n"""

            cmd_list = ["1", "2", "3", "turn around", "go back", "return", "walk back", "search", "look", "examine"]
            cmd = getcmd(cmd_list)

            if cmd == "1":
                nicePrintRed("HALT IN THE NAME OF THE EMPEROR! YOU CAN'T ESCAPE!\n")
                
                nicePrint(
                    "The guards see you and start advancing thowards, spears and lanterns raised.\n")
                combat_situation()
            elif cmd == "2":
                sneak_around(items)
            elif cmd=="3":
                if not backyard:
                    print("You can not do that, try something else.\n")
                    getcmd(cmd_list) 
                else:
                    sneak_backyard(items)
            elif cmd== "search" or cmd =="look" or cmd =="examine":
                if not start_searched:
                    start_search()    
                else: 
                    nicePrint("There is nothing to find here.\n")
                    start(items)     
            elif cmd == "turn around" or cmd =="go back" or cmd =="return" or cmd =="walk back":
                turn_around = "With the merchant's men after you, your only hope is Altdorf.\n"
                getcmd(cmd_list)
            else: 
                print("You can not do that, try something else.\n")
                getcmd(cmd_list)

        elif backyard:
            print()
            print("""1. Approach the Warden's outpost directly, even though it will end badly .
2. Sneak around the Warden's outpost, tyring to stay in the shadows avoiding it completely.
3. Sneak around to the back of the outpost, on the right.\n""")

            caller_text = """1. Approach the Warden's outpost directly, even though it will end badly .
2. Sneak around the Warden's outpost, tyring to stay in the shadows avoiding it completely.
3. Sneak around to the back of the outpost, on the right.\n"""
            
            cmd_list = ["1", "2", "3", "turn around", "go back", "return", "walk back", "search", "look", "examine"]
            cmd = getcmd(cmd_list)

            if cmd == "1":
                nicePrintRed("HALT IN THE NAME OF THE EMPEROR! YOU CAN'T ESCAPE!\n")
                
                nicePrint("""The guards see you and start advancing thowards, spears and lanterns raised
                time is short, what do you do?\n""")
                
                combat_situation()
            elif cmd == "2":
                sneak_around(items)
                nicePrint("You move silently to the left of the outpost.\n")
            elif cmd=="3":
                if not backyard:
                    print("You can not do that, try something else.\n")
                    getcmd(cmd_list) 
                else:
                    sneak_backyard(items) 
            elif cmd== "search" or cmd=="look" or cmd=="examine":
                if not start_searched:
                    start_search()    
                else: 
                    nicePrint("There is nothing to find here.\n") 
                    start(items)   
            elif cmd == "turn around" or cmd=="go back" or cmd=="return" or cmd=="walk back":
                turn_around = "With the merchant's men after you, your only hope is Altdorf.\n"
                       
            else:
                nicePrint("You can not do that, try something else.\n")
                getcmd(cmd_list)

        elif river:
            print()
            print("""1. Approach the Warden's outpost directly, even though it will end badly .
2. Sneak to the river bank.\n""")
            

            caller_text = """1. Approach the Warden's outpost directly, even though it will end badly .
2. Sneak to the river bank\n.
"""
            
            cmd_list = ["1", "2", "3", "turn around", "go back", "return", "walk back", "search", "look", "examine"]
            cmd = getcmd(cmd_list)

            if cmd == "1":
                nicePrintRed("HALT IN THE NAME OF THE EMPEROR! YOU CAN'T ESCAPE!\n")
                
                nicePrint("""The guards see you and start advancing thowards, spears and lanterns raised
                time is short, what do you do?\n""")
                combat_situation()
            elif cmd == "2":
                nicePrint("You move silently to the left of the outpost.\n")
                sneak_around(items)
            elif cmd=="3":
                if not backyard:
                    print("You can not do that, try something else.\n")
                    getcmd(cmd_list) 
                else:
                    sneak_backyard(items) 
            elif cmd== "search" or cmd =="look" or cmd =="examine":
                if not start_searched:
                    start_search()    
                else: 
                    nicePrint("There is nothing to find here.\n")
                    start(items)   
            elif cmd == "turn around" or cmd =="go back" or cmd =="return" or cmd =="walk back":
                turn_around = "With the merchant's men after you, your only hope is Altdorf.\n"
                
                getcmd(cmd_list)
            
            else:
                print("You can not do that, try something else.\n")
                getcmd(cmd_list)

        
        else:
            print()
            print("""1. Approach the Warden's outpost directly, even though it will end badly.
2. Sneak around the Warden's outpost, tyring to stay in the shadows avoiding it completely.\n""")

            caller_text = """1. Approach the Warden's outpost directly, even though it will end badly .
2. Sneak around the Warden's outpost, tyring to stay in the shadows avoiding it completely.\n"""

            cmd_list = ["1", "2", "turn around", "go back", "return", "walk back", "search", "look", "examine"]
            cmd = getcmd(cmd_list)

            if cmd == "1":
                nicePrintRed("HALT IN THE NAME OF THE EMPEROR! YOU CAN'T ESCAPE!\n")
                
                nicePrint("""The guards see you and start advancing thowards, spears and lanterns raised.
                time is short, what do you do?\n""")
                combat_situation()
            elif cmd == "2":
                nicePrint("You sneak to the left of the outpost.\n")
                sneak_around(items)
            elif cmd=="3":
                if not backyard:
                    print("You can not do that, try something else.\n")
                    getcmd(cmd_list) 
                else:
                    sneak_backyard(items) 
            elif cmd== "search" or cmd =="look" or cmd =="examine":
                if not start_searched:
                    start_search()    
                else: 
                    nicePrint("There is nothing to find here.\n")
                    start(items)    
            elif cmd == "turn around" or cmd =="go back" or cmd =="return" or cmd =="walk back":
                turn_around = "With the merchant's men after you, your only hope is Altdorf.\n"
                
                getcmd(cmd_list)
            
            else:
                print("You can not do that, try something else.\n")
                getcmd(cmd_list)

      
    if fire:
        empty_porch_counter = 0
        porch_emptied = True
        start_counter = 1
        
    if start_counter == 0:
        print()
        nicePrint("""You are in the bushes next to the road leading to the outpost,
        this is a good place to stay out of sight and think about what to do,
        or to search your surrounding, but you should be careful.\n""")
        nicePrint("""The road Wardens will surely be suspicious of a lone traveler in the dead of the night like this.
        Or even worse there could be a warrant on your head.\n""")
        time.sleep(1)
    elif start_counter > 3:
        if porch_emptied:
            print()
            nicePrint("""You are hidden in the bushes next to the main road 
            nothing has changed since the last time.\n""")
            start_counter=0
        else:
            print()
            nicePrintRed("HALT! WHO GOES THERE!")
            nicePrint(
                "The guards see you and start advancing thowards, spears and lanterns raised.\n")
            nicePrint("The time is short, what do you do?\n")

            combat_situation()
    elif start_counter > 2:
        if porch_emptied:
            print()
            nicePrint("""You are hidden by the main road ,
            nothing has changed since the last time.\n""")
            start_counter = 0
            
        else:
            print()
            nicePrint(
                "The Wardens at the gate seem to notice something in your direction.\n")

    else:
        print()
        nicePrint("""You are hidden by the main road ,
            nothing has changed since the last time.\n""")
    start_counter += 1
    print()

    nicePrint("After a moment you decide to : \n")
    
    if river and backyard and porch_emptied:
        if not wardens_return:
            print("""1. Sneak to the front of the outpost, the Wardens have left and now the front of the Outpost is empty.
2. Sneak to the river bank.
3. Sneak around to the back of the outpost, on the right.\n""")

            caller_text="""1. Sneak to the front of the outpost, the Wardens have left and now the front of the Outpost is empty.
2. Sneak to the river bank.
3. Sneak around to the back of the outpost, on the right.\n"""

            cmd_list = ["1", "2", "3", "turn around", "go back", "return", "walk back", "search", "look", "examine"]
            cmd = getcmd(cmd_list)

            if cmd == "1":
                nicePrint("You move to the now empty porch.\n")
                empty_porch(items)
                
            elif cmd == "2":
                nicePrint("You silently move to the river.\n")
                sneak_around(items)
            elif cmd == "3":
                nicePrint("You decide to sneak to the back of the outpost.\n")
                sneak_backyard(items)
            
            elif cmd== "search" or cmd =="look" or cmd =="examine":
                if not start_searched:
                    start_search()    
                else: 
                    nicePrint("There is nothing to find here.")
                    start(items)
            
            elif cmd == "turn around" or cmd =="go back" or cmd =="return" or cmd == "walk back":
                turn_around = "With the merchant's men after you, your only hope is Altdorf.\n"
                
                getcmd(cmd_list)
            
            else:
                nicePrint("You can not do that, try something else.")
                getcmd(cmd_list)

        else:
            print("""1. The Wardens have returned to the outpost, approach them even though it will end badly.
2. Sneak to the river bank.
3. Sneak around to the back of the outpost, on the right.\n""")
            caller_text="""1. The Wardens have returned to the outpost, approach them even though it will end badly.
2. Sneak to the river bank.
3. Sneak around to the back of the outpost, on the right.\n"""

            cmd_list = ["1", "2", "3", "turn around", "go back", "return", "walk back", "search", "look", "examine"]
            cmd = getcmd(cmd_list)

            if cmd == "1":
                nicePrint("You muster all of your courage and approach the outpost.\n")
                combat_situation()
                
            elif cmd == "2":
                nicePrint("You silently move to the river.\n")
                sneak_around(items)
            elif cmd == "3":
                nicePrint("You decide to sneak to the back of the outpost.\n")
                sneak_backyard(items)
            
            elif cmd== "search" or cmd =="look" or cmd =="examine":
                if not start_searched:
                    start_search()    
                else: 
                    nicePrint("There is nothing to find here.")
                    start(items)
            
            elif cmd == "turn around" or cmd =="go back" or cmd =="return" or cmd == "walk back":
                turn_around = "With the merchant's men after you, your only hope is Altdorf."
                nicePrint(turn_around)
                print()
                getcmd(cmd_list)
            
            else:
                print("You can not do that, try something else.")
                getcmd(cmd_list)

    elif river and backyard:
        print("""1. Approach the Warden's outpost directly, like a respectable burgher.
2. Sneak to the Warden's outpost, to try to get a better view of the situation.
3. Sneak to the river bank.
4. Sneak around to the back of the outpost, on the right.\n""")
        caller_text="""1. Approach the Warden's outpost directly, like a respectable burgher.
2. Sneak to the Warden's outpost, to try to get a better view of the situation.
3. Sneak to the river bank.
4. Sneak around to the back of the outpost, on the right.\n"""

        cmd_list = ["1", "2", "3", "4", "turn around", "go back", "return", "walk back", "search", "look", "examine"]
        cmd = getcmd(cmd_list)

        if cmd == "1":
            nicePrint("You step onto the road and approach the outpost.\n")
            approach_directly(items)
        elif cmd == "2":
            nicePrint("After a moment you decide to sneak to get a closet look.\n")
            sneak_to_the_wardens(items)   
        elif cmd == "3":
            nicePrint("You silently move to the river.\n")
            sneak_around(items)
        elif cmd == "4":
            nicePrint("Silently you move to the back of the outpost.\n")
            sneak_backyard(items)
        
        elif cmd== "search" or cmd =="look" or cmd =="examine":
            if not start_searched:
                start_search()    
            else: 
                nicePrint("There is nothing to find here.")
                start(items)
        
        elif cmd == "turn around" or cmd =="go back" or cmd =="return" or cmd == "walk back":
            turn_around = "With the merchant's men after you, your only hope is Altdorf."
            nicePrint(turn_around)
            print()
            getcmd(cmd_list)
        
        else:
            print("You can not do that, try something else.")
            getcmd(cmd_list)


    elif river and porch_emptied:
        if not wardens_return:
            print("""1. Sneak to the front of the outpost, the Wardens have left and now the front of the Outpost is empty.
2. Sneak to the river bank.\n""")
            caller_text="""1. Sneak to the front of the outpost, the Wardens have left and now the front of the Outpost is empty.
2. Sneak to the river bank.\n"""

            cmd_list = ["1", "2", "turn around", "go back", "return", "walk back", "search", "look", "examine"]
            cmd = getcmd(cmd_list)

            if cmd == "1":
                nicePrint("You step onto the road and approach the outpost.\n")
                empty_porch(items)
            elif cmd == "2":
                nicePrint("You silently move to the river.\n")
                sneak_around(items)
            elif cmd== "search" or cmd =="look" or cmd =="examine":
                if not start_searched:
                    start_search()    
                else: 
                    nicePrint("There is nothing to find here.")
                    start(items)
            
            elif cmd == "turn around" or cmd =="go back" or cmd =="return" or cmd == "walk back":
                turn_around = "With the merchant's men after you, your only hope is Altdorf."
                nicePrint(turn_around)
                print()
                getcmd(cmd_list)
            
            else:
                print("You can not do that, try something else.")
                getcmd(cmd_list)

        else:
            print("""1. The Wardens have returned to the outpost, approach them even though it will end badly.
2. Sneak to the river bank.\n""")
            caller_text="""1. The Wardens have returned to the outpost, approach them even though it will end badly.
2. Sneak to the river bank.\n"""

            cmd_list = ["1", "2", "turn around", "go back", "return", "walk back", "search", "look", "examine"]
            cmd = getcmd(cmd_list)

            if cmd == "1":
                nicePrint("You muster all of your courage and approach the outpost.\n")
                combat_situation()
            elif cmd == "2":
                nicePrint("You silently move to the river.\n")
                sneak_around(items)
            elif cmd== "search" or cmd =="look" or cmd =="examine":
                if not start_searched:
                    start_search()    
                else: 
                    nicePrint("There is nothing to find here.")
                    start(items)
            
            elif cmd == "turn around" or cmd =="go back" or cmd =="return" or cmd == "walk back":
                turn_around = "With the merchant's men after you, your only hope is Altdorf."
                nicePrint(turn_around)
                print()
                getcmd(cmd_list)
            
            else:
                print("You can not do that, try something else.")
                getcmd(cmd_list)

    elif backyard and porch_emptied:
        if not wardens_return:
            print("""1. Sneak to the front of the outpost, the Wardens have left and now the front of the Outpost is empty.
2. Sneak around the Warden's outpost, tyring to stay in the shadows avoiding it completely.
3. Sneak around to the back of the outpost, on the right.\n""")
            caller_text="""1. Sneak to the front of the outpost, the Wardens have left and now the front of the Outpost is empty.
2. Sneak around the Warden's outpost, tyring to stay in the shadows avoiding it completely.
3. Sneak around to the back of the outpost, on the right.\n"""

            cmd_list = ["1", "2","3","4", "turn around", "go back", "return", "walk back", "search", "look", "examine"]
            cmd = getcmd(cmd_list)

            if cmd == "1":
                nicePrint("You step onto the road and approach the outpost.\n")
                empty_porch(items)
            elif cmd == "2":
                nicePrint("You sneak around the Warden's outpost, tyring to stay in the shadows avoiding it completely.\n")
                sneak_around(items)
            elif cmd == "3":
                nicePrint("You decide to sneak to the back of the outpost.\n")
                sneak_backyard(items)
            elif cmd== "search" or cmd =="look" or cmd =="examine":
                if not start_searched:
                    start_search()    
                else: 
                    nicePrint("There is nothing to find here.")
                    start(items)
            
            elif cmd == "turn around" or cmd =="go back" or cmd =="return" or cmd == "walk back":
                turn_around = "With the merchant's men after you, your only hope is Altdorf."
                nicePrint(turn_around)
                print()
                getcmd(cmd_list)
            
            else:
                print("You can not do that, try something else.")
                start(items)

        else:
            print("""1. The Wardens have returned to the outpost, approach them even though it will end badly.
2. Sneak around the Warden's outpost, tyring to stay in the shadows avoiding it completely.
3. Sneak around to the back of the outpost, on the right.\n""")
            caller_text="""1. The Wardens have returned to the outpost, approach them even though it will end badly.
2. Sneak around the Warden's outpost, tyring to stay in the shadows avoiding it completely.
3. Sneak around to the back of the outpost, on the right.\n"""


            cmd_list = ["1", "2","3", "turn around", "go back", "return", "walk back", "search", "look", "examine"]
            cmd = getcmd(cmd_list)

            if cmd == "1":
                nicePrint("You muster all of your courage and approach the outpost.\n")
                combat_situation()
            elif cmd == "2":
                nicePrint("You sneak around the Warden's outpost, tyring to stay in the shadows avoiding it completely.\n")
                sneak_around(items)
            elif cmd == "3":
                nicePrint("You decide to sneak to the back of the outpost.\n")
                sneak_backyard(items)
            elif cmd== "search" or cmd =="look" or cmd =="examine":
                if not start_searched:
                    start_search()    
                else: 
                    nicePrint("There is nothing to find here.")
                    start(items)
            
            elif cmd == "turn around" or cmd =="go back" or cmd =="return" or cmd == "walk back":
                turn_around = "With the merchant's men after you, your only hope is Altdorf."
                nicePrint(turn_around)
                print()
                getcmd(cmd_list)
            
            else:
                print("You can not do that, try something else.")
                getcmd(cmd_list)
    elif backyard:
        print("""1. Approach the Warden's outpost directly, like a respectable burgher.
2. Sneak to the Warden's outpost, to try to get a better view of the situation.
3. Sneak around the Warden's outpost, tyring to stay in the shadows avoiding it completely.
4. Sneak around to the back of the outpost, on the right.\n""")
        caller_text="""1. Approach the Warden's outpost directly, like a respectable burgher.
2. Sneak to the Warden's outpost, to try to get a better view of the situation.
3. Sneak around the Warden's outpost, tyring to stay in the shadows avoiding it completely.
4. Sneak around to the back of the outpost, on the right.\n"""

        cmd_list = ["1", "2","3", "4", "turn around", "go back", "return", "walk back", "search", "look", "examine"]
        cmd = getcmd(cmd_list)

        if cmd == "1":
            nicePrint("You step onto the road and approach the outpost.\n")
            approach_directly(items)
        elif cmd == "2":
            nicePrint("You decide to move closer to get a better view.\n")
            sneak_to_the_wardens(items)
        elif cmd == "3":
            nicePrint("You sneak around the Warden's outpost, tyring to stay in the shadows avoiding it completely.\n")
            sneak_around(items)
        elif cmd == "4":
            nicePrint("You decide to sneak to the back of the outpost.\n")
            sneak_backyard(items)
        elif cmd== "search" or cmd =="look" or cmd =="examine":
            if not start_searched:
                start_search()    
            else: 
                nicePrint("There is nothing to find here.")
                start(items)
        
        elif cmd == "turn around" or cmd =="go back" or cmd =="return" or cmd == "walk back":
            turn_around = "With the merchant's men after you, your only hope is Altdorf."
            nicePrint(turn_around)
            print()
            getcmd(cmd_list)
        
        else:
            print("You can not do that, try something else.")
            getcmd(cmd_list)

    elif river:
        print("""1. Approach the Warden's outpost directly, like a respectable burgher.
2. Sneak to the Warden's outpost, to try to get a better view of the situation.
3. Sneak to the river bank.\n""")
        caller_text="""1. Approach the Warden's outpost directly, like a respectable burgher.
2. Sneak to the Warden's outpost, to try to get a better view of the situation.
3. Sneak to the river bank.\n"""

        cmd_list = ["1", "2","3", "turn around", "go back", "return", "walk back", "search", "look", "examine"]
        cmd = getcmd(cmd_list)

        if cmd == "1":
            nicePrint("You step onto the road and approach the outpost.\n")
            approach_directly(items)
        elif cmd == "2":
            nicePrint("You decide to move closer to get a better view.\n")
            sneak_to_the_wardens(items)
        elif cmd == "3":
            nicePrint("Silently you move to the river.\n")
            sneak_around(items)
        
        elif cmd== "search" or cmd =="look" or cmd =="examine":
            if not start_searched:
                start_search()    
            else: 
                nicePrint("There is nothing to find here.")
                start(items)
        
        elif cmd == "turn around" or cmd =="go back" or cmd =="return" or cmd == "walk back":
            turn_around = "With the merchant's men after you, your only hope is Altdorf."
            nicePrint(turn_around)
            print()
            getcmd(cmd_list)
        
        else:
            print("You can not do that, try something else.")
            getcmd(cmd_list)
    else:
        print("""1. Approach the Warden's outpost directly, like a respectable burgher.
2. Sneak to the Warden's outpost, to try to get a better view of the situation.
3. Sneak around the Warden's outpost, tyring to stay in the shadows avoiding it completely.\n""")
        caller_text="""1. Approach the Warden's outpost directly, like a respectable burgher.
2. Sneak to the Warden's outpost, to try to get a better view of the situation.
3. Sneak around the Warden's outpost, tyring to stay in the shadows avoiding it completely.\n"""

        cmd_list = ["1", "2","3", "turn around", "go back", "return", "walk back", "search", "look", "examine"]
        cmd = getcmd(cmd_list)

        if cmd == "1":
            nicePrint("You step onto the road and approach the outpost.\n")
            approach_directly(items)
        elif cmd == "2":
            nicePrint("You decide to move closer to get a better view.\n")
            sneak_to_the_wardens(items)
        elif cmd == "3":
            nicePrint("Silently you move through the bushes to the left of the outpost, avoding it.\n")
            sneak_around(items)
        
        elif cmd== "search" or cmd =="look" or cmd =="examine":
            if not start_searched:
                start_search()    
            else: 
                nicePrint("There is nothing to find here.")
                start(items)
        
        elif cmd == "turn around" or cmd =="go back" or cmd =="return" or cmd == "walk back":
            turn_around = "With the merchant's men after you, your only hope is Altdorf."
            nicePrint(turn_around)
            print()
            getcmd(cmd_list)
        
        else:
            print("You can not do that, try something else.")
            getcmd(cmd_list) 

    
    
    




kitchen_backdoor_first = False
nail_puller_taken = False
#When the player is in the backyard
def in_the_backyard(items):

        global snorri_found
        global wounded
        global club_taken
        global in_the_backyard_first
        global kitchen_backdoor_first
        
        def shed(items):
            
            global fire
            global wounded
            global club_taken
            global dock_found
            global shed_first
            global paddle_taken
            global in_the_backyard_first
            global rope_taken
            global nail_puller_taken

            if not shed_first:
                nicePrint("""Praise Sigmar!
                The inside of the shed is dry, 
                the roof isn't leaking, 
                the walls are solid.\n""")
                time.sleep(1)
                nicePrint("""There are no raindrops on your hat, no wind in your face.\n""")
                time.sleep(1)
                nicePrint("It seems like forever since the last time you were inside and not running from someone.\n")
                time.sleep(1)
                nicePrint("It's almost peaceful here.\n")
                input("Press enter.\n")
                nicePrint("In the shed there is a assortment of tools, bales of hay, rope and a boat paddle.\n")
                nicePrint("After a serene moment you decide to : \n")
                shed_first=True
            else:
                nicePrint("""The shed is the same as the last time. 
What do you do : \n""")
            if paddle_taken and rope_taken:
                print("""3. Go back outside to the backyard.
4. Take some tools.\n""")
                global caller_text
                caller_text = """3. Go back outside to the backyard.
4. Take some tools.\n"""
            elif paddle_taken:
                print("""2. Take the rope.
3. Go back outside to the backyard.
4. Take some tools.\n""") 
                caller_text = """2. Take the rope.
3. Go back outside to the backyard.
4. Take some tools.\n"""
            elif rope_taken:
                print("""1. Take the paddle.
3. Go back outside to the backyard.
4. Take some tools.\n""")
                caller_text = """1. Take the paddle.
3. Go back outside to the backyard.
4. Take some tools.\n"""
            else:   
                print("""1. Take the paddle.
2. Take the rope.
3. Go back outside to the backyard.
4. Take some tools.\n""")
                caller_text = """1. Take the paddle.
2. Take the rope.
3. Go back outside to the backyard.
4. Take some tools.\n"""

            cmd_list = ["1", "2", "3","4", "search", "look", "examine" , "burn", "fire", "pipe"]
            cmd = getcmd(cmd_list)

            if cmd == "1":
                if not paddle_taken:

                    if not dock_first:
                        nicePrint("""You don't need it without a boat,
                        there's not a lot of things you can do with it except to paddle, 
                        and not one that you wish to do now.\n""")
                        shed(items)
                    else:                       
                        nicePrint("""This looks like a paddle for the boat at the dock.
                        It's too cumbersome to carry it and sneak around,
                        take the paddle and go to the dock?\n""")
                        time.sleep(1)
                        print("""1. Yes
2. No\n""")             
                        cmd_list = ["1", "2", "yes", "no"]
                        cmd = getcmd(cmd_list)

                        if cmd=="1" or cmd.lower()=="yes":
                            nicePrint("""You take the paddle and walk back into the rain.
                            Carefully you sneak down to the river dock.\n""")
                            items.update({"paddle":"good for boating and not much else."})
                            paddle_taken = True
                            dock(items)        
                        elif cmd=="2" or cmd.lower() == "no":
                            nicePrint("You leave the paddle in the shed.\n")
                            shed(items)
                        else:
                            nicePrint("You can't do that, try something else.\n")
                            shed(items)
                else: 
                    nicePrint("You can't do that, try something else.\n")
                    shed(items)
            elif cmd=="2":
                if not rope_taken:
                    nicePrint("""The rope is about a thumb width and strong, neatly folded, 
                    there are about dozen loops.\n """)
                    time.sleep(1)
                    nicePrint("""You pack it over your shoulder like a pouch, 
                    so you can carry it without being slowed down.\n""")
                    items.update({"rope":"ordinary rope, it could be used for tying or climbing or something else."})
                    rope_taken=True
                else:
                    nicePrint("You can't do that try something else.\n")
                shed(items)
            elif cmd=="3":
                nicePrint("You leave the shed and return to the backyard.\n")
                in_the_backyard(items)
            elif cmd=="4":
                if not jump_solution:
                    nicePrint("You don't need any tools.\n")
                else:
                    if not nail_puller_taken:
                        nicePrint("You find a nail puller, it can be used to remove the board from the table.\n")
                        items.update({"nail puller":"simple tool for pulling nails"})
                        nail_puller_taken=True
                    else:
                        nicePrint("There is nothing you need here.\n")
                shed(items)
            elif cmd.lower() == "burn" or cmd.lower() == "fire" or cmd.lower() == "pipe":
                if "pipe" in items:
                    nicePrint("""You take the pipe, the embers barely alive,
                    after a long draw they glow brightly.\n""")
                    time.sleep(2)
                    nicePrint("After another smoke you throw the pipe into the hay.\n")
                    del items["pipe"]
                    time.sleep(2)
                    nicePrint("""At first nothing happens, 
                    a few moments later a shy trail of smoke emerges from within.
                    Then another and another, soon the whole shed is filled with smoke
                    and in the center fire starts its deadly dance.\n""")
                    input("Press enter.\n")
                    nicePrint("""You quickly leave the backyard,
                    from a distance you can see the shed being swallowed by the flames.
                    The whole landscape illuminated by it.\n""")
                    time.sleep(2)
                    nicePrint("""You hear shouting and cursing, 
                    the Wardens are now all in the backyard trying to deal with the fire.\n""")
                    time.sleep(2)
                    fire=True
                    porch_emptied = True
                    empty_porch_counter = 0
                    sneak_backyard(items)
            elif cmd.lower()== "search" or cmd.lower()== "look" or cmd.lower()== "examine":
                nicePrint("The shed holds no secrects, there is nothing else to find here.\n")
                shed(items)
            else:
                nicePrint("You can't do that try something else.\n")
                shed(items)



        if not in_the_backyard_first:
            if wounded:
                nicePrint("""Your face burns even in the cold rain, with your fingers you can feel lacerated skin,
                once it heals it will leave you prettier than before.
                Your left hand is badly injured,
                you can move it but every twich of muscules is an agony, 
                it will be useless for any physical actions.\n""")
                time.sleep(1)
                nicePrint("""You are in the backyard, a couple of shrubs decorate the muddy yard,
            to your left is the shed and in front of you is the door leading inside the house.\n""")
                input("Press enter.\n")
                in_the_backyard_first = True
            else:    
                nicePrint("""You are in the backyard, a couple of shrubs decorate the muddy yard,
                to your left is the shed and in front of you is the door leading inside the house.\n""")
                input("Press enter.\n")
                in_the_backyard_first = True
        else:
            nicePrint("You are in the backyard and nothing has changed.\n")

        nicePrint("What do you do : \n")
        if "grappling hook" in items:
            print("""1. Sneak to the door.
2. Go to the shed.
3. Turn around and exit the backyard.
4. Climb through the open window using the grappling hook.\n""")
            global caller_text
            caller_text = """1. Sneak to the door.
2. Go to the shed.
3. Turn around and exit the backyard.
4. Climb through the open window using the grappling hook.\n"""
        else:
            print("""1. Sneak to the door.
2. Go to the shed.
3. Turn around and exit the backyard.\n""")
            
            caller_text = """1. Sneak to the door.
2. Go to the shed.
3. Turn around and exit the backyard.\n"""

        cmd_list = ["1", "2", "3","4", "search", "look", "examine"]
        cmd = getcmd(cmd_list)

        if cmd=="1":
            if kitchen_backdoor_first:
                nicePrint("The light still shines from the inside.\n")
                print("""1. Open the door.
2. Walk away from the door, back to the yard.\n""")
                caller_text="""1. Open the door.
2. Walk away from the door, back to the yard.\n"""
                
            else:
                nicePrint("Stepping carefully through the yard you approach the back door.\n")
                time.sleep(2)
                nicePrint("""The door is wooden and plain, underneath it light escapes to the outside,
                next to the door is a club, leaned against the wall.\n""")
                input("Press enter.\n")
                nicePrint("You decide to : \n")
                print("""1. Open the door.
2. Walk away from the door, back to the yard.\n""")
                caller_text="""1. Open the door.
2. Walk away from the door, back to the yard.\n"""
                kitchen_backdoor_first = True
                
                   
            cmd_list = ["1", "2", "search", "listen", "examine", "club", "take club", "pick up club"]
            cmd = getcmd(cmd_list)

            if cmd=="1":
                if snorri_found:
                    nicePrint("You carefully open the door, not to wake anybody inside.\n")
                    kitchen(items)
                nicePrint("You open the door and enter the outpost.\n")
                kitchen(items)
            elif cmd=="2":
                nicePrint("You decide to go back to backyard.\n")
                in_the_backyard(items)
            elif cmd.lower() == "search" or cmd.lower() == "listen" or cmd.lower() == "examine":
                if snorri_out:
                    nicePrint("You hear nothing.\n")
                else:
                    nicePrint("""Carefully you put your ear to the door
                    and on the other side you hear a rumbling sound
                    like a thunder
                    but outside it's just raining there's no thunder now.\n""")
                    time.sleep(2)
                    nicePrint("""It takes you a moment to realise, thats snoring,
                    someone is inside.\n""")
                    snorri_found=True
                    time.sleep(1)
                    nicePrint("You step back and decide to : \n")
                    in_the_backyard(items)
            elif cmd.lower()=="club" or cmd.lower()=="take club" or cmd.lower()== "pick up club":
                
                if not club_taken :
                    nicePrint("You take the club.\n")
                    items.update({"club":"a crude club made of strong wood, covered with dents and bite marks?!? It could be used as a weapon especially for stunning."})
                    club_taken = True
                    in_the_backyard(items)
                else :
                    nicePrint("There is nothing to take.\n")
                    in_the_backyard(items)
            else:
                nicePrint("You can't do that, try something else.\n")
                getcmd(cmd_list)
        
        elif cmd=="2":
            if not shed_first:
                nicePrint("""The shed is a solid build it was made to last,
                it is not a large cabin it could fit a handful of people inside.\n""")
                time.sleep(1)
                nicePrint("""It's back wall is positioned against the inner wall of the backyard,
                the only door is facing the outpost.\n""")
                input("Press enter.\n")
            else:
                nicePrint("The shed looks the same.\n")
            nicePrint("What do you do : \n")
            print("""1. Enter the shed.
2. Walk away.\n""")
            caller_text="""1. Enter the shed.
2. Walk away.\n"""

            cmd_list = ["1", "2", "search", "look", "examine"]
            cmd = getcmd(cmd_list)

            if cmd=="1":
                shed(items)
            elif cmd=="2":
                nicePrint("You walk back to the center of the backyard.\n")
                in_the_backyard(items)
            elif cmd.lower() == "search" or cmd.lower() == "look" or cmd.lower() == "examine":
                nicePrint("There's only mud here.\n")
            else:
                nicePrint("You can't do that, try something else.\n")
                getcmd(cmd_list)
            in_the_backyard(items)
        elif cmd =="3":
            nicePrint("You walk out of the backyard.\n")
            sneak_backyard(items)
        elif cmd=="4":
            if "grappling hook" in items and not wounded:
                nicePrint("""You swing the grappling hook a couple of times to get the momentum
                and throw it into the open window.\n""")
                time.sleep(2)
                nicePrint("""The hook lands inside and you pull it
                after a moment it is securely hooked to something.\n""")
                time.sleep(1)
                nicePrint("""pulling yourself up through the rain you reach the first floor of the outpost.\n""")
                large_room(items)
            elif "grappling hook" in items and wounded:
                nicePrint("""With your wounded arm you don't have the strength to scale the building wall.\n""")
                in_the_backyard(items)
            else:
                nicePrint("You can't do that try something else.\n")
                in_the_backyard(items)
       
        elif cmd=="search" or cmd== "look" or cmd== "examine":
            nicePrint("""As you walk over the yard you barely notice in the dark
            scattered animal bones or what's left of them, 
            at least you hope they are animal.\n""")
            getcmd(cmd_list)
        else:
            nicePrint("You can't do that, try something else.\n")
            getcmd(cmd_list)








#when the player is on the dock
def dock(items):
        
            global paddle_in_boat
            global dock_first
            global wounded

            if not dock_first:
                nicePrint("""The path leads down to the river,
                it's a winding trail with a sturdy wooden handrail,
                the end is lost in the dark.\n""")
                time.sleep(1)
                nicePrint("""Following it you find yourself at a small dock on the river,
                wind and rain slashing your face.\n""")
                time.sleep(1)
                nicePrint("""The dock is a small wooden platform on the river,
                from here you can see the river, it's other side is out of sight,
                the sound deep, flow is strong and smells of wilderness.\n""")
                time.sleep(1)
                nicePrint("""The river is almost higher than the dock, 
                bigger waves splash over the wooden platform.\n""")
                input("Press enter.\n")
                nicePrint("""Tightly tied to the dock is a small boat, 
                rhythmically knocking against the dock
                it's paddle missing.\n""")
                dock_first = True
            else:
                nicePrint("You are at the dock, nothing has changed.\n")
            
            nicePrint("What do you do : \n")
                
            if paddle_in_boat or "paddle" in items:
                print("""1. Go back up to the backyard.
2. Take the boat and paddle to the other bank.\n""")
                global caller_text
                caller_text="""1. Go back up to the backyard.
2. Take the boat and paddle to the other bank.\n"""

            else:
                print("1.  Go back up to the backyard.\n")
                caller_text="1. Go back up to the backyard.\n"
            
            cmd_list = ["1", "2", "search", "look", "examine"]
            cmd = getcmd(cmd_list)

            if cmd == "1":
                if "paddle" in items:
                    nicePrint("You leave the paddle in the boat and return to the backyard.\n")
                    del items["paddle"]
                    paddle_in_boat = True
                    sneak_backyard(items)
                else:
                    nicePrint("You return uphill to the backyard.\n")
                    sneak_backyard(items)
            elif cmd=="2":
                if "paddle" in items or paddle_in_boat:
                    if not wounded:
                        nicePrint("You untie the boat and jump in.\n")
                        time.sleep(1)
                        nicePrint("The river grabs the small boat and it starts to drift downriver.\n")
                        time.sleep(1)
                        nicePrint("""The boat rocks like a leaf on wind,
                        your heart stops with each wave
                        the water is cold and dark.\n""")
                        time.sleep(1)
                        nicePrint("""Soon you pass under the bridge, it's stone arches tower over you,
                        and once on the other side you can see the lights from the outpost.\n""")
                        input("Press enter.")
                        nicePrint("""You paddle to the best of your abilities but the current is too strong,
                        the wind and the rain fill your boat with water
                        but you carry on through the night.\n""")
                        time.sleep(2)
                        nicePrint("Dawn finds you exausted and wet to the bone, barely able to hold the paddle.\n")
                        time.sleep(1)
                        nicePrint("""The river slows in a natural widening
                        and you spend the last bits of your strength to reach the other bank.\n""")
                        time.sleep(1)
                        nicePrint("""Your legs are shaking but you manage to crawl on land
                        it is still raining
                        you drag yourself up the muddy river bank
                        and find that you are thrown off course
                        it will take you days to reach Altdorf.\n""")
                        time.sleep(1)
                        nicePrint("""You can only hope that your employers will be merciful.\n""")
                        time.sleep(2)
                        nicePrint("""GAME OVER
                        Aufiderzein!""")
                        time.sleep(3)
                        sys.exit(1)
                    else:
                        nicePrint("You untie the boat and jump in.\n")
                        time.sleep(1)
                        nicePrint("The river grabs the small boat and it starts to drift downriver.\n")
                        time.sleep(1)
                        nicePrint("""The boat rocks like a leaf on wind,
                        your heart stops with each rock
                        the water is cold and dark.\n""")
                        time.sleep(1)
                        nicePrint("""You try to paddle, fighting against the current,
                        as you sink the paddle into the water pain shoots through your wounded arm.\n""")
                        time.sleep(1)
                        nicePrint("""Instinctively you release the paddle and cradle your arm,
                        the boat starts to rock and turns over.\n""")
                        time.sleep(1)
                        nicePrint("""The world turns dark, you struggle to find the surface,
                        but the river is stronger.
                        You hold your breath as much as you can.\n""")
                        input("Press enter.\n")
                        nicePrint("""Your body is caught on the brigde coulmn,
                        nobody notices it, just another piece of dirt the rain washed up.\n""")
                        time.sleep(3)
                        nicePrint("""You have died.
                        GAME OVER.""")
                        time.sleep(3)
                        sys.exit(1)

                elif cmd.lower() == "search" or cmd.lower() == "look" or cmd.lower() == "examine":
                    nicePrint("There is nothing to find here except cold water.\n")
                    dock(items)
                    
                else:
                    nicePrint("There is no point in using the boat with out the paddle.\n")
                    dock(items)
            else:
                nicePrint("You can't do that try something else.\n")
                getcmd(cmd_list)






sneak_backyard_first = False
dog_discovered = False
backyard_door_open = False
lantern_found = False
dock_found = False
on_wall_first = False
walked_the_wall = False
dock_first = False
wounded  = False
in_the_backyard_first = False
club_taken = False
shed_first = False
paddle_taken = False
paddle_in_boat = False
rope_taken = False
fire = False


#when the player is on the backside of the outpost
def sneak_backyard(items):

    global dog_discovered
    global backyard_door_open
    global sneak_backyard_first
    global lantern_found
    global empty_porch_counter
    global dock_found
    global on_wall_first
    global walked_the_wall
    global dock_first
    global wounded
    global in_the_backyard_first
    global fire
        
    
    def at_the_backyard_door(items):

        global dock_found
        global wounded
        global backyard_door_open

        nicePrint("""Following the wall you reach the wooden gate,
        a simple door with a simple lock, its not meant to be locked, just closed.\n""")
        time.sleep(1)
        nicePrint("Open it?\n")
        print("1. Yes.")
        print("2. No.\n")

        cmd_list = ["1", "2", "yes", "no", "search", "look", "examine"]
        cmd = getcmd(cmd_list)

        if cmd == "1" or cmd.lower() == "yes":
            nicePrint("""As you open the backyard gate it leaves a trail in the mud,
            as you step into the backyard almost immediately you find yourself on your back in the mud.\n""")
            time.sleep(1)
            nicePrint("""On top of you is a dog but it's too big to be a dog,
            the stench of wet fur is overwhelming.
            It's huge jaws snap at you with a deep growling sound.
            You instinctively raise your arm to protect your throat 
            while searching for your dagger with the other.\n""")
            input("Press enter.\n")
            nicePrint("""Pain shoots through your whole body as the beast bites your forearm,
            and starts to jerk it around moving you whole in the mud like a rag doll,
            you drop your dagger into the mud.
            With it's front paw it slashes you across the cheek.\n""")
            input("Press enter.\n")
            nicePrint("""As suddenly as it started the dog stops it's attack.
            The beast's ayes catch a glimpse of the opened gate
            for a moment you could see the dilemma 
            only for a moment
            the dog releases you from it's grip and runs out through the opened gate.\n""")
            time.sleep(2)
            nicePrint("""You lay in the cold mud your arm is injured
            and your face is wet and warm.\n""")
            if wounded:
                nicePrint("""As you lay in the mud and look after the huge dog
                all you can do is hobble about
                your injuries are too much
                pain is overwhelming
                your strenth gone.\n""")
                time.sleep(2)
                nicePrint("""You try to get up but fall facedown into the mud
                your last breath is dirt.\n""")
                time.sleep(2)
                nicePrint("""In the morning your body is tossed into the river
                never to be found again.
                Your possesions used to increase the outposts budget.\n""")
                time.sleep(2)
                nicePrintMenacing("""You have died,
                GAME OVER\n""")
                time.sleep(3)
                sys.exit(1)
            wounded = True
            backyard_door_open = True
            in_the_backyard(items)

        elif cmd=="2" or cmd.lower() == "no":
            nicePrint("You leave the door and step back.\n")
            sneak_backyard(items)
        elif cmd.lower() == "search" or cmd.lower() == "look" or cmd.lower() == "examine":
            nicePrint("""Looking quickly at your surrounding you spot something,
            to the far right of the yard and the outpost there is a path leading down to the river.\n""")
            dock_found = True
            at_the_backyard_door(items)
        else:
            nicePrint("That isn't a good idea, the thing is still inside.\n")
            at_the_backyard_door(items)

    
    
    
    def backyard_search():
        nicePrint("""Searching around the back of the outpost you find a discarded lantern,
        half of it submerged in the mud,
        it's glass is shattered but there is still oil inside the metal casing\n.""")
        nicePrint("Take the lantern : \n")
        print("""1. Yes
2. No""")

        cmd_list = ["1", "2", "yes", "no"]
        cmd = getcmd(cmd_list)

        if cmd=="1" or cmd.lower()=="yes":
            nicePrint("You clean the mud off the lantern and take it.\n")
            items.update({"broken lantern":"the glass is broken but the fuse and oil seem to useable, it could be used as light source or for something else."})
            lantern_found = True
            sneak_backyard(items)
        elif cmd=="2" or cmd.lower() =="no":
            nicePrint("You leave the lantern in the mud.\n")
            sneak_backyard(items)
        else:
            nicePrint("You can't do that, try something else.\n")
            getcmd(cmd_list)




    if fire or wardens_eliminated:
        pass
    else:
        if empty_porch_counter > 3 :
            wardens_return=True
            porch_emptied=False

    if fire:
        nicePrint("""Shadows dance all around as the fire lights the outpost, 
        the Wardens shout and run in the backyard.
        It seems that all of them are now in the backyard.\n""")
        time.sleep(2)
        nicePrint("After snapping out of the hypnotic fire transe you decide to :\n ")
        if dock_found:
            print("""1. Go to the front of the outpost.
2. Sneak past the busy Wardens down to the river dock.\n""")
            global caller_text
            caller_text="""1. Go to the front of the outpost.
2. Sneak past the busy Wardens down to the river dock.\n"""
        else:
            print("1. Go to the front of the outpost.\n")
            caller_text="""1. Go to the front of the outpost.\n"""
                
        cmd_list = ["1", "2", "search", "look", "examine"]
        cmd = getcmd(cmd_list)

        if cmd=="1":
            empty_porch_counter = 0
            start(items)
        elif cmd=="2":
            if dock_found:
                empty_porch_counter = 0
                dock(items)
            else:
                nicePrint("You can't do that, try something else.\n")
        elif cmd.lower()=="search" or cmd.lower()== "look" or cmd.lower()==  "examine":
            if not lantern_found:
                backyard_search()
            else:
                nicePrint("There is nothing more to find here.\n")
                sneak_backyard(items)
        else:
            nicePrint("You can't do that, try something else.\n")
            getcmd(cmd_list)

    if not sneak_backyard_first:
        nicePrint("""Quietly you run across the muddy road and find yourself near the outpost.
        Keeping to the ground and using the trees as cover you position yourself so 
        that the building hides you from the sight of Wardens on the front porch.\n""")
        time.sleep(2)
        nicePrint("""Now you can see the back side of the outpost,
        There is much less light, no lanterns shine here.\n""")
        time.sleep(2)
        nicePrint("""The back has no windows on the ground floor,
        there are several windows on the upper floor,
        one to the river side of the building seems to be opened
        the only one that is lit is neareast to you.\n""")
        time.sleep(2)
        nicePrint("""A low stone wall protrudes from the building making a small backyard.
        The wall is a little higher than yourself and there is a wooden door leading inside the yard.\n""")
        sneak_backyard_first = True
        input("Press enter.\n")
    else:
        nicePrint("Nothing has changed at the back of the ouptost.\n")
    
    if backyard_door_open and dock_found:
        nicePrint("You decide to : \n")
        print("""1. Go back to the main road.
2. Go into the backyard.
3. Follow the trail down to the river.\n""")

        caller_text = """1. Go into the backyard.
2. Go back to the main road.
3. Follow the trail down to the river.\n"""

        cmd_list = ["1", "2", "3", "search", "look", "examine", "window", "look window", "look at window"]
        cmd = getcmd(cmd_list)

        if cmd=="1":
            nicePrint("You return to the main road.")
            empty_porch_counter +=1 
            start(items)
                            
        elif cmd=="2":
            if not backyard_door_open:
                nicePrint("You can't do that, try something else.\n")
                sneak_backyard(items) 
            in_the_backyard(items) 
            
        elif cmd == "3":
            if not dock_found:
                nicePrint("You can't do that, try something else.\n")
                sneak_backyard(items) 
            dock(items)           

        elif cmd.lower()=="search" or cmd.lower()== "look" or cmd.lower()== "examine":
            backyard_search()

        elif cmd.lower()=="window" or cmd.lower()== "look window" or cmd.lower()== "look at window":
            nicePrint("""Looking up to the only lit window on the outpost you have to protect your eyes from the rain
            for a time nothing happens but eventually  you see shadows dancing on the window
            definitely there is someone in that room.\n""")
            sneak_backyard(items)
        else:
            nicePrint("You can't do that try something else.\n")
            getcmd(cmd_list)




    elif dog_discovered and dock_found:
        nicePrint("You decide to : \n")
        print("""1. Sneak to the wall.
2. Climb over the wall.
3. Enter through the door in the wall.
4. Go back to the main road.
5. Climb quietly onto the wall.
6. Follow the trail down to the river.\n""")

        caller_text = """1. Sneak to the wall.
2. Climb over the wall.
3. Enter through the door in the wall.
4. Go back to the main road.
5. Climb quietly onto the wall.
6. Follow the trail down to the river.\n"""

        cmd_list = ["1", "2", "3", "4", "5", "6", "search", "look", "examine", "window", "look window", "look at window"]
        cmd = getcmd(cmd_list)

        if cmd == "1":
            if backyard_door_open:
                nicePrint("You can't do that, try something else.\n")
                sneak_backyard(items)
            if not dog_discovered:
                nicePrint("""Moving like a shadow through the rain
                moments later you crouch next to the wet wall.\n""")
                input("Press enter.\n")
                nicePrint("From the other side of the wall you can hear movement through muddy ground\n")
                time.sleep(2)
                nicePrint("and a nervous dog growl\n")
                time.sleep(2)
                nicePrint("a really big dog's growl.\n")
                    
                dog_discovered = True
                empty_porch_counter +=1 
                sneak_backyard(items)
            else:
                nicePrint("You already learned all that you can, there is no point to go sneak to the wall again\n")
                sneak_backyard(items)
        
        elif cmd=="2":
            if backyard_door_open:
                nicePrint("You can't do that, try something else.\n")
                sneak_backyard(items)
            if not dog_discovered:
                nicePrint("""You find a stone in the wall and a suitable foothold
                and in a couple of moments you jump across it into the backyard.\n""")
                input("Press enter.\n")
                nicePrint("""Your boots sink ancle deep into the soft cold mud.
                The back yard is unlit and the only light is coming from the window above.\n""")
                time.sleep(2)
                nicePrint("""You quckly spot your surrounding, to the left is the back of the outpost,
                on the right nested on the wall of the backyard is\n""")
                nicePrintRed("SPLAT")
                time.sleep(2)
                nicePrint("""You push your face out of the mud,
                something big and strong has knocked you to the ground.\n""")
                time.sleep(1)
                nicePrint("You instinctively swing around, dagger in hand.\n")
                time.sleep(1)
                nicePrint("""In the shadows through the rain you see a pair of eyes burning with rage,
                set of teeth almost shining in the window light,
                the beast is huge its fur dark and covered with mud.\n""")
                time.sleep(1)
                nicePrint("It moves straight towards you, not running but slowly.")
                nicePrint("The thing that passes through your mind is that it didn't bark at all.\n")
                input("Press enter.\n")
                nicePrint("""In the morning what is left of your ragged corpse is tossed into the river,
                in the backyard the huge dog's paw squishes a small metal ball deeper into the mud.\n""")
                nicePrint("""You have died,
                GAME OVER\n""")
                sys.exit(1)
            else:
                nicePrint("With that thing there you really don't wont do jump inside.\n")
                sneak_backyard(items)

        elif cmd=="3":
            empty_porch_counter += 1
            if backyard_door_open:
                nicePrint("You can't do that, try something else.\n")
                sneak_backyard(items)
            if not dog_discovered:

                at_the_backyard_door(items)
            else:
                nicePrint("That beast looks like it doesn't want to let you in, maybe try some other way.\n")
                sneak_backyard(items)
        elif cmd=="4":
            nicePrint("You return to the main road.")
            empty_porch_counter +=1 
            start(items)
        elif cmd=="5":
            if backyard_door_open:
                nicePrint("You can't do that, try something else.\n")
                sneak_backyard(items)
            if dog_discovered:
                if not on_wall_first:
                    nicePrint("""In a couple of moments you are at the stone wall,
                    quickly you find some protruding stones in the wall and scale it easily.\n""")
                    time.sleep(2)
                    nicePrint("""Crouching on the top of the wall you are seen by no eyes,
                    The back yard is closed by all sides, along the wall there is a small gate leading into the yard,
                    on the back wall of the outpost there is a door leading inside.
                    Nested against the inside of the wall there is a shed.\n""")
                    time.sleep(2)
                    nicePrint("""Moving like a shadow through the rain a beast of a dog roams the yard.
                    The thing is huge, the largest dog you have ever seen, if it's a dog at all.
                    It looks nervous and agitated, not stopping like a beast in a cage.
                    It hasn't noticed you.\n""")
                    on_wall_first=True
                else:
                    nicePrint("You climb on the wall, nothing has changed.\n")

                input("Press enter.\n")
                nicePrint("You decide to :\n")
                if "fish" in items:
                    print("""1. Walk on the wall to the gate.
2. Jump back down.
3. Throw the dog a fish.\n""")
                    caller_text = """1. Walk on the wall to the gate.
2. Jump back down.
3. Throw the dog a fish.\n"""
                else:
                    print("""1. Walk on the wall to the gate.
2. Jump back down.\n""") 
                    caller_text = """1. Walk on the wall to the gate.
2. Jump back down.\n"""
                empty_porch_counter +=1
            else:
                nicePrint("You can't do that, try something else.")
                sneak_backyard(items)
            
            cmd_list = ["1", "2","3"]
            cmd = getcmd(cmd_list)

            if cmd=="1":
                if not walked_the_wall:
                    nicePrint("""Balancing you walk along the slippery stone wall,
                    passing by the shed you get a better look at it.\n""")
                    time.sleep(1)
                    nicePrint("""It's made of rough wooden planks but it seems to be a solid build,
                    the planks are packed tightly and the roof is covered with tar,
                    probably it's dry inside.\n""")
                    input("Press enter.\n")
                    nicePrint("""You continue to follow the wall, all the time keeping an eye on the dog.
                    It hasn't noticed you or has no interest, but it's continuously moving around the yard.\n""")
                    time.sleep(1)
                    nicePrint("""You manage to reach the gate without falling off the wall,
                    from here you can see the surrounding area,
                    the gate is wooden and simple it has no lock on it,
                    and seems the only way to enter or leave the yard\n""")
                    walked_the_wall=True
                    time.sleep(1)
                else:
                    nicePrint("You navigate the wall and get to the gate.\n")

                nicePrint("Open the gate?\n")
                print("""1. Yes
2. No\n""")

                caller_text = """1. Yes
2. No\n"""

                cmd_list=["1","2", "yes", "no", "search", "look", "examine"]
                cmd = getcmd(cmd_list)

                if cmd=="1" or cmd.lower()=="yes":
                    nicePrint("""Hanging from the top of the wall you strech yourself thowards the door lock.\n""")
                    input("Press enter.\n")
                    nicePrint("Everything is wet and slippery\n")
                    time.sleep(1)
                    nicePrint("but you manage to reach the lock and raise the lock\n")
                    time.sleep(1)
                    nicePrint("pull yourself back to the top of the wall and slide the door open.\n")
                    time.sleep(1)
                    nicePrint("""You don't know when it came but the dark shape of the dog is already standing in front of the door
                    silent and tense.
                    For a moment it hesitates\n""")
                    time.sleep(1)
                    nicePrint("""just for a moment, and then it starts running outside
                    mud flies into the air as the massive creature runs through the gate
                    and dissapears into the woods.\n""")
                    time.sleep(1)
                    nicePrint("The backyard is now empty.\n")
                    backyard_door_open = True
                    sneak_backyard(items)
                elif cmd=="2" or  cmd.lower()=="no":
                    nicePrint("you leave the door closed and jump down from the wall.\n")
                    sneak_backyard(items)
                
                elif cmd.lower()=="search" or cmd.lower()== "look" or cmd.lower()== "examine":
                    if not dock_found:
                        nicePrint("""From atop the wall you have a better vantage point of the surroundings.
                        To the right shrubs and trees dissapear in the dark,
                        to the left is the outpost,
                        in front the river streches like a unpassable obstacle.\n""")
                        time.sleep(2)
                        nicePrint("""Lightning stirkes and for a moment it's bright like a day,
                        you see a path with a wooden handrail leading down to the river.\n""")
                        time.sleep(1)
                        nicePrint("""The lightning flash passes and the world is dark again.\n""")
                        dock_found = True
                    else:
                        nicePrint("There is nothing left to be found here.\n")
                    nicePrint("Open the gate?\n")
                    print("""1. Yes
2. No\n""")     

                    cmd_list=["1","2", "yes", "no"]
                    cmd = getcmd(cmd_list)

                    if cmd=="1" or cmd.lower()=="yes":
                        nicePrint("""Hanging from the top of the wall you strech yourself thowards the door handle.\n""")
                        input("Press enter.\n")
                        nicePrint("Everything is wet and slippery\n")
                        time.sleep(1)
                        nicePrint("but you manage to reach the handle and raise the it\n")
                        time.sleep(1)
                        nicePrint("pull yourself back to the top of the wall and slide the door open.\n")
                        time.sleep(1)
                        nicePrint("""You don't know when it came but the dark shape of the dog is already standing in front of the door
                        silent and tense.
                        For a moment it hesitates\n""")
                        time.sleep(1)
                        nicePrint("""just for a moment, and then it starts running outside
                        mud flies into the air as the massive creature runs through the gate
                        and dissapears into the woods.\n""")
                        time.sleep(1)
                        nicePrint("The backyard is now empty.\n")
                        backyard_door_open = True
                        sneak_backyard(items)
                    elif cmd=="2" or  cmd.lower()=="no":
                        nicePrint("you leave the door closed and jump down from the wall.\n")
                        sneak_backyard(items)
                    else:
                        nicePrint("You can't do that, try something else.\n")
                        getcmd(cmd_list)
            elif cmd=="2":
                nicePrint("You jump down outside the backyard, mud splashes around your boots.\n")
                sneak_backyard(items)
            
            elif cmd=="3": 
                if "fish" in items: 
                    nicePrint("""You toss the fish to the muddy ground in front of the dog,
                    it sniffs the fish, rasies it's head and sees you on the wall,
                    inspite the cold shivers go down your back as you lock eyes with the beast.\n""")
                    input("Press enter.\n")
                    nicePrint("""The dog takes the fish and starts to crunch it with it's jaws,
                    you have a feeling it will not bother you anymore.\n""")
                    backyard_door_open = True
                    sneak_backyard(items)
                else:
                    nicePrint("You can't do that, try something else.\n")
                    sneak_backyard(items) 
                    
        elif cmd == "6":
            if not dock_found:
                nicePrint("You can't do that, try something else.\n")
                sneak_backyard(items) 
            dock(items)           

        elif cmd.lower()=="search" or cmd.lower()== "look" or cmd.lower()== "examine":
            backyard_search()

        elif cmd.lower()=="window" or cmd.lower()== "look window" or cmd.lower()== "look at window":
            nicePrint("""Looking up to the only lit window on the outpost you have to protect your eyes from the rain
            for a time nothing happens but eventually  you see shadows dancing on the window
            definitely there is someone in that room.\n""")
            sneak_backyard(items)
        else:
            nicePrint("You can't do that try something else.\n")
            getcmd(cmd_list)

    elif dock_found:

        nicePrint("You decide to : \n")
        print("""1. Sneak to the wall.
2. Climb over the wall.
3. Enter through the door in the wall.
4. Go back to the main road.
5. Follow the path down to the river.\n""")

        caller_text = """1. Sneak to the wall.
2. Climb over the wall.
3. Enter through the door in the wall.
4. Go back to the main road.
5. Follow the path down to the river.\n"""
    
    

    
        cmd_list = ["1", "2", "3", "4", "5","search", "look", "examine", "window", "look window", "look at window"]
        cmd = getcmd(cmd_list)

        if cmd == "1":
            if backyard_door_open:
                nicePrint("You can't do that, try something else.\n")
                sneak_backyard(items)
            if not dog_discovered:
                nicePrint("""Moving like a shadow through the rain
                moments later you crouch next to the wet wall.\n""")
                input("Press enter.\n")
                nicePrint("From the other side of the wall you can hear movement through muddy ground\n")
                time.sleep(2)
                nicePrint("and a nervous dog growl\n")
                time.sleep(2)
                nicePrint("a really big dog's growl.\n")
                    
                dog_discovered = True
                empty_porch_counter +=1 
                sneak_backyard(items)
            else:
                nicePrint("You already learned all that you can, there is no point to go sneak to the wall again\n")
                sneak_backyard(items)
        
        elif cmd=="2":
            if backyard_door_open:
                nicePrint("You can't do that, try something else.\n")
                sneak_backyard(items)
            if not dog_discovered:
                nicePrint("""You find a stone in the wall and a suitable foothold
                and in a couple of moments you jump across it into the backyard.\n""")
                input("Press enter.\n")
                nicePrint("""Your boots sink ancle deep into the soft cold mud.
                The back yard is unlit and the only light is coming from the window above.\n""")
                time.sleep(2)
                nicePrint("""You quckly spot your surrounding, to the left is the back of the outpost,
                on the right nested on the wall of the backyard is\n""")
                nicePrintRed("SPLAT")
                time.sleep(2)
                nicePrint("""You push your face out of the mud,
                something big and strong has knocked you to the ground.\n""")
                time.sleep(1)
                nicePrint("You instinctively swing around, dagger in hand.\n")
                time.sleep(1)
                nicePrint("""In the shadows through the rain you see a pair of eyes burning with rage,
                set of teeth almost shining in the window light,
                the beast is huge its fur dark and covered with mud.\n""")
                time.sleep(1)
                nicePrint("It moves straight towards you, not running but slowly.")
                nicePrint("The thing that passes through your mind is that it didn't bark at all.\n")
                input("Press enter.\n")
                nicePrint("""In the morning what is left of your ragged corpse is tossed into the river,
                in the backyard the huge dog's paw squishes a small metal ball deeper into the mud.\n""")
                nicePrint("""You have died,
                GAME OVER\n""")
                sys.exit(1)
            else:
                nicePrint("With that thing there you really don't wont do jump inside.\n")
                sneak_backyard(items)

        elif cmd=="3":
            empty_porch_counter += 1
            if backyard_door_open:
                nicePrint("You can't do that, try something else.\n")
                sneak_backyard(items)
            if not dog_discovered:
                at_the_backyard_door(items)
            else:
                nicePrint("That beast looks like it doesn't want to let you in, maybe try some other way.\n")
                sneak_backyard(items)
        elif cmd=="4":
            nicePrint("You return to the main road.")
            empty_porch_counter +=1 
            start(items)
        elif cmd=="5":
            if not dock_found:
                nicePrint("You can't do that, try something else.\n")
                sneak_backyard(items) 
            dock(items) 
        elif cmd.lower()=="search" or cmd.lower()== "look" or cmd.lower()== "examine":
            backyard_search()

        elif cmd.lower()=="window" or cmd.lower()== "look window" or cmd.lower()== "look at window":
            nicePrint("""Looking up to the only lit window on the outpost you have to protect your eyes from the rain
            for a time nothing happens but eventually  you see shadows dancing on the window
            definitely there is someone in that room.\n""")
            sneak_backyard(items)
        else:
            nicePrint("You can't do that try something else.\n")
            getcmd(cmd_list)

    elif backyard_door_open:  
        print("""1. Go back to the main road.
2. Go into the backyard.\n""")
       
        caller_text = """1. Go into the backyard.
2. Go back to the main road.\n"""

        cmd_list = ["1", "2", "search", "look", "examine", "window", "look window", "look at window"]
        cmd = getcmd(cmd_list)

        if cmd=="1":
            nicePrint("You return to the main road.")
            empty_porch_counter +=1 
            start(items)
                            
        elif cmd=="2":
            if not backyard_door_open:
                nicePrint("You can't do that, try something else.\n")
                sneak_backyard(items) 
            in_the_backyard(items) 
            
        elif cmd.lower()=="search" or cmd.lower()== "look" or cmd.lower()== "examine":
            backyard_search()

        elif cmd.lower()=="window" or cmd.lower()== "look window" or cmd.lower()== "look at window":
            nicePrint("""Looking up to the only lit window on the outpost you have to protect your eyes from the rain
            for a time nothing happens but eventually  you see shadows dancing on the window
            definitely there is someone in that room.\n""")
            sneak_backyard(items)
        else:
            nicePrint("You can't do that try something else.\n")
            getcmd(cmd_list)
    
    elif dog_discovered:
        nicePrint("You decide to : \n")
        print("""1. Sneak to the wall.
2. Climb over the wall.
3. Enter through the door in the wall.
4. Go back to the main road.
5. Climb quietly onto the wall.\n""")
        caller_text = """1. Sneak to the wall.
2. Climb over the wall.
3. Enter through the door in the wall.
4. Go back to the main road.
5. Climb quietly onto the wall.\n"""

        cmd_list = ["1", "2", "3", "4", "5", "search", "look", "examine", "window", "look window", "look at window"]
        cmd = getcmd(cmd_list)

        if cmd == "1":
            if backyard_door_open:
                nicePrint("You can't do that, try something else.\n")
                sneak_backyard(items)
            if not dog_discovered:
                nicePrint("""Moving like a shadow through the rain
                moments later you crouch next to the wet wall.\n""")
                input("Press enter.\n")
                nicePrint("From the other side of the wall you can hear movement through muddy ground\n")
                time.sleep(2)
                nicePrint("and a nervous dog growl\n")
                time.sleep(2)
                nicePrint("a really big dog's growl.\n")
                    
                dog_discovered = True
                empty_porch_counter +=1 
                sneak_backyard(items)
            else:
                nicePrint("You already learned all that you can, there is no point to go sneak to the wall again\n")
                sneak_backyard(items)
        
        elif cmd=="2":
            if backyard_door_open:
                nicePrint("You can't do that, try something else.\n")
                sneak_backyard(items)
            if not dog_discovered:
                nicePrint("""You find a stone in the wall and a suitable foothold
                and in a couple of moments you jump across it into the backyard.\n""")
                input("Press enter.\n")
                nicePrint("""Your boots sink ancle deep into the soft cold mud.
                The back yard is unlit and the only light is coming from the window above.\n""")
                time.sleep(2)
                nicePrint("""You quckly spot your surrounding, to the left is the back of the outpost,
                on the right nested on the wall of the backyard is\n""")
                nicePrintRed("SPLAT")
                time.sleep(2)
                nicePrint("""You push your face out of the mud,
                something big and strong has knocked you to the ground.\n""")
                time.sleep(1)
                nicePrint("You instinctively swing around, dagger in hand.\n")
                time.sleep(1)
                nicePrint("""In the shadows through the rain you see a pair of eyes burning with rage,
                set of teeth almost shining in the window light,
                the beast is huge its fur dark and covered with mud.\n""")
                time.sleep(1)
                nicePrint("It moves straight towards you, not running but slowly.")
                nicePrint("The thing that passes through your mind is that it didn't bark at all.\n")
                input("Press enter.\n")
                nicePrint("""In the morning what is left of your ragged corpse is tossed into the river,
                in the backyard the huge dog's paw squishes a small metal ball deeper into the mud.\n""")
                nicePrint("""You have died,
                GAME OVER\n""")
                sys.exit(1)
            else:
                nicePrint("With that thing there you really don't wont do jump inside.\n")
                sneak_backyard(items)

        elif cmd=="3":
            empty_porch_counter += 1
            if backyard_door_open:
                nicePrint("You can't do that, try something else.\n")
                sneak_backyard(items)
            if not dog_discovered:
                at_the_backyard_door(items)
                
            else:
                nicePrint("That beast looks like it doesn't want to let you in, maybe try some other way.\n")
                sneak_backyard(items)
        elif cmd=="4":
            nicePrint("You return to the main road.")
            empty_porch_counter +=1 
            start(items)
        elif cmd=="5":
            if backyard_door_open:
                nicePrint("You can't do that, try something else.\n")
                sneak_backyard(items)
            if dog_discovered:
                if not on_wall_first:
                    nicePrint("""In a couple of moments you are at the stone wall,
                    quickly you find some protruding stones in the wall and scale it easily.\n""")
                    time.sleep(2)
                    nicePrint("""Crouching on the top of the wall you are seen by no eyes,
                    The back yard is closed by all sides, along the wall there is a small gate leading into the yard,
                    on the back wall of the outpost there is a door leading inside.
                    Nested against the inside of the wall there is a shed.\n""")
                    time.sleep(2)
                    nicePrint("""Moving like a shadow through the rain a beast of a dog roams the yard.
                    The thing is huge, the largest dog you have ever seen, if it's a dog at all.
                    It looks nervous and agitated, not stopping like a beast in a cage.
                    It hasn't noticed you.\n""")
                    on_wall_first=True
                else:
                    nicePrint("You climb on the wall, nothing has changed.\n")

                input("Press enter.\n")
                nicePrint("You decide to :\n")
                if "fish" in items:
                    print("""1. Walk on the wall to the gate.
2. Jump back down.
3. Throw the dog a fish.\n""")
                    caller_text = """1. Walk on the wall to the gate.
2. Jump back down.
3. Throw the dog a fish.\n"""
                else:
                    print("""1. Walk on the wall to the gate.
2. Jump back down.\n""") 
                    caller_text = """1. Walk on the wall to the gate.
2. Jump back down.\n"""
                empty_porch_counter +=1
            else:
                nicePrint("You can't do that, try something else.")
                sneak_backyard(items)
            
            cmd_list = ["1", "2","3"]
            cmd = getcmd(cmd_list)

            if cmd=="1":
                if not walked_the_wall:
                    nicePrint("""Balancing you walk along the slippery stone wall,
                    passing by the shed you get a better look at it.\n""")
                    time.sleep(1)
                    nicePrint("""It's made of rough wooden planks but it seems to be a solid build,
                    the planks are packed tightly and the roof is covered with tar,
                    probably it's dry inside.\n""")
                    input("Press enter.\n")
                    nicePrint("""You continue to follow the wall, all the time keeping an eye on the dog.
                    It hasn't noticed you or has no interest, but it's continuously moving around the yard.\n""")
                    time.sleep(1)
                    nicePrint("""You manage to reach the gate without falling off the wall,
                    from here you can see the surrounding,
                    the gate is wooden and simple it has no lock on it,
                    and seems the only way to enter or leave the yard\n""")
                    walked_the_wall=True
                    time.sleep(1)
                else:
                    nicePrint("You navigate the wall and get to the gate.\n")

                nicePrint("Open the gate?\n")
                print("""1. Yes
2. No\n""")

                caller_text = """1. Yes
2. No\n"""

                cmd_list=["1","2", "yes", "no", "search", "look", "examine"]
                cmd = getcmd(cmd_list)

                if cmd=="1" or cmd.lower()=="yes":
                    nicePrint("""Hanging from the top of the wall you strech yourself thowards the door lock.\n""")
                    input("Press enter.\n")
                    nicePrint("Everything is wet and slippery\n")
                    time.sleep(1)
                    nicePrint("but you manage to reach the lock and raise the lock\n")
                    time.sleep(1)
                    nicePrint("pull yourself back to the top of the wall and slide the door open.\n")
                    time.sleep(1)
                    nicePrint("""You don't know when it came but the dark shape of the dog is already standing in front of the door
                    silent and tense.
                    For a moment it hesitates\n""")
                    time.sleep(1)
                    nicePrint("""just for a moment, and then it starts running outside
                    mud flies into the air as the massive creature runs through the gate
                    and dissapears into the woods.\n""")
                    time.sleep(1)
                    nicePrint("The backyard is now empty.\n")
                    backyard_door_open = True
                    sneak_backyard(items)
                elif cmd=="2" or  cmd.lower()=="no":
                    nicePrint("you leave the door closed and jump down from the wall.\n")
                    sneak_backyard(items)
                
                elif cmd.lower()=="search" or cmd.lower()== "look" or cmd.lower()== "examine":
                    if not dock_found:
                        nicePrint("""From atop the wall you have a better vantage point of the surroundings.
                        To the right shrubs and trees dissapear in the dark,
                        to the left is the outpost,
                        in front the river streches like a unpassable obstacle.\n""")
                        time.sleep(2)
                        nicePrint("""Lightning stirkes and for a moment it's bright like a day,
                        you see a path with a wooden handrail leading down to the river.\n""")
                        time.sleep(1)
                        nicePrint("""The lightning flash passes and the world is dark again.\n""")
                        dock_found = True
                    else:
                        nicePrint("There is nothing left to be found here.\n")
                    nicePrint("Open the gate?\n")
                    print("""1. Yes
2. No\n""")     

                    cmd_list=["1","2", "yes", "no"]
                    cmd = getcmd(cmd_list)

                    if cmd=="1" or cmd.lower()=="yes":
                        nicePrint("""Hanging from the top of the wall you strech yourself thowards the door handle.\n""")
                        input("Press enter.\n")
                        nicePrint("Everything is wet and slippery\n")
                        time.sleep(1)
                        nicePrint("but you manage to reach the handle and raise the it\n")
                        time.sleep(1)
                        nicePrint("pull yourself back to the top of the wall and slide the door open.\n")
                        time.sleep(1)
                        nicePrint("""You don't know when it came but the dark shape of the dog is already standing in front of the door
                        silent and tense.
                        For a moment it hesitates\n""")
                        time.sleep(1)
                        nicePrint("""just for a moment, and then it starts running outside
                        mud flies into the air as the massive creature runs through the gate
                        and dissapears into the woods.\n""")
                        time.sleep(1)
                        nicePrint("The backyard is now empty.\n")
                        backyard_door_open = True
                        sneak_backyard(items)
                    elif cmd=="2" or  cmd.lower()=="no":
                        nicePrint("you leave the door closed and jump down from the wall.\n")
                        sneak_backyard(items)
                    else:
                        nicePrint("You can't do that, try something else.\n")
                        getcmd(cmd_list)
            elif cmd=="2":
                nicePrint("You jump down outside the backyard, mud splashes around your boots.\n")
                sneak_backyard(items)
            
            elif cmd=="3": 
                if "fish" in items: 
                    nicePrint("""You toss the fish to the muddy ground in front of the dog,
                    it sniffs the fish, rasies it's head and sees you on the wall,
                    inspite the cold shivers go down your back as you lock eyes with the beast.\n""")
                    input("Press enter.\n")
                    nicePrint("""The dog takes the fish and starts to crunch it with it's jaws,
                    you have a feeling it will not bother you anymore.\n""")
                    backyard_door_open = True
                    sneak_backyard(items)
                else:
                    nicePrint("You can't do that, try something else.\n")
                    sneak_backyard(items) 
                    
        elif cmd.lower()=="search" or cmd.lower()== "look" or cmd.lower()== "examine":
            backyard_search()

        elif cmd.lower()=="window" or cmd.lower()== "look window" or cmd.lower()== "look at window":
            nicePrint("""Looking up to the only lit window on the outpost you have to protect your eyes from the rain
            for a time nothing happens but eventually  you see shadows dancing on the window
            definitely there is someone in that room.\n""")
            sneak_backyard(items)
        else:
            nicePrint("You can't do that try something else.\n")
            getcmd(cmd_list)

    else:
        nicePrint("You decide to : \n")
        print("""1. Sneak to the wall.
2. Climb over the wall.
3. Enter through the door in the wall.
4. Go back to the main road.\n""")

        caller_text = """1. Sneak to the wall.
2. Climb over the wall.
3. Enter through the door in the wall.
4. Go back to the main road.\n"""
    
    

    
        cmd_list = ["1", "2", "3", "4", "search", "look", "examine", "window", "look window", "look at window"]
        cmd = getcmd(cmd_list)

        if cmd == "1":
            if backyard_door_open:
                nicePrint("You can't do that, try something else.\n")
                sneak_backyard(items)
            if not dog_discovered:
                nicePrint("""Moving like a shadow through the rain
                moments later you crouch next to the wet wall.\n""")
                input("Press enter.\n")
                nicePrint("From the other side of the wall you can hear movement through muddy ground\n")
                time.sleep(2)
                nicePrint("and a nervous dog growl\n")
                time.sleep(2)
                nicePrint("a really big dog's growl.\n")
                    
                dog_discovered = True
                empty_porch_counter +=1 
                sneak_backyard(items)
            else:
                nicePrint("You already learned all that you can, there is no point to go sneak to the wall again\n")
                sneak_backyard(items)
        
        elif cmd=="2":
            if backyard_door_open:
                nicePrint("You can't do that, try something else.\n")
                sneak_backyard(items)
            if not dog_discovered:
                nicePrint("""You find a stone in the wall and a suitable foothold
                and in a couple of moments you jump across it into the backyard.\n""")
                input("Press enter.\n")
                nicePrint("""Your boots sink ancle deep into the soft cold mud.
                The back yard is unlit and the only light is coming from the window above.\n""")
                time.sleep(2)
                nicePrint("""You quckly spot your surrounding, to the left is the back of the outpost,
                on the right nested on the wall of the backyard is\n""")
                nicePrintRed("SPLAT")
                time.sleep(2)
                nicePrint("""You push your face out of the mud,
                something big and strong has knocked you to the ground.\n""")
                time.sleep(1)
                nicePrint("You instinctively swing around, dagger in hand.\n")
                time.sleep(1)
                nicePrint("""In the shadows through the rain you see a pair of eyes burning with rage,
                set of teeth almost shining in the window light,
                the beast is huge its fur dark and covered with mud.\n""")
                time.sleep(1)
                nicePrint("It moves straight towards you, not running but slowly.")
                nicePrint("The thing that passes through your mind is that it didn't bark at all.\n")
                input("Press enter.\n")
                nicePrint("""In the morning what is left of your ragged corpse is tossed into the river,
                in the backyard the huge dog's paw squishes a small metal ball deeper into the mud.\n""")
                nicePrint("""You have died,
                GAME OVER\n""")
                sys.exit(1)
            else:
                nicePrint("With that thing there you really don't wont do jump inside.\n")
                sneak_backyard(items)

        elif cmd=="3":
            empty_porch_counter += 1
            if backyard_door_open:
                nicePrint("You can't do that, try something else.\n")
                sneak_backyard(items)
            if not dog_discovered:
                at_the_backyard_door(items)
            else:
                nicePrint("That beast looks like it doesn't want to let you in, maybe try some other way.\n")
                sneak_backyard(items)
        elif cmd=="4":
            nicePrint("You return to the main road.")
            empty_porch_counter +=1 
            start(items)
        elif cmd.lower()=="search" or cmd.lower()== "look" or cmd.lower()== "examine":
            backyard_search()

        elif cmd.lower()=="window" or cmd.lower()== "look window" or cmd.lower()== "look at window":
            nicePrint("""Looking up to the only lit window on the outpost you have to protect your eyes from the rain
            for a time nothing happens but eventually  you see shadows dancing on the window
            definitely there is someone in that room.\n""")
            sneak_backyard(items)
        else:
            nicePrint("You can't do that try something else.\n")
            getcmd(cmd_list)


#when comabt happens
def combat_situation():

    global combat
    combat=True

    if wounded:
        nicePrint("""Your mind races and heart pounds,
        you reach for your weapon but sharp pain reminds you of the wounded arm.\n""")
        time.sleep(2)
        nicePrint("""You manage to draw your dagger with your off hand
        and await the Wardens attack.""")
        input("Press enter.\n")
        nicePrint("""You swing defensively but it is hopeless.
        A crossbow bolt strikes your gut and another Warden's spear finds your chest.
        You taste blood in your mouth and loose all of your strength.\n""")
        time.sleep(2)
        nicePrintMenacing("The world becomes blurry and in the end dark.\n")
        nicePrintMenacing("""GAME OVER
        You have died.\n""")        
        time.sleep(3)
        sys.exit(1)
    if crossbow_taken:
        nicePrint("There is no time to prepare the crossbow now.\n")
    nicePrint("""As much as you always wanted to avoid these situations you have been here before.
Weapons will be drawn and blood shed.
You know how to hold your ground in a fight but close combat is not your game.\n""")
    if "hook" in items:
        nicePrint("""Use hook as a secondary weapon, 
        it is not an excellent weapon but it will increase your chances.\n""")
        print("""1. Yes
    2.No\n""")
        cmd_list=["1","2","yes","no"]
        cmd = getcmd(cmd_list)
        if cmd=="1" or cmd.lower()=="yes":
            nicePrint("""You attack the approaching Wardens dagger in one and a hook in other hand.
            You catch the first spear with the hook and deflect the other with the dagger.
            The Wardens curse as you lock them both in clinch.\n""")
            time.sleep(2)
            nicePrint("""Sharp pain in your leg breaks the stalemate, 
            the guard dog is tearing at your calf.
            The pain is too great and you drop your guard.\n""")
            time.sleep(2)
            nicePrint("""The older Warden takes his chance and stikes
            throwing you to the mud, they lash at you with out mercy.
            The last you feel is the taste of mud.\n""")
            nicePrintMenacing("""GAME OVER
            You have died.\n""")        
            time.sleep(3)
            sys.exit(1)
        elif cmd=="2" or cmd.lower()=="no":
            nicePrint("You draw your trusted dagger and engage the Wardens.\n")
            time.sleep(2)
            nicePrint("""You try to use a feint the first Warden by moving to his side,
            but you are outmatched, they use the length of their spears
            and trusted tactics.\n""")
            time.sleep(2)
            nicePrint("""One Warden thrust at your leg , 
            you manage to block, but realise that it was just a trick,
            the other stabs you through the stomach.
            You writhe with pain as he pulls the spear.
            Blood and guts mix with the mud.\n""")
            input("Press enter.\n")
            nicePrint("""You are still conscious as they search you 
            and decide to throw you in the river.
            The bride is tall and the fall feels like eternity.\n""")
            nicePrintMenacing("""GAME OVER
            You have died.\n""")        
            time.sleep(3)
            sys.exit(1)
        else:
            nicePrint("You can't do that, try something else.\n")
            combat_situation()
    elif "club" in items:
        nicePrint("""Use the club as a secondary weapon, it is not a sword but hits hard.\n""")
        cmd_list=["1","2","yes","no"]
        cmd = getcmd(cmd_list)
        if cmd=="1" or cmd.lower()=="yes":
            nicePrint("""You attack the approaching Wardens dagger in one and a club in other hand.
            You block the first spear with the club and deflect the other with the dagger.
            The Wardens curse as you lock them both in clinch.\n""")
            time.sleep(2)
            nicePrint("""Sharp pain in your leg breaks the stalemate, 
            the guard dog is tearing at your calf.
            The pain is too great and you drop your guard.\n""")
            time.sleep(2)
            nicePrint("""The older Warden takes his chance and stikes
            throwing you to the mud, they lash at you with out mercy.
            The last you feel is the taste of mud.\n""")
            nicePrintMenacing("""GAME OVER
            You have died.\n""")        
            time.sleep(3)
            sys.exit(1)
        elif cmd=="2" or cmd.lower()=="no":
            nicePrint("You draw your trusted dagger and engage the Wardens.\n")
            time.sleep(2)
            nicePrint("""You try to use a feint the first Warden by moving to his side,
            but you are outmatched, they use the length of their spears
            and trusted tactics.\n""")
            time.sleep(2)
            nicePrint("""One Warden thrust at your leg , 
            you manage to block, but realise that it was just a trick,
            the other stabs you through the stomach.
            You writhe with pain as he pulls the spear.
            Blood and guts mix with the mud.\n""")
            input("Press enter.\n")
            nicePrint("""You are still conscious as they search you 
            and decide to throw you in the river.
            The bride is tall and the fall feels like eternity.\n""")
            nicePrintMenacing("""GAME OVER
            You have died.\n""")        
            time.sleep(3)
            sys.exit(1)
        else:
            nicePrint("You can't do that, try something else.\n")
            combat_situation()
    else:
        nicePrint("You can't do that, try something else.\n")
        getcmd(cmd_list)
    
#The choices when the player approaches the Wardens directly
def choice():
    print()
    print("1. Show the guards your papers.")
    print("2. Don't show your papers.")
    cmd_list = ["1", "2", "run", "go back", "escape", "attack", "fight", "combat"]
    cmd = getcmd(cmd_list)
    if cmd=="1":
        if "traveling papers" in items:
            del items["traveling papers"]
            nicePrint("The older Warden takes your papers and looks at them under the light.")
            print()
            input("Press enter.")
            nicePrintRed("Right Ulrich, we have us here a swindler.")
            print()
            nicePrint("Younger guard swings his spear, pointing the tip to your chest")
            print()
            nicePrintRed("Don't make this difficult, it will hurt you more than it will us.")
            print()
            input("Press enter.")
            print("1. Surrender")
            print("2. Run")
            print("3. Fight")
            print()
            cmd_list = ["1", "2", "3"]
            cmd = getcmd(cmd_list)
            if cmd=="1":
                nicePrint("""After a moment you decide to suerrender to the Wardens, 
                You are taken inside the outpost building and locked in cell in the basement.
                You are stripped of your belongings, the guards just glance over the prize,
                not giving it any attention.""")
                print()
                input("Press enter.")
                nicePrint("""A couple of days pass dully, the rain still drumming outside.
                Your arrival in Altdorf is unnoticed by anyone, after a quick trial you are sentenced
                to a month in jail""")
                print()
                input("Press enter.")
                nicePrint("""Eventually you are released, you are a little rougher around the edges,
                    but free,
                now you just have to explain to your employers what happend to their prize.""" )
                print()
                print("Game Over")
                print("Auf wiederzhn!.")
                try:
                    sys.exit(1)
                except SystemExit as e:
                    pass

            elif cmd=="2":
                print()
                nicePrint("""You pretend to take out your papers but,
                suddenly you turn around and start running back to the road,
                leaving the unprepared guards behind.""")
                print()
                nicePrint("""The most important skill for a thief is running, you thought, smiling,
                rain washing your face""")
                print()
                input("Press enter.")
                nicePrint("""Your world turns pitch black, a well placed hit to the back of the head
                knocks you unconscious""")
                print()
                nicePrint("Another guard steps around the corner with a club in hand.")
                print()
                nicePrint("You awake with a splitting headache in a prisoner cart on the road to Altodrf.")
                print()
                nicePrint("After a quick trial you are sentenced to a month in jail")
                print()
                input("Press enter.")
                nicePrint("""Eventually you are released, you are a little rougher around the edges,
                    but free,
                now you just have to explain to your employers what happend to their prize.""" )
                print()
                print("Game Over")
                print("Auf wiederzhn!.")
                time.sleep(3)
                try:
                    sys.exit(1)
                except SystemExit as e:
                    pass
            
            elif cmd == "3":
                print()
                nicePrint("""You pretend to pull out your papers but instead draw your dagger,
                with your left hand you push away the spear and immediately slash at the younger guard.
                He steps back supprised trying to point his spear towards you, 
                but his long weapon a disadvantage in this situation.""")
                print()
                input("Press enter.")
                nicePrint("""You charge him and close the distance, shlashing him across the chest.
                His uniform opening like i flower revealing a crimson red inside.""")
                print()
                input("Press enter.")
                nicePrint("His face a mix of fear and surprise, you continue to attack.")
                nicePrint("""A dull pain from your back draws your attention from the young Warden,
                In the moment you thought that you cought your jacket on something, your movement limited,
                but the bloody spear tip protruding from your stomach makes you realize that it's something else.""")
                print()
                input("Press enter.")
                nicePrint("""Your arms loose strength as the older Warden pulls his spear from you,
                you collapse to the muddy road, your knees sinking into the soft mud.
                Another, this time sharper pain from the back.
                Your face hits the cold mud.""" )
                print()
                input("Press enter.")
                nicePrintMenacing("The last thing you think is that running is the most important skill for a thief")
                print()
                input("Press enter.")
                nicePrintMenacing("running away")
                nicePrint("You have died.")
                print()
                print("Game Over")
                print("Auf wiederzhn!.")
                try:
                    sys.exit(1)
                except SystemExit as e:
                    pass
            else:
                nicePrint("You can't do that, try something else.")
                cmd = getcmd(cmd_list)
        

    elif cmd=="2" :
        print()
        nicePrint("""You decide not to show your papers to the wardens, these are fake and they whould surely notice.
        It's better to be caught without any papers than with forgeries""")
        print()
        input("Press enter.")
        nicePrint("""No traveling papers, eh?
        You do realize that we HAVE to arrest you now, says the older Warden, sarcastically.""")
        print()
        nicePrint("""They search you and take anything of value, including the prize,
        in the morning  the bridge gates are opened and you continue on your way to Altodrf""")
        print()
        input("Press enter.")
        nicePrint("""Its still raining when you make it to the narrow strets of the city,
        you are cold, wet and dirt poor,
        and you have to expalin to your employers what happened.""")
        print()
        print("Game Over")
        print("Auf wiederzhn!.")
        try:
            sys.exit(1)
        except SystemExit as e:
            pass

    elif cmd=="run" or cmd =="go back" or cmd == "escape":
        print()
        nicePrint("""You pretend to take out your papers but,
                suddenly you turn around and start running back to the road,
                leaving the unprepared guards behind.""")
        print()
        nicePrint("""The most important skill for a thief is running, you thought, smiling,
        rain washing your face""")
        print()
        input("Press enter.")
        nicePrint("""Your world turns pitch black, a well placed hit to the back of the head
        knocks you unconscious""")
        print()
        nicePrint("Another guard steps around the corner with a club in hand.")
        print()
        nicePrint("You awake with a splitting headache in a prisoner cart on the road to Altodrf.")
        print()
        nicePrint("After a quick trial you are sentenced to a month in jail")
        print()
        input("Press enter.")
        nicePrint("""Eventually you are released, you are a little rougher around the edges,
            but free,
        now you just have to explain to your employers what happend to their prize.""" )
        print()
        print("Game Over")
        print("Auf wiederzhn!.")
        try:
            sys.exit(1)
        except SystemExit as e:
            pass

    elif cmd=="attack" or cmd =="fight" or cmd =="combat":
        print()
        nicePrint("""You pretend to pull out your papers but instead draw your dagger,
                with your left hand you push away the spear and immediately slash at the younger guard.
                He steps back supprised trying to point his spear towards you, 
                but his long weapon a disadvantage in this situation.""")
        print()
        input("Press enter.")
        nicePrint("""You charge him and close the distance, shlashing him across the chest.
        His uniform opening like i flower revealing a crimson red inside.""")
        print()
        input("Press enter.")
        nicePrint("His face a mix of fear and surprise, you continue to attack.")
        nicePrint("""A dull pain from your back draws your attention from the young Warden,
        In the moment you thought that you cought your jacket on something, your movement limited,
        but the bloody spear tip protruding from your stomach makes you realize that it's something else.""")
        print()
        input("Press enter.")
        nicePrint("""Your arms loose strength as the older Warden pulls his spear from you,
        you collapse to the muddy road, your knees sinking into the soft mud.
        Another, this time sharper pain from the back.
        Your face hits the cold mud.""" )
        print()
        input("Press enter.")
        nicePrintMenacing("The last thing you think is that running is the most important skill for a thief")
        print()
        input("Press enter.")
        nicePrintMenacing("running away")
        nicePrint("You have died.")
        print()
        print("Game Over")
        print("Auf wiederzhn!.")
        try:
            sys.exit(1)
        except SystemExit as e:
            pass
    else:
        nicePrint("You can't do that, try something else.")
        cmd = getcmd(cmd_list)

#When the Wardens return to the front proch
def wardens_have_returned(items):

    global combat
    combat = True

    
    nicePrintRed("HALT BRIGAND!\n")
    time.sleep(1)
    nicePrint("""You are interrupted by a shout from behind and a thud of a crossbow bolt next to your head
    as you swing around you see the two Wardens, soaked and mad,
    the dog is held back only by the rope in Wardens hands.\n""")
    time.sleep(1)
    nicePrintRed("""Surrender or die bastard.\n""")
    print("""1. Surrender.
2. Fight
3. Run.\n""")

    cmd_list = ["1", "2", "3"]
    cmd = getcmd(cmd_list)        

    if cmd=="1":
        if wounded:
            nicePrint("""You reach for the blade but the pain reminds you of your wounded arm.
            Evaluating the situation you decide to surrender to the Wardens.\n""")
            time.sleep(1)
            nicePrint("""The Wardens approach you carefully from two sides, spears pointed at you.
            They quickly disarm and tie you.
            They grunge and curse you and the rain.
            Once they see all that you have done they argue weather to bother with you or to throw you in the river.
            You are saved only by the word of the highest ranking Warden,
            a brass pin decorating his leather west.
            You are thrown in the basement cell, your torn up arm and face and bleeding.\n""")
            time.sleep(2)
            nicePrint("""In the morning a cart takes you tied up to Altdorf, 
            where you are sentenced to months in jail.\n""")
            input("Press enter.\n")
            nicePrint("""Time passes slowly, your arm gets worse and worse.
            the prison physician cuts it off without gloatin or joy.\n""")
            time.sleep(2)
            nicePrint("""Next weeks are a blur, mixture of dreamless nights and waking nightmares.
            Weeks turn into months and eventually you are released, 
            skinny and worn out, with scars to remind you of your last job.
            The valuable prize lost you only hope that your employers have forgotten about you.\n""")
            nicePrint("GAME OVER")
            time.sleep(3)
            sys.exit(1)
        else:
            nicePrint("""you asses the situation and then raise your hands surrendering to the Wardens.
            The Wardens approach you carefully from two sides, spears pointed at you.
            They quickly disarm and tie you.
            They grunge and curse you and the rain.
            Once they see all that you have done they argue weather to bother with you or to throw you in the river.
            You are saved only by the word of the highest ranking Warden,
            a brass pin decorating his leather west.
            You are stripped of your possesions and thrown in the basement cell, 
            to await the morning carriage for Altodrf.""")
            input("Press enter.\n")
            nicePrint("""The morning is cold and gloomy, it is raining for the whole day,
            soon you are brought before a magistrate and sentenced to a couple of months of jail time.\n""")
            time.sleep(2)
            nicePrint("""Time passes and eventually you are released one sunny morning, 
            only a couple of street cats see you celebrate your freedom
            You can only hope that your employers have forgotten about you.\n""")
    elif cmd == "2":
        combat_situation()
    elif cmd=="3":
        nicePrint("""You pretend to surrender and when the Wardens approach to subdue,
        you dash forward through them.\n""")
        time.sleep(1)
        nicePrint("""The most important skill for a thief is running,
        running away.\n""")
        input("Press enter.\n")
        nicePrint("Mud flies form the ground as you leave the surprised Wardens to curse after you.\n")
        time.sleep(2)
        nicePrintRed("THUD!\n")
        nicePrint("""At first moment it felt as if somebody hit you with a stone
        but a few heartbeats later you realise that a stone has a sharp point,
        like a crossbow bolt, sticking from your back.
        You continue for a couple of more steps when your legs betray you.\n""")
        time.sleep(2)
        nicePrint("""On your knees in the mud you can do nothing but wait for the Wardens to collect you like a bag of potatoes.
        The world is fading, or is the rain too strong?!?
        You barely notice when they pick you up, they argue for a short time about what to do with you.\n""")
        time.sleep(2)
        nicePrintRed("""The river for him,
        i don't want to have to explain the carcass to the sargent.\n""")
        time.sleep(2)
        nicePrintMenacing("""The last thing you remeber is the rumbling river under you
        and soon all turns to dark.\n""")
        time.sleep(2)
        nicePrint("""GAME OVER
        You have died.\n""")
        time.sleep(3)
        sys.exit(1)
    else:
        nicePrint("You can't do that, try something else.\n")
        getcmd(cmd_list)

    
#When the player crosses the bridge
def crossing_the_bride():
    nicePrint("""As you leave the bridge gate behind you and quickly run accross the stone bridge
    it is for the first time that you can really comprehend the size of the river.
    Here the wind and the rain are even stronger, 
    you have to hold onto your cloak and hat.
    It feels like forever to reach the other side 
    but finally you are far away from the Wardens reach.\n""")
    time.sleep(2)
    nicePrint("""You continue through the night and with daybreak reach the city.
    It's walls and spires a welcome sight in the gloomy sunless morning.
    With a smile on your face you ponder how will you spend your riches.
    It is still raining.\n""")
    time.sleep(2)
    nicePrint("""Congratulations, you have successfully finished the game!
    Revel in your victory!\n""")
    time.sleep(3)
    sys.exit(1)



empty_porch_counter = 0
wardens_return = False
empty_porch_first = False
pipe_taken = False
bride_gate_first = False
porch_door_first = False
snorri_out=False
kitchen_first=False
kitchen_searched=False

#When the player is in the kitchen
def kitchen(items):

    def snorri_fight():
        
        global kitchen_searched
        global snorri_out
        global wounded 
        global combat 
        global kitchen_first
        global snorri_found

        nicePrint("""Pull the dagger from his arm and stab him again or 
        leave the dagger and try to attack him barehanded?
1. Stab with the dagger.
2. Use your hands.\n""")

        cmd_list=["1","2", "kick","leg","groin"]
        cmd = getcmd(cmd_list)   

        if cmd=="1":
            nicePrint("""His grip is iron but you manage to hold onto your dagger
            and you manage to wrench it out of his arm.\n""")
            time.sleep(1)
            nicePrint("""Through clenched teeth he growls in pain, 
            his grip loosing slightly but still holding you.\n""")
            time.sleep(1)
            nicePrint("""You raise the dagger for another stab 
            but the Warden removes one arm from your throat and punches you in the face
            simultaneously as you stab him in the shoulder.\n""")
            time.sleep(2)
            nicePrint("""For a couple of moments all you see is white
            your world has become the opposite of complete dark.\n""")
            time.sleep(2)
            nicePrint(".....")
            time.sleep(2)
            nicePrint("""Youre not sure how much time has pased when you come back,
            the kitchen is a mess, things are scattered around everywhere
            the Warden is lying on his back there is a lot of blood on the floor.\n""")
            time.sleep(2)
            nicePrint("""And not all of it his, moment later pain kicks in,
            your face feels numb but when you move, swallow or even blink 
            your head feels like it will explode.\n""")
            time.sleep(2)
            nicePrint("""Your arm hurts and you can't move it, 
            still in shock you dumbly look down at it and see your dagger\n""")
            time.sleep(2)
            nicePrintMenacing("buried in it\n")
            time.sleep(2)
            nicePrint("""biting your lip not to scream you pull the dagger out,
            almost passing out
            using a kitchen rag you tie up your arm.\n""")
            time.sleep(2)
            nicePrint("""Youre wounded, your face is mangled 
            you can move your arm but it useless for any physical action.\n""")
            if wounded:
                nicePrint("""You stand over the big Warden
                a smile of victory on your face.\n""")
                input("Press enter.\n")
                nicePrint("""But as the battle fury subsides you realise
                that your injuries are serious.\n""")
                time.sleep(2)
                nicePrint("""You try to take a step but fall onto the Warden,
                using the last bits of your strength you grab the table edge
                but your arm betrays you.\n""")
                time.sleep(2)
                nicePrint("""You fall down and loose consciousness
                in the morning your body is tossed into the river
                never to be found again.
                Your possesions used to increase the outposts budget.\n""")
                time.sleep(2)
                nicePrintMenacing("""You have died,
                GAME OVER\n""")
                time.sleep(3)
                sys.exit(1)
            
            snorri_out = True
            wounded = True
            combat = False
            kitchen_first = True
            snorri_found=True
            kitchen(items)
        elif cmd=="2":
            nicePrint("""You leave the dagger in his arm, 
            it looks like he doesn't even notice it \n""")
            time.sleep(2)
            nicePrint("""he's holding you with both hands by the throat
            it feels like hanging, you cant't breathe.\n""")
            time.sleep(2)
            nicePrint("""You try to hit his elbows, a maneuver you know 
            but it's like hitting a brick wall.\n""")
            time.sleep(2)
            nicePrint("You need air.\n")
            time.sleep(2)
            nicePrint("""You go for his face, digging your fingers into his eyes
            he grunts 
            your vision is fading
            you feel wet under your fingers\n""")
            time.sleep(2)
            nicePrint("""You squeeze harder
            he squeezes stronger
            after a quiet snapping sound
            you fade away.\n""")
            time.sleep(2)
            nicePrint("""In the morning your body is tossed into the river 
            from the bridge without any kind of ceremony.
            On the bridge a very large man is curiously inspecting a small metal ball.\n""")
            time.sleep(2)
            nicePrintMenacing("""You have died,
                GAME OVER\n""")
            time.sleep(3)
            sys.exit(1)
        elif cmd.lower()=="kick" or cmd.lower()=="leg" or cmd.lower()=="groin":
            nicePrint("""The Wardens grip is incredibly strong
            but you have been in this situation before\n""")
            time.sleep(2)
            nicePrint("""you execute "the critical hit to the nads" maneuver
            slamming your leg into his groin\n""")
            time.sleep(2)
            nicePrint("""It takes a moment but the Warden's eyes turn watery and his face deforms
            he releases you and stumbles back holding his groin.\n""")
            time.sleep(2)
            nicePrint("""Catching your breath your hand falls on a heavy iron pan
            without thinking you swing it 
            and knock the Warden out.\n""")
            time.sleep(2)
            nicePrint("""He hits the floor and probably won't wake up any time soon.\n""")
            snorri_out = True
            combat=False
            kitchen_first = True
            snorri_found=True
            kitchen(items)
        else:
            nicePrint("You can't do that, try something else.\n")
            getcmd(cmd_list)

        


    global combat
    global caller_text
    global snorri_out
    global kitchen_first

    if fire:
        nicePrint("""You enter the kitchen, through the open backyard door
        you can see the flames consuming the shed despite the rain 
        and the Wardens trying to stop the inferno from reaching the outpost.\n""")
        time.sleep(2)
        nicePrint("""Their dancing shadows remind you of some forbidden ritual.
        It is not wise to stay here any moment one of the Wardens could turn around 
        and see you.
        You quickly retreat to the front room.\n""")
        front_room(items)


    if snorri_found:
        if snorri_out:
            nicePrint("In the kitchen all is the same.\n")
        else:   
            if not kitchen_first:
                nicePrint("""The door opens slowly to reveal a kitchen,
                it's dry, warm and surprisingly clean,
                there is another door leading out of the kitchen on the opposite wall.\n""")
                time.sleep(2)
                nicePrint("""A large stove dominates the kitchen, 
                cupbooards are on every wall,
                a large simple wooden table is in the middle of the room\n""")
                time.sleep(2)
                nicePrint("""and sitting by the table a mountain of a man sleeps,
                his snoring fills the room,
                arms crossed under his clean shaven bold head,
                you can see that his nose was broken more than once,
                he is wearing a Warden's uniform
                in front of him an empty mug.\n""")
                kitchen_first=True
            else:
                nicePrint("""Nothing has changed in the kitchen,
                the Warden in still sleeping on the table.\n""")

        input("Press enter.\n")
        nicePrint("What do you do : \n")
        if not snorri_out: 
            if "rope" in items:
                print("""1. Kill the sleeping Warden.
2. Move to the front room.
3. Go to the backyard.
4. Tie up the sleeping Warden.
\n""")
                caller_text="""1. Kill the sleeping Warden.
2. Move to the front room.
3. Go to the backyard.
4. Tie up the sleeping Warden.
\n"""

                cmd_list=["1","2","3","4", "search", "look", "examine"]
                cmd = getcmd(cmd_list)    

                if cmd=="1":
                    nicePrint("""You move next to the unsuspecting Warden,
                    draw the dagger\n""")
                    time.sleep(2)
                    nicePrintMenacing("""and stab him in the side of the neck
                    he jumps as if scared 
                    trying to speak but only gurgles
                    and quickly falls limply
                    blood runs from his neck and mouth onto the table.\n""")
                    snorri_out=True
                    time.sleep(2)
                    kitchen(items)
                elif cmd=="2":
                    if not snorri_out:
                        nicePrint("""You carefully move and leave the Warden to his sleep
                        but as you go for the door a sound of crunching wood from behind 
                        stops you in your tracks.\n""")
                        time.sleep(2)
                        nicePrint("You turn around only to see the huge Warden staring at you.\n")
                        input("Press enter.\n")
                        nicePrint("""he is surprised to see you as you are to find him there
                        but his confusion is momentarily gone and his stare is sharp as a knife
                        and fixated on you.\n""")
                        input("Press enter.\n")
                        nicePrint("The Warden stands up with unusal speed and throws himself at you.\n")
                        time.sleep(2)
                        nicePrint("""You shake off the surprise and reach for your dagger
                        drawing it just as the huge man grabs you by the throat\n""")
                        time.sleep(2)
                        nicePrint("""you stab him in the arm, blood starts to run
                        he grunts but doesn't release his grip.\n""")
                        time.sleep(2)
                        nicePrint("What do you do :\n")
                        snorri_fight()
                    else:
                        nicePrint("You sneak to the front room.\n")
                        front_room(items)
                
                elif cmd=="3":
                    if fire:
                        nicePrint("""All the Wardens are out there dealing with the fire, 
                        they would kill you immediately.\n""")
                        kitchen(items)
                    if backyard_door_open:
                        if not snorri_out:
                            nicePrint("""You carefully move and leave the Warden to his sleep
                            but as you go for the door a sound of crunching wood from behind 
                            stops you in your tracks.\n""")
                            time.sleep(2)
                            nicePrint("You turn around only to see the huge Warden staring at you.\n")
                            input("Press enter.\n")
                            nicePrint("""he is surprised to see you as you are to find him there
                            but his confusion is momentarily gone and his stare is sharp as a knife
                            and fixated on you.\n""")
                            input("Press enter.\n")
                            nicePrint("The Warden stands up with unusal speed and throws himself at you.\n")
                            time.sleep(2)
                            nicePrint("""You shake off the surprise and reach for your dagger
                            drawing it just as the huge man grabs you by the throat\n""")
                            time.sleep(2)
                            nicePrint("""you stab him in the arm, blood starts to run
                            he grunts but doesn't release his grip.\n""")
                            time.sleep(2)
                            nicePrint("What do you do :\n")
                            snorri_fight()
                        else:
                            nicePrint("You go out to the backyard.\n")
                            in_the_backyard(items)
                    else:
                        if not snorri_out:
                            nicePrint("""You carefully move and leave the Warden to his sleep
                            but as you go for the door a sound of crunching wood from behind 
                            stops you in your tracks.\n""")
                            time.sleep(2)
                            nicePrint("You turn around only to see the huge Warden staring at you.\n")
                            input("Press enter.\n")
                            nicePrint("""he is surprised to see you as you are to find him there
                            but his confusion is momentarily gone and his stare is sharp as a knife
                            and fixated on you.\n""")
                            input("Press enter.\n")
                            nicePrint("The Warden stands up with unusal speed and throws himself at you.\n")
                            time.sleep(2)
                            nicePrint("""You shake off the surprise and reach for your dagger
                            drawing it just as the huge man grabs you by the throat\n""")
                            time.sleep(2)
                            nicePrint("""you stab him in the arm, blood starts to run
                            he grunts but doesn't release his grip.\n""")
                            time.sleep(2)
                            nicePrint("What do you do :\n")
                            snorri_fight()
                        else:
                            nicePrint("You go out to the backyard.\n")
                            time.sleep(2)
                            nicePrint("""You open the door that leads to the back yard of the outpost and step out into the rain.
                            The backyard is surrounded by a stone wall, and mostly empty.
                            The ground is muddy and your boots sink,
                            a few shrubs and a shed is all there i \n""")
                            nicePrintRed("SPLAT")
                            time.sleep(2)
                            nicePrint("""You push your face out of the mud,
                            something big and strong has knocked you to the ground.\n""")
                            time.sleep(1)
                            nicePrint("You instinctively swing around, dagger in hand.\n")
                            time.sleep(1)
                            nicePrint("""In the shadows through the rain you see a pair of eyes burning with rage,
                            set of teeth almost shining in the window light,
                            the beast is huge its fur dark and covered with mud.\n""")
                            time.sleep(1)
                            nicePrint("It moves straight towards you, not running but slowly.")
                            nicePrint("The thing that passes through your mind is that it didn't bark at all.\n")
                            input("Press enter.\n")
                            nicePrint("""In the morning what is left of your ragged corpse is tossed into the river,
                            in the backyard the huge dog's paw squishes a small metal ball deeper into the mud.\n""")
                            nicePrint("""You have died,
                            GAME OVER\n""")
                            time.sleep(3)
                            sys.exit(1)
                elif cmd=="4":
                    if "rope" in items:
                        nicePrint("""It was a long time ago when you had to tie up your first victim
                        and even longer since you had to escape the bonds for the first time
                        one could say that you are an expert.\n""")
                        time.sleep(2)
                        if wounded:
                            nicePrint("Clenching your teeth to fight the pain of your wounds")
                        nicePrint("""You unwind the rope and strategically approach the sleeping Warden
                        after a couple of moments of planning\n""")
                        nicePrintMenacing("""you first carefully thread the rope around his feet\n""")
                        nicePrint("""and then quickly slide the rope under his arms
                        and wrap it around the back of his neck
                        and pull it tightly.\n""")
                        time.sleep(2)
                        nicePrint("""The huge Warden wakes surprised tries to stand 
                        but immediately falls to the ground
                        you quckly gag him with a kitchen rag.\n""")
                        time.sleep(2)
                        nicePrint("""He tries to break his bonds using brute strength
                        only managing to tie himself even more
                        his voice now only a mumble.\n""")
                        snorri_out=True
                        kitchen(items)
                                
                elif cmd.lower()=="search" or cmd.lower()== "look" or cmd.lower()== "examine":
                    if not kitchen_searched :

                        nicePrint("""You carefully search the kitchen
                        grabbing a mouthfull of dried meat and fruits
                        it's been a while since you ate
                        carefully not to wake the Warden.\n""")
                        if snorri_out:
                            pass    
                        time.sleep(2)
                        nicePrint("""Among the things in the kitchen you find a heavy iron pan,
                        use it to knock out the Warden?
                        1. Yes
2. No\n""")
                        caller_text="""1. Yes
2. No\n"""
                        cmd_list = ["1", "2", "yes", "no"]
                        cmd = getcmd(cmd_list)

                        if cmd=="1" or cmd.lower() == "yes":
                            nicePrint("""Since you were small you had to learn how to knock out people
                            one of the necessary skills on the streets of Altdorf\n""")
                            time.sleep(2)
                            nicePrint("""You prepare the pan, assesing it's weight
                            and quietly move next to the unsuspecting Warden.\n""")
                            time.sleep(2)
                            nicePrint("""carefully you prepare the blow, 
                            watching for the angle and speed
                            you reise your arm\n""")
                            input("Press enter.\n")
                            nicePrintRed("THUD!\n")
                            time.sleep(2)
                            nicePrint("""The Warden falls from the chair to the ground with a sigh
                            blood starts to flow from the side of his head
                            his snoring is replaced with deep heavy breathing.\n""")
                            time.sleep(2)
                            nicePrint("He will wake up with a bad headache but not anytime soon.\n")
                            snorri_out=True
                            kitchen_searched = True
                            kitchen(items)
                        elif cmd=="2" or cmd=="no":
                            nicePrint("You leave the pan.\n")
                            kitchen(items)
                        else:
                            nicePrint("You can't do that, try something else.\n")
                            kitchen(items)
                    else:
                        nicePrint("There is nothing useful here anymore.\n")
                else:
                    nicePrint("You can't do that, try something else.\n")
                    getcmd(cmd_list)
        



            elif "club" in items:
                print("""1. Kill the sleeping Warden.
2. Move to the front room.
3. Knock out the Warden.
4. Go to the backyard.\n""")
                caller_text="""1. Kill the sleeping Warden.
2. Move to the front room.
3. Knock out the Warden.
4. Go to the backyard.\n"""

                cmd_list=["1","2","3","4", "search", "look", "examine"]
                cmd = getcmd(cmd_list)    

                if cmd=="1":
                    nicePrint("""You move next to the unsuspecting Warden,
                    draw the dagger\n""")
                    time.sleep(2)
                    nicePrintMenacing("""and stab him in the side of the neck
                    he jumps as if scared 
                    trying to speak but only gurgles
                    and quickly falls limply
                    blood runs from his neck and mouth onto the table.\n""")
                    snorri_out=True
                    time.sleep(2)
                    kitchen(items)
                elif cmd=="2":
                    if not snorri_out:
                        nicePrint("""You carefully move and leave the Warden to his sleep
                        but as you go for the door a sound of crunching wood from behind 
                        stops you in your tracks.\n""")
                        time.sleep(2)
                        nicePrint("You turn around only to see the huge Warden staring at you.\n")
                        input("Press enter.\n")
                        nicePrint("""he is surprised to see you as you are to find him there
                        but his confusion is momentarily gone and his stare is sharp as a knife
                        and fixated on you.\n""")
                        input("Press enter.\n")
                        nicePrint("The Warden stands up with unusal speed and throws himself at you.\n")
                        time.sleep(2)
                        nicePrint("""You shake off the surprise and reach for your dagger
                        drawing it just as the huge man grabs you by the throat\n""")
                        time.sleep(2)
                        nicePrint("""you stab him in the arm, blood starts to run
                        he grunts but doesn't release his grip.\n""")
                        time.sleep(2)
                        nicePrint("What do you do :\n")
                        snorri_fight()
                    else:
                        nicePrint("You sneak to the front room.\n")
                        front_room(items)
                elif cmd=="3":
                    if "club" in items:
                        nicePrint("""Since you were small you had to learn how to knock out people
                        one of the necessary skills on the streets of Altdorf\n""")
                        time.sleep(2)
                        nicePrint("""You prepare the club, assesing it's weight
                        and quietly move next to the unsuspecting Warden.\n""")
                        time.sleep(2)
                        nicePrint("""carefully you prepare the blow, 
                        watching for the angle and speed
                        you reise your arm\n""")
                        input("Press enter.\n")
                        nicePrintRed("THUD!\n")
                        time.sleep(2)
                        nicePrint("""The Warden falls from the chair to the ground with a sigh
                        blood starts to flow from the side of his head
                        his snoring is replaced with deep heavy breathing.\n""")
                        time.sleep(2)
                        nicePrint("He will wake up with a bad headache but not anytime soon.\n")
                        snorri_out=True
                        kitchen(items)
                    else:
                        nicePrint("You can't do that, try something else.\n")
                        kitchen(items)
                elif cmd=="4":
                    if fire:
                        nicePrint("""All the Wardens are out there dealing with the fire, 
                        they would kill you immediately.\n""")
                        kitchen(items)
                    if backyard_door_open:
                        if not snorri_out:
                            nicePrint("""You carefully move and leave the Warden to his sleep
                            but as you go for the door a sound of crunching wood from behind 
                            stops you in your tracks.\n""")
                            time.sleep(2)
                            nicePrint("You turn around only to see the huge Warden staring at you.\n")
                            input("Press enter.\n")
                            nicePrint("""he is surprised to see you as you are to find him there
                            but his confusion is momentarily gone and his stare is sharp as a knife
                            and fixated on you.\n""")
                            input("Press enter.\n")
                            nicePrint("The Warden stands up with unusal speed and throws himself at you.\n")
                            time.sleep(2)
                            nicePrint("""You shake off the surprise and reach for your dagger
                            drawing it just as the huge man grabs you by the throat\n""")
                            time.sleep(2)
                            nicePrint("""you stab him in the arm, blood starts to run
                            he grunts but doesn't release his grip.\n""")
                            time.sleep(2)
                            nicePrint("What do you do :\n")
                            snorri_fight()
                        else:
                            nicePrint("You go out to the backyard.\n")
                            in_the_backyard(items)
                    else:
                        if not snorri_out:
                            nicePrint("""You carefully move and leave the Warden to his sleep
                            but as you go for the door a sound of crunching wood from behind 
                            stops you in your tracks.\n""")
                            time.sleep(2)
                            nicePrint("You turn around only to see the huge Warden staring at you.\n")
                            input("Press enter.\n")
                            nicePrint("""he is surprised to see you as you are to find him there
                            but his confusion is momentarily gone and his stare is sharp as a knife
                            and fixated on you.\n""")
                            input("Press enter.\n")
                            nicePrint("The Warden stands up with unusal speed and throws himself at you.\n")
                            time.sleep(2)
                            nicePrint("""You shake off the surprise and reach for your dagger
                            drawing it just as the huge man grabs you by the throat\n""")
                            time.sleep(2)
                            nicePrint("""you stab him in the arm, blood starts to run
                            he grunts but doesn't release his grip.\n""")
                            time.sleep(2)
                            nicePrint("What do you do :\n")
                            snorri_fight()
                        else:
                            nicePrint("You go out to the backyard.\n")
                            time.sleep(2)
                            nicePrint("""You open the door that leads to the back yard of the outpost and step out into the rain.
                            The backyard is surrounded by a stone wall, and mostly empty.
                            The ground is muddy and your boots sink,
                            a few shrubs and a shed is all there i \n""")
                            nicePrintRed("SPLAT")
                            time.sleep(2)
                            nicePrint("""You push your face out of the mud,
                            something big and strong has knocked you to the ground.\n""")
                            time.sleep(1)
                            nicePrint("You instinctively swing around, dagger in hand.\n")
                            time.sleep(1)
                            nicePrint("""In the shadows through the rain you see a pair of eyes burning with rage,
                            set of teeth almost shining in the window light,
                            the beast is huge its fur dark and covered with mud.\n""")
                            time.sleep(1)
                            nicePrint("It moves straight towards you, not running but slowly.")
                            nicePrint("The thing that passes through your mind is that it didn't bark at all.\n")
                            input("Press enter.\n")
                            nicePrint("""In the morning what is left of your ragged corpse is tossed into the river,
                            in the backyard the huge dog's paw squishes a small metal ball deeper into the mud.\n""")
                            nicePrint("""You have died,
                            GAME OVER\n""")
                            time.sleep(3)
                            sys.exit(1)
                                                
                elif cmd.lower()=="search" or cmd.lower()== "look" or cmd.lower()== "examine":
                    nicePrint("""You carefully search the kitchen
                    grabbing a mouthfull of dried meat and fruits
                    it's been a while since you ate
                    carefully not to wake the Warden.\n""")
                    time.sleep(2)
                    nicePrint("""Among the things in the kitchen you find a heavy iron pan,
                    use it to knock out the Warden?
                    1. Yes
2. No\n""")
                    caller_text="""1. Yes
2. No\n"""
                    cmd_list = ["1", "2", "yes", "no"]
                    cmd = getcmd(cmd_list)

                    if cmd=="1" or cmd.lower() == "yes":
                        nicePrint("""Since you were small you had to learn how to knock out people
                        one of the necessary skills on the streets of Altdorf\n""")
                        time.sleep(2)
                        nicePrint("""You prepare the pan, assesing it's weight
                        and quietly move next to the unsuspecting Warden.\n""")
                        time.sleep(2)
                        nicePrint("""carefully you prepare the blow, 
                        watching for the angle and speed
                        you reise your arm\n""")
                        input("Press enter.\n")
                        nicePrintRed("THUD!\n")
                        time.sleep(2)
                        nicePrint("""The Warden falls from the chair to the ground with a sigh
                        blood starts to flow from the side of his head
                        his snoring is replaced with deep heavy breathing.\n""")
                        time.sleep(2)
                        nicePrint("He will wake up with a bad headache but not anytime soon.\n")
                        snorri_out=True
                        kitchen(items)
                    elif cmd=="2" or cmd=="no":
                        nicePrint("You leave the pan.\n")
                        kitchen(items)
                    else:
                        nicePrint("You can't do that, try something else.\n")
                        kitchen(items)
                else:
                    nicePrint("You can't do that, try something else.\n")
                    getcmd(cmd_list)

            else:
                print("""1. Kill the sleeping Warden.
2. Move to the front room.
3. Go to the backyard.\n""")
                caller_text="""1. Kill the sleeping Warden.
2. Move to the front room.
3. Go to the backyard.\n"""

                cmd_list=["1","2","3", "search", "look", "examine"]
                cmd = getcmd(cmd_list)    

                if cmd=="1":
                    nicePrint("""You move next to the unsuspecting Warden,
                    draw the dagger\n""")
                    time.sleep(2)
                    nicePrintMenacing("""and stab him in the side of the neck
                    he jumps as if scared 
                    trying to speak but only gurgles
                    and quickly falls limply
                    blood runs from his neck and mouth onto the table.\n""")
                    snorri_out=True
                    time.sleep(2)
                    kitchen(items)
                elif cmd=="2":
                    if not snorri_out:
                        nicePrint("""You carefully move and leave the Warden to his sleep
                        but as you go for the door a sound of crunching wood from behind 
                        stops you in your tracks.\n""")
                        time.sleep(2)
                        nicePrint("You turn around only to see the huge Warden staring at you.\n")
                        input("Press enter.\n")
                        nicePrint("""he is surprised to see you as you are to find him there
                        but his confusion is momentarily gone and his stare is sharp as a knife
                        and fixated on you.\n""")
                        input("Press enter.\n")
                        nicePrint("The Warden stands up with unusal speed and throws himself at you.\n")
                        time.sleep(2)
                        nicePrint("""You shake off the surprise and reach for your dagger
                        drawing it just as the huge man grabs you by the throat\n""")
                        time.sleep(2)
                        nicePrint("""you stab him in the arm, blood starts to run
                        he grunts but doesn't release his grip.\n""")
                        time.sleep(2)
                        nicePrint("What do you do :\n")
                        snorri_fight()
                    else:
                        nicePrint("You sneak to the front room.\n")
                        front_room(items)
                
                elif cmd=="3":
                    if fire:
                        nicePrint("""All the Wardens are out there dealing with the fire, 
                        they would kill you immediately.\n""")
                        kitchen(items)
                    if backyard_door_open:
                        if not snorri_out:
                            nicePrint("""You carefully move and leave the Warden to his sleep
                            but as you go for the door a sound of crunching wood from behind 
                            stops you in your tracks.\n""")
                            time.sleep(2)
                            nicePrint("You turn around only to see the huge Warden staring at you.\n")
                            input("Press enter.\n")
                            nicePrint("""he is surprised to see you as you are to find him there
                            but his confusion is momentarily gone and his stare is sharp as a knife
                            and fixated on you.\n""")
                            input("Press enter.\n")
                            nicePrint("The Warden stands up with unusal speed and throws himself at you.\n")
                            time.sleep(2)
                            nicePrint("""You shake off the surprise and reach for your dagger
                            drawing it just as the huge man grabs you by the throat\n""")
                            time.sleep(2)
                            nicePrint("""you stab him in the arm, blood starts to run
                            he grunts but doesn't release his grip.\n""")
                            time.sleep(2)
                            nicePrint("What do you do :\n")
                            snorri_fight()
                        else:
                            nicePrint("You go out to the backyard.\n")
                            in_the_backyard(items)
                    else:
                        if not snorri_out:
                            nicePrint("""You carefully move and leave the Warden to his sleep
                            but as you go for the door a sound of crunching wood from behind 
                            stops you in your tracks.\n""")
                            time.sleep(2)
                            nicePrint("You turn around only to see the huge Warden staring at you.\n")
                            input("Press enter.\n")
                            nicePrint("""he is surprised to see you as you are to find him there
                            but his confusion is momentarily gone and his stare is sharp as a knife
                            and fixated on you.\n""")
                            input("Press enter.\n")
                            nicePrint("The Warden stands up with unusal speed and throws himself at you.\n")
                            time.sleep(2)
                            nicePrint("""You shake off the surprise and reach for your dagger
                            drawing it just as the huge man grabs you by the throat\n""")
                            time.sleep(2)
                            nicePrint("""you stab him in the arm, blood starts to run
                            he grunts but doesn't release his grip.\n""")
                            time.sleep(2)
                            nicePrint("What do you do :\n")
                            snorri_fight()
                        else:
                            nicePrint("You go out to the backyard.\n")
                            time.sleep(2)
                            nicePrint("""You open the door that leads to the back yard of the outpost and step out into the rain.
                            The backyard is surrounded by a stone wall, and mostly empty.
                            The ground is muddy and your boots sink,
                            a few shrubs and a shed is all there i \n""")
                            nicePrintRed("SPLAT")
                            time.sleep(2)
                            nicePrint("""You push your face out of the mud,
                            something big and strong has knocked you to the ground.\n""")
                            time.sleep(1)
                            nicePrint("You instinctively swing around, dagger in hand.\n")
                            time.sleep(1)
                            nicePrint("""In the shadows through the rain you see a pair of eyes burning with rage,
                            set of teeth almost shining in the window light,
                            the beast is huge its fur dark and covered with mud.\n""")
                            time.sleep(1)
                            nicePrint("It moves straight towards you, not running but slowly.")
                            nicePrint("The thing that passes through your mind is that it didn't bark at all.\n")
                            input("Press enter.\n")
                            nicePrint("""In the morning what is left of your ragged corpse is tossed into the river,
                            in the backyard the huge dog's paw squishes a small metal ball deeper into the mud.\n""")
                            nicePrint("""You have died,
                            GAME OVER\n""")
                            time.sleep(3)
                            sys.exit(1)
                
                elif cmd.lower()=="search" or cmd.lower()== "look" or cmd.lower()== "examine":
                    nicePrint("""You carefully search the kitchen
                    grabbing a mouthfull of dried meat and fruits
                    it's been a while since you ate
                    carefully not to wake the Warden.\n""")
                    time.sleep(2)
                    nicePrint("""Among the things in the kitchen you find a heavy iron pan,
                    use it to knock out the Warden?
                    1. Yes
2. No\n""")
                    caller_text="""1. Yes
2. No\n"""
                    cmd_list = ["1", "2", "yes", "no"]
                    cmd = getcmd(cmd_list)

                    if cmd=="1" or cmd.lower() == "yes":
                        nicePrint("""Since you were small you had to learn how to knock out people
                        one of the necessary skills on the streets of Altdorf\n""")
                        time.sleep(2)
                        nicePrint("""You prepare the pan, assesing it's weight
                        and quietly move next to the unsuspecting Warden.\n""")
                        time.sleep(2)
                        nicePrint("""carefully you prepare the blow, 
                        watching for the angle and speed
                        you reise your arm\n""")
                        input("Press enter.\n")
                        nicePrintRed("THUD!\n")
                        time.sleep(2)
                        nicePrint("""The Warden falls from the chair to the ground with a sigh
                        blood starts to flow from the side of his head
                        his snoring is replaced with deep heavy breathing.\n""")
                        time.sleep(2)
                        nicePrint("He will wake up with a bad headache but not anytime soon.\n")
                        snorri_out=True
                        kitchen(items)
                    elif cmd=="2" or cmd=="no":
                        nicePrint("You leave the pan.\n")
                        kitchen(items)
                    else:
                        nicePrint("You can't do that, try something else.\n")
                        kitchen(items)
                else:
                    nicePrint("You can't do that, try something else.\n")
                    getcmd(cmd_list)

        else:
            print("""1. Move to the front room.
2. Go to the backyard.\n""")
            caller_text="""1. Move to the front room.
2. Go to the backyard.\n"""

        cmd_list=["1","2", "search", "look", "examine"]
        cmd = getcmd(cmd_list)    

        
        if cmd=="1":
            if not snorri_out:
                nicePrint("""You carefully move and leave the Warden to his sleep
                but as you go for the door a sound of crunching wood from behind 
                stops you in your tracks.\n""")
                time.sleep(2)
                nicePrint("You turn around only to see the huge Warden staring at you.\n")
                input("Press enter.\n")
                nicePrint("""he is surprised to see you as you are to find him there
                but his confusion is momentarily gone and his stare is sharp as a knife
                and fixated on you.\n""")
                input("Press enter.\n")
                nicePrint("The Warden stands up with unusal speed and throws himself at you.\n")
                time.sleep(2)
                nicePrint("""You shake off the surprise and reach for your dagger
                drawing it just as the huge man grabs you by the throat\n""")
                time.sleep(2)
                nicePrint("""you stab him in the arm, blood starts to run
                he grunts but doesn't release his grip.\n""")
                time.sleep(2)
                nicePrint("What do you do :\n")
                snorri_fight()
            else:
                nicePrint("You sneak to the front room.\n")
                front_room(items)
        
        elif cmd=="2":
            if fire:
                nicePrint("""All the Wardens are out there dealing with the fire, 
                they would kill you immediately.\n""")
                kitchen(items)
            if backyard_door_open:
                if not snorri_out:
                    nicePrint("""You carefully move and leave the Warden to his sleep
                    but as you go for the door a sound of crunching wood from behind 
                    stops you in your tracks.\n""")
                    time.sleep(2)
                    nicePrint("You turn around only to see the huge Warden staring at you.\n")
                    input("Press enter.\n")
                    nicePrint("""he is surprised to see you as you are to find him there
                    but his confusion is momentarily gone and his stare is sharp as a knife
                    and fixated on you.\n""")
                    input("Press enter.\n")
                    nicePrint("The Warden stands up with unusal speed and throws himself at you.\n")
                    time.sleep(2)
                    nicePrint("""You shake off the surprise and reach for your dagger
                    drawing it just as the huge man grabs you by the throat\n""")
                    time.sleep(2)
                    nicePrint("""you stab him in the arm, blood starts to run
                    he grunts but doesn't release his grip.\n""")
                    time.sleep(2)
                    nicePrint("What do you do :\n")
                    snorri_fight()
                else:
                    nicePrint("You go out to the backyard.\n")
                    in_the_backyard(items)
            else:
                if not snorri_out:
                    nicePrint("""You carefully move and leave the Warden to his sleep
                    but as you go for the door a sound of crunching wood from behind 
                    stops you in your tracks.\n""")
                    time.sleep(2)
                    nicePrint("You turn around only to see the huge Warden staring at you.\n")
                    input("Press enter.\n")
                    nicePrint("""he is surprised to see you as you are to find him there
                    but his confusion is momentarily gone and his stare is sharp as a knife
                    and fixated on you.\n""")
                    input("Press enter.\n")
                    nicePrint("The Warden stands up with unusal speed and throws himself at you.\n")
                    time.sleep(2)
                    nicePrint("""You shake off the surprise and reach for your dagger
                    drawing it just as the huge man grabs you by the throat\n""")
                    time.sleep(2)
                    nicePrint("""you stab him in the arm, blood starts to run
                    he grunts but doesn't release his grip.\n""")
                    time.sleep(2)
                    nicePrint("What do you do :\n")
                    snorri_fight()
                else:
                    nicePrint("You go out to the backyard.\n")
                    time.sleep(2)
                    nicePrint("""You open the door that leads to the back yard of the outpost and step out into the rain.
                    The backyard is surrounded by a stone wall, and mostly empty.
                    The ground is muddy and your boots sink,
                    a few shrubs and a shed is all there i \n""")
                    nicePrintRed("SPLAT")
                    time.sleep(2)
                    nicePrint("""You push your face out of the mud,
                    something big and strong has knocked you to the ground.\n""")
                    time.sleep(1)
                    nicePrint("You instinctively swing around, dagger in hand.\n")
                    time.sleep(1)
                    nicePrint("""In the shadows through the rain you see a pair of eyes burning with rage,
                    set of teeth almost shining in the window light,
                    the beast is huge its fur dark and covered with mud.\n""")
                    time.sleep(1)
                    nicePrint("It moves straight towards you, not running but slowly.")
                    nicePrint("The thing that passes through your mind is that it didn't bark at all.\n")
                    input("Press enter.\n")
                    nicePrint("""In the morning what is left of your ragged corpse is tossed into the river,
                    in the backyard the huge dog's paw squishes a small metal ball deeper into the mud.\n""")
                    nicePrint("""You have died,
                    GAME OVER\n""")
                    time.sleep(3)
                    sys.exit(1)
                                
        elif cmd.lower()=="search" or cmd.lower()== "look" or cmd.lower()== "examine":
            nicePrint("""You carefully search the kitchen
            grabbing a mouthfull of dried meat and fruits
            it's been a while since you ate
            carefully not to wake the Warden.\n""")
            time.sleep(2)
            nicePrint("""Among the things in the kitchen you find a heavy iron pan,
            use it to knock out the Warden?
            1. Yes
2. No\n""")
            caller_text="""1. Yes
2. No\n"""
            cmd_list = ["1", "2", "yes", "no"]
            cmd = getcmd(cmd_list)

            if cmd=="1" or cmd.lower() == "yes":
                nicePrint("""Since you were small you had to learn how to knock out people
                one of the necessary skills on the streets of Altdorf\n""")
                time.sleep(2)
                nicePrint("""You prepare the pan, assesing it's weight
                and quietly move next to the unsuspecting Warden.\n""")
                time.sleep(2)
                nicePrint("""carefully you prepare the blow, 
                watching for the angle and speed
                you reise your arm\n""")
                input("Press enter.\n")
                nicePrintRed("THUD!\n")
                time.sleep(2)
                nicePrint("""The Warden falls from the chair to the ground with a sigh
                blood starts to flow from the side of his head
                his snoring is replaced with deep heavy breathing.\n""")
                time.sleep(2)
                nicePrint("He will wake up with a bad headache but not anytime soon.\n")
                snorri_out=True
                kitchen(items)
            elif cmd=="2" or cmd=="no":
                nicePrint("You leave the pan.\n")
                kitchen(items)
            else:
                nicePrint("You can't do that, try something else.\n")
                kitchen(items)
        else:
            nicePrint("You can't do that, try something else.\n")
            getcmd(cmd_list)
    else:
        combat = True
        nicePrint("""You open the door to reveal a kitchen
        it is clean and orderly on the walls are pantries
        here is dry and warm
        big stove warms the room 
        in the middle of the kitchen there is a table
        next to the table sits a huge man in the Wardens uniform
        his bald head carries the evidence of more than one brawl\n""")
        time.sleep(2)
        nicePrint("and you just woke him up\n")
        time.sleep(2)
        nicePrint("""he is surprised to see you as you are to find him there
        but his confusion is momentarily gone and his stare is sharp as a knife
        and fixated on you.\n""")
        input("Press enter.\n")
        nicePrint("The Warden stands up with unusal speed and throws himself at you.\n")
        time.sleep(2)
        nicePrint("""You shake off the surprise and reach for your dagger
        drawing it just as the huge man grabs you by the throat\n""")
        time.sleep(2)
        if wounded :
            nicePrint("""You try to stab him with the dagger but your attack is feeble.
            Your wounded arm is useless, he deflects your strike with ease.\n""")
            nicePrint("""he's holding you with both hands by the throat
            it feels like hanging, you cant't breathe.\n""")
            time.sleep(2)
            nicePrint("""You try to hit his elbows, a maneuver you know 
            but your strength is gone.\n""")
            time.sleep(2)
            nicePrint("You need air.\n")
            time.sleep(2)
            nicePrint("""You try to go for his face,  
            your vision is fading\n""")
            time.sleep(2)
            nicePrint("""he squeezes stronger
            after a quiet snapping sound
            you fade away.\n""")
            time.sleep(2)
            nicePrint("""In the morning your body is tossed into the river 
            from the bridge without any kind of ceremony.
            On the bridge a very large man is curiously inspecting a small metal ball.\n""")
            time.sleep(2)
            nicePrint("""You have died,
                GAME OVER\n""")
            time.sleep(3)
            sys.exit(1)
        else:
            nicePrint("""you stab him in the arm, blood starts to run
            he grunts but doesn't release his grip.\n""")
            
            time.sleep(2)
            nicePrint("What do you do :\n")
            snorri_fight()



office_first=False
key_found = False

#When the plaer is in the kitchen
def office(items):

    global caller_text
    global office_first
    global key_found
    if fire:
        if office_first:
                nicePrint("""You are in the office everything is the same.\n""")
                time.sleep(2)
                nicePrint("""The bonfire from the backyard is shining through the windows.\n""")
            
        else:
            nicePrint("""You enter a room that looks like an office.
            Fire in the backyard casts light inside.
            and everything casts long shadows that move as if alive.\n""")

            nicePrint("""The room is decorated with banners and a heraldric shield,
            Imperial flag and a flag of the Elector count hang on the wall
            and a large map, you have never seen a map this complicated, 
            and can only guess what it represent, Reikland, the Empire or the whole world.\n""")
            time.sleep(2)
            nicePrint("""The shield is with a green background depicting a bear,
            you can not recognize which noble house or order it represents.\n""")
            time.sleep(2)
            nicePrint("""A couple of closets are on the walls, 
            a simple bed neatly prepared, 
            in the center of the room a massive desk,
            in the background a fireplace is burning making this room pleasantly warm.\n""")
            office_first=True
        nicePrint("After a quick look around you decide to : \n")
        print("""1. Search the desk.
    2. Look at the map.
    3. Go to the sleeping room.\n""")
        
        caller_text="""1. Search the desk.
    2. Look at the map.
    3. Go to the sleeping room.\n"""

        cmd_list=["1","2","3", "search", "look", "examine"]
        cmd = getcmd(cmd_list)

        if cmd == "1":
            nicePrint("""You approach the desk, it is large and looks expensive.
            On the desk numerous papers, and even books, though these probably aren't valuable,
            ink and quill but the whole desk is orderly.\n """)
            time.sleep(2)
            nicePrint("""Among the things on the desk lies a set of keys on a metal ring,
            one considerably larger.\n""")
            input("Press enter.\n")
            print("""1. Take the keys.
    2. Leave them on the desk.\n""")

            cmd_list=["1","2","yes", "no"]
            cmd = getcmd(cmd_list)

            if cmd=="1" or cmd.lower()=="yes":
                if not key_found:
                    nicePrint("You pocket the keys.\n")
                    items.update({"bridge key":"a bundle of keys connected by a metal ring, one is standing out."})
                    key_found=True
                else:
                    nicePrint("You can't do that, try something else.\n")
                    
            elif cmd=="2" or cmd.lower()=="no":
                nicePrint("You leave the keys on the desk for now.\n")
                
            else:
                nicePrint("You can't do that, try something else.\n")
                getcmd(cmd_list)            

            office(items)
        elif cmd=="2":
            nicePrint("""You walk over to the map,
            you know how to read smaller maps but this is something beyond you.
            It looks to show a very large area, no idea how big the area is.
            You can only guess that the makrers on it show entire towns and villages,
            There are lines of different colors connecting the markers.
            Some spots on the map are marked with different colors.\n""")
            office(items)
        elif cmd=="3":
            nicePrint("You return to the cold sleeping room.\n")
            sleeping_room(items)
        elif cmd.lower()=="search" or cmd.lower()== "look" or cmd.lower()=="examine":
            nicePrint("There is nothing special here that you whould want now.\n")
            office(items)
        else:
            nicePrint("You can't do that, try something else.\n")
            getcmd(cmd_list)
    else:
        nicePrint("""You think somebody is inside, 
        it's difficult to be sure the rain outside is making a lot of noise
        but you think you can hear voices.\n""")
        input("Press enter.\n")
        nicePrint("Open the door and enter?\n")
        print("""1. Yes
2. No\n""")

        caller_text= """Open the door and enter?
1. Yes
2. No\n"""

        cmd_list=["1","2","yes", "no"]
        cmd = getcmd(cmd_list)

        if cmd== "1" or cmd.lower()=="yes":
            nicePrint("""You draw your dagger and quickly open the door to catch the occupant offguard.\n""")
            time.sleep(2)
            nicePrint("""As the door swings open you see a large room that looks like a magistrate's office or a merchant's work room.
            A big desk covered with books and papers, a fireplace in the back of the room.\n""")
            time.sleep(2)
            nicePrint("""In the room two faces stare at you, one younger sitting at the desk closer to the door clearly confused
            and an older bearded one sitting behind the desk, not so confused.
            Both are wearing Wardens uniforms, the older man's uniform is a bit more elaborated than the other.\n""")
            time.sleep(2)
            nicePrint("""For a split second you hesitate, you did't expect to find two of them here,
            but now there's no turning back.
            You charge at the closer Warden using the element of surprise.\n""")
            input("Press enter.\n")
            nicePrint("""You charge through the room at the younger Warden your dagger against his quill,
            you dash a couple of steps while he is frozen in terror.\n""")
            time.sleep(2)
            nicePrint("""A flash and a loud bang fill the room as you are tossed back.
            At first you are confused stumbling backward
            but the pain that shoots thorugh your whole body makes you forget about the Wardens.\n""")
            time.sleep(2)
            nicePrint("""You try to use your hands to stop your entrails from escaping, 
            clutching your stomach you fall to the ground.
            The older Warden steps from behind the desk,
            a large and stocky man with a seasoned calm look on his face
            a blackpowdered pistol smoking in his hand.
            On his chest embroidered is a sigil of a bear, matching the one on the shiled on the wall.\n""")
            time.sleep(2)
            nicePrint("""Your vision starts to fade, 
            you can hear them discussing whether to dispose of the bloody carpert alongside you.\n""")
            time.sleep(2)
            nicePrint("""Your remains are rolled in a carpet and carried to the river,
            together with all your possesions you are swallowed by the river.\n""")
            time.sleep(2)
            nicePrintMenacing("""You have died.
            GAME OVER.""")
            time.sleep(3)
            sys.exit(1)       
        elif cmd=="2" or cmd.lower()=="no":
            nicePrint("You quietly back up from the door.\n")
            sleeping_room(items)
        else:
            nicePrint("You can't do that, try something else.\n")
            sleeping_room(items) 

    


large_room_first=False
jump_solution = False

#When the player is in the large room on the first floor
def large_room(items):

    global large_room_first
    global jump_solution
    global caller_text
    global nail_puller_taken

    if not large_room_first:
        nicePrint("""You are in large room, windows are on three walls,
        one side is overlooking the front, other the back of the ouptost
        and the third is looking to the river.\n""")
        time.sleep(2)
        nicePrint("""You can see the river rolling far below, dark and massive.
        The bride is straight and long its other end invisible in the dark.\n""")
        nicePrint("""The walls of the room are decorated by stuffed hunting trophies
        heraldric shields and banners.
        You recognize the imperial flag and that of the Elector count but others are unknown to you.\n""")
        time.sleep(2)
        nicePrint("""Here is cold and the air is humid, a couple of windows are opened 
        on both sides of the room, one to the back and one to the front.\n""")
        time.sleep(2)
        nicePrint("""In the middle of the room sits a large table, it could fit two dozen seats.
        The chairs are placed orderly around it.
        There is only one exit, a doorway.\n""")   
        large_room_first=True
        if fire:
            nicePrint("""The burning shed in the backyard casts light,
            shadows dance all across the room\n""")
    else:
        nicePrint("You are in the large room and nothing has changed.\n")
    nicePrint("After a moment of thought you decide to : \n")

    print("""1. Go to the back window.
2. Move to the front window.
3. Check the table.
4. Go to the next room.\n""")
    caller_text="""1. Go to the back window.
2. Move to the front window.
3. Check the table.
4. Go to the next room.\n"""

    cmd_list = ["1", "2", "3", "4", "search", "look", "examine"]
    cmd = getcmd(cmd_list)

    if cmd == "1":
        nicePrint("You approach the back window, and can see the back of the outpost.\n")
        if fire :
            nicePrint("""From the window you have a good look of the raging fire,
            it's tentacles almost reaching the wall of the outpost.
            It's a strange dance, fire against rain
            and for now fire is winning.\n""")
            large_room(items)

        if "grappling hook" in items:
            
            nicePrint("Climb down to the backyard using the grappling hook?\n")
            print("""1. Yes
2. No""")
            caller_text="""1. Yes
2. No"""
            cmd_list = ["1", "2", "yes", "no"]
            cmd = getcmd(cmd_list)

            if cmd=="1" or cmd.lower()== "yes":
                nicePrint("You climb down the back side of the outpost to the backyard.\n")
                in_the_backyard(items)
            elif cmd=="2" or cmd.lower()== "no":
                nicePrint("You decide to stay here.\n")
                large_room(items)
            else:
                nicePrint("You can't do that, try something else.\n")
                large_room(items)
        large_room(items)
    elif cmd == "2":
        nicePrint("This window is opened, through the front window you can see the front of the outpost.\n")
        if fire or wardens_eliminated:
            nicePrint("It's deserted now.\n")
        else:
            nicePrint("""You know the Wardens are downstairs, their shadows are moving around.\n""")
        nicePrint("""The roof of the bridge gate is just a couple of steps away from this window,
        too far for a jump.\n""")
        jump_solution = True
        large_room(items)  
    elif cmd=="3":
        if jump_solution:
            nicePrint("""You approach the large table it is not covered with cloth.
            Nothing special about it, the top part made out of simple boards
            a couple of steps long
            wide enough for a person to walk
            and thick enough to carry your weight.\n""")
            input("Press enter.\n")
            print("""1. Use a board between the window and bridge gate roof?
2. Not now.\n""")
            caller_text="""1. Use a board between the window and bridge gate roof?
2. Not now.\n"""


            cmd_list = ["1", "2", "yes", "no"]
            cmd = getcmd(cmd_list)

            if cmd=="1" or cmd.lower()== "yes":
                if nail_puller_taken:
                    nicePrint("""Using the nail puller you pull one board off the table and carefully place it on the window's edge.
                    And then slide it to the bridge gate roof
                    and after a couple of tries find a solid position.\n""")
                    input("Press enter.\n")
                    nicePrint("""Carefully you step into the rain a floor above the ground,
                    the wind and the rain strinking your face.\n""")
                    time.sleep(2)
                    nicePrint("""Your heart races as you wobble in the night,
                    a lightning tears the sky.\n""")
                    time.sleep(2)
                    nicePrint("""After a few agonising steps you finally reach the bridge gate roof.
                    Without looking back you stumble to the other side of the gate.\n""")
                    crossing_the_bride()
                else:
                    nicePrint("You can't remove the board with out somekind of tool, your dagger won't do.\n")
                    large_room(items)
            elif cmd=="2" or cmd.lower()== "no":
                nicePrint("You decide to stay here.\n")
                large_room(items)
            else:
                nicePrint("You can't do that, try something else.\n")
                large_room(items) 
        else:
            nicePrint("""You approach the large table it is not covered with cloth.
            Nothing special about it, the top part made out of simple boards
            They are loosly nailed to the table, 
            you could remove them if you had some tool.\n""")
            large_room(items)
    elif cmd=="4":
        nicePrint("You walk through the doorway into the next room.\n")
        sleeping_room(items)
    elif cmd.lower()=="search" or cmd.lower()== "look" or cmd.lower()== "examine":
        nicePrint("You search the room, but there is nothing here of value that you can take with you.\n")
        large_room(items)
    else:
        nicePrint("You can't do that, try something else.\n")
        getcmd(cmd_list)

    

sleeping_room_first = False

#When the player is in the Warden's sleeping
def sleeping_room(items):


    def chest(chest_number):
        

        cmd = str(chest_number)
        
        if cmd=="1":
            nicePrint("""You approach the first chest
            your lock pick makes quick work of the lock.\n""")
            time.sleep(2)
            nicePrint("""Inside you find different pieces of clothes,
            used but in good condition and at the bottom\n""")
            nicePrint("""two gold crowns, glittering in the dark.
            You pocket the money\n""")
            del items["lock pick"]
            items.update({"two gold crowns":"A small fortune, more than a good months earning."})
            sleeping_room(items)
        elif cmd=="2":
            nicePrint("""You approach the second chest
            your lock pick makes quick work of the lock.\n""")
            time.sleep(2)
            nicePrint("""Inside you find different pieces of clothes,
            used but in good condition and at the bottom\n""")
            nicePrint("""a small metal locket, looks like silver.
            You take the locket.\n""")
            del items["lock pick"]
            items.update({"silver locket":"It's made of silver with nice engravings, to some love it will fetch a decent amount."})
            sleeping_room(items)
        elif cmd=="3":
            nicePrint("""You approach the third chest
            your lock pick makes quick work of the lock.\n""")
            time.sleep(2)
            nicePrint("""Inside you find different pieces of clothes,
            used but in good condition and at the bottom\n""")
            nicePrint("""a small leather pouch, inside something soft, tobacco but, not the cheap stuff.
            You take the tobacco pouch\n""")
            del items["lock pick"]
            items.update({"expensive tobacco":"By the smell alone you can tell that this is high quailty, expensive."})
            sleeping_room(items)
        elif cmd=="4":
            nicePrint("""You approach the fourth chest
            your lock pick makes quick work of the lock.\n""")
            time.sleep(2)
            nicePrint("""Inside you find different pieces of clothes,
            used but in good condition and at the bottom\n""")
            nicePrint("""A tinderbox, inside is carefully padded with cloth and in it three transparent colored stones.
            You take the stones\n""")
            del items["lock pick"]
            items.update({"magic stones":"These look like something a wizard could want or just trinkets, pretty."})
            items.update({"prize":"It looks the same but now it's definitely hot to the touch, you can feel vibrations and light coming from inside!"})
            sleeping_room(items)
        elif cmd=="5":
            nicePrint("You can't make your mind and use a children's rime to pick a chest.\n")
            chest(random.randint(1, 4))
        else:
            nicePrint("You can't do that, try something else.\n")
            sleeping_room(items) 

    global caller_text
    global sleeping_room_first

    if not sleeping_room_first:
        nicePrint("""The stairs from the ground floor end in the middle of a medium sized room
        there are no lit lanterns here but, some light comes from the windows.
        Simple sleeping bunks are scattered across the room, at the foot of each is a chest.\n""")
        time.sleep(2)
        nicePrint("""On one wall there is a closed door, 
        you can see that there is light on the other side.\n""")
        if not large_room_first:
            nicePrint("On the other just a doorway into the other, much larger room.\n")
        sleeping_room_first = True
        if fire:
            nicePrint("""The burning shed in the backyard casts light,
            shadows dance all across the room\n""")
    else:
        nicePrint("You are in the sleeping room, everything is the same.\n")

    input("Press enter.\n")
    nicePrint("After a moment you decide to : \n")
    print("""1. Go to the closed door on the right.
2. Move to the large room on the left.
3. Search the chests.
4. Go downstairs.\n""")
    caller_text="""1. Go to the closed door on the right.
2. Move to the large room on the left.
3. Search the chests.
4. Go downstairs.\n"""

    cmd_list = ["1", "2", "3", "4", "search", "look", "examine"]
    cmd = getcmd(cmd_list)

    if cmd == "1":
        nicePrint("You carefully approach the closed door.\n")
        office(items)
    elif cmd== "2":
        nicePrint("You move to the large room.\n")
        large_room(items)
    elif cmd== "3":
        nicePrint("""There are five beds and five chests.
        All of them have locks except one, that bed looks like it's not used.
        The unlocked chest is empty.
        All the others are locked.\n""")
        input("Press enter.\n")
        print("""1. Pick the lock on a chest if you have a lock pick.
2. Leave the chests alone.\n""")

        cmd_list = ["1", "2"]
        cmd = getcmd(cmd_list)

        if cmd=="1":
            if "lock pick" in items:
                nicePrint("""Which chest do you wish to open :
                1.
                2.
                3.
                4.
                5. Leave it to chance, pick one at random.\n""")
                time.sleep(2)
                nicePrint("You unlock : \n")
                
                chest_number_correct = False

                while not chest_number_correct:
                    chest_number = input()
                    if chest_number == "1" or chest_number == "2" or chest_number == "3" or chest_number == "4" or chest_number == "5":
                        chest_number_correct = True
                    else:
                        nicePrint("You can't do that, try something else.\n")

                chest(chest_number)
                
            else:
                nicePrint("You don't have a lock pick.\n")
                sleeping_room(items)
        elif cmd=="2":
            nicePrint("You decide not to bother with the chests.\n")
            sleeping_room(items)
        else:
            nicePrint("You can't do that, try something else.\n")
            getcmd(cmd_list) 
        sleeping_room(items)
    elif cmd=="4":
        nicePrint("You decide to sneak downstairs.\n")
        front_room(items)
    elif cmd=="search" or cmd== "look" or cmd== "examine":
        nicePrint("""There is nothing here besides the chests,
        the room is ascetic,
        from the windows you can see the front and the back of the outpost.\n""")
        sleeping_room(items)
    else :
        nicePrint("You can't do that, try something else.\n")
        getcmd(cmd_list)


front_room_first = False
snorri_found = False
crossbow_taken = False
basement_first = False
front_door_open = False

#When the player is in the front room of the outpost.
def front_room(items):

    global front_room_first
    global caller_text
    global front_room
    global snorri_found

    def first_floor(items):
        print("Youre ont the frist floor")
        front_room(items)

    def basement(items):

        global crossbow_taken
        global basement_first
        global caller_text

        if not basement_first:
            nicePrint("""The light from the broken lantern casts wobbly shadows everywhere
            but it is enough so you can see your surrounding.
            There are around two dozen steps leading down into the basement
            and once you reach the end you find yourself in large dark room.\n""")
            time.sleep(2)
            nicePrint("""The walls are made of large stones they look solid and they aren't
            leaking, on one side of the room are cells with iron bars the Warden's jail,
            if you are not careful you might end up in one of these.\n""")
            time.sleep(2)
            nicePrint("""Here is unusally dry for a basement
            and you realise why, this basement is storeroom of the outpost.
            Barrels with food, water, wine, leather, cloth, and even weapon racks.\n""")
            time.sleep(2)
            nicePrint("""Swords, spears, halberds and even some breastplates neatly arranged on the rack
            None of it useful for you now, big weapons will just get in the way when sneaking around
            and you are not good at using them, armour especially but\n""")
            time.sleep(2)
            nicePrint("""a crossbow could be very usefull, like the one sitting on the rack.\n""")
            basement_first = True
        else:
            nicePrint("You are in the basement and everything is the same.\n")
        input("Press enter.\n")
        nicePrint("After a moment you decide to : \n")

        if crossbow_taken:
            print("""1. Go back upstairs to the front room.
2. Inspect the cells.\n""")
            caller_text="""1. Go back upstairs to the front room.
2. Inspect the cells. \n"""

            cmd_list = ["1", "2", "search", "look", "examine"]
            cmd = getcmd(cmd_list)

            if cmd=="1":
                nicePrint("You decide to return upstairs to the front room.\n")
                front_room(items)
            elif cmd=="2":
                nicePrint("""Shadows dance all around the basement as you walk towards the prison cells
                you have seen them before, from the inside mostly
                there are five, built into the wall of the basement with strong iron bars in the front.
                By the look of everything these are only used to provide temporary accommodation
                probably the prisoners are soon transferred to a larger prison.\n""")
                basement(items)
            elif cmd.lower()=="search" or cmd.lower()== "look" or cmd.lower()== "examine":
                nicePrint("""You search the basement but find nothing that you need.\n""")
                basement(items)
            else:
                nicePrint("You can't do that, try something else.\n")
                getcmd(cmd_list)
                        

        else:
            print("""1. Go back upstairs to the front room.
2. Take the crossbow.
3. Inspect the cells.\n""")
            caller_text="""1. Go back upstairs to the front room.
2. Take the crossbow.
3. Inspect the cells. \n"""

            cmd_list = ["1", "2", "3", "search", "look", "examine"]
            cmd = getcmd(cmd_list)

            if cmd=="1":
                nicePrint("You decide to return upstairs to the front room.\n")
                front_room(items)
            elif cmd=="2" :
                if not crossbow_taken:
                    nicePrint("You take the crossbow and some bolts.\n")
                    crossbow_taken = True
                    items.update({"crossbow":"a small crossbow, not strong to penetrate armour but will stop an unarmoured enemy, simple to use, solid Imperial craftmanship."})
                    basement(items)
                else:
                    nicePrint("You can't do that, try something else.\n") 
                    basement(items)
            elif cmd=="3":
                nicePrint("""Shadows dance all around the basement as you walk towards the prison cells
                you have seen them before, from the inside mostly
                there are five, built into the wall of the basement with strong iron bars in the front.
                By the look of everything these are only used to provide temporary accommodation
                probably the prisoners are soon transferred to a larger prison.\n""")
                basement(items)
            elif cmd.lower()=="search" or cmd.lower()== "look" or cmd.lower()== "examine":
                nicePrint("""You search the basement but find nothing that you need.\n""")
                basement(items)
            else:
                nicePrint("You can't do that, try something else.\n")
                getcmd(cmd_list)
            
              
    if not front_room_first:
        
        nicePrint("""You enter a dark room, some light comes through the broken window
        casting long shadows everywhere.
        The room is large and filled with furniture
        desk, chairs, shelves reside in the dark.\n""")
        time.sleep(2)
        nicePrint("""As your eyes get used to the darkness you start to see small items everywhere
        on the side wall of the room a set of stairs leading somewhere down
        next to them a set of stairs leading up to the first floor\n""")
        front_room_first = True
        if not kitchen_first:
            nicePrint("""and far at the back of the room light shines under a door.\n""")
        
    else:
        nicePrint("The front room hasn't changed.\n")
    nicePrint("What do you do : \n")
    
    if kitchen_first and front_room_first:
        print("""1. Go to the stairs leading down.
2. Approach the stairs to the second floor.
3. Return to the kithcen.
4. Go out to the front porch.\n""")
        caller_text="""1. Go to the stairs leading down.
2. Approach the stairs to the second floor.
3. Return to the kithcen.
4. Go out to the front porch.\n"""
    elif kitchen_first:
        print("""1. Go to the stairs leading down.
2. Approach the stairs to the second floor.
3. Return to the kithcen.
4. Go out to the front porch.\n""")
        caller_text="""1. Go to the stairs leading down.
2. Approach the stairs to the second floor.
3. Return to the kithcen.
4. Go out to the front porch.\n"""
    elif front_room_first:
        print("""1. Go to the stairs leading down.
2. Approach the stairs to the second floor.
3. Move to the door at the back of the room with the light on the other side.
4. Return to the front porch.\n""")
        caller_text="""1. Go to the stairs leading down.
2. Approach the stairs to the second floor.
3. Move to the door at the back of the room with the light on the other side.
4. Return to the front porch.\n"""


    cmd_list = ["1", "2", "3", "4", "search", "look", "examine"]
    cmd = getcmd(cmd_list)

    if cmd=="1":
        nicePrint("""Sliding through the shadows you move around the room
        and are on the top of the stairs leading down to somekind of a basement.\n""")
        time.sleep(2)
        nicePrint("""You step down carefully following the wall
        it is pitch black you can see absolutely nothing
        there is no point in going down here with out a light source.\n""")

        if "pipe" in items and "broken lantern" in items:
            nicePrint("""Light the broken lantern with the pipe, 
            although it's broken it will shed enough light.
1. Yes
2. No.\n""")

            caller_text="""Light the broken lantern with the pipe, 
            although it's broken it will shed enough light.
1. Yes
2. No.\n"""

            cmd_list = ["1", "2", "yes", "no"]
            cmd = getcmd(cmd_list)

            if cmd =="1" or cmd.lower()=="yes":
                nicePrint("You light the broken lantern and proceed downstairs.\n")
                del items["pipe"]
                del items["broken lantern"]
                basement(items)
            elif cmd=="2" or cmd.lower()=="no":
                nicePrint("You decide to leave the dark basement and return to the room\n")
                front_room(items)
            else:
                nicePrint("You can't do that, try something else.\n")
                getcmd(cmd_list)
        else:
            nicePrint("""Without something to light your way there is nothing that you can do downstairs.\n""")
            front_room(items)
    elif cmd=="2":
        nicePrint("""Moving quietly you approach the base of the stairs leading up to the first floor.
        It is a simple wooden staircase with walls on both sides,
        upstairs is quiet and dark.\n""")
        input("Press enter.\n")
        nicePrint("Go up to the first floor?\n")
        print("""1. Yes
2. No.\n""")
        caller_text="""1. Yes
2. No.\n"""

        cmd_list = ["1", "2", "yes", "no"]
        cmd = getcmd(cmd_list)

        if cmd =="1" or cmd.lower()=="yes":
            nicePrint("Pressed against the wall you slowly move up stairs.\n")
            sleeping_room(items)
        elif cmd=="2" or cmd.lower()=="no":
            nicePrint("For now you decide to return to the room\n")
            front_room(items)
        else:
            nicePrint("You can't do that, try something else.\n")
            front_room(items)
    elif cmd=="3":
        nicePrint("""Sneaking through the dark room you find yourself next to the door in the back of the room.
        It's a simple wooden door without a lock,
        underneath light escapes from the other side.\n""")
        input("Press enter.\n")
        nicePrint("What do you do : \n")
        print("""1. Open the door.
2. Return to the room.\n""")
        caller_text="""1. Open the door.
2. Return to the front room.\n"""

        cmd_list = ["1", "2", "yes", "no", "search", "listen", "examine"]
        cmd = getcmd(cmd_list)

        if cmd=="1":
            if snorri_found:
                nicePrint("You quietly open the door not to wake anybody inside.\n")
                kitchen(items)
            nicePrint("You open the door.\n")
            kitchen(items)
        elif cmd=="2":
            nicePrint("You decide to quietly return to the front room.\n")
            front_room(items)
        elif cmd.lower()=="search" or cmd.lower()== "listen" or cmd.lower()== "examine":
            if fire or snorri_out:
                nicePrint("You hear nothing.\n")
                front_room(items)
            else:
                nicePrint("""Carefully you put your ear to the door,
                there is noise coming from the other side\n""")
                time.sleep(2)
                nicePrint("not sure what it is\n")
                time.sleep(2)
                nicePrint("somebody talking\n")
                time.sleep(2)
                nicePrint("it's definitely a human voice\n")
                time.sleep(2)
                nicePrint("but it's not saying anything coherent\n")
                time.sleep(2)
                nicePrint("""and then it hits you,
                it is a human voice
                a snoring voice
                a deep snoring voice.\n""")
                snorri_found=True
                front_room(items)
        else:
            nicePrint("You can't do that, try something else.\n")
            front_room(items)
    elif cmd=="4":
        if porch_emptied:
            nicePrint("You decide to go out to the front porch.\n")
            empty_porch(items)
        else: 
            nicePrint("The Wardens are on the porch it would be suicide to go out there.\n")
            front_room(items)
    elif cmd.lower()=="search" or cmd.lower()== "look" or cmd.lower()== "examine":
        nicePrint("""This room is too dark for you to find anything useful,
        you can navigate it but searching is impossible
        and its too dangerous to light the room
        the Wardens might notice.\n""")
        front_room(items)    
    else:
        nicePrint("You can't do that, try something else.\n")
        getcmd(cmd_list)

front_door_open = False

#When the front porch is empty.
def empty_porch(items):
    
    global wardens_return
    global empty_porch_counter
    global empty_porch_first
    global caller_text
    global fire
        
    #When the player is on the bridge gate.
    def bridge_gate(items):
        global wardens_return
        global empty_porch_counter
        global bride_gate_first
        global fire

        if fire or wardens_eliminated:
            pass
        else:
            if empty_porch_counter > 3 :
                wardens_return=True
                porch_emptied=False

        if not wardens_return or wardens_eliminated:
            if not bride_gate_first :
                nicePrint("""You approach the bride, this side of the bride is covered with a roof,
    it covers the bride like a small house and just like a house it has a door.
    On the door a massive lock closes a chain wrapped around the door handles.
    The doors are closed tightly there isn't enough room to squeeze thorugh\n""")
                input("Press enter.\n")
                nicePrint("""Under the roof to the right there is a notice board.
    The only light comes from the lanterns on the outpost.\n""")
                bride_gate_first = True
            else:
                nicePrint("You are at the bride gate, nothing has changed.\n")
            nicePrint("What do you do : \n")
            
            if "bridge key" in items:
                print("1. Unlock the bride door.")
                print("2. Return to the porch.\n")
                global caller_text
                caller_text = """1. Unlock the bride door.
2. Return to the porch.\n"""

                
                cmd_list = ["1", "2", "3", "4", "notice board", "notice", "board", "search", "look", "examine"]
                cmd = getcmd(cmd_list)

                if cmd=="1" :
                    if "bridge key" in items:
                        nicePrint("""The large key fits perfectly into the bride lock.
        The mechanism is in good order and it takes only one move of the key and the lock opens.\n""")
                        input("Press enter.\n")
                        nicePrint("""The door swings open without a sound,
        under the roof you can only hear the drumming the rain
        you run through the bridge gate and onto the bridge.\n""")
                        crossing_the_bride()
                    else:
                        nicePrint("You can't do that, try something else.\n")
                        bridge_gate(items)
                elif cmd=="2":
                        nicePrint("You return to the porch.\n")
                        empty_porch_counter +=1
                        empty_porch(items)    
                                
                elif cmd.lower() == "notice board" or cmd.lower() == "notice" or cmd.lower() == "board": 
                    nicePrint("""Quickly you glance at the notice board next to the gate.
    You do not find yourself as a wanted person, for now.
    There are some information about using the gate.
    The gate toll is 1 schilling per two legs, 2 schilling per four legs and 3 schillings per cart,
    the Wardens have the right to charge extra if needed.
    Gate toll is obligatory for ALL travelers.
    Travelling papers are also mandatory.
    By the order of the Elector Count Lenny's travelling citchen is freed of all road and gate tolls.\n 
    """ )
                    getcmd(cmd_list)
                elif cmd.lower()== "search" or cmd.lower()== "look" or cmd.lower()== "examine":
                    nicePrint("There is no time to search here.\n")
                    getcmd(cmd_list) 
                else:
                    print("You can not do that, try something else.\n")
                    getcmd(cmd_list)
                empty_porch(items)


            
            elif "grappling hook" in items:
                if not wounded:
                    print("1. Climb over the bride gate.")
                    print("2. Return to the porch.\n")
                    caller_text = """1. Climb over the bride gate.
    2. Return to the porch.\n"""
                else:
                    nicePrint("""You could use the grappling hook to climb over the gate
                    but you arm is too damadged.
                    You will have to find some other way.\n""")
                    bridge_gate(items)

                cmd_list = ["1", "2", "notice board", "notice", "board", "search", "look", "examine"]
                cmd = getcmd(cmd_list)

                if cmd == "1":
                    if wounded and "grappling hook" in items:
                        nicePrint("""You could use the grappling hook to climb over the gate
                        but you arm is too damadged.
                        You will have to find some other way.\n""")
                        bridge_gate(items)
                    if "grappling hook" in items:
                        nicePrint("""You unravel the grappling hook and swing the hook a couple of times 
                        and then let it fly through the rain.\n""")
                        time.sleep(2)
                        nicePrint("""Glimmer of steel in the dark tells you that the hook finished on the roof of the bridge gate.
                        You pull slightly and can feel the hook sliding across the roof.\n""")
                        time.sleep(2)
                        nicePrint("""Until the rope starts to resist your pull, the hook is cought on something.
                        With no time to waste you start climbing, 
                        the wind and the rain making your task even more difficult.
                        The rope is wet and slippery but you manage to rach the roof of the bridge gate.\n""")
                        time.sleep(2)
                        nicePrint("""Standing on the top you can see the huge river below you, 
                        the bridge in front of you is long and made of stone.
                        You pull the rope, removing the evidence and walk to the other side of the roof.
                        You hang from the roof and than drop to the bride and run away from the gate.\n""")
                        crossing_the_bride()
                    else:
                        nicePrint("You can't do that, try something else.\n")
                        bridge_gate(items)
                elif cmd=="2":
                        nicePrint("You return to the porch.\n")
                        empty_porch_counter +=1
                        empty_porch(items)    
                                
                elif cmd.lower() == "notice board" or cmd.lower() == "notice" or cmd.lower() == "board": 
                    nicePrint("""Quickly you glance at the notice board next to the gate.
    You do not find yourself as a wanted person, for now.
    There are some information about using the gate.
    The gate toll is 1 schilling per two legs, 2 schilling per four legs and 3 schillings per cart,
    the Wardens have the right to charge extra if needed.
    Gate toll is obligatory for ALL travelers.
    Travelling papers are also mandatory.
    By the order of the Elector Count Lenny's travelling citchen is freed of all road and gate tolls.\n 
    """ )
                    getcmd(cmd_list)
                elif cmd.lower()== "search" or cmd.lower()== "look" or cmd.lower()== "examine":
                    nicePrint("There is no time to search here.\n")
                    getcmd(cmd_list) 
                else:
                    print("You can not do that, try something else.\n")
                    getcmd(cmd_list)
                empty_porch(items)
    

            elif "lock pick" in items:
                print("1. Try to pick the lock with your lockpick.")
                print("2. Return to the porch.\n")
                caller_text = """1. Try to pick the lock with your lockpick.
2. Return to the porch.\n"""
            
                cmd_list = ["1", "2", "notice board", "notice", "board", "search", "look", "examine"]
                cmd = getcmd(cmd_list)

                if cmd=="1" :
                    if "lock pick" in items:
                        nicePrint("""You skilfully insert the lockpick into the large lock,
        You can feel it clicking into place inside the lock.
        Immediately you start to defeat the mechanism.\n""")
                        time.sleep(2)
                        input("Press enter.\n")
                        colorama.init()
                        print(Fore.RED+"CRACK!"+Style.RESET_ALL)
                        time.sleep(2)
                        nicePrint("""The lockpick snaps in two but the lock remains locked.
        You will have to find another way to unlock it.\n""")
                        del items["lock pick"]
                        bridge_gate(items)
                    else:
                        nicePrint("You can't do that, try something else.\n")
                        bridge_gate(items)
                elif cmd=="2":
                        nicePrint("You return to the porch.\n")
                        empty_porch_counter +=1
                        empty_porch(items)    
                
                elif cmd.lower() == "notice board" or cmd.lower() == "notice" or cmd.lower() == "board": 
                    nicePrint("""Quickly you glance at the notice board next to the gate.
    You do not find yourself as a wanted person, for now.
    There are some information about using the gate.
    The gate toll is 1 schilling per two legs, 2 schilling per four legs and 3 schillings per cart,
    the Wardens have the right to charge extra if needed.
    Gate toll is obligatory for ALL travelers.
    Travelling papers are also mandatory.
    By the order of the Elector Count Lenny's travelling citchen is freed of all road and gate tolls.\n 
    """ )
                    getcmd(cmd_list)
                elif cmd.lower()== "search" or cmd.lower()== "look" or cmd.lower()== "examine":
                    nicePrint("There is no time to search here.\n")
                    getcmd(cmd_list) 
                else:
                    print("You can not do that, try something else.\n")
                    getcmd(cmd_list)
                empty_porch(items)


            else:
                print("1. Return to the porch.\n")
                caller_text = """1. Return to the porch.\n"""


            cmd_list = ["1", "notice board", "notice", "board", "search", "look", "examine"]
            cmd = getcmd(cmd_list)

           
            if cmd=="1":
                    nicePrint("You return to the porch.\n")
                    empty_porch_counter +=1
                    empty_porch(items)    
            
                 
            elif cmd.lower() == "notice board" or cmd.lower() == "notice" or cmd.lower() == "board": 
                nicePrint("""Quickly you glance at the notice board next to the gate.
You do not find yourself as a wanted person, for now.
There are some information about using the gate.
The gate toll is 1 schilling per two legs, 2 schilling per four legs and 3 schillings per cart,
the Wardens have the right to charge extra if needed.
Gate toll is obligatory for ALL travelers.
Travelling papers are also mandatory.
By the order of the Elector Count Lenny's travelling citchen is freed of all road and gate tolls.\n 
""" )
                getcmd(cmd_list)
            elif cmd.lower()== "search" or cmd.lower()== "look" or cmd.lower()== "examine":
                nicePrint("There is no time to search here.\n")
                getcmd(cmd_list) 
            else:
                print("You can not do that, try something else.\n")
                getcmd(cmd_list)
            empty_porch(items)


            
        else:
            wardens_have_returned(items)

    
    def front_door(items):

        global wardens_return
        global empty_porch_counter
        global porch_door_first
        global pipe_taken
        global front_door_open 
        global wardens_eliminated
        global fire

        if fire or wardens_eliminated:
            pass
        else:
            if empty_porch_counter > 3 :
                wardens_return=True
                porch_emptied=False

       
        if not wardens_return or wardens_eliminated:
            if not porch_door_first:
                nicePrint("""As you step under the roof of the porch it is for the first time in the last couple of days
                that you do not feel the rain, you almost sigh with relief, 
                the wooden floor beneath your feet is solid
                in contrast to the muddy ground.\n""")
                time.sleep(1)
                nicePrint("""The porch has a rough wooden floor and is covered by a roof,
                there is a table with a couple of chairs, on the table a wooden pipe,
                some shards of broken glass from the window.\n""" )
                time.sleep(1)
                nicePrint("""In the middle of the front wall of the outpost is a door, leading inside.
                The door is sturdy, wooden with iron parts strenghtening it.\n""")
                input("Press enter.\n")
                nicePrint("The door is locked as you discover when you try to open it.\n")
                porch_door_first = True
                nicePrint("After a moment of tranquility you decide to :\n")
            else:
                nicePrint("In front of the porch door you decide to :\n")
            
            if front_door_open:
                print("""3. Return to the front of the porch.
4. Go into the front room.\n""" )
                global caller_text
                caller_text="""3. Return to the front of the porch.
4. Go into the front room.\n"""    

            elif "lock pick" in items:
                print("1. Try to pick the lock.")
                print("2. Force the door.")
                print("3. Return to the front of the porch.")

                caller_text="""1. Try to pick the lock.
2. Force the door.
3. Return to the front of the porch.\n"""
            else:
                print("2. Force the door.")
                print("3. Return to the front of the porch.")

                caller_text="""2. Force the door
3. Return to the front of the porch.\n"""
            
            cmd_list = ["1", "2", "3","4","window", "use window", "enter through window", "enter window",
    "search", "look", "examine", "pipe", "take pipe", "grab pipe", "pick up pipe", "window look", 
    "look window", "look inside"]
            cmd = getcmd(cmd_list)

            if cmd=="1" :
                if "lock pick" in items:
                    nicePrint("""The lock pick slides into the door lock
                    after a little fiddling you feel it catching the lock mechanism,
                    and instantly you start to unlock.\n""")
                    time.sleep(2)
                    nicePrint("Turning the lock to the left.\n")
                    time.sleep(2)
                    nicePrint("Turning the lock to the right.\n")
                    time.sleep(2)
                    colorama.init()
                    print(Fore.GREEN + "CLICK" + Style.RESET_ALL)
                    nicePrint("""The lock clicks open and the door lazily slides open
                    revealing the dark inside.\n""")
                    if fire or wardens_eliminated:
                        pass
                    else:
                        nicePrint("You can hear the Wardens returning.\n")
                        wardens_return = True
                    front_door_open = True
                                           
                    del items["lock pick"]
                    front_room(items)
                                  
                else:
                    print("You can not do that, try something else.\n")
                    front_door(items)
            elif cmd=="2":
                nicePrint("""Stepping back to gather speed 
                you slam the door with all of your strength.\n""")
                time.sleep(2)
                nicePrint("""And immediately regret it, the door is unmoved by your attempt
                but your shoulder hurts like hell,
                you shut your mouth tightly to stop the scream of pain.\n""")
                time.sleep(2)
                nicePrint("This door will not yield, you have to find some other way.\n")
                
                front_door(items)
                
            elif cmd=="3":
                nicePrint("You return to the front of the porch.\n")
                empty_porch_counter +=1
                empty_porch(items)
            elif cmd == "4":
                if front_door_open:
                    nicePrint("You open the door and enter the front room.\n")
                    front_room(items)
                else:
                    nicePrint("You can't do that, try something else.\n")
                    front_door(items)  
            elif cmd.lower() == "window" or cmd.lower() == "use window" or cmd.lower() == "enter through window" or cmd.lower() == "enter window": 
                nicePrint("""Following the pieces of broken glass on the wooden floor
                you notice the window, it was destoryed when you threw the stone.\n""")
                input("Press enter.")
                nicePrint("""The hole in the glass isn't that big,
                but the glass is no match for your steel,
                using your dagger you chip away the rest of the glass.\n""")
                time.sleep(2)
                if fire or wardens_eliminated:
                    nicePrint("You climb through the window into the dark room.\n")
                    
                else:
                    nicePrint("""As you climb through the window into the darkness
                    you can hear the Wardens returning.\n""")
                    wardens_return = True
                    
                front_room(items)
            elif cmd.lower() == "pipe" or cmd.lower() == "take pipe" or cmd.lower() == "grab pipe" or cmd.lower() == "pick up pipe":
                if not pipe_taken:
                    print()
                    nicePrint("You take the pipe from the table.\n")
                    items.update({"pipe":"a simple smoking pipe, made out of wood, the tobaco inside is still smoking."})
                    pipe_taken = True
                    front_door(items)
                else:
                    print()
                    nicePrint("You can't do that, try something else.\n")
                    front_door(items)
            elif  cmd.lower()== "window look" or cmd.lower()=="look window" or cmd.lower()== "look inside":
                nicePrint("""You peek through the broken window,
                at first you only see darkness.\n""")
                input("Press enter.")
                nicePrint("""As your eyes adjust to the darkness you start to see shapes inside the room.
                chairs and a table, some shelves on the walls, 
                nothing is moving and all is quiet.\n""")
                time.sleep(2)
                nicePrint("""In the far back of the dark room you see ray of light
                coming from the next room under the door.\n""")
                getcmd(cmd_list)
            elif cmd.lower()== "search" or cmd.lower()== "look" or cmd.lower()== "examine":
                nicePrint("There is no time to search here.\n")
                getcmd(cmd_list) 
            else:
                print("You can not do that, try something else.\n")
                getcmd(cmd_list)

                
        else:
            wardens_have_returned(items)

    
    if fire or wardens_eliminated:
        pass
    else:
        if empty_porch_counter > 3 :
            wardens_return=True
            porch_emptied=False



    if wardens_eliminated:
        empty_porch_first = True
        input("Press enter.\n")

    if not empty_porch_first :
        nicePrint("""You nervously step out the relative safety of the shadows and move to the now empty front porch.\n""")
        empty_porch_first = True
        input("Press enter.\n")

    if not fire :
        if not wardens_return or wardens_eliminated:
            nicePrint("""On the porch to the right there is a door leading inside the outpost, 
            directly in front of you is the bride gate.\n""")
            nicePrint("Quickly you decide to : \n")
            print("1. Return to the main road.")
            print("2. Go to the bride gate.")
            print("3. Move to the door leading inside.\n")
                
            caller_text =""""1. Return to the main road.
2. Go to the bride gate.
3. Move to the door leading inside.\n"""

            cmd_list = ["1", "2", "3", "search", "look", "examine"]
            cmd = getcmd(cmd_list)
            
            if cmd=="1" :
                nicePrint("You quietly return to the bushes near the main road.\n")
                empty_porch_counter +=1
                start(items)
            elif cmd=="2":
                nicePrint("You go towards the bridge.\n")
                empty_porch_counter +=1
                bridge_gate(items)
                
            elif cmd=="3":
                nicePrint("You move to the front door.\n")
                empty_porch_counter +=1
                front_door(items)
                
            elif cmd.lower()== "search" or cmd.lower()== "look" or cmd.lower()== "examine":
                nicePrint("There is no time to search here.\n")
                getcmd(cmd_list) 
            else:
                print("You can not do that, try something else.\n")
                getcmd(cmd_list)
            

        else:
            wardens_have_returned(items) 
        if not wardens_eliminated:
            nicePrint("Through the rain on the left you can hear the Wardens in the distance, they could be back at any moment.\n")
        
    else:
        
        nicePrint("The night sky is glowing with fire from the other side of the outpost\n")
        nicePrint("Quickly you decide to : \n")
        print("1. Return to the bushes next to the main road.")
        print("2. Go to the bride gate.")
        print("3. Move to the door leading inside.")
        print()

        caller_text = """1. Return to the bushes next to the main road.
2. Go to the bride gate.
3. Move to the door leading inside."""


        cmd_list = ["1", "2", "3", "search", "look", "examine"]
        cmd = getcmd(cmd_list)
        
        if cmd=="1" :
            nicePrint("You quietly return to the bushes near the main road.\n")
            empty_porch_counter +=1
            start(items)
        elif cmd=="2":
            nicePrint("You go towards the bridge.\n")
            empty_porch_counter +=1
            bridge_gate(items)
            
        elif cmd=="3":
            nicePrint("You move to the front door.\n")
            empty_porch_counter +=1
            front_door(items)
              
        elif cmd.lower()== "search" or cmd.lower()== "look" or cmd.lower()== "examine":
            nicePrint("There is no time to search here.\n")
            getcmd(cmd_list) 
        else:
            print("You can not do that, try something else.\n")
            getcmd(cmd_list)
        

        
    




guard_alert = False
combat = False
backyard=False

#When the player approaches the Wardens directly.
def approach_directly(items):
    
    
    global combat
    global backyard
    global guard_alert
    combat = True
    
    if wounded:
        nicePrint("""The guards will instantly be alerted by your wounds, there is no point in approaching them directly now.""")
        start(items)
    if not guard_alert:
        guard_alert = True
        nicePrint("""You straighten yourself and walk the road with confidence,
        soon you are a but a handful of steps away from the building.
        Its a one story house with a porch next to the road,
        Imperial flag and a flag of the Elector count hang on the facade.
        The house seems well maintained, lanterns shed light on the surrounding area.""")
        print()
        input("Press enter.")
        nicePrint("""As you continue to approach, a dog barks and two guards in Warden's uniforms from the porch
        raise their lanterns and spears to greet you.""")
        print()
        input("Press enter.")
        nicePrint("""With a corner of your eye you notice than the outpost has a backyard.
        The outpost is seated next to the river and a bride leading across has a roof on this side,
        and a locked gate""")
        backyard=True
        print()
        input("Press enter.")
        nicePrintRed("HALT! WHO GOES THERE!")
        print()
        nicePrint("""The older guard shouts in your direction, his helmet covering the head,
        but his graying mustache betray his age.""")
        print()
        nicePrint("""The younger one, not more than twenty, steps out in the rain grudgingly,
        leaving the dog tied to the post""")
        print()
        nicePrintRed("State your name and business!")
        print()
        input("Press enter.")
        nicePrint("What do you say : ")
        print()
        print("1. I am a merchant from Altdorf returning home after a business trip.")
        print("2. I am a courrier carrying an urgent message to Altdorf.")
        print("3. Inquisitional matters, let me pass! ")
        print("4. I am just a burgher caught by the rain on the road.")
        print("5. say what ever you want.")

        cmd_list = ["1", "2", "3", "4", "5", "run", "go back", "escape", "attack", "fight", "combat"]
        cmd = getcmd(cmd_list)
        if cmd=="1":
            nicePrintGreen("I am a merchant from Altdorf returning home after a business trip.\n")
            nicePrintRed("Strange time for a mercahnt to be travelling, show me your papers.\n")
            choice()

        elif cmd=="2":
            nicePrintGreen("I am a courrier carrying an urgent message to Altdorf.\n")
            nicePrintRed("Allright courrier show me your papers.\n")
            choice()
            
        elif cmd=="3":
            nicePrintGreen("Inquisitional matters, let me pass! \n")
            nicePrint("The guards flinch and exchange a look.\n")
            nicePrintRed("Pardon me Inqusitionar but we must see your papers.\n")
            choice()
        elif cmd == "4":
            nicePrintGreen("I am just a burgher caught by the rain on the road.\n")
            nicePrintRed("""What manner of misfortune made you walk the road at this night?
            Let's see your papers.\n""")
            choice()
        elif cmd=="5":
            nicePrint("You say:\n")
            nicePrintGreen( input())
            nicePrintRed ("Your papers!\n")
            choice()
        elif cmd=="run" or "go back" or "escape":
            nicePrint(""" Suddenly you turn around and start running back to the road,
                leaving the unprepared guards behind.\n""")
            nicePrint("""The most important skill for a thief is running, you thought, smiling,
            rain washing your face\n""")
            input("Press enter.\n")
            nicePrint("""Dashing through the rain you quickly get lost in the dark bushes,
            The Wardens not motivated enough to chase you.
            You can hear them cursing the rain\n""")
            input("Press enter.\n")
            nicePrint("""You stop to catch your breath and think about your next move.
            The Wardens are not chasing you but are on alert now\n""")
            guard_alert = True
            start(items)
            
        elif cmd=="attack" or "fight" or "combat":
            nicePrint("""Without warning you attack the dagger is quickest to draw,
                using the element of surprise you attack the nearest Warden.
                He steps back supprised trying to point his spear towards you, 
                but his long weapon a disadvantage in this situation.\n""")
            input("Press enter.\n")
            nicePrint("""You charge him and close the distance, shlashing him across the chest.
            His uniform opening like i flower revealing a crimson red inside.\n""")
            input("Press enter.\n")
            nicePrint("His face a mix of fear and surprise, you continue to attack.\n")
            nicePrint("""You quickly turn around to face the other guard, but instead of charging at you
            he is busy with unleashing the dog.
            A scary looking beast with it's rageful eyes fixed on you.
            Before you can react the dog is free and with flashing speed tosses itself at you.\n""")
            input("Press enter.\n")
            nicePrint("""You instinctively raise one arm to protect your face and the dog goes for it.
            The sheer force of the animal's body knocks you on the ground.
            You manage to land a blow with your dagger but a Warden's spear to your side paralizes you with pain.\n""")
            input("Press enter.\n")
            nicePrint("""Your arms loose strength as the older Warden pulls his spear from you,
            you collapse to the muddy road, your face hits the cold mud.\n""")
            input("Press enter.\n")
            nicePrintMenacing("The last thing you think is that running is the most important skill for a thief\n")
            input("Press enter.\n")
            nicePrintMenacing("running away\n")
            nicePrint("""
            GAME OVER \n""")
            time.sleep(3)
            sys.exit(1)
            
            
        else:
            nicePrint("You can't do that. Try something else.\n")
            getcmd(cmd_list)
            
    else:
        print("The guards charge at you!\n")
        combat_situation()

    


sneaked_to_the_wardens = False
sneak_to_the_wardens_searched = False
porch_emptied = False
stone_thrown = False

#When the player sneaks to the Wardens to get more info.
def sneak_to_the_wardens(items):

    global sneaked_to_the_wardens
    global caller_text
    global stone_thrown

    def sneak_to_the_wardens_search():
        global sneak_to_the_wardens_searched
        nicePrint("You search your surroundings and find a fist sized stone in the wet ground.\n")
        
        nicePrint("Take it?\n")
        
        print("""1. Yes.
2. No.\n""")

        cmd_list = ["1", "2", "yes", "no"]
        cmd = getcmd(cmd_list)

        if cmd.lower()=="1" or cmd.lower()=="yes":
            nicePrint("You pick up the stone.\n")
            sneak_to_the_wardens_searched = True
            items.update({"stone":"a fist sized stone, nothing special about it."})
        elif cmd.lower()=="2" or cmd.lower()=="no":
            nicePrint("You leave the stone on the ground.\n")
            
        else:
            print("You can not do that, try something else.\n")
            getcmd(cmd_list)
        sneak_to_the_wardens(items)
        

    if not sneaked_to_the_wardens:
        
        sneaked_to_the_wardens = True
        nicePrint("""You move quietly through the bushes without being detected, 
        and soon you are able to see the front of the outpost.\n""")
        
        nicePrint("""Its a one story house with a porch next to the road,
            Imperial flag and a flag of the Elector count hang on the facade.
            The house seems well maintained, lanterns shed light on the surrounding area.
            You think that there is somekind of a backyard of the outpost\n""")
        global backyard
        backyard = True
        
        input("Press enter.")
        nicePrint("""On the front porch two guards in Wardens uniforms sit and chat, 
        you are too far away to hear what they are talking about. 
        Next to them a large dog is lying down tied to one of the posts of the porch.
        With the rain hiding you all of them are unaware of your presence.\n""")
        
        input("Press enter.")
        nicePrint("""The road goes directly to the front of the outpost and after that into a bride.
        Apparently this outpost is overlooking a river crossing.
        From here you are not sure how wide the river is.
        The bride has a roofed section on this side of the river and a gate.
        A large lock glimmering on the lantern light\n""")
        
        input("Press enter.")
        nicePrint("""All the windows are dark, except one on first floor, furthest from the bridge.\n""")
    else:
        
        nicePrint("""You are hiding in the bushes in front of the outpost 
        nothing has changed since the last time.\n""")
        
    
    nicePrint("You decide to : \n")
    
    if "stone" in items and river:
        print("""1. Return to the main road.")
2. Move quietly to the river.
3. Throw a stone at the Wardens to cause a distraction and quckly move away.
   If this works it will work only once, they won't fall for the trick again.
   Throw it now?.\n""")

        caller_text = """1. Return to the main road.
2. Move quietly to the river.
3. Throw a stone at the Wardens and quckly move away.\n"""

    elif "stone" in items:
        print("""1. Return to the main road.
2. Continue to move silently to the left of the outpost.
3. Throw a stone at the Wardens to cause a distraction and quckly move away.
   If this works it will work only once, they won't fall for the trick again.
   Throw it now?.\n""")
        
        caller_text = """1. Return to the main road.
2. Continue to move silently to the left of the outpost.
3. Throw a stone at the Wardens and quckly move away.\n"""
    elif river :
        print("""1. Return to the main road.
2. Move quietly to the river.\n""")

        caller_text = """1. Return to the main road.
2. 2. Move quietly to the river.\n"""
    else:
        print("""1. Return to the main road.
2. Continue to move silently to the left of the outpost.\n""")

    cmd_list = ["1", "2", "3", "search", "look", "examine"]
    cmd = getcmd(cmd_list)

    if cmd=="1":
        start(items)
    elif cmd=="2":
        sneak_around(items)
    elif cmd=="3":
        if "stone" in items:
            if not stone_thrown:
                print()
                nicePrint("""You throw a stone at the porch of the outpost and quckly move away
Behind you you can hear glass shatering, the Wardens cursing and dog barking\n""")
                del items["stone"]
                
                input("Press enter.")
                nicePrint("""As you reach the main road, hiding in the bushes you see the Wardens leaving the outpost
                and going to the spot from where you threw the stone\n""")
                
                input("Press enter.")
                nicePrint("The porch is now empty.\n")
                               
                stone_thrown = True
                global porch_emptied
                porch_emptied = True
                start(items)
            else:
                nicePrint("""They won't wall for the stone trick again, 
                you whould only attract the Warden's attention to your self.\n""")
        else:
            nicePrint("You can't do that. Try something else.\n")
            sneak_to_the_wardens(items)
       
    elif cmd == "search" or  cmd =="look" or cmd =="examine":
        if not sneak_to_the_wardens_searched:
            sneak_to_the_wardens_search()
            
        else:
            nicePrint("There is nothing to find here.\n")
            sneak_to_the_wardens(items)
 
    else:
        nicePrint("You can't do that. Try something else.\n")
        getcmd(cmd_list)



river = False
river_searched = False

#When the player sneaks to the river.
def sneak_around(items):
    
    global wardens_return
    global empty_porch_counter
    global river
    global river_searched
    global fire
    global porch_emptied

    if fire or wardens_eliminated:
        pass
    else:
        if empty_porch_counter > 3 :
            wardens_return=True
            porch_emptied=False
            
    if not river:

        nicePrint("""You sneak around the Warden's outpost keeping to the shadows and the bushes,
        you manage to avoid being detected, the night and the rain your allies.""")
        print()
        input("Press enter.")

        nicePrint("""Moving to the left of the building you make past it, 
        in the distance you can almost hear voices.""")
        print()
        time.sleep(1)

        nicePrint("""Soon you are overwhelmed with a rumbling sound, and moments later your leg slips 
        you find yourself rolling on a muddy slope.""")
        print()
        time.sleep(2)

        nicePrint("""You manage to get a grip on a tree branch""")
        print()
        input("Press enter.")

        nicePrint("""in front of you like a enormus worm burrowing through the ground 
        streches a river, its water dark and murky,
        overflowing,
        the rain only making it fatter.""")
        print()

        nicePrint("""Once you steady yourself you can see that the only crossing in sight is the bridge,
        nested against the Wardens's outpost, its silhouette barely visiable against the dark skies.""")
        print()
        time.sleep(2)
    else:
        print()
        nicePrint(
            "You return to the bank of the humming river, its waters dark and frightening")
        print()
    river = True


    nicePrint("After some thoughts you decide to :")
    print()
    print("1. Jump into the river and try to swim to the other bank.")
    print("2. Turn around and return to the road.")

    global caller_text
    caller_text = """1. Jump into the river and try to swim to the other bank.
2. Turn around and return to the road."""


    cmd_list = ["1", "2", "search", "look", "examine"]
    cmd = getcmd(cmd_list)

    if cmd == "1":

        nicePrint("You muster all your courage and toss yourself into the river.\n")
        time.sleep(2)

        nicePrint("The shock of the cold water is like a knife.\n")
        time.sleep(3)

        nicePrint("""You instinctively reach for the surface but in the dark you don't know
        where up is.\n""")
        time.sleep(4)

        nicePrint("The water tastes like dirt and soon you faint.\n")
        

        nicePrint("""The river carries your body far away, 
        days later some farmers will find your bloated corpse.\n""")
        time.sleep(2)

        nicePrintMenacing("Still clutching to something inside a pocket.\n")
        nicePrint("You have died, GAME OVER.")
        time.sleep(3)
        try:
            sys.exit(1)
        except SystemExit as e:
            pass
    elif cmd == "2":

        print()
        nicePrint("You decide to backtrack to the road and try something else.\n")
        if porch_emptied:
            empty_porch_counter += 1 
        start(items)

    elif cmd== "search" or cmd =="look" or cmd =="examine":
        if river_searched:
            nicePrint("There is nothing to find here.")
            sneak_around(items)
        else:
            nicePrint("""You search the surrounding river bank, it is a difficult task.
            The night is dark, the skies covered with rain clouds, and the ground is almost as liquid as the river.
            But you catch a glimse of metal, down near the river's edge.
            You slide down to it and it turns out to be a large fishing hook with the fish still attached.
            The fish is dead and covered with mud.
            This must have fallen of some fisherman's boat upriver.
            """)
            
            #caller_text ="""1. Jump into the river and try to swim to the other bank.
#2. Turn around and return to the road."""
            #global caller_text
            print()
            nicePrint("Take it?")
            print()
            print("1. Yes.")
            print("2. No.")
            cmd_list = ["1", "2", "yes", "no"]
            cmd = getcmd(cmd_list)

            if cmd=="1" or cmd =="yes":
                nicePrint("You pick up the hook with the fish.")
                print()
                river_searched = True
                items.update({"fish and hook":"a large fishing hook with a fish still attached"})
                sneak_around(items)
            elif cmd=="2" or cmd =="no":
                nicePrint("You leave the fish and hook in the mud")
                sneak_around(items)
            else:
                nicePrint("You can not do that, try something else.")
                getcmd(cmd_list)
    else:
        
        nicePrint("You can not do that, try something else.")
        getcmd(cmd_list)


#Game intro.
def intro():
    skipIntro = input(
        """Press 's' to skip intro or any other key to continue.""")
    if skipIntro.lower() == "s":
        print("Skipping intro.")
        start(items)
    else:
        input("Press enter.")
        time.sleep(2)

        nicePrint("""Its still raining, after two days on the road it is still rainig.
        The edges of your hat are like waterfalls and your traveling clothes are damp, 
        but still you never cursed the rain. """)
        print("\n")
        input("Press enter.")

        time.sleep(1)

        nicePrint("""The rain has washed away your tracks and scent from the road and kept the 
        merchants men and dogs at bay""")
        time.sleep(1)
        print("\n")
        input("Press enter.")

        nicePrint("""You press your hand against your pocket, just to make sure that the prize has not
        dissapeared.
        Still there, almost warm to the touch. 
        Or is it the thought of the fat bag of gold Crowns that await you in Altdorf?""")
        time.sleep(1)
        print("\n")
        input("Press enter.")

        time.sleep(1)
        nicePrint("""You lost a couple of friends on this job but, that only means that the reward is all yours.
        Hans and Ulma knew what they were getting themselves into
        you mourn more for the real traveling papers that Ulma was carrying.
        You always thought that running was the most important skill for a thief,""")
        time.sleep(1)
        print()

        nicePrint("running away.")
        time.sleep(1)
        print("\n")
        input("Press enter.")

        nicePrint("""You are now in a race against time, the employers were
        explicit, they need their prize quickly.
        Now the city of Altdorf and a small fortune is but a days travel away. 
        You shake the cold and press on as the lights by the road glimmer in the rainy night""")
        time.sleep(1)
        print("\n")
        input("Press enter.")

        nicePrint("Following the muddy road you approach the lights.")
        time.sleep(1)
        print("\n")
        print("By Ranald's curse!")

        nicePrint(""" You stop dead in your tracks.
        You recognize the building by the side of the road.
        It is the road Wardens outpost!""")
        print("\n")
        input("Press enter.")
        start(items)

#Start screen otpions
def start_screen_options():
    option = input(">>>")
    if option.lower() == "play":
        intro()
    elif option.lower() == "help":
        print("""\n How to play : type your input + enter, 
        sometimes you can enter commands that are not on the menu.
        Use your imagination and have fun! 
        'inventory' to view your inventory or 'q' to quit
        You can always type 'help' for help""")
        input("Press enter.")
        start_screen()
    elif option.lower() == "quit":
        print("You leave your fate in Sigmar's hands")
        print("Auf wiederzhn!.")
        try:
            sys.exit(1)
        except SystemExit as e:
            pass
    elif option.lower()=="credits":

        print("""Scenario by Radoš, Rastko, Nik""")
        print("A game by Nik.")
        input("Press enter.")
        start_screen()
    else:
        print("You can not do that, choose something else.")
        input("Press enter.")
        start_screen()

#Starting screen
def start_screen():
    colorama.init()
    print(Fore.RED+""",---.    .--.  ,-..-. .-..-.   .-.  .-. .-.,-.  ,--,   .-. .-. _______ 
| .-.\  / /\ \ |(||  \| | \ \_/ )/  |  \| ||(|.' .'    | | | ||__   __|
| `-'/ / /__\ \(_)|   | |  \   (_)  |   | |(_)|  |  __ | `-' |  )| |   
|   (  |  __  || || |\  |   ) (     | |\  || |\  \ ( _)| .-. | (_) |   
| |\ \ | |  |)|| || | |)|   | |     | | |)|| | \  `-) )| | |)|   | |   
|_| \)\|_|  (_)`-'/(  (_)  /(_|     /(  (_)`-' )\____/ /(  (_)   `-'   
    (__)         (__)     (__)     (__)       (__)    (__)             """+Style.RESET_ALL)

    print(Fore.YELLOW + "\t\t*******************************" +Style.RESET_ALL)
    print(Fore.YELLOW + "\t\t* A rainy night in Old World  *" +Style.RESET_ALL)
    print(Fore.YELLOW + "\t\t*******************************" +Style.RESET_ALL)
    print(Fore.YELLOW + "\t\t*           -Play-            *" +Style.RESET_ALL)
    print(Fore.YELLOW + "\t\t*           -Help-            *" +Style.RESET_ALL)
    print(Fore.YELLOW + "\t\t*           -Quit-            *" +Style.RESET_ALL)
    print(Fore.YELLOW + "\t\t*******************************" +Style.RESET_ALL)
    start_screen_options()



#start_screen()

