##given two strings of equal length merge them into one string 
#assume the string doesnt have  a white space 

def zip(string1 , string2):
    s1 = []
    s2 = []
    s1[:] = string1
    s2[:] = string2
    output = ""
    for indx , char  in enumerate(s1):
        output+= char + s2[indx]        
    return output

print(zip("Dog","Cat"))