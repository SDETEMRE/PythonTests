groceries_list = ['Eggs', 'Milk', 'Rice']

groceries_list.append('Chicken')
groceries_list.extend( ('Beef','Oranges', 'Onion') )

print(len(groceries_list))
print(groceries_list)

groceries_list[-2] = 'Cherry'
print(groceries_list)

print('------------------------------')

numbers_list = [10, 20, 30, 40, 50, 60, 70, 80]

numbers_list[2:4] = [66,77]
print(numbers_list)