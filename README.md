# Virtual MIDI Friend
```bash
██╗   ██╗██╗██████╗ ████████╗██╗   ██╗ █████╗ ██╗  
██║   ██║██║██╔══██╗╚══██╔══╝██║   ██║██╔══██╗██║  
██║   ██║██║██████╔╝   ██║   ██║   ██║███████║██║   
╚██╗ ██╔╝██║██╔══██╗   ██║   ██║   ██║██╔══██║██║ 
 ╚████╔╝ ██║██║  ██║   ██║   ╚██████╔╝██║  ██║███████╗   
  ╚═══╝  ╚═╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚══════╝  

             ███╗   ███╗██╗██████╗ ██╗     
             ████╗ ████║██║██╔══██╗██║       
             ██╔████╔██║██║██║  ██║██║          
             ██║╚██╔╝██║██║██║  ██║██║            
             ██║ ╚═╝ ██║██║██████╔╝██║              
             ╚═╝     ╚═╝╚═╝╚═════╝ ╚═╝                
                                                   
     ███████╗██████╗ ██╗███████╗███╗   ██╗██████╗         
     ██╔════╝██╔══██╗██║██╔════╝████╗  ██║██╔══██╗          
     █████╗  ██████╔╝██║█████╗  ██╔██╗ ██║██║  ██║            
     ██╔══╝  ██╔══██╗██║██╔══╝  ██║╚██╗██║██║  ██║              
     ██║     ██║  ██║██║███████╗██║ ╚████║██████╔╝                
     ╚═╝     ╚═╝  ╚═╝╚═╝╚══════╝╚═╝  ╚═══╝╚═════╝                 
                                            V0.1
```
*This thing is still a draft / work in progress and is buggy.

Virtual MIDI friend is a quick prototyping environnemtn to experiment with algorithms processing MIDI signals. This project was born because I needed to find easy way to convert MIDI notes from any inputs into a series of control changes (CC) for the Korg KP3 and the KAOSSILATOR Pro. While I was programing it, I was wondering : what if I want to test different algorithms? Or what if I want to have multiple virtual MIDI "bots" at the same time? I would have to handle the MIDI IN and OUT each time if I start from scratch and run each script manually-ish. This is why I made the Virtual MIDI Friend, so I can manage multiple MIDI bots and experiment with their processing of the MIDI signal.

## How it works?
You first sketch a “friend”, which means giving it a name and choosing its inputs and outputs midi ports. You then write some functions to handle the MIDI signals passing trough your virtual MIDI friend. Finaly, you "summon" that friend with the chosen algorithm.

## Environnement
I create and run this script on ubuntu 19.10 and the VMFriend.py file use the gnome-terminale for "summoning" and gedit for algorithms editing. You can change the gedit to any text editor of your choice and you can also change de terminal used. In the VMFriend.py file there is a section for that :
```Python3
# DEFAULT TERMINAL TOOL
edit_tool = "gedit"   # You can use other things like nano, vim or your favorite code editor
subprocess_tool = "gnome-terminal"    # you can probably use other "terminals" here
```

#### `Warning!`
If you use another terminal environment you might need to adjust one line in the "summon_vir_friend" function to add some specific argument relative to your chosen terminal environment. The line you should change starts with "temp_cmd = " and are the subprocess arguments. You can look at python "subprocess" for more info.


## Dependencies
I use to run it with python3 and both file use mido, numpy & panda module and you should be able to install them easely like this :
```Python3
pip3 install mido
pip3 install numpy
pip3 install panda
```

## How to run
### 1- By using the CLI through MVFriend.py :
```
Python3 MVFriend.py
```
### 2- By directly summoning a friend like the following 
```bash
python3 Algorithmz.py NAME INPUT[] OUTPUT[] ALGORITHM
```
NAME : your VMFriend's name<br />
INPUT[] : a list of input devices<br />
OUTPUT[] : a list of output devices<br />
ALGORITHM : the selected algorithm.<br />

## Current Algorithms in the Algorithmz.py file
### Base:<br />
- <b>Test</b> : Print 5 time "This is a test" then close
- <b>Flood_me_input</b> : Print the input MIDI signals
- <b>MIDI_Through_Simple</b> : Pass the MIDI signle from one device to another
- <b>Micro_Randomize_Through</b> : Send a random note at a random velocity at random interval but sync with MIDI input
- <b>KORG_KAOSS</b> : Translate MIDI note to X, Y coordinate in CC Values. This was made to be able to send MIDI notes to the KORG KP3 and/or the KAOSSILATOR.

### Extra<br />
- <b>KAOSS_AND_KP3</b> : Same as KORG_KAOSS but you can control both at the same time. It uses channel 0 and 1 to route the signal to the specified machine.
- <b>RANDOM_VDRUM_TO_KORG</b> : Randomize MIDI signal in CC for Korg from MIDI drum, or any other MIDI instrument.

### To do:<br />
- <b>Clock_me</b> : Pass clock signal from IN to OUT

----------------------------------------------------
