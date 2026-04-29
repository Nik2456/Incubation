#Apposite face dice value

def opp_face_value(n):
    if n==1:
        return 6
    elif n==2:
        return 5
    elif n==3:
        return 4
    elif n==4:
        return 3
    elif n==5:
        return 2
    else:
        return 1
print(opp_face_value(1))
