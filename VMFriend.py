# coding=utf-8
import sys
import os.path
from os import path
import time
import mido
import pandas as pd
import numpy as np
import subprocess
import atexit

# This came to life because I needed a quick way to try different algorithms to process MIDI signal
# between to specified devices. 
#                                                    
# CLI section          
# ------------------                                          
#
# This script is a CLI for managing multiple "virtual MIDI friend"
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

#Print system path for debug purpose
#print(sys.path)

# SKETCH DATA
FRIENDS_DATA = {'Name':[], 'INPUT':[], 'OUTPUT':[]}
V_M_FRIEND_LIST = []

algo_list = []

# DEFAULT TERMINAL TOOL
edit_tool = "gedit"   # You can use other things like nano or vim
subprocess_tool = "gnome-terminal"    # you can probably use other "terminals" here

# Main loop menu
def main_menu():
    main_loop = True
    try:
        while main_loop == True:
            algo_list = update_algo_list()
            print("")
            print("██╗   ██╗██╗██████╗ ████████╗██╗   ██╗ █████╗ ██╗  ")        
            print("██║   ██║██║██╔══██╗╚══██╔══╝██║   ██║██╔══██╗██║  ")        
            print("██║   ██║██║██████╔╝   ██║   ██║   ██║███████║██║   ")       
            print("╚██╗ ██╔╝██║██╔══██╗   ██║   ██║   ██║██╔══██║██║ ")     
            print(" ╚████╔╝ ██║██║  ██║   ██║   ╚██████╔╝██║  ██║███████╗   ")    
            print("  ╚═══╝  ╚═╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚══════╝  ")   
            print("")                                                             
            print("             ███╗   ███╗██╗██████╗ ██╗     ")                                
            print("             ████╗ ████║██║██╔══██╗██║       ")                              
            print("             ██╔████╔██║██║██║  ██║██║          ")                           
            print("             ██║╚██╔╝██║██║██║  ██║██║            ")                         
            print("             ██║ ╚═╝ ██║██║██████╔╝██║              ")                       
            print("             ╚═╝     ╚═╝╚═╝╚═════╝ ╚═╝                ")                     
            print("                                                   ")                   
            print("     ███████╗██████╗ ██╗███████╗███╗   ██╗██████╗         ")                 
            print("     ██╔════╝██╔══██╗██║██╔════╝████╗  ██║██╔══██╗          ")               
            print("     █████╗  ██████╔╝██║█████╗  ██╔██╗ ██║██║  ██║            ")             
            print("     ██╔══╝  ██╔══██╗██║██╔══╝  ██║╚██╗██║██║  ██║              ")           
            print("     ██║     ██║  ██║██║███████╗██║ ╚████║██████╔╝                ")         
            print("     ╚═╝     ╚═╝  ╚═╝╚═╝╚══════╝╚═╝  ╚═══╝╚═════╝                 ")
            print("                                            V0.1")
            # MENU
            print("\n    ---     ---     ---     ---     ---     ---")
            print("      Nbr of Virtual MIDI Friend Sketchs ["+str(nbr_of_sketch())+"]")                                        
            print("    ---     ---     ---     ---     ---     ---")
            print("\n-- [ OPTIONS ] --\n")
            print("\t[1] - Sketch a VMFriend\t\t[2] - List VMFriend")
            print("\t[3] - Edit\Add Algorithms\t[4] - List Algorithms")
            print("\t[5] - Show MIDI OUTput\t\t[6] - Show MIDI INput")
            print("\t[7] - Refresh\t\t\t[8] - Other Stuff")
            print("\n\t[9] - QUIT or Ctrl+c \t\t[!] - Summon a VMFriend")
            # CASE CHOICE
            case = input('\n[ --> ]  ')
            try:
                if (str(case) == "!"):
                    summon_vir_friend(algo_list) 
                elif (int(case) == 1):                    
                    sketch_vir_friend()
                elif (int(case) == 2):
                    list_friends()
                elif (int(case) == 5):
                    list_output()
                elif (int(case) == 6):
                    list_output()
                elif (int(case) == 3):
                    temp_cmd = [subprocess_tool, "--", edit_tool, "Algorythmz.py"]
                    subprocess.run(temp_cmd) 
                elif (int(case) == 4): # I should probably do a function here
                    print("\n-----[Algorythmz List]-----------------------")
                    for algo in algo_list:                    
                        print("\t[-] "+algo)
                    print("-----------------------------------------------")
                    input("Press Enter to Continue")
                elif (int(case) == 7):
                    os.system('clear')
                elif (int(case) == 8):
                    print("[ * ] - To be programmed")
                elif (int(case) == 9):
                    main_loop = False
                else:
                    print("\n[!] A error occure, sorry about that [!]")
            except:
                print("\n[!] A error occure, I should probably fix this ... [!]")
    except KeyboardInterrupt:
        print("Bye!")
        quit

# Count the number of Sketch
def nbr_of_sketch():
    i=0
    for obj in V_M_FRIEND_LIST:
        i=i+1
    return i    

# Load information about all VMFriends
def load_friends_data():
    temp_name = []
    temp_midi_out = []
    temp_midi_in = []
    for obj in V_M_FRIEND_LIST:
        temp_name.append(obj.v_name)
        temp_midi_out.append(obj.OUTPUT)
        temp_midi_in.append(obj.INPUT)
        FRIENDS_DATA['Name']=temp_name
        FRIENDS_DATA['INPUT']=temp_midi_in
        FRIENDS_DATA['OUTPUT']=temp_midi_out

# Return a list of algorithm from algorithmz.py
def update_algo_list():
    temp_cmd = ["python3", "Algorithmz.py", "list"]
    temp_list = str(subprocess.check_output(temp_cmd))[4:-4].replace("'", "").split(", ")
    #print(str(str(subprocess.check_output(temp_cmd))[4:-4]))
    return temp_list

# Print a table fo VMFriends
def list_friends():
    load_friends_data()
    df = pd.DataFrame(FRIENDS_DATA,columns=['Name', 'OUTPUT', 'INPUT'])
    print("\n-----[VMFriend List]-----------------------")
    print(df)
    print("---------------------------------------------")
    input("Press Enter to Continue")

# List detected MIDI OUTPUT port
def list_output():
    print("-----------------------------------------------")
    for device in mido.get_output_names() :
        print("[*] " + device)
    print("-----------------------------------------------")
    input("Press Enter to Continue")
# List detected MIDI INPUT port
def list_input():
    print("-----------------------------------------------")
    for device in mido.get_input_names() :
        print("[*] " + device)
    print("-----------------------------------------------")
    input("Press Enter to Continue")

# Sketching a VMFriend !
def sketch_vir_friend():
    print("\n[ -_- ] - Give a name to your friend : ")
    temp_name = input('[ --> ]  ')
    try:    
        V_M_FRIEND_LIST.append(virtual_friend(temp_name))
        for obj in V_M_FRIEND_LIST:
            if (obj.v_name == temp_name):
                obj.choose_port()
            else:
                pass
        print("[*] - News friend "+temp_name+" was created !\n")
    except: 
        print("[!] Sketch fail, something did not work [!]")

# Summon a VMFriend
def summon_vir_friend(algo_list):
    print("[ -_- ] - Summon who?", end="\t")
    # List available VMFriend
    i=1
    for obj in V_M_FRIEND_LIST:
        if (i == 1):
            print("["+str(i)+"] - "+obj.v_name)
            i=i+1
        elif (i > 1):
            print("\t\t\t["+str(i)+"] - "+obj.v_name)
            i=i+1
    temp_summ = input("[ --­> ]  ")
    
    print("[ -_- ] - With which algorythm?", end="\t")
    # List available algorythmz
    a=1
    for algo in algo_list:
        if (a == 1):
            print("["+str(a)+"] - "+algo)
            a=a+1
        elif (a > 1):
            print("\t\t\t\t["+str(a)+"] - "+algo)
            a=a+1
    temp_algo = input("[ --­> ]  ")

    print(str(algo_list[int(temp_algo)-1]))

    #Summoning (Executing a subprocess and passing data to Algorithmz.py)
    try:    
        temp_cmd = [subprocess_tool, "--", "python3", "Algorithmz.py", "run", str(V_M_FRIEND_LIST[int(temp_summ)-1].v_name), str(V_M_FRIEND_LIST[int(temp_summ)-1].OUTPUT), str(V_M_FRIEND_LIST[int(temp_summ)-1].INPUT), str(algo_list[int(temp_algo)-1])]
    except:
        print("[!] - Command not valid")
    try:
        subprocess.run(temp_cmd)
        print("[ * - . Summoning "+V_M_FRIEND_LIST[int(temp_summ)-1].v_name+". - *]")
    except:
        print("[ *!* ] - Subprocess fail to execute I think ...")

# - - - - VIRTUAL FRIEND CLASS DEFINITION - - - - - 
class virtual_friend:
    def __init__(self, n = ""):
        self.v_name = n
        self.INPUT = []
        self.OUTPUT = []

    def choose_port(self):
        # CHOOSE OUPUT 
        nbr_output = int(input("[?] - How many output port ?"))
        nbr_output_device = len(mido.get_output_names())
        print("[ "+self.v_name+" ] - -  CHOOSE OUTPUTS  - - ")
        for i in range (0, nbr_output):
            xx = 1   # Counter, ID
            for device in mido.get_output_names() :
                print("["+str(xx)+"] " + device)
                xx = xx + 1
            print("["+str(xx)+"] NONE")
            MIDI_OUT = input('[ --> ]  ')
            try:
                if (int(MIDI_OUT) <= nbr_output_device):
                    MIDI_OUT = mido.get_output_names()[int(MIDI_OUT)-1]
                    self.OUTPUT.append(MIDI_OUT)
                elif (int(MIDI_OUT) == nbr_output_device+1) :
                    self.OUTPUT.append("None")
                else:
                    print("\n[!] - No OUTPUT port selected")
            except:
                print("[!] - Invalid entry !")

        # CHOOSE INPUT
        nbr_input = int(input("[?] - How many input port ?"))
        nbr_input_device = len(mido.get_input_names())
        print("[ "+self.v_name+" ] - -  CHOOSE INPUTS  - - ")
        for i in range (0, nbr_input):
            xx = 1 # Counter, ID
            for device in mido.get_input_names() :
                print("["+str(xx)+"] "+device)
                xx = xx + 1
            print("["+str(xx)+"] NONE")
            MIDI_IN = input('[ --> ]  ')
            try:
                if (int(MIDI_IN) <= nbr_input_device):
                    MIDI_IN = mido.get_input_names()[int(MIDI_IN)-1]
                    self.INPUT.append(MIDI_IN)
                elif (int(MIDI_IN) == nbr_input_device+1) :
                    self.INPUT.append("None")
                else :
                    print("\n[!] - No INPUT port selected")
            except:
                print("[!] - Invalid entry!")

if __name__== "__main__":
    main_menu()
