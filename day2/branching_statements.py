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
        pass # if you will decide to implement later you may use pass it is abstraction(you may use it in function
        #if statement class or method you may chck the below conditions )
    print(i)

def function():
    pass

if True:
    pass

class Class:
    def method(self):
        pass

    pass


