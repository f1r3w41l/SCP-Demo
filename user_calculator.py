print("Give me two numbers Sir/Mam ")
flag_a=1
flag_b=1
while flag_a==1 or flag_b==1:
    a=input("Input the first number here - ")
    if a.isnumeric():
        x=int(a)
        flag_a=0
    else:
        print("Enter a INTEGER NUMBER for A")
    b=input("Input the second number here - ")
    if b.isnumeric():
        x=int(b)
        flag_b=0
    else:
        print("Enter a INTEGER NUMBER for B")
        
print(f"This is your addition - {int(a)+int(b)} ")
