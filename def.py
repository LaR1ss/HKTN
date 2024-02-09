print("Write your name please")
a = input()
print("Thank you! Now please write your age")
age = int(input())

def hello(a, age):
    print(f'Hello {a}!')
    print(f'Your age is {age}')

hello(a, age)