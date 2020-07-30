''' Write code using find() and string slicing (see section 6.10) to extract the number at the end of the line below. 
Convert the extracted value to a floating pointnumber and print it out. '''

#CODE:

text="X-DSPAM-Confidence: 0.8475" 
pos=text.find(":")
while(text[pos]==""): 
    pos+=1 
val=text[pos+1:] 
print(float(val)) 


#Output:0.8475
