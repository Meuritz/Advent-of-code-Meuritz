import re

#clean the corrupted logs
def retrive_operations(log):
    x = re.findall(r"mul\(\d+,\d+\)|don't\(\)|do\(\)", log)
    return x

#do the mul operation
def mul(clean_input):
    
    result = 0
    flag = True

    for x in clean_input:
        
        if x == "don't()":
            flag = False

        elif x == "do()":
            flag = True
            continue

        if flag == True:
            numbers = re.findall(r"\d+", x)
            result += int(numbers[0])*int(numbers[1])
        
    return result

#main

#retrive the data from the file
f = open("unput.txt", "r")

data = f.read()
#data = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"

#close the file
f.close()

print(mul(retrive_operations(data)))

