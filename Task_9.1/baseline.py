#Условия задания
#Компьютер загадывает число от 1 до 100. Программа ищет число меньше чем за 20 попыток
   
#Метрика качества

#Результаты оцениваются по среднему количеству попыток при 10000 повторений. Необходимо добиться минимального количество попыток.

#Что практикуем

#Учимся писать хороший код на Python. Учимся работать с IDE. Учимся работать с GitHub.

#Поехали

import numpy as np

number = np.random.randint(1, 101) # загадываем число

s=0
n=1
count = 10

if number <= count:
    def predict_number(number):
        s = 0
        count_func = n
        while True:
            count_func +=1
            if predict_number == number:
                break
    print (f'"Ваше число: " {predict_number} , "мы нашли его за: " {count_func} "попыток!")
        
        
elif count < number <= count+10:
    def predict_number(number):
        s = 0
        count_func = n+10
        while True:
            count_func +=1
            if predict_number == number:
                break
    print (f'"Ваше число: " {predict_number} , "мы нашли его за: " {count_func} "попыток!")
        
        
elif count+10 < number <= count+20:
    def predict_number(number):
        s = 0
        count_func = n+20
        while True:
            count_func +=1
            if predict_number == number:
                break
    print (f'"Ваше число: " {predict_number} , "мы нашли его за: " {count_func} "попыток!")
        
        
elif count+20 < number <= count+30:
    def predict_number(number):
        s = 0
        count_func = n+30
        while True:
            count_func +=1
            if predict_number == number:
                break
    print (f'"Ваше число: " {predict_number} , "мы нашли его за: " {count_func} "попыток!")
        
        
elif count+30 < number <= count+40:
    def predict_number(number):
        s = 0
        count_func = n+40
        while True:
            count_func +=1
            if predict_number == number:
                break
    print (f'"Ваше число: " {predict_number} , "мы нашли его за: " {count_func} "попыток!")
        
        
elif count+40 < number <= count+50:
    def predict_number(number):
        s = 0
        count_func = n+50
        while True:
            count_func +=1
            if predict_number == number:
                break
    print (f'"Ваше число: " {predict_number} , "мы нашли его за: " {count_func} "попыток!")
        
        
elif count+50 < number <= count+60:
    def predict_number(number):
        s = 0
        count_func = n+60
        while True:
            count_func +=1
            if predict_number == number:
                break
    print (f'"Ваше число: " {predict_number} , "мы нашли его за: " {count_func} "попыток!")
        
        
elif count+60 < number <= count+70:
    def predict_number(number):
        s = 0
        count_func = n+70
        while True:
            count_func +=1
            if predict_number == number:
                break
    print (f'"Ваше число: " {predict_number} , "мы нашли его за: " {count_func} "попыток!")
        
        
elif count+70 < number <= count+80:
    def predict_number(number):
        s = 0
        count_func = n+80
        while True:
            count_func +=1
            if predict_number == number:
                break
    print (f'"Ваше число: " {predict_number} , "мы нашли его за: " {count_func} "попыток!")
        
        
elif count+80 < number <= count+90:
    def predict_number(number):
        s = 0
        count_func = n+90
        while True:
            count_func +=1
            if predict_number == number:
                break
    print (f'"Ваше число: " {predict_number} , "мы нашли его за: " {count_func} "попыток!")
        
        
else number > 90:
    def predict_number(number):
        s = 0
        count_func = n+90
        while True:
            count_func +=1
            if predict_number == number:
                break
    print (f'"Ваше число: " {predict_number} , "мы нашли его за: " {count_func} "попыток!")
    