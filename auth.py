class auth:
    def __int__(self):
        self.name=none
        self.user_name=none
        self.password=none
        self.email_id=none

    def register(self):
        self.name= input ("enter full name:")
        self.user_name= input ("enter username:")
        self.password= input ("enter password:")
        self.email_id= input ("enter email_id:")
        try:
            with open(self.user_name + ".txt",'r') as data:
                print("user_name already exist")
        except FileNotFoundError:
            with open(self.user_name + ".txt",'w') as data:
             data.write(self.name + "\n" + self.user_name + "\n" + self.password + "\n" + self.email_id + "\n")

             print("user register successfully")
    def login(self): 
        self.user_name= input ("enter username:")
        self.password= input ("enter password:")
        
        try:
            with open(self.user_name + ".txt",'r') as data:
                Newdata =data.read()
                Newdata=Newdata.split('\n')
                self.name=Newdata[0]
                self.user_name=Newdata[1]
                self.password=Newdata[2]
                self.email_id=Newdata[3]
                if self.password == self.password:

                    print("user logged")
                    print(f"name :{self.name}")
                    
        except FileNotFoundError:
            print("user not found")
obj= auth()

while(True):
    print("enter 1 for new register ")   
    print("enter 2 for login ")   
    print("enter 3 for exit...! ") 
    choice = int(input("enter your choice :"))
    match(choice):
        case 1:
            obj.register()
            break
        case 2:
            obj.login()
            break
        case 3:
            print("exiting.....!")
            break
        case _:
            print("invalid choice")  


