Travelling=input("Yes or No:")
while Travelling=='Yes':
    num=int(input("No of People Travelling:"))
    for n in range(1,num+1):
        Name=input("Name:")
        age=input("Age:")
        Sex=input("Sex:")
        print(Name)
        print(age)
        print(Sex)

    Travelling=input("Forgot Someone:")    
