c_user=['Avi','Hari','jothi','Guna','lax']
n_user=['ram','Sai','AVI','JOTHI','Sugu']
cuser=c_user.lower()
nuser=n_user.lower()
for i in nuser:
    for j in cuser:
        if i==j:
            print(f'username {i} already present , please enter new username')
        else:
            print(f'username {i} is available')


