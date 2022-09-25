def vstavka(spisok):
  element=input("Enter new element ")
  i=input("Введіть після якого індексу потріюно вставити новий елемент ")
  i=int(i)
  spisok.insert(i+1, element)
fruits = ['raspberry', 'strawberry', 'blueberry'] 
print("Початковий список: ")
print(fruits)
vstavka(fruits)
print("Список після функції: ")
print(fruits)
