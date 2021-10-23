import pwnedpasswords

def check(pwd):
    pwd_con = pwnedpasswords.check(pwd)
    if(pwd_con == 0):
        return True
    else:
        return False