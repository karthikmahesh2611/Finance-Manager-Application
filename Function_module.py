from mysql_table_class import *
import config
import os
import datetime

#Initialise the database table classes
table1 = Account_Table()
table2 = IncomeSourcecode_Table()
table3 = TransacCode_Table()
table4 = Income_Table()
table5 = Expenditure_Table()


def add_new_account():
	os.system('cls')
	print('Existing accounts:')
	show_all_accounts()
	name = input('\nEnter the name of your Account: ')
	acc_num = input('Enter the account number if applicable: ')
	open_bal = input('Enter the opening balance for the account: ')
	table1.add(name,acc_num)

	os.system('cls')
	print('\nNew Account added and ready to use')
	show_all_accounts()

	now = datetime.datetime.now()
	date = str(now.date())
	result = table1.search_lastn(1)
	table4.add(date,'3000',str(result[0][0]),'Opening Balance for Acc: ' + name , open_bal)
	print('\n\nOpening Balance added to income')



def add_new_incomesource():
	os.system('cls')
	print('Existing Income Source:')
	show_all_incomesource()
	src = input('\nEnter new Income Source: ')
	table2.add(src)
	os.system('cls')
	print('New income source added and ready to use\n')
	show_all_incomesource()



def add_new_transcode():
	os.system('cls')
	print('Existing Expenditure code:')
	show_all_trascat()
	categ = input('\nEnter description for the new Expenditure Category: ')
	table3.add(categ)

	os.system('cls')
	print('New Expenditure category added and ready to use\n')
	show_all_trascat()


def add_income():
	os.system('cls')
	date = input('Enter date of transaction YYYY-MM-DD format: ')

	os.system('cls')
	show_all_incomesource()
	src = input('\nEnter income source code (from the existing ones shown above): ')
	
	os.system('cls')
	show_all_accounts()
	acc = input('\nEnter the Account code (from the exisiting ones shown above): ')

	os.system('cls')
	desc = input('Enter a brief description (max 100 characters): ')
	amt = input('\nEnter the amount (max 2 decimals): ')

	table4.add(date,src,acc,desc,amt)
	os.system('cls')
	print('\nIncome added successfully')



def add_expenditure():
	os.system('cls')
	date = input('Enter date of transaction YYYY-MM-DD format: ')
	desc = input('Enter a brief description (max 100 characters): ')

	os.system('cls')
	show_all_trascat()
	transac_code = input('\nEnter the expenditure category code (from the existing ones shown above): ')
	
	os.system('cls')
	show_all_accounts()
	acc = input('\nEnter the Account code from which the expenditure occured(from the exisiting ones shown above): ')

	os.system('cls')
	amt = input('\nEnter the amount (max 2 decimals): ')
	bal = account_balance(acc)
	if int(amt) >= bal:
		print('Insufficient funds in the account {}. Balance is {}'.format(acc,bal))
		print('Entry Failed!!')
		return
	else:
		table5.add(date,desc,transac_code,acc,amt)
		os.system('cls')
		print('\nTransaction entry successfull')
		return


def amount_transfer():

	os.system('cls')
	print('Existing accounts:')
	show_all_accounts()
	src_acc = input('\nEnter the Account id of the source account: ')
	dest_acc = input('Enter the Account id to which amounts needs to be transferred: ')
	amt = input('Enter the amount to be transferred: ')
	now = datetime.datetime.now()
	date = str(now.date())
	bal = account_balance(src_acc)

	if int(amt) > bal:
		os.system('cls')
		print('Insufficient funds in the account {}. Balance is {}'.format(src_acc,bal))
		print('Transfer failed!!')
		return
	else:
		table5.add(date,'Transfer to account ' + dest_acc,'1000',src_acc,amt)
		table4.add(date,'3000',dest_acc,'Transfer from account ' + src_acc,amt)
		os.system('cls')
		print('Transfer completed')
		print('Balance in Account {}: {}'.format(src_acc,account_balance(src_acc)))
		print('Balance in Account {}: {}'.format(dest_acc,account_balance(dest_acc)))
		return









	

###################################################################################

def show_all_incomesource():
	result = table2.search_all()
	print('Below is list of all Income sources available')
	print('\nCode    Source_Name\n')
	for (a,b) in result:
		print('{}    {}'.format(a,b))


def show_all_accounts():
	result = table1.search_all()
	print('\nBelow is List of Accounts added')
	print('\nAcc_code Acc_Name   Acc_Num\n')
	for (a,b,c) in result:
		print('{}    {}  {}'.format(a,b,c))


def show_all_trascat():
	result = table3.search_all()
	print('\nBelow is List of all Expenditure categories')
	print('\nCode    Transaction_category\n')
	for (a,b) in result:
		print('{}    {}'.format(a,b))



def show_all_income():
	print('\nBelow is List of all Income Entries')
	print('\nid   Date    Income_Source_Code  Account_code  Amount   Description\n')
	for (a,b,c,d,e,f) in table4.search_all():
		print('{}  {}  {}              {}         {}   {}'.format(a,b,c,d,f,e))


def show_all_expenditure():
	print('\nBelow is List of all Expenditure Entries')
	print('\nid   Date    Category_Code  Account_Code  Amount   Description\n')
	for (a,b,c,d,e,f) in table5.search_all():
		print('{}  {}  {}           {}        {}    {}'.format(a,b,d,e,f,c))




###################################################################################

def account_balance(acc_id):
	sum1 = 0
	sum2 = 0
	for income in table4.search(4,acc_id):
		sum1 += int(income[5])

	for expend in table5.search(5,acc_id):
		sum2 += int(expend[5])

	return(sum1-sum2)




























