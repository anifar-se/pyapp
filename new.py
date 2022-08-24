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









