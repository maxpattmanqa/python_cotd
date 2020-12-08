
def challenge1(string):
    string_as_list  = list(string.split(' '))
    string_as_list.sort()
    output = []


    for word in string_as_list:
        if word not in output:
            output.append(word)
        
    print(output)
    return

challenge1("hello world and practice makes perfect and hello world again")