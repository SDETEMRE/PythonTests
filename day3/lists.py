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

print('------------------------------')

nums = []
for x in range(1,51):
    nums.append(x)
print(nums)

print('------------------------------')

divisible_by_5 = []

for x in nums:
    if x % 5 == 0:
        divisible_by_5.append(x)

print(divisible_by_5)

divisible_by_5 = [x for x in nums if x%5 == 0]

print(divisible_by_5)