import re

class Logfile:
	
	def count_err(self):
		c_error = 0
		c_info = 0
		c_warning = 0

		myfile=open("log.txt","r")
		for x in myfile:
			d=myfile.readline()
			print(d)
			c_err = re.compile(r'(\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2}.\d{3}) (\w*)')
			regex_get = c_err.search(d)
			result = regex_get.group(2)
			if result == 'ERROR':
				c_error = c_error + 1
			elif result == 'INFO':
				c_info = c_info + 1
			elif result == 'WARNING':
				c_warning = c_warning + 1

		myfile.close()

		print("TOTAL ERROR : ",c_error)
		print("TOTAL WARNING : ",c_warning)
		print("TOTAL INFORMTION : ",c_info)
		
		
		


ob = Logfile()
ob.count_err()
	
