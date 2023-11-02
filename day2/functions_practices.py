import numbers


def eligibleToVote (age:numbers, country:str):

    if age >= 18:
        print(f'eligibleToVote({age}, "{country}")')
    else:
        print('You are not eligible to vote!')


eligibleToVote(22,'USA')

eligibleToVote(17,'GER')

def elementsOfTwoLists(tuple1:tuple, tuple2:tuple):

    for x in range(0, len(tuple1)):
        if tuple1[x] in tuple2:
            print(tuple1[x])

elementsOfTwoLists((1,2,3,4,5),(4,5,6,7,8))


def oddOrEven(tup1 : tuple):
    even=0
    odd=0

    for x in range(0,len(tup1)):
        if tup1[x]%2 == 0:
            even += 1
        else:
            odd += 1
    print(f'There are {even} even numbers and {odd} odd numbers')


numbers = (1, 2, 3, 4, 5, 6, 7)
oddOrEven(numbers)

word = ('Anna','Java')
rev = (word[0][::-1])
print(rev)

def palindrome(tup : tuple):

    for x in range(0, len(tup)):

        if tup[x] == (tup[x][::-1]):
            print(tup[x])



words = ('Java', 'Anna', 'python', 'Cydeo', 'Level')
palindrome(words)