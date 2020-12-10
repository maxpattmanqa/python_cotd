##given two strings of equal length merge them into one string 
#assume the string doesnt have  a white space 

def zip(string1 , string2):
    s1,s2,output = [],[],""
    s1[:], s2[:] = string1,string2
    for indx , char  in enumerate(s1):
        output+= char + s2[indx]        
    return output

print(zip("Dog","Cat"))