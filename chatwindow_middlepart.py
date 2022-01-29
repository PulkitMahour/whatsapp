def chats(chat_side, chat_color, chat, time):
	return "<div class='"+ chat_side + "' >" + \
				"<div class='" + chat_color + "' >" +\
					"<p class=chat_window_text>" + chat + "</p>" +\
					"<p class=chat_time>" + time + "</p>" +\
				"</div>" +\
			"</div>"