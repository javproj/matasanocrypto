""" 

    Take in 2 hex strings of equal length, XOR, then return hex
    @author: Jesse Vazquez


"""
import sys
import bhd_fns

####
def xorChars(char1, char2):
    """Function that takes in 2 characters (0/1) and returns appropriate
    XOR value"""
    if char1 == char2:
        return "0"
    else:
        return "1"
        
def xor(string1, string2):
    """Function that will XOR 2 strings and return the formatted 
        hex of the XOR"""
    #Exit if not the same length    
    if len(string1) != len(string2):
        sys.exit("Strings not of equal length")
        
    #Now we need to get binary of the hex string
    s1binary = ""
    s2binary = ""

    cnt = 0     #counter

    #loop through and get binary values
    while cnt < len(string1):
        s1binary += bhd_fns.h2b(string1[cnt])
        s2binary += bhd_fns.h2b(string2[cnt])
        cnt += 1

    xorstr = ""     #return string

    cnt = 0     #reset counter

    #Get xor values and append to xorstr
    while cnt < len(s1binary):
        xorstr += xorChars(s1binary[cnt], s2binary[cnt])
        cnt += 1

    hexOut = ""     #init return string

    cnt = 0     #reset again

    while cnt < len(xorstr):
        hexOut += bhd_fns.b2h(xorstr[cnt:cnt+4])
        cnt += 4

    #print the hex now    
    return hexOut
####
