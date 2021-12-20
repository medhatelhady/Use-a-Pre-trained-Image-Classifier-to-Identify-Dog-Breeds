dogs_set = set()
with open('dognames.txt', 'r') as file:
    for line in file:
        dogs_set.add(line.strip())
        
print(dogs_set)