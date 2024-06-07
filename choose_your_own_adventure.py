name= input("Type your name:")
print("Welcome", name, "to this adventure!")
answer=input("You are on a dirt road,it has come to an end you can go to left and right,which side you wanna choose? ").lower()
if answer=="left":
    answer=input("You come to a river,you can walk arounnd it or swim across!Type walk to walk or swim to swim across it. ").lower()
    if answer=="swim":
     print("You swan across and were eaten by an alligator!")
    elif answer=="walk":
     print("you walkedor many miles,ran out of water and you lost the game!")
    else:
      print("Not a valid option.You lose.")
elif answer=="right":
  answer=input("You came to a bridge, it looks woobly,do you want to cross it or go back? Type cross/back" ).lower()
  if answer=="back":
   print("You go back nd lose.")
  elif answer=="cross":
    print("You cross the bridge and meet a stranger. Do you talk to them(Yes/no)?")
    if answer=="yes":
      print("You talk to the stranger they gave you gold. YOU WIN!")
    elif answer=="no":
      print("You ignore the stranger and they are offended and you lose.")
    else: 
     print("Not a valid option. You lose.") 
  else: 
    print("Not a valid option. You lose.")


