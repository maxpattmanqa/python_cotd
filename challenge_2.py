# Challenge Write a function that accepts a sentence and calculates the number of upper case letters and lower case letters 


def find_num_cases(input):
    num_upper_case = 0
    num_lower_case = 0
    words = input
    chars = []
    chars[:] = words
    
    for char in chars:
        if(char.islower()):
            num_lower_case+=1
        elif(char.isupper()):
            num_upper_case+=1
        else: # probably whitespace
            continue

    print("UPPER CASE : " + str(num_upper_case)+'\n')
    print("LOWER CASE : " + str(num_lower_case)+'\n')



find_num_cases("Hello world!")