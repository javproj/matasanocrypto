"""
    Hexadecimal <-> Decimal <-> Binary conversion functions
    Includes:
"""
import sys

#-----INIT VARS###
hexAlphas = {
    "a" : 10,
    "b" : 11,
    "c" : 12,
    "d" : 13,
    "e" : 14,
    "f" : 15
}

#Used for getting hex alphas values from their numerical equivalent
hexVals = {
    10 : "a",
    11 : "b",
    12 : "c",
    13 : "d",
    14 : "e",
    15 : "f"
}

#array holding letters to check against
alpha = ["a", "b", "c", "d", "e", "f", "A", "B", "C", "D", "E", "F"]

#counter
cnt = 0

#-----Functions####
def d2b(decimalIn, bits):
    """ Decimal to Binary function. Takes in a decimal string and a bits amount for output"""    
    #initialize remainder
    rem = 0
    
    #need to get the integer if fed a string
    dec = int(decimalIn)
    

    #string to store binary value
    binval = ""
    
    #fn for getting binary value
    while dec > 0:
        rem = dec % 2 #remainder
        dec = dec / 2
    
        binval += str(rem)

    #Need length of binval for appropriate output 
    binLength = len(binval) - 1

    #Depending on size of binval
    if len(binval) > bits:
        sys.exit("Requested bit output is greater than binary bit amount")
    else:
        padamt = bits - len(binval)    
        binval += "0"*padamt

    #Reverse binary string for appropriate value
    binval = binval[::-1]

    return binval

def h2b(hexIn):
    """Hexadecimal to Binary"""
    cnt = 0     #Reset counter just in case
    
    hbOut = ""  #initialize return value
    
    while cnt < len(hexIn):
        if hexIn[cnt] in alpha:    
            hbOut += d2b(hexAlphas[hexIn[cnt].lower()], 4)
        else:
            hbOut += d2b(hexIn[cnt], 4)
        cnt += 1            

    return hbOut

def b2d(binIn):
    """Binary to Decimal"""
    
    cnt = 0     #init counter    

    decVal = 0  #init return decimal value
    
    revbin = binIn[::-1] #Need to reverse input binary for fn

    while cnt < len(binIn):
        if int(revbin[cnt]) is 1:
            decVal += 2**cnt
    
        cnt += 1  #increment x

    return decVal

def d2h(dhIn):
    """Decimal to Hex"""
    
    #need to catch if it's a zero
    if dhIn is 0:
        return "0"
    
    #Convert to int
    dec = int(dhIn)

    #initialize remainder
    rem = 0

    #string to store hex value
    hexval = ""

    while dec > 0:
        rem = dec % 16
        dec = dec / 16
    
        if rem in hexVals:
            hexval += str(hexVals[rem])
        else:
            hexval += str(rem)

    #Reverse hexval to get appropriate value
    hexval = hexval[::-1]

    return hexval

def b2h(bhIn):
    """Binary to Hex"""
    
    hexOut = "" #init return string
    
    #first pad with zero's if input not multiple of 4 for clarity
    if (len(bhIn) % 4) != 0:
        cnt = 0                 #init cnt        
        t = bhIn[::-1]          #temp for padding
        t += "0"*(len(bhIn)%4)  #pad
        bhIn = t[::-1]          #reverse t for padded bhIn

    #Use b2d fn to get decimal value
    deciVal = b2d(bhIn)   

    #Now return hex using d2h
    return d2h(deciVal)

def h2d(inval):
    """Hex to Decimal"""
    return b2d(h2b(inval))

#-----/FUNCTIONS###
