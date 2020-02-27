#generate_news

line1 = '                    <div class="col-md-7">'
line2 = '                      <div class="form-group">'
line3_space = '                        '
line4 = '                      </div>'
line5 = '                    </div>'
form_space = '                      '

def merge_temp_files():
	hdata = bdata = fdata = "" 
  
	# Reading data from header 
	with open('.//templates//temp_news_files//header.html',"r") as hd: 
	    hdata = hd.read() 
	  
	# Reading data from body 
	with open('.//templates//temp_news_files//body.html',"r") as bd: 
	    bdata = bd.read()

	# Reading data from header 
	with open('.//templates//temp_news_files//footer.html',"r") as ft: 
	    fdata = ft.read()
	  
	# Merging 3 files 
	tot_data = hdata
	tot_data += "\n"
	tot_data += bdata
	tot_data += "\n"
	tot_data += fdata 
	  
	with open ('.//templates//cust_news.html', 'w') as cnews: 
	    cnews.write(tot_data) 


def generate_news(newslist):
	try:
		out_file = open('.//templates//temp_news_files//body.html',"w")
	except IOError as FOerr:
		print('File Open error', FOerr)
	else:
		for item in newslist:
			link = item['link']
			title = item['title']
			out_file.write(line1 + '\n')
			out_file.write(line2 + '\n')
			line3 = line3_space + '<a href="' + link + '" class="form-control">' + title + '</a>'
			out_file.write(line3 + '\n')
			out_file.write(line4 + '\n')
			out_file.write(line5 + '\n')
	finally:
		out_file.close()

	return merge_temp_files()
