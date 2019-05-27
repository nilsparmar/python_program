import re
import os


class Logfile:

	def get_filepath(self):
		self.path = 'D:\Study\Python\gitrecord\python_program\log.txt'
		# path = str(input('Enter File Path:'))
		# assert os.path.exists(self.path), "I did not find the file at, "+str(self.path)
		with open(self.path) as myfile:
			data = myfile.read()
		return data


	def count_err(self):
		self.path_result = self.get_filepath()
		print(self.path_result)
		
			
		r1 = re.findall(r"ERROR|WARNING|INFO",self.path_result)
		print(r1)
		
		
		print("Total ERRORS : ",r1.count('ERROR'))
		print("Total WARNING : ",r1.count('WARNING'))
		print("Total INFORMATION : ",r1.count('INFO'))
		
	
ob = Logfile()
ob.get_filepath()
ob.count_err()
	
