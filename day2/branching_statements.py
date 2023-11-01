for i in range(0,5):
    print(i)
    if i==3:
        break # exits the loop
print('-------------------')

for i in range(1,8):
    if i == 3 or i == 4:
        continue # skips to the next iteration
    print(i)

print('-------------------')

for i in range(1,8):
    if i == 3 or i == 4:
        pass # if you will decide to implement later you may use pass it is abstraction
    print(i)
