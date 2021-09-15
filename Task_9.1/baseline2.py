import numpy as np


def random_predict (predict_number):
    number = np.random.randint(1, 101)
    
    #Для начала разделим список из 100 чисел на 10
    if number <=10:
        pre_number = range(1,11)
    elif 10 < number <=20:
        pre_number = range(11,21)
    elif 20 < number <=30:
        pre_number = range(21,31)
    elif 30 < number <=40:
        pre_number = range(31,41)
    elif 40 < number <=50:
        pre_number = range(41,51)
    elif 50 < number <=60:
        pre_number = range(51,61)
    elif 60 < number <=70:
        pre_number = range(61,71)
    elif 70 < number <=80:
        pre_number = range(71,81)
    elif 80 < number <=90:
        pre_number = range(81,91)
    elif number > 90:
        pre_number = range(91,101)
    
    
    predict_number = pre_number[0] #Присвоим искомому числу первую цифру списка
    
    
    while True: #Запускаем цикл поиска
        predict_number += 1
        if predict_number == number:
            break
        
        
    print(f"Загаданное число было {predict_number}")

random_predict (predict_number)
