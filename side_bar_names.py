def names_and_stuff(img_lnk, name, sidebar_chat, last_seen, id_num):
	return "<div id=" + id_num + " class= name_section onClick= load_things(this.id) >" + \
				"<img class= img_photo  src=" + img_lnk + ">" + \
				"<div class= name_and_chat >" + \
					"<p id=b" +id_num+ " class= name_text >" + name + "</p>" +\
					"<p class= chat_text >" + sidebar_chat + "</p>" +\
				"</div>" +\
				"<div>" +\
					"<p class= last_seen_names >" + last_seen + "</p>" +\
				"</div>" +\
			"</div>" +\
			"<div class= name_sec_hr style = display:block ></div>"