'''Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form: X-DSPAM-Confidence: 0.8475 
Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below. 
Do not use the sum() function or a variable named sum in your solution.when you are testing below enter mbox-short.txt as the file name. '''


#CODE:
fname = input("Enter file name:") 
fh = open(fname) 
C=0 
s=0.0 
for line in fh: 
    if line.startswith("X-DSPAM-Confidence:"): 
        text= line 
        pos=text.find(":") 
        post=1
        val=text[pos+1:]
        val=float(val) 
        C=C+1 
        s=s+val
print("Average spam confidence:",(s/float(C))) 


#INPUT:mbox-short.txt

#OUTPUT:0.750718518519 
