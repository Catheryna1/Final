# -*- coding: utf-8 -*-
"""
Created on Wed Jun  9 04:50:35 2021

@author: Catheryna
"""

import random
import csv
import matplotlib.pyplot as plt

class Bank():
    def __init__(self):
        pass
class Accounts(Bank):
    def __init__(self, first_name, last_name, account_ID = "", active = 1, balance = 0):
        Bank.__init__(self)
        self.first_name = first_name
        self.last_name = last_name
        self.account_ID = account_ID
        self.active = active
        self.balance = balance
    def print_INDIVIDUAL(self):
        pass
    def print_All(self):
        pass
class Savings(Accounts):
    def __init__(self):
        pass
    def check_account(self, search_ID):
        csv_file = csv.reader(open('savings Account.csv', 'r'), delimiter = ',')
        for row in csv_file:
            if search_ID == row[2]:
                print('Account found')
                
    def print_INDIVIDUAL(self,search_ID):
        data = total_accounts
        file = open('Savings Account Update.csv', 'w', newline = '')
        with file:
            write = csv.writer(file)
            write.writerows(data)
            
        print(total_accounts)
        
        table = []
        csv_file = csv.reader(open('Savings Account Update.csv', 'r'), delimiter = ',')
        flag = False
        for row in csv_file:
            if search_ID == row[2]:
                table.append(row)
                print()
        if flag == False:
            print('Account not found. \n')
            
    def print_ALL(self):
        table = []
        total_accounts.sort(key = lambda total_accounts: total_accounts[1])

        for row in total_accounts:
            table.append(row)
        print()   
    def withdrawl(self, total_account, user_acount_ID, user_withdraw):
        flag = False
        for account in total_accounts:
            if account[2] == user_account_ID and account[4] == True and account[3] >= user_withdraw:
                account[3] -= user_withdraw
                print(account)
                flag = True
        if flag == False:
            print('Incorrect information or account not found.')
    def deposit(self,total_accounts, user_account_ID, user_deposit):
        flag = False
        for account in total_accounts:
            if account[2] == user_account_ID and account[4] == True:
                new_balance = account[3] + user_deposit
                account[3]= new_balance
                print(account)
                flag = True
        if flag == False:
            ('why.')
    def plot_all(self, total_accounts):
        data = {}
        for account in total_accounts:
            data[account[2]] = account[3]
        account_ids = list(data.keys())
        account_bal = list(data.values())
        plt.bar(account_ids, account_bal, color = 'green',width = 0.6)
        plt.xlabel('Account IDs')
        plt.ylabel('Balance')
        plt.title('Savings accounts')
        plt.show()
        
    def close_account(self, total_account, user_account_ID):
        flag = False
        for account in total_account:
            if account[2] == user_account_ID and account[4] == True:
                account[4] = False
                flag = True
                print('Account Closed')
        if flag == False:
            print('Incorrect information or account not found.')

class Checkings(Accounts):
    def __init__(self):
        pass
    
    def check_account(self, search_ID):
        csv_file = csv.reader(open('checkings Account.csv', 'r'), delimiter = ',')
        for row in csv_file:
            if search_ID == row[2]:
                print('Account found.')
    def print_INDIVIDUAL(self,search_ID):
        data = total_accounts_checkings
        file = open('Checkings Account Update.csv', 'w', newline = '')
        with file:
            write = csv.writer(file)
            write.writerows(data)
            
        print(total_accounts_checkings)
        
        table = [] 
        csv_file = csv.reader(open('Checkings Account Update.csv', 'r'), delimiter = ',')
        for row in csv_file:
            if search_ID == row[2]:
                table.append(row)
                print()
                
    def print_ALL(self):
        table = [] 
        
        total_accounts_checkings.sort(key = lambda total_accounts_checkings: total_accounts_checkings[1])
        
        for row in total_accounts_checkings:
            table.append(row)
        print()
        
    def withdrawl(self, total_accounts_checkings, user_account_ID, user_withdrawl):
        flag = False
        for account in total_accounts_checkings:
            if account[2] == user_account_ID and account[4] == True and account[3] >= user_withdrawl:
                account[3] == user_withdrawl
                print(account)
                flag = True
        if flag == False:
            print("Incorrect account information or account doesn't exist.")
    
    def deposit(self, total_accounts_checkings, user_account_ID, user_deposit):
        flag = False
        for account in total_accounts_checkings:
            if account[2] == user_account_ID and account[4] == True:
                new_balance = account[3] = user_deposit
                account[3] = new_balance
                print(account)
                flag = True
        if flag == False:
            print("Incorrect account information or account doesn't exist.")
    def plot_ALL(self, total_accounts_checkings):
        data = {}
        for account in total_accounts_checkings:
                data[account[2]] = account[3]
                
        account_ids = list(data.keys())
        account_bal = list(data.values())
        
        plt.bar(account_ids, account_bal, color = 'green', width = 0.6)
        plt.xlabel('Account IDs')
        plt.ylabel('Balance')
        plt.title('Savings accounts')
        plt.show()
    def close_account(self, total_accounts_checkings, user_account_ID):
        flag = False
        try:
            for account in total_accounts_checkings:
                if account[2] == user_account_ID and account[4] == True:
                    account[4] = False
        except:
            if flag == False:
                raise Exception("Incorrect account information or account doesn't exist.")
            
if __name__ == '__main__':
    total_accounts = []
    total_accounts_checkings = []
    savings_check = {}
    checkings_check = {}
    
    while True:
        print('(0) Make a savings account')
        print('(1) Make a checkings account')
        print('(2) Search for an account')
        print('(3) Search for all accounts')
        print('(4) deposit')
        print('(5) withdraw')
        print('(6) Graph balances')
        print('(7) Close account')
        print('(8) Exit')
        
        user_select = int(input("Select an option: \n"))
        
        if user_select == 0:
            print('OPening savings account')
            first_name = input('Enter first name: ')
            last_name = input('Enter last name: ')
            balance = float(input('Enter deposit: '))
            account_type = 'savings'
            savings_key = first_name + ':' + last_name + ':' + account_type
            
            user_select = first_name + ':' + last_name + ':' + account_type
        
            if savings_key in savings_check.keys():
                print('Account already exist.')
            else:
                savings_check[savings_key] = 1
                account_ID = ''
            
                ID = random.randint(0,9)
                account_ID = (account_ID + last_name + str(ID) + account_type)
                active = True
                account = [first_name, last_name, account_ID, balance, active, account_type]
                total_accounts.append(account)
            
                with open('Savings Account.csv', 'a', newline = '') as file:
                    savings_writer = csv.writer(file)
                    savings_writer.writerow(account)
                    file.close()
                print('Account created : ',first_name, last_name, 'Account ID:', account_ID)
                print(total_accounts)
        elif user_select ==1:
            print('Opening checking account')
            first_name = input('Enter first name: ')
            last_name = input('Enter last name: ')
            balance = float(input('Enter deposit: '))
            account_type = 'checkings'
            
            checkings_key = first_name + ':' + last_name + ':' + account_type
            
            if checkings_key in checkings_check.keys():
                    print('Account already exists.')
            else:
                checkings_check[checkings_key] = 1
                account_ID = ''
                
                ID = random.randint(0,9)
                account_ID = (account_ID + last_name + str(ID) + account_type)
                active = True
                account = [first_name, last_name, account_ID, balance, active, account_type]
                total_accounts_checkings.append(account)
                
                with open('Checkings Account.csv', 'a', newline = '') as file:
                    checkings_writer = csv.writer(file)
                    checkings_writer.writerow(account)
                    
                    file.close()
                    
                print('Account created:', first_name, last_name, 'Account Id: ', account_ID)
                
        elif user_select == 2:
            print('Search Account')
            account_type = input('Checkings or savings?')
            if account_type == "savings":
                search_ID = input('Enter account ID: ')
                obj = Savings()
                obj.check_account(search_ID)
                obj.print_INDIVIDUAL(search_ID)
                
            elif account_type == 'checkings':
                search_ID = input('Enter account ID: ')
                obj = Checkings()
                obj.check_account(search_ID)
                obj.print_INDIVIDUAL(search_ID)
            else: 
                print('Enter valid account type')
                
        elif user_select == 3:
            print('Search All accounts')
            account_type = input('Are the accounts checking or savings?')
            if account_type == 'savings':
                savings = Savings()
                savings.print_ALL()
                
            elif account_type == 'checkings':
                checkings = Checkings()
                checkings.print_ALL()
        elif user_select == 4:
            print('Deposit')
            account_type = input('checkings or savings?')
            if account_type == 'savings':
                user_account_ID = input("Enter ID: ")
                user_deposit = float(input('Enter a deposit amount: '))
                savings = Savings()
                savings.deposit(total_accounts, user_account_ID, user_deposit)
                
            elif account_type == 'checkings':
                user_account_ID = input("Enter ID: ")
                user_deposit = float(input('Enter a deposit amount: '))
                checkings = Checkings()
                checkings.deposit(total_accounts_checkings, user_account_ID, user_deposit)
            else:
                print('Enter valid account type')
                
        elif user_select == 5:
            print("Withdrawl")
            account_type = input('checkings or savings?')
            if account_type == 'savings':
                user_account_ID = input('Enter account ID: ')
                user_withdraw = float(input('Enter withdrawl amount: '))
                savings = Savings()
                savings.withdrawl(total_accounts, user_account_ID, user_withdraw)
                
            elif account_type == 'checking':
                user_account_ID = input('Enter account ID: ')
                user_withdraw = float(input('Enter withdrawl amount: '))
                checkings = Checkings()
                checkings.withdrawl(total_accounts_checkings, user_account_ID, user_withdraw)
            else:
                print("Enter valid account type")
        elif user_select == 6:
            print('Graphing accounts')
            account_type = input("Do you want to graph checkings or savings? ")
            
            if account_type == 'savings':
                savings = Savings()
                savings.plot_all(total_accounts)
            elif account_type == 'checkings':
                checkings = Checkings()
                checkings.plot_ALL(total_accounts_checkings)
            else:
                print('Enter valid acount type')
        elif user_select == 7:
            print("Close account")
            account_type = input('checkings or savings? ')
            if account_type == 'savings':
                user_account_ID = input("Enter account ID: ")
                savings = Savings()
                savings.close_account(total_accounts, user_account_ID)
            elif account_type == 'checkings':
                user_account_ID = input("Enter account ID: ")
                checkings = Checkings()
                checkings.close_account(total_accounts_checkings, user_account_ID)
        elif user_select == 8:
            print('Exiting')
            break
                
        
            
             