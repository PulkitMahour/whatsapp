from http.server import BaseHTTPRequestHandler, HTTPServer
import os
from http.cookies import SimpleCookie
from function_code import *

who_is_the_user = ''

class handler(BaseHTTPRequestHandler):

	def do_GET(self):
		global who_is_the_user
		if self.path[:7] == '/images':
			self.path = '/whatsapp_images' + self.path[7:]

			if self.path[1:] != '':
				
				if os.path.isfile(self.path[1:]):
					
					with open(self.path[1:], 'rb') as f:
						self.send_response(200)
						self.send_header("Content-type", "image/png")
						self.end_headers()
						self.wfile.write(f.read())

		elif self.path == '/':
			cookies = SimpleCookie(self.headers.get('Cookie'))
			if 'username' in cookies:
				who_is_the_user = cookies['username'].value
				self.send_response(200)
				self.send_header("Content-type", "text/html")
				self.end_headers()
				self.wfile.write(bytes(main_html(cookies['username'].value), 'utf-8'))
			else:
				self.send_response(302)
				self.send_header('Location','/login')
				self.end_headers()

		elif self.path[:9] == '/contacts':
			contact_name = self.path[10:].split('=')
			cookies = SimpleCookie(self.headers.get('Cookie'))
			self.send_response(200)
			self.send_header("Content-type", "text/html")
			self.end_headers()
			self.wfile.write(bytes(chat_change_on_request(contact_name[1], cookies['username'].value), 'utf-8'))

		elif self.path[:13] == '/message-send':
			input_dict = {}
			query_parameter = self.path[14:].split('&')
			for part in query_parameter:
				part_split = part.split('=')
				input_dict[part_split[0]] = part_split[1]

			self.send_response(200)
			self.send_header("Content-type", "text/html")
			self.end_headers()
			mysql_inserter(input_dict['message'].replace("%20"," "), input_dict['name_id'], input_dict['send_time'].replace("%20", " "), who_is_the_user)


		elif self.path[:6] == '/login':
			dictionary = {}
			query_p = self.path[7:].split('&')
			if query_p != ['']:
				for part in query_p:
					part_split = part.split('=')
					dictionary[part_split[0]] = part_split[1]
				if 'username' in dictionary and 'password' in dictionary:
					if check_the_user(dictionary['username'],dictionary['password']):

						self.send_response(302)
						self.send_header("Content-type", "text/html")
						cookie = SimpleCookie()
						cookie['username'] = dictionary['username']
						cookie['password'] = dictionary['password']
						for morsel in cookie.values():
							self.send_header("Set-Cookie", morsel.OutputString())
						
						self.send_header('Location','/')
						self.end_headers()

					else:
						self.send_response(200)
						self.send_header('Content-type','text/html')
						self.end_headers()
						self.wfile.write(bytes('Invalid Request please try again to login', 'utf-8'))
			else:
				self.send_response(200)
				self.send_header('Content-type','text/html')
				self.end_headers()
				self.wfile.write(bytes(ho_ho(), 'utf-8'))

		else:
			self.send_response(404)
			self.send_header('Content-type','text/html')
			self.end_headers()
			self.wfile.write(bytes('Invalid Request', 'utf-8'))

try:
	with HTTPServer(('localhost', 9999), handler) as server:
		server.serve_forever()
		
except KeyboardInterrupt:
	pass
