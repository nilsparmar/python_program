
'''Perform below task 
   1) Create a class with dock string (brief disc & ex. of usage)
   takse 3 arguments 1. IP, 2. username & password
   2) Create a function takes one argument as vm_name
   & check vm is exist in my_data & return True or False accordingly
   3)Create 2nd method name 'power_on' takes vm name & perform power on operation(fake)
   It verify if vm exist or not using check vm method
   And chech power state is off or on
   If exiist than change power_state from OFF to ON if already on than print msg 
   4) Power off method as power on'''

#take on task at a time & commint it
   
class System_data:



	def __init__(self, ip, username, password):
		self.ip = ip
		self.username = username
		self.password = password

	def get_vm(self, v):
		self.v = v
		# print(vm['value'])
		x='vm-1012'
		for key in v:
			# for i in range(len(v['value'])):
			if x == v[key][1]['vm']:
				print("True")
			else:
				print("False")
				

		



ob1 = System_data(1,'nilsparmar','nils123')

my_data = {'value': [{'memory_size_MiB': 4096, 'vm': 'vm-1000', 'name': 'SP3-RHEL-68-2x2-REG-1-DATA-1', 'power_state': 'POWERED_ON', 'cpu_count': 4},
 {'memory_size_MiB': 2048, 'vm': 'vm-1012', 'name': 'Centos-75-tb-15', 'power_state': 'POWERED_ON', 'cpu_count': 4},
 {'memory_size_MiB': 2048, 'vm': 'vm-1013', 'name': 'Centos-75-tb-16', 'power_state': 'POWERED_ON', 'cpu_count': 4}, 
 {'memory_size_MiB': 2048, 'vm': 'vm-1014', 'name': 'Centos-75-tb-17', 'power_state': 'POWERED_ON', 'cpu_count': 4}, 
 {'memory_size_MiB': 2048, 'vm': 'vm-1015', 'name': 'Centos-75-tb-18', 'power_state': 'POWERED_ON', 'cpu_count': 4}, 
 {'memory_size_MiB': 2048, 'vm': 'vm-1016', 'name': 'Centos-75-tb-19', 'power_state': 'POWERED_ON', 'cpu_count': 4}, 
 {'memory_size_MiB': 2048, 'vm': 'vm-1017', 'name': 'Centos-75-tb-20', 'power_state': 'POWERED_ON', 'cpu_count': 4}, 
 {'memory_size_MiB': 2048, 'vm': 'vm-1018', 'name': 'Centos-75-tb-21', 'power_state': 'POWERED_ON', 'cpu_count': 4}, 
 {'memory_size_MiB': 4096, 'vm': 'vm-1019', 'name': 'SP3-RHEL-68-2x2-REG-2-CORE-0', 'power_state': 'POWERED_ON', 'cpu_count': 4}, 
 {'memory_size_MiB': 4096, 'vm': 'vm-1020', 'name': 'SP3-RHEL-68-2x2-REG-2-CORE-1', 'power_state': 'POWERED_ON', 'cpu_count': 4}, 
 {'memory_size_MiB': 4096, 'vm': 'vm-1021', 'name': 'SP3-RHEL-68-2x2-REG-2-DATA-0', 'power_state': 'POWERED_ON', 'cpu_count': 4}, 
 {'memory_size_MiB': 4096, 'vm': 'vm-1022', 'name': 'SP3-RHEL-68-2x2-REG-2-DATA-1', 'power_state': 'POWERED_ON', 'cpu_count': 4}, 
 {'memory_size_MiB': 4096, 'vm': 'vm-1059', 'name': 'PCE-ISO-CONSOL-POC', 'power_state': 'POWERED_OFF', 'cpu_count': 4}, 
 {'memory_size_MiB': 4096, 'vm': 'vm-1060', 'name': 'RHEL-68-2x2-1823-DATA-1', 'power_state': 'POWERED_ON', 'cpu_count': 4}, 
 {'memory_size_MiB': 4096, 'vm': 'vm-1061', 'name': 'RHEL-68-2x2-1823-CORE-0', 'power_state': 'POWERED_ON', 'cpu_count': 4}, 
 {'memory_size_MiB': 4096, 'vm': 'vm-1062', 'name': 'RHEL-68-2x2-1823-CORE-1', 'power_state': 'POWERED_ON', 'cpu_count': 4}, 
 {'memory_size_MiB': 4096, 'vm': 'vm-1063', 'name': 'RHEL-68-2x2-1823-DATA-0', 'power_state': 'POWERED_ON', 'cpu_count': 4}, 
 {'memory_size_MiB': 6144, 'vm': 'vm-109', 'name': 'PCE-SNC-raj-01', 'power_state': 'POWERED_ON', 'cpu_count': 4}, 
 {'memory_size_MiB': 2048, 'vm': 'vm-1117', 'name': 'Centos-75-tb-22', 'power_state':'POWERED_ON','memory_size_MiB': 4096},
 {'vm': 'vm-697', 'name': 'RHEL-68', 'power_state': 'POWERED_OFF', 'cpu_count': 4}, {'memory_size_MiB': 4096,}]}

ob1.get_vm(my_data)



