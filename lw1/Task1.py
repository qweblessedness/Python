a=int(input("Enter a: "))
while(a<1 or a>100):
  a=int(input("Enter a again: "))
b=int(input("Enter b: "))
while(b<1 or b>100):
  b=int(input("Enter b again: "))
if(a>b):
  X=a*b+1
elif a==b:
  X=25
else:
  X=(a-5)/b
print("Answer: ",X)
