import re
password = input("Please Enter Your Password Which You Whats To Check\n")
if re.fullmatch(r'[A-Za-z0-9@#$%^&+=]{8,}', password):
    print("Your Password Is Safe You Can Use It")
else:
    print("Your Password Is Not Safe You Can't Use It")