#vacccuum world problem- simple reflex agent

fileopen=open('input.txt','r')
fileout=open('output.txt', 'w')
i=1
newline=""
with fileopen as inputfile:
	for line in inputfile:
		location, status = line.split(",")
		if i>1:
			newline="\n"
		else:
			newline=""
		if status[:-1] == 'Dirty' or status[:-1]=='Dirt':
			fileout.write(newline+"Suck")
		elif location == 'A':
			fileout.write(newline+"Right")
		elif location == 'B':
			fileout.write(newline+"Left")
		i+=1