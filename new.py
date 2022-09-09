pin1=2345
guess_count=0
guess_limit=2
while guess_count<guess_limit:
      guess_pin=int(input("Enter pin: "))
      guess_count+=1
if guess_pin==pin1:
    print("Login!")
else:
    print("Check your pin again and try some other time!")


def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a, b):
    return a*b
def divide(a,b):
    return a/b
print("1.Add")
print("2.Sub")
print("3.Mult")
print("4.Div")
print("Enter choice to proceed with your calculations")
while True:
    choice=input("enter option:")
    if choice=="1":
        num1=int(input("enter num1:"))
        num2=int(input("enter num2:"))
        print(num1+num2)
        break
    elif choice=="2":
        num1=int(input("enter num1:"))
        num2=int(input("enter num2:"))
        print(num1-num2)
        break
    elif choice=="3":
        num1=int(input("enter num1:"))
        num2=int(input("enter num2:"))
        print(num1*num2)
        
        break
    elif choice=="4":
        num1=int(input("enter num1:"))
        num2=int(input("enter num2:"))
        print(num1/num2)
        break
    else:
        print("no more calculations")


color=["blue","green","yellow","pink","red"]
guess_limit=2
guess_count=0
while guess_count<guess_limit:
    guess_color=input("enter color:")
    guess_count+=1
    if guess_color==color[0]:
        print("correct!")
        break
    elif guess_color==color[1]:
        print("corect!")
        break
    elif guess_color==color[2]:
        print("coreect!")
        break
    elif guess_color==color[3]:
        print("coreect!")
        break
    elif guess_color==color[4]:
        print("corect!")
        break

    else:
     print("wait for another turn!")











