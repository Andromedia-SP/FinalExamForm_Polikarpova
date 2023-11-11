#INTRO TO IT 2nd COURSE
# Задача: найти второе наибольшее число в списке
def second_largest(numbers):
    first = 0
    second = 0
    for n in numbers:
        if n > first:
            first, second = n, first  
        elif first > n > second:
            second = n
    return second or None

print(second_largest([10, 4, 9, 4, 9, 10, 4]))
