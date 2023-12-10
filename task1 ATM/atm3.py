from ast import While


class ATM:
    def __init__(self,balance):
        self.balance= balance
        
    def history(self):
       history=[]
       for i in history:
           if i > 0:
             print('printing transaction history')
             print(history)
           else:
             print('NO TRANSACTION HISTORY')

    def deposit(self):
       x = int(input('how many times: '))
    
       while x > 0:
          x=x-1
          amount= float(input('enter deposit amount: '))
          self.balance += amount 
          self.history.append('your deposit{amount} , your{balance}')
          print(f'deposit sucess{amount}. your balance{self.balance}')
        
    def withdraw(self):
       x = int(input('how many times: '))
    
       while x > 0:
         x=x-1
         amount= float(input('enter withdraw amount: '))
         self.balance -= amount 
         self.history.append('your deposit{amount} , your{balance}')
         print(f'withdraw sucess{amount}. your balance{self.balance}')
      
    def transfer(self):
        id=input("enter user id to transfer amount :") 
        amount=input("enter amount to transfer :")
        self.balance -= amount 
        self.history.append('your deposit{amount} , your{balance}')
        print("Amount {amount} transfered sucessfully to {id} ")
        
        print(f'deposit sucess{amount}. your balance{self.balance}')
        
         
        
    def check_balance(self):
      print('YOUR ACCOUNT BALANCE...')
      print(self.balance)
a=ATM(0)        
        
class menu:
 def display_menu(self):
    print('\n ATM MENU')
    print('1. Transaction History')
    print('2.Withdraw')
    print('3.Deposit')
    print('4.Transfer')
    print('5.Quit')
m=menu()       
        
        
class main:
  def create_user(self,user_id,pin):
    def __init__(self): 
      users = {user_id , pin}
      if user_id and pin in users:
       print('user created sucessfully')
      else:
       print('invalid')
       
       
       
  def checker(self,user_id_checker,pin_checker,user_id,pin):
      if user_id_checker == user_id and pin_checker == pin:
          print('WELCOME TO ATM')
          value = True
          while True:
           m.display_menu()
           choice= input('enter your choice(1-5) ')
           if choice == '1':
             a.history()
           elif choice =='2':
             a.withdraw()
           elif choice =='3':
             a.deposit()
           elif choice =='4':
            a.transfer()
           elif choice =='5':
             print('exiting ATM.')
             break
           else:
            print('invali2d choice')
      else:
          print("invalid user")
      
         
      
        
       
    
        
        

x=main()


user_id =input("Enter user_id creating user: ")
pin     = input("Enter pin :")
x.create_user(user_id , pin)


  
user_id_checker = input("Enter your user id : ")
user_pin        = input('Enter user PIN : ')
x.checker(user_id_checker ,user_pin,user_id,pin) 

       
a.deposit()
a.withdraw()
a.history()

