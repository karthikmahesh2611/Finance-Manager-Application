import pymysql as database
import config



class Account_Table:


	
	def __init__(self):
		self.table_name = 'Account_Code_Mapping'
		self.cln_map = {1:"Account_Code",2:"Account_Name",3:"Account_Num"}

	def __str__(self):
		output = 'Host Name: ' + config.db_host + '\n' + 'Database Name: ' + config.db_name + '\n' + 'Table Name: ' + self.table_name
		return(output)


	def add(self,acc_name,acc_num):
		connection = database.connect(host=config.db_host, user=config.db_user, password=config.db_passwd, db=config.db_name)
		mysql = connection.cursor()
		sql1 = "INSERT INTO " + self.table_name + " (" + self.cln_map[2] + ", " + self.cln_map[3] + ") VALUES ('" + acc_name + "','" + acc_num + "');"
		mysql.execute(sql1)
		connection.commit()
		connection.close()

	def search(self,col_num,value):
		connection = database.connect(host=config.db_host, user=config.db_user, password=config.db_passwd, db=config.db_name)
		mysql = connection.cursor()
		sql1 = "SELECT * from " + self.table_name + " WHERE " + self.cln_map[col_num] + " = '" + value + "';"
		mysql.execute(sql1)
		result = mysql.fetchall()
		connection.close()
		return(result)

	def search_all(self,col_num=1):
		connection = database.connect(host=config.db_host, user=config.db_user, password=config.db_passwd, db=config.db_name)
		mysql = connection.cursor()
		sql1 = "SELECT * from " + self.table_name + " ORDER BY " + self.cln_map[col_num] + " DESC;"
		mysql.execute(sql1)
		result = mysql.fetchall()
		connection.close()
		return(result)


	def search_lastn(self,limit,col_num=1):
		connection = database.connect(host=config.db_host, user=config.db_user, password=config.db_passwd, db=config.db_name)
		mysql = connection.cursor()
		sql1 = "SELECT * from " + self.table_name + " ORDER BY " + self.cln_map[col_num] + " DESC LIMIT " + str(limit) + ";"
		mysql.execute(sql1)
		result = mysql.fetchall()
		connection.close()
		return(result)



class IncomeSourcecode_Table:


	def __init__(self):
		self.table_name = 'Income_Sourcecode_mapping'
		self.cln_map = {1:"Source_Code",2:"Source_Name"}

	def __str__(self):
		output = 'Host Name: ' + config.db_host + '\n' + 'Database Name: ' + config.db_name + '\n' + 'Table Name: ' + self.table_name
		return(output)

	def add(self,src_name):
		connection = database.connect(host=config.db_host, user=config.db_user, password=config.db_passwd, db=config.db_name)
		mysql = connection.cursor()
		sql1 = "INSERT INTO " + self.table_name + " (" + self.cln_map[2] + ") VALUES ('" + src_name +"');"
		mysql.execute(sql1)
		connection.commit()
		connection.close()

	def search(self,col_num,value):
		connection = database.connect(host=config.db_host, user=config.db_user, password=config.db_passwd, db=config.db_name)
		mysql = connection.cursor()
		sql1 = "SELECT * from " + self.table_name + " WHERE " + self.cln_map[col_num] + " = '" + value + "';"
		mysql.execute(sql1)
		result = mysql.fetchall()
		connection.close()
		return(result)

	def search_all(self,col_num=1):
		connection = database.connect(host=config.db_host, user=config.db_user, password=config.db_passwd, db=config.db_name)
		mysql = connection.cursor()
		sql1 = "SELECT * from " + self.table_name + " ORDER BY " + self.cln_map[col_num] + " DESC;"
		mysql.execute(sql1)
		result = mysql.fetchall()
		connection.close()
		return(result)

	def search_lastn(self,limit,col_num=1):
		connection = database.connect(host=config.db_host, user=config.db_user, password=config.db_passwd, db=config.db_name)
		mysql = connection.cursor()
		sql1 = "SELECT * from " + self.table_name + " ORDER BY " + self.cln_map[col_num] + " DESC LIMIT " + str(limit) + ";"
		mysql.execute(sql1)
		result = mysql.fetchall()
		connection.close()
		return(result)


class TransacCode_Table:


	def __init__(self):
		self.table_name = 'Transaction_Category_Code_Mapping'
		self.cln_map = {1:"Transaction_Category_Code",2:"Description"}

	def __str__(self):
		output = 'Host Name: ' + config.db_host + '\n' + 'Database Name: ' + config.db_name + '\n' + 'Table Name: ' + self.table_name
		return(output)

	def add(self,desc):
		connection = database.connect(host=config.db_host, user=config.db_user, password=config.db_passwd, db=config.db_name)
		mysql = connection.cursor()
		sql1 = "INSERT INTO " + self.table_name + " (Description) VALUES ('" + desc +"');"
		mysql.execute(sql1)
		connection.commit()
		connection.close()

	def search(self,col_num,value):
		connection = database.connect(host=config.db_host, user=config.db_user, password=config.db_passwd, db=config.db_name)
		mysql = connection.cursor()
		sql1 = "SELECT * from " + self.table_name + " WHERE " + self.cln_map[col_num] + " = '" + str(value) + "';"
		mysql.execute(sql1)
		result = mysql.fetchall()
		connection.close()
		return(result)

	def search_all(self,col_num=1):
		connection = database.connect(host=config.db_host, user=config.db_user, password=config.db_passwd, db=config.db_name)
		mysql = connection.cursor()
		sql1 = "SELECT * from " + self.table_name + " ORDER BY " + self.cln_map[col_num] + " DESC;"
		mysql.execute(sql1)
		result = mysql.fetchall()
		connection.close()
		return(result)

	def search_lastn(self,limit,col_num=1):
		connection = database.connect(host=config.db_host, user=config.db_user, password=config.db_passwd, db=config.db_name)
		mysql = connection.cursor()
		sql1 = "SELECT * from " + self.table_name + " ORDER BY " + self.cln_map[col_num] + " DESC LIMIT " + str(limit) + ";"
		mysql.execute(sql1)
		result = mysql.fetchall()
		connection.close()
		return(result)


class Income_Table:


	def __init__(self):
		self.table_name = 'Income_Records'
		self.cln_map = {1:"Transaction_id",2:"Transaction_date",3:"Income_Source_Code",4:"Account_code",5:"Description",6:"Amount"}

	def __str__(self):
		output = 'Host Name: ' + config.db_host + '\n' + 'Database Name: ' + config.db_name + '\n' + 'Table Name: ' + self.table_name
		return(output)

	def add(self,date,source_code,acc_code,desc,amount):
		connection = database.connect(host=config.db_host, user=config.db_user, password=config.db_passwd, db=config.db_name)
		mysql = connection.cursor()
		sql1 = "INSERT INTO " + self.table_name + " (" + self.cln_map[2] + ", " + self.cln_map[3] + ", " + self.cln_map[4] + ", " + self.cln_map[5] + ", " + self.cln_map[6] + ") VALUES ('" + date + "','" + source_code + "','" + acc_code + "','" + desc + "','" + amount + "');"
		mysql.execute(sql1)
		connection.commit()
		connection.close()

	def search(self,col_num,value):
		connection = database.connect(host=config.db_host, user=config.db_user, password=config.db_passwd, db=config.db_name)
		mysql = connection.cursor()
		sql1 = "SELECT * from " + self.table_name + " WHERE " + self.cln_map[col_num] + " = '" + str(value) + "';"
		mysql.execute(sql1)
		#Since this table can be really large we first fetch the results in batches of 100 and 
		#than use python generators to yield one at a time
		while True:
			results = mysql.fetchmany(100)
			if not results:
				connection.close()
				break
			for result in results:
				yield result


	def search_all(self,col_num=1):
		connection = database.connect(host=config.db_host, user=config.db_user, password=config.db_passwd, db=config.db_name)
		mysql = connection.cursor()
		sql1 = "SELECT * from " + self.table_name + " ORDER BY " + self.cln_map[col_num] + " DESC;"
		mysql.execute(sql1)
		#Since this table can be really large we first fetch the results in batches of 100 and 
		#than use python generators to yield one at a time
		while True:
			results = mysql.fetchmany(100)
			if not results:
				connection.close()
				break
			for result in results:
				yield result

	def search_lastn(self,limit,col_num=1):
		connection = database.connect(host=config.db_host, user=config.db_user, password=config.db_passwd, db=config.db_name)
		mysql = connection.cursor()
		sql1 = "SELECT * from " + self.table_name + " ORDER BY " + self.cln_map[col_num] + " DESC LIMIT " + str(limit) + ";"
		mysql.execute(sql1)
		#Since this table can be really large we first fetch the results in batches of 100 and 
		#than use python generators to yield one at a time
		while True:
			results = mysql.fetchmany(100)
			if not results:
				connection.close()
				break
			for result in results:
				yield result


class Expenditure_Table:

	
	def __init__(self):
		self.table_name = 'Daily_Expenditure'
		self.cln_map = {1:"Transaction_id",2:"Transaction_date",3:"Description",4:"Transaction_Category_Code",5:"Transaction_Account_Code",6:"Transaction_Amount"}

	def __str__(self):
		output = 'Host Name: ' + config.db_host + '\n' + 'Database Name: ' + config.db_name + '\n' + 'Table Name: ' + self.table_name
		return(output)

	def add(self,date,desc,trascat_code,acc_code,amount):
		connection = database.connect(host=config.db_host, user=config.db_user, password=config.db_passwd, db=config.db_name)
		mysql = connection.cursor()
		sql1 = "INSERT INTO " + self.table_name + " (" + self.cln_map[2] + ", " + self.cln_map[3] + ", " + self.cln_map[4] + ", " + self.cln_map[5] + ", " + self.cln_map[6] + ") VALUES ('" + date + "','" + desc + "','" + trascat_code + "','" + acc_code + "','" + amount +"');"
		mysql.execute(sql1)
		connection.commit()
		connection.close()


	def search(self,col_num,value):
		connection = database.connect(host=config.db_host, user=config.db_user, password=config.db_passwd, db=config.db_name)
		mysql = connection.cursor()
		sql1 = "SELECT * from " + self.table_name + " WHERE " + self.cln_map[col_num] + " = '" + str(value) + "';"
		mysql.execute(sql1)
		#Since this table can be really large we first fetch the results in batches of 100 and 
		#than use python generators to yield one at a time
		while True:
			results = mysql.fetchmany(100)
			if not results:
				connection.close()
				break
			for result in results:
				yield result

	def search_all(self,col_num=1):
		connection = database.connect(host=config.db_host, user=config.db_user, password=config.db_passwd, db=config.db_name)
		mysql = connection.cursor()
		sql1 = "SELECT * from " + self.table_name + " ORDER BY " + self.cln_map[col_num] + " DESC;"
		mysql.execute(sql1)
		#Since this table can be really large we first fetch the results in batches of 100 and 
		#than use python generators to yield one at a time
		while True:
			results = mysql.fetchmany(100)
			if not results:
				connection.close()
				break
			for result in results:
				yield result


	def search_lastn(self,limit,col_num=1):
		connection = database.connect(host=config.db_host, user=config.db_user, password=config.db_passwd, db=config.db_name)
		mysql = connection.cursor()
		sql1 = "SELECT * from " + self.table_name + " ORDER BY " + self.cln_map[col_num] + " DESC LIMIT " + str(limit) + ";"
		mysql.execute(sql1)
		#Since this table can be really large we first fetch the results in batches of 100 and 
		#than use python generators to yield one at a time
		while True:
			results = mysql.fetchmany(100)
			if not results:
				connection.close()
				break
			for result in results:
				yield result









