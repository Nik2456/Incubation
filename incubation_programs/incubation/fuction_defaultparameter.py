def voting(age=20):
    if age<18:
        print("You are not able to vote")
    else:
        print("You are going to vote")


voting()
voting(25)
voting(15)
voting(18)