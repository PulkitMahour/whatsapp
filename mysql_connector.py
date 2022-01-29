import mysql.connector

detail_dic = {'host':'127.0.0.1',
				'user':'root',
				'password':'tjwff7xdxc',
				'database':'pulkit'}

def mysql_connector():
	mydb = mysql.connector.connect(
	  host = detail_dic['host'],
	  user = detail_dic['user'],
	  password = detail_dic['password'],
	  database = detail_dic['database']
	)
	return mydb

def take_data_from_mysql(sql_statement):
	calling = mysql_connector()
	mycursor = calling.cursor()
	mycursor.execute(sql_statement)
	myresult = mycursor.fetchall()

	field_names = []
	names_lst = []
	dic = {}

	for i in mycursor.description:
		field_names.append(i[0])

	for a in myresult:
		for index in range(len(a)):
			dic[field_names[index]] = a[index]
		names_lst.append(dic)
		dic = {}
	return names_lst

def mysql_inserter(message, name_id, sending_time, user_name):
	calling = mysql_connector()
	mycursor = calling.cursor()

	sql = "INSERT INTO all_chat (id, chat_side, chat_color, chat, time, user_name) VALUES (%s, %s, %s, %s, %s, %s)"
	val = [
	(name_id, 'chat_box right_txt', 'whatsapp_chat right_color', str(message), str(sending_time), str(user_name)),
	(user_name, 'chat_box', 'whatsapp_chat', str(message), str(sending_time), str(name_id))]

	mycursor.executemany(sql, val)
	calling.commit()