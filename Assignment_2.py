'''

#Task_1: Check if a number is even or odd

num =int(input('Enter a number to check even or odd: '))

if (num%2 ==0):
    print(num,'is an even number.')
else:
    print(num,'is an odd number.')
'''

#Task_2: Sum of integers from 1 to 50
sum=0
for x in range(1,51):
    sum=sum+x
print('The sum of numbers from 1 to 50 is:',sum)