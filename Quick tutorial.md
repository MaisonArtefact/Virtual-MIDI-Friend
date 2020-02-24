# Quick Tutorial
### The basic steps to make this script work is: <br />
[ 1-<b>Sketch</b> a Virtual Midi Friend ] <br />
[ 2-<b>Summon</b> a Virtual Midi Friend ] <br />
<br />

#### The next example show how to show/print the MIDI message from a plugged MIDI instrument or a virtual instrument.
<br />

### The main menu <br />

```bash
-- [ OPTIONS ] --

        [1] - Sketch a VMFriend         [2] - List VMFriend
        [3] - Edit\Add Algorithms       [4] - List Algorithms
        [5] - Show MIDI OUTput          [6] - Show MIDI INput
        [7] - Refresh                   [8] - Other Stuff

        [9] - QUIT or Ctrl+c            [!] - Summon a VMFriend

[ --> ] 
```

<br />
[1] <b>Sketch a VMFriend</b> : Create a new VMFriend<br />
[2] <b>List VMFriends</b> : Show a list of ALL VMFriends <br />
[3] <b>Edit/Add Algorithms</b> : Open the Algorithms.py file in gedit (or any other text editor)<br />
[4] <b>List Alogorithms</b> : Show a list all algorithms in the file Algorithms.py<br />
[5] <b>Show MIDI OUTpout</b> : Show a list of all MIDI OUTput entity<br />
[6] <b>Show MIDI INput</b> : Show a list of all MIDI INput entity<br />
[7] <b>Refresh</b> : You might want to refresh after adding or edit some algorithms <br />
[8] <b>Other Stuff</b> : Does nothings ... .. .<br />
[9] <b>Quit</b> : Quit<br />
[!] <b>Summon a VMFriend</b> : To summon a VMFriend with a specific algorithm<br />
<br />

## [ 1-<b>Sketch</b> a Virtual Midi Friend ] <br />
I create a friend (option #1 from the main menu), I name it "Smith".

```bash
[ -_- ] - Give a name to your friend : 
[ --> ]  Smith  
```
<br />
I choose to have 1 output source and I choose the Midi Through.

```bash
[?] - How many output port ?1
[ Smith ] - -  CHOOSE OUTPUTS  - - 
[1] KAOSSILATOR PRO:KAOSSILATOR PRO MIDI 1 20:0
[2] Midi Through:Midi Through Port-0 14:0
[3] NONE
[ --> ]  2
```
<br />
I also choose to have 1 input source, then I choose my KAOSSILATOR PRO.

```bash
[?] - How many input port ?1
[ Smith ] - -  CHOOSE INPUTS  - - 
[1] KAOSSILATOR PRO:KAOSSILATOR PRO MIDI 1 20:0
[2] Midi Through:Midi Through Port-0 14:0
[3] NONE
[ --> ]  1
```
<br />
Et voilà!

```bash
[*] - News friend Smith was created !
```
<br />

### Confirm that everything is all right by listing my VMFriend (opt #2 on main menu) <br />
```bash
-----[VMFriend List]-----------------------
    Name                                   OUTPUT                                          INPUT
0  Smith  [Midi Through:Midi Through Port-0 14:0]  [KAOSSILATOR PRO:KAOSSILATOR PRO MIDI 1 20:0]
---------------------------------------------
Press Enter to Continue
```
<br />
This is useful went you have multiple VMFriends <br />

## [ 2-<b>Summon</b> a Virtual Midi Friend ] <br />
I will now need to choose which VMFriend and with which algorithm. In my case I only have one sketch so I choose my VMFriend Smith. <br />
```bash
[ -_- ] - Summon who?	[1] - Smith
[ --­> ]  1
```
Than I choose the "Flood Me Input" Algorithm.
```bash
[ -_- ] - With which algorithm?	[1] - test
			        [2] - flood_me_input
			        [3] - KORG_KAOSS
			        [4] - KAOSS_AND_KP3
[ --­> ]  2
```
Then a new terminal window open and I get flooded by the midi msg (all!) <br />
```bash
------[Smith]---------------------------------------------------
ALGORITHM : flood_me_input
MIDI OUTPUT : ['Midi Through:Midi Through Port-0 14:0']
MIDI INPUT : ['KAOSSILATOR PRO:KAOSSILATOR PRO MIDI 1 20:0']

[ ! ] - Opening port ... .. .
[*] - port1 is open with Midi Through:Midi Through Port-0 14:0

[ ! ] - Lunching selected algorithm ... .. .

clock time=0
clock time=0
clock time=0
clock time=0
clock time=0
clock time=0
clock time=0
clock time=0
...
```
