import sys
import time
import mido
                                                    
# Algorithmz section          
# ------------------                                          
#
# MIDI_OUT and MIDI_IN are two list of port. 
# Output are open as port1, port2, port3, port'n' ...
#
# Simply create a function inside the "algorithmzz" object and you will be able to
# summon a friend that will process the MIDI signal with that function.
#
# Use 'portx' to ouput signal and 'MIDI_IN[x]' to access the input source
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

class algorithmzz(object):

    # Test algorythm
    def test(self):
        for i in range (0, 5):
           print('This is a test !!', end='\r')
           time.sleep(2.5)

    # Algorithm that print the input signals of the first elements in the MIDI IN list
    def flood_me_input(self):
        try:
            while True:
                with mido.open_input(MIDI_IN[0]) as inport:
                    for msg in inport:
                        print(msg)
        except KeyboardInterrupt :
            pass
        return 0

    # Algorithm to control a KAOSSILATOR or a KAOSPAD from MIDI note
    # Use the first listed device for I/O, "port1" & "MIDI_IN[0]"
    # All notes received are converted to CC parameter for X and Y
    def KORG_KAOSS(self):
        # Basic CC Control
        msg_on = mido.Message('control_change', channel=0, control=92, value=127, time=0)
        msg_off = mido.Message('control_change', channel=0, control=92, value=0, time=0)
            # Transfering Note and velocity into X and Y value for the KAOSSILATOR PRO
        def send_note_to_kaoss(Val, Velo):
            msg_out_x = mido.Message('control_change', channel=0, control=12, value=Val)
            msg_out_y = mido.Message('control_change', channel=0, control=13, value=Velo)
            port1.send(msg_out_x)
            port1.send(msg_out_y)
            #print("[OUT] - " + str(msg_out_x), end="\r")
            #print("[OUT] - " + str(msg_out_y), end="\r")

        # Translate the signals from a MIDI to some CC for a KAOSSILATOR PRO
        while True:
            with mido.open_input(MIDI_IN[0]) as inport:
                for msg in inport:
                    try:
                        if (msg.type == 'note_on'):
                            port1.send(msg_on)
                            send_note_to_kaoss(msg.note, msg.velocity)
                            print("[IN] - "+str(msg), end="\r")
                        elif (msg.type == 'note_off'):
                            port1.send(msg_off)
                        else :
                            pass
                        print("[IN] - "+str(msg), end="\r")
                    except:
                        try:
                            if (msg.control > 0):
                                print("[IN] - "+str(msg), end="\r")
                        except:
                            pass

    # Control KAOSSILATOR & KP3 !!
    # Use channel 0 and 1 to assign device                    
    def KAOSS_AND_KP3(self):
        # Basic CC Control
        msg_on = mido.Message('control_change', channel=0, control=92, value=127, time=0)
        msg_off = mido.Message('control_change', channel=0, control=92, value=0, time=0)

        # Translate the signals from a MIDI note to CC for a KAOSSILATOR PRO and KP3
        while True:
            with mido.open_input(MIDI_IN[0]) as inport:
                for msg in inport:
                    try:
                        if (msg.type == 'note_on'):
                            if (msg.channel == 0):
                                port1.send(msg_on)
                                msg_out_x = mido.Message('control_change', channel=0, control=12, value=int(((msg.note-34)/93)*127))
                                msg_out_y = mido.Message('control_change', channel=0, control=13, value=msg.velocity)
                                port1.send(msg_out_x)
                                port1.send(msg_out_y)
                                print("[OUT] - " + str(msg_out_x), end="\r")
                                #print("[IN] - "+str(msg), end="\r")
                            elif (msg.channel == 1):
                                port2.send(msg_on)
                                msg_out_x = mido.Message('control_change', channel=0, control=12, value=int(((msg.note-34)/93)*127))
                                msg_out_y = mido.Message('control_change', channel=0, control=13, value=msg.velocity)
                                port2.send(msg_out_x)
                                port2.send(msg_out_y)
                                print("[OUT] - " + str(msg_out_x), end="\r")
                                #print("[IN] - "+str(msg), end="\r")
                            else:
                                pass
                        elif (msg.type == 'note_off'):
                            if (msg.channel == 0):
                                port1.send(msg_off)
                            elif (msg.channel == 1):
                                port2.send(msg_off)
                        else :
                            pass
                        #print("[IN] - "+str(msg), end="\r")
                    except:
                            pass




# - - - - - - - - - - - -  END OF ALGORITHMZ CLASS - - - - - - - - - - - -
# ------------------------------------------------------------------------

# Return a list of all algorithm in the algorithmzz class
def list_algo():
    algo_list = []
    for func in algorithmzz.__dict__:
        if (func.startswith("__")):
            pass
        else:
            algo_list.append(func)       
    return algo_list

# __main__ function for the summoning purpose
if __name__== "__main__":
    if (sys.argv[1] == "list"):
        print(list_algo())
    elif (sys.argv[1 == "run"]):

        # RETREVING SUMMONING SETTINGS
        VMF_NAME = sys.argv[2]
        algo = str(sys.argv[5])
        # Creating MIDI OUT list
        MIDI_OUT = []
        midi_out_list = sys.argv[3][1:len(sys.argv[3])-1].split(", ")
        for things in midi_out_list:
            MIDI_OUT.append(things[1:len(things)-1]) 
        # Creating MIDI IN list 
        MIDI_IN = []     
        midi_in_list = sys.argv[4][1:len(sys.argv[4])-1].split(", ")
        for thing in midi_in_list:
            MIDI_IN.append(thing[1:len(thing)-1])

        # Opening ports and creating list
        port_out = []
        print("------["+VMF_NAME+"]---------------------------------------------------")
        print("ALGORITHM : "+algo)
        print("MIDI OUTPUT : "+str(MIDI_OUT))
        print("MIDI INPUT : "+str(MIDI_IN))
        print("\n[ ! ] - Opening port ... .. .")

        # Opening port
        for i in range (0, len(MIDI_OUT)):
            try:
                globals()['port'+str(i+1)] = mido.open_output(MIDI_OUT[i])
                print("[*] - port"+str(i+1)+" is open with " + str(MIDI_OUT[i]))
                time.sleep(0.5)
            except:
                if MIDI_OUT[i] == "None":
                    print("[*] - No device specified for port"+str(i+1)+" (None)")
                else:
                    print("[*] - port"+str(i+1)+" failed to open with " + MIDI_OUT[i])
                time.sleep(0.5)
        print("\n[ ! ] - Lunching selected algorithm ... .. .\n")
        try:
            #Executing the selected algorithm
            algo_lib = algorithmzz()
            algorithme_du_moment = getattr(algo_lib, algo)()
        except:
            print("Error lunching algorithm, sorry about that ... .. .")
            pass
    else:
        pass



    exit()
