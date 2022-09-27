from random import *
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
