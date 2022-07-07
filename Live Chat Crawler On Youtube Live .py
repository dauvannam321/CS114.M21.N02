#Import package
import chat_downloader #Thank xenova for creating this fookin vjppr0 lib
from chat_downloader import ChatDownloader
import os
import re
#Now copy and paste something like
url = 'https://www.youtube.com/watch?v=Ejzw6Htgj7c'#Only the football live stream which has chat replay
chat = ChatDownloader().get_chat(url=url,start_time=None,end_time=None)#Get chats from url
save_path='C:/Users/ADMIN/Desktop/data.txt'
d = 0
lst = []
# Create a generator
for message in chat:
	"""Crawled chat should be like this
	{
    ...
    "message_id": "xxxxxxxxxx",
    "message": "actual message goes here",
    "message_type": "text_message",
    "timestamp": 1613761152565924,
    "time_in_seconds": 1234.56,
    "time_text": "20:34",
    "author": {
        "id": "UCxxxxxxxxxxxxxxxxxxxxxxx",
        "name": "username_of_sender",
        "images": [
            ...
        ],
        "badges": [
            ...
        ]
    },
    ...
}"""
	#In here we just get 7000 messages
	#if(d>7000):break
	if (len(message['message'])>1):# iterate over messages
		with open(save_path, 'a', encoding='utf-8') as outfile:
			str = message['message']#Just take message content
			import re
			a = re.findall(':.*?:', str)#We will remove all emote, which start and end with char ':'
			for sub in a:
				str = str.replace(sub, '')
			# Now we try to remove all the same message content by create a substring without space char and check if it existed, write to file
			st=str.replace(' ','')
			if (str!='' and lst.count(st)==0):
			   outfile.write(str)
			   outfile.write('\n')
			   #Append this substring and ready for the next checking time
			   lst.append(st)
			   d = d + 1


