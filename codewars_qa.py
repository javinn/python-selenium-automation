#  Homework 5-4

def over_the_road(address, n):
    if address % 2 == 1:
        return (n - (address - 1) // 2) * 2
    else:
        return (n - address // 2) * 2 + 1


def unique_letter(input_string):
    for char in input_string:
        if input_string.lower().count(char.lower()) == 1:
            return char
    return 'xoxoxo'


print(unique_letter('Amazon'))

def solve(n):

    if 0 <= n <= 18:
        return n
    n_str = str(n)
    number_1 = '5'*(len(n_str)-1)
    number_2 = str(n - int(number_1))

    digital_sum = 0
    for digs in number_1 + number_2:
        digital_sum += int(digs)

    return digital_sum