import re
def check(password):
    if re.fullmatch(r'[A-Za-z0-9@#$%^&+=]{8,}', password):
        return True
    else:
        return False