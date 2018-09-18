
def new_password(oldpassword,newpassword):
    if (oldpassword == newpassword)==False and len(newpassword) >=6 and any(i.isdigit() for i in newpassword):
        return True
    else:
        return False
new_password("test1234","test1234567")

