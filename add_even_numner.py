### Adding Even Number 
#1 option
total = 0
for number in range(2, 101, 2):
    total += number
print(total)

#2 option
total2 = 0 
for number in range(1, 100):
    if number %2 == 0:
        total2 += number
print(total2)

