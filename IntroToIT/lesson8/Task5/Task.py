#INTRO TO IT 2nd COURSE
# Задача: сгенерировать список всех четных чисел до N
def generate_evens(n):
    return [i for i in range(1, n + 1) if i % 2 == 0] 
