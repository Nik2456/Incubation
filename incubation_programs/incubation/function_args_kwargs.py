def student(*args,**kwargs):
    print("role_no=",args)
    print(kwargs)

    for arg in args:
        print("Roll no=",arg,kwargs)

student(1,5,7,9,name="Anil",age=25,ht=3)

