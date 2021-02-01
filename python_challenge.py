"""Input your age. If you are 18 or over, print the message “You can vote”,
if you are aged 17, print the message “You can learn to drive”,
if you are 16, print the message “You can buy a lottery ticket”,
if you are under 16, print the message “You can go Trick-or-Treating”
Enter a random string, which includes only digits. Write a function sum_digits which will find a sum of digits in this string
Write a Python program to get the largest number from a list."""

age = int(input("Please input your age - "))

if age >= 18:
    print('You can vote')
elif age == 17:
    print('You can learn to drive')
elif age == 16:
    print('You can buy a lottery ticket')
else:
    print('You can go Trick-or-Treating')



def sum_digits(input_string):
    result = 0
    # Option 1
    # for digit in input_string:
    #     result += int(digit)

    # Option 2
    input_string = int(input_string)
    while input_string != 0:
        result += input_string % 10
        input_string //= 10

    return result

print (sum_digits('123456789'))

def max_number (my_list):
    max_num = my_list[0]
    for number in my_list:
        if number > max_num:
            max_num = number
    return max_num

print(max_number([199,2,222,4,56,656]))