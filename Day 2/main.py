f = open("palle.txt", "r")

data = []

#retrive the data from the file
for line in f:
    line = line.strip()
    
    riga = []
    numero =""

    for i in line:
        
        if i.isdigit():
            numero += i
        else:
            riga.append(int(numero))
            numero = ""
    riga.append(int(numero))
    data.append(riga)

#check how many safe lines we have
safe = 0

#iterate the over the list that are stored in data
for line in data:
    
    #variables
    crescente = False
    decrescente = False
    difference = True

    #iterate over the line
    for x in range(len(line)-1):
        if line[x] > line[x+1]:
            decrescente = True

        elif line[x] < line[x+1]:
            crescente = True
        
        elif line[x] == line[x+1]:
            crescente = True
            decrescente = True
            
        #if both flag are true we break
        if crescente and decrescente:
            break

        if not (1 <= abs(line[x] - line[x + 1]) <= 3):
            difference = False

     
    #if conditions are meet we increment the counter
    if (crescente ^ decrescente) and difference:
        safe += 1

print(safe)
    
