def menu():
    print("0.Exit")
    print("1.Insert a new admin")
    print("2.Insert a student")
    print("3.Final grade")
    return

def adminInsert(admins, admin_pass):
    print("What is the new admin?\n")
    newAdmin = input()
    print("What is the password?\n")
    newPass = input()
    admins.append(newAdmin)
    admin_pass.append(newPass)
    print('\n')
    print(admins)
    print(admin_pass)
    return 


grade = []
user = input("Username: ")
password = input("Password: ") 

admins = ['John', 'Marry', 'Henry']
admin_pass = ['111', '222', '333']

if user not in admins :
    print("not found")
elif (password in admin_pass) and (admins.index(user) == admin_pass.index(password)) : 
    print("Welcome admin!")
    id=1
else:
    print("Wrong password")

while id == 1:
    menu()
    OptionSelected = int(input("Select an option: "))
    
    match OptionSelected:
        case 0:
            break
        case 1:
            adminInsert(admins,admin_pass)
    

        
    
    
