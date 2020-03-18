#Robert Lapore
#CPS-3320 Python Programming Project 1

def getCount():
	if hsname == "union high school":
		whatInstrument = inst.index(instname)
		union[whatInstrument] += 1
	if hsname == "linden high school":
		whatInstrument = inst.index(instname)
		linden[whatInstrument] += 1
	if hsname == "hillside high school":
		whatInstrument = inst.index(instname)
		union[whatInstrument] += 1

#Get info from user
instname = input("Please enter an instrument name: ").lower()
hsname = input("Please enter the high school name: ").lower()

inst = ["piano","guitar", "violin", "voice", "saxophone"]
schools = ["union high school", "linden high school", "hillside high school"]

#array counter for union
union = [0,0,0,0,0]
#array counter for hillside
hillside = [0,0,0,0,0]
#array counter for linden
linden = [0,0,0,0,0]

#if in both lists high school and inst
#whatInstrument matches retrieves the index from name of the instrument
# HINT: union = ["pianoCount","guitarCount", "violinCount", "voiceCount", "saxophoneCount"]
if instname in inst and hsname in schools:
   getCount()
else:
    print("Invalid instrument or high school. Please try again. ")
    getCount()

#keeprunning allows the program to keep running
keepRunning = input("Are there any more students? y/n: ").lower()
while keepRunning == "y":
    instname = input("Please enter an instrument: ").lower()
    hsname = input("Please enter the high school name: ").lower()
    if instname in inst and hsname in schools:
        if hsname == "union high school":
            whatInstrument = inst.index(instname)
            union[whatInstrument] += 1
        if hsname == "linden high school":
            whatInstrument = inst.index(instname)
            linden[whatInstrument] += 1
        if hsname == "hillside high school":
            whatInstrument = inst.index(instname)
            hillside[whatInstrument] += 1
    keepRunning = input("Are there any more students? y/n: ").lower()
    if keepRunning == "n":
        break
#If user chooses to end the program, print the results
if keepRunning == "n":
#prints students with instrument
#whatIndex matches the index of the school array with the index of the instrument name, therefore returning the name of the instrument for the number of students
    for i in union:
        if i > 0:
            whatIndex = union.index(i)
            print("There are ", i, " students at union high school that play ", inst[whatIndex])
    for i in linden:
        if i > 0:
            whatIndex = linden.index(i)
            print("There are ", i, " students at linden high school that play ", inst[whatIndex])
    for i in hillside:
        if i > 0:
            whatIndex = hillside.index(i)
            print("There are ", i, " students at hillside high school that play ", inst[whatIndex])