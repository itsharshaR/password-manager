import pwnedpasswords

pwd = input("Please Enter Your Password To Check Wheather Its Leaked Or Not")
pwd_con = pwnedpasswords.check(pwd)

if(pwd_con == 0):
    print("Your Password Is safe To Use")
else:
    print("Your Password Is Been Leaked On Web")