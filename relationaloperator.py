age=int(input("Enter the age of person\t"))
if age>18:
    print("Person has write to vote")
    print("person can drive")
    print("person is adult")
elif age<18:
    print("cant dreive")
    print("Not eligible for vote")
    print("is child")
elif age==18:
    print("can drive")
    print("not elilgoble for vote")
else:
    print("You entered wrong choice")    