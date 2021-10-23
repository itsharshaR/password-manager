print("Welcome To Password Manager\n")
while(True):
    ch = int(input("Please Enter Your choice\n1.Show All Passwords\n2.Add New Password\n"))
    if(ch == 1):
        with open('db.txt','r') as fp:
            passs = fp.readlines()
            for i in passs:
                print(i,end='')
    elif(ch == 2):
        name = input("Please Name Of The Website Or Thing For Which Your Saving Password\n")
        uname = input("Please Enter Your Username\n")
        pwd = input("Please Enter Your Password\n")

        with open('db.txt','a+') as fp:
            fp.write(f'["{name}","{uname}","{pwd}"]\n')

