import math
from random import *
def function(a,b):
  Z=(math.sqrt(2)-math.sqrt(3*a))/(2*b)
  print("Z= ",Z);
def computer(num):
  com_num=randint(1, 100)
  while True:
   if(num<com_num):
    print("Моє чісло більше")
    num=int(input("Enter new number n: "))
   elif(num>com_num):
    print("Моє чісло менше")
    num=int(input("Enter new number: "))
   else:
    print("Ви вгадали")
    break
n=int(input("Enter n: "))
m=int(input("Enter m: "))
function(n,m)
computer(n)
