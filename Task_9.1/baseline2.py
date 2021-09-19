
#Условия задания

#Компьютер загадывает целое число от 1 до 100, и нам его нужно угадать. Под «угадать» подразумевается «написать программу, которая угадывает число».
#Алгоритм учитывает информацию о том, больше ли или меньше случайное число нужного нам числа.
#Представлен шаблон baseline из скринкаста.

#Метрика качества

#Результаты оцениваются по среднему количеству попыток при 10000 повторений. Необходимо добиться минимального количество попыток.

import numpy as np

def number_guessing(number):
    left = 1
    right = 101
    count = 0
    while True:
        count += 1
        predict = (left+right) // 2  # предполагаемое число
        if predict == number:
            break
        elif predict < number:
            left = predict + 1
        elif predict > number:
            right = predict - 1
    print(f"Загаданное компьютером число {number}, угаданное {predict}")
    return count  # выход из цикла, если угадали



def score_game(game_core):
    """Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число"""
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы эксперимент был воспроизводим!
    random_array = np.random.randint(1, 101, size=1000)
    for number in random_array:
        count_ls.append(game_core(number))
    score = np.mean(count_ls)
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return score

score_game(number_guessing)