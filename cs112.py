import chat_downloader
from chat_downloader import ChatDownloader
import os
import re
def extract_data_comment(line):
	line = re.sub(",|\?|\.|\[|\]|\"|-|;|:|\(|\)|\\|_|\*|&|\^|\$|!|'|\/|–", " ", line)
	line = re.sub("\s{2,}", " ", line)
	line = re.sub("\n", "", line)
	return re.findall("[a-zA-Z]{1,}", line)
url = 'https://www.youtube.com/watch?v=Ejzw6Htgj7c'
chat = ChatDownloader().get_chat(url=url)
# create a generator
d = 0
lst = []
for message in chat:
	if (len(message['message'])>1):# iterate over messages
		with open('C:/Users/ADMIN/Desktop/data.txt', 'a', encoding='utf-8') as outfile:
			str = message['message']

			import re
			a = re.findall(':.*?:', str)
			for sub in a:
				str = str.replace(sub, '')
			st=str.replace(' ','')
			if (str!='' and lst.count(st)==0):
			   outfile.write(str)
			   outfile.write('\n')
			   lst.append(st)
			   d = d + 1


