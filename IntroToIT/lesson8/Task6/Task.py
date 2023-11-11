#INTRO TO IT 2nd COURSE
# Задача: вернуть строку в обратном порядке
def reverse_string(s):
    reversed_s = ''
    for char in s:
        reversed_s = reversed_s + char
    return reversed_s
