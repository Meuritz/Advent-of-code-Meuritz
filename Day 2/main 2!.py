#funzione per controllare una linea
def line_checker(list1, error):
    
    line = list1

    #flags
    crescente = False
    decrescente = False
    difference = True
    error_set = error

    #iteration over the line
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
          if error_set:  
            break
          else:
              line.remove(line[x])
              line_checker(line, True)
              break

        if not (1 <= abs(line[x] - line[x + 1]) <= 3):
            if error_set:  
                difference = False
            else:
              line.remove(line[x])
              line_checker(line, True)
              break
            
    #if conditions are meet we increment the counter
    if (crescente ^ decrescente) and difference:
        return True
    else:
        return False

#main
f = open("input.txt", "r")

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


safe = 0

for x in data:
    result = line_checker(x, False)
    
    if result:
        safe += 1

print(safe)