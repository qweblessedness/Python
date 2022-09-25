number_fib1 = 0
number_fib2 = 1
 
n = input("Номер ряда Фибоначчи: ")
n = int(n)
index = 0
line = ['0', '1']

if n + 2 <= 1: 
    line = ['0']
elif n + 2 == 2:
    line = ['0','1']

while index < n - 2:
    sum_fib = number_fib1 + number_fib2
    number_fib1, number_fib2 = number_fib2, sum_fib
    index += 1
    line +=str(number_fib2) 

print("Последовательность чисел Фибоначчи", line)
