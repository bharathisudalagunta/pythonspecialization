'''Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages.
You can pull the hour out from the 'From' line by finding the time and then splitting the string a second time using a colon. 
From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008 
Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below. '''

#CODE:

name=input("ENTER FILE NAME:")
if(len(name)<1) : name="mb.txt"
h=open(name)
d={}
c=0
for line in h:
    if(not line.startswith('From')):
        continue
    line=line.split()
    if(line[0]=='From'):
        line=line[5].split(':')
        for hrs in line[0].split():
            if(hrs not in d):
                d[hrs]=1
            else:
                d[hrs]+=1
for key,value in sorted(d.items()):
    print(key,value)

#INPUT:ENTER FILE NAME:mb.txt


'''OUTPUT:

04 3
06 1
07 1
09 2
10 3
11 6
14 1
15 2
16 4
17 2
18 1
19 1'''
