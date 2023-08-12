'''
Напишите код, который запрашивает число и сообщает является ли оно простым или составным. 
Используйте правило для проверки: «Число является простым, если делится нацело только на единицу и на себя». 
Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.
'''

def composite(number: int):
    if number & 1 == 0:
        return number == 2
    step = 3
    while step * step <= number and number % step != 0:
        step += 2
    return step * step > number

number: int = -1
while number < 0 or number > 100_000:
    number = int(input("Введите число от 0 до 100_000: "))
print(["Это составное число", "Это простое число"][composite(number)])