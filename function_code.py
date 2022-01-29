from side_bar_names import *
from chatwindow_middlepart import *
from mysql_connector import *

def main_html(user_name):
	x = ''
	y = ''
	z = ''
	css = open('whatsapp.html','r').read()

	sidebar = open('side_bar.html','r').read()
	lst = take_data_from_mysql("SELECT * FROM contacts WHERE user_id =%s"%('"'+user_name+'"'))

	for i in range(len(lst)):
		x += names_and_stuff(lst[i]["img_lnk"], lst[i]["name"], lst[i]["sidebar_chat"], lst[i]["last_msg"], lst[i]['id'])
		
	chatwindow = open('chat_window.html','r').read()
	
	chatwindow_lowerpart = open('chatwindow_lowerpart.html', 'r').read()
	end = open('end.html','r').read()

	whatsApp = css + sidebar + x + chatwindow + z + chatwindow_lowerpart + end
	return whatsApp

def chat_change_on_request(ids, username):
	x = ''
	chat_divs = "<div id=chat_" + str(ids) + " class=chat_window_middlepart >"
	all_chat = take_data_from_mysql("SELECT * FROM all_chat WHERE id =%s AND user_name =%s"%('"'+ids+'"','"'+username+'"'))
	
	for i in all_chat:
		x += chats(i["chat_side"], i["chat_color"], i["chat"], i["time"])
	chat_divs_end = '</div>'

	return chat_divs + x + chat_divs_end

def check_the_user(username, password):
	result = take_data_from_mysql("SELECT * FROM username_password WHERE username="+'"'+username+'"')
	
	if result == []:
		return False
	else:
		for j in result:
			if j['username'] == username and j['password'] == password:
				return True
			else:
				return False

def ho_ho():
	return open('login_page.html','r').read()