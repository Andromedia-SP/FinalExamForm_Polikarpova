#INTRO TO IT 2nd COURSE

# Задача 14: Сумма двух наибольших элементов списка. 
# Правильное решение :)
def not_wrong_sum_of_two_largest(lst):
    return sum(sorted(lst)[-2:])
