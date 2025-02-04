def again():
    print("do you want to play again")
    print("1 for play again")
    print("2 for end")
    r=int(input("enter a number"))
    if(r==1):
        happy()
    if(r==2):
        print("THE END")
def happy():
    print("jungle game")
    print("enter 1 for left")
    print("enter 2 for right")
    a=int(input("enter a number"))
    if(a==1):
        print("enter 1 for left")
        print("enter 2 for right")
        b=int(input("enter a number"))
        if(b==1):
            print("GAME OVER")
        if(b==2):
            print("animals")
            print("GAME OVER")
    if(a==2):
        print("enter 1 for left")
        print("enter 2 for right ")
        c=int(input("enter a number"))
        if(c==1):
            print("enter 1 for help")
            print("enter 2 for no help")
            d=int(input("enter a number"))
            if(d==1):
                print("WIN")
            again()
            if(d==2):
                print("LOSE")
        if(c==2):
            print("GAME OVER")
happy()

