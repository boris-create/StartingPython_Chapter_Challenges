# Age Classifier

# ask user to enter persons age
person = int(input("What is your age? "))
# display whether person is an 'infant, child, teenager, or an adult'
if person <= 1:
    print("You are an infant.")
elif person > 1 and person < 13:
    print("You are a child.")
elif person >= 13 and person < 20:
    print("You are a teenager.")
else:
    print("You are an adult.")
