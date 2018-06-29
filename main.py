if __name__ == "__main__":
	from Function_module import *
	import os


	while True:

		Iterator = 'True'
		#Clear screen
		os.system('cls')

		print('Select the operation you want to perform:')
		print('1 > Add new Account')
		print('2 > Add new Income_Source')
		print('3 > Add new Expenditure Category')
		print('4 > Add entry for expenditure')
		print('5 > Add entry for Income')
		print('6 > Tranfer amount to different account/Withdraw Cash')
		print('7 > View Reports')
		print('8 > Exit')
		ans1 = input('Enter the number to select the operation: ')

		if (ans1 == '1'):
			#Invoke the add account function
			#Check Iterator value
			while (Iterator == 'True'):
				#The function takes two objects and one function as argument
				add_new_account()
				while True:
					print('\nSelect one of the options:')
					print('1 > Exit to Main Menu')
					print('2 > Add another account')
					ans2 = input('Enter your selection:')
					if (ans2 == '1'):
						Iterator = 'False'
						break
					elif(ans2 == '2'):
						break
					else:
						os.system('cls')
						print('Invalid option. Try Again.')
						continue
			continue

		elif (ans1 == '2'):
			#Invoke the add new expenditure category function
			#Check Iterator value
			while (Iterator == 'True'):
				#The function takes one table object and one function as argument
				add_new_incomesource()
				while True:
					print('\nSelect one of the options:')
					print('1 > Exit to Main Menu')
					print('2 > Add another Income Source')
					ans2 = input('Enter your selection:')
					if (ans2 == '1'):
						Iterator = 'False'
						break
					elif(ans2 == '2'):
						break
					else:
						os.system('cls')
						print('Invalid option. Try Again.')
						continue
			continue

		elif (ans1 == '3'):
			#Invoke the add expenditure code function
			#Check Iterator value
			while (Iterator == 'True'):
				#The function takes two objects and one function as argument
				add_new_transcode()
				while True:
					print('\nSelect one of the options:')
					print('1 > Exit to Main Menu')
					print('2 > Add another expenditure category')
					ans2 = input('Enter your selection:')
					if (ans2 == '1'):
						Iterator = 'False'
						break
					elif(ans2 == '2'):
						break
					else:
						os.system('cls')
						print('Invalid option. Try Again.')
						continue
			continue


		elif (ans1 == '4'):
			#Invoke the add expenditure entry function
			#Check Iterator value
			while (Iterator == 'True'):
				#The function takes two objects and one function as argument
				add_expenditure()
				while True:
					print('\nSelect one of the options:')
					print('1 > Exit to Main Menu')
					print('2 > Add another entry')
					ans2 = input('Enter your selection:')
					if (ans2 == '1'):
						Iterator = 'False'
						break
					elif(ans2 == '2'):
						break
					else:
						os.system('cls')
						print('Invalid option. Try Again.')
						continue
				continue


		elif (ans1 == '5'):
			#Invoke the add income entry
			#Check Iterator value
			while (Iterator == 'True'):
				#The function takes two objects and one function as argument
				add_income()
				while True:
					print('\nSelect one of the options:')
					print('1 > Exit to Main Menu')
					print('2 > Add another entry')
					ans2 = input('Enter your selection:')
					if (ans2 == '1'):
						Iterator = 'False'
						break
					elif(ans2 == '2'):
						break
					else:
						os.system('cls')
						print('Invalid option. Try Again.')
						continue
				continue

		elif (ans1 == '6'):
			#Invoke the add account function
			#Check Iterator value
			while (Iterator == 'True'):
				#The function takes two objects and one function as argument
				amount_transfer()
				while True:
					print('\nSelect one of the options:')
					print('1 > Exit to Main Menu')
					print('2 > Add another entry')
					ans2 = input('Enter your selection:')
					if (ans2 == '1'):
						Iterator = 'False'
						break
					elif(ans2 == '2'):
						break
					else:
						os.system('cls')
						print('Invalid option. Try Again.')
						continue
				continue

		elif (ans1 == '7'):
			os.system('cls')
			print('This feature is under Development. Sorry for the inconvinience.')
			ans2 = input('Press any Key to return')
			continue

		elif (ans1 == '8'):
			os.system('cls')
			print('Good Bye & Have a nice Day')
			break











