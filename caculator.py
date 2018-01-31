from sys import argv
class Calculator():
	def __init__(self,info):
		self.info = info
	def computation(self,cash):
		cash = int(cash)
		taxbase = cash-(cash*0.165) -3500
		if taxbase>0:
			if taxbase<=1500:
				tax = taxbase*0.03
			elif taxbase>1500 and taxbase <=4500:
				tax = taxbase *0.1-105
			elif taxbase>4500 and taxbase <=9000:
				tax = taxbase * 0.2-555
			elif taxbase>9000 and taxbase <=35000:
				tax = taxbase*0.25- 1005
			elif taxbase>35000 and taxbase <=55000:
				tax = taxbase * 0.3 - 2755
		else:
			tax = 0
		salary = cash-(cash*0.165)-tax
		format(salary,'.2f')
		return salary
	def income(self):
		salaryTable = {}
		idTable = []
		for tmp in self.info:
			id,salary = tmp.split(":")
			salary = self.computation(salary)
			idTable.append(id)
			salaryTable[id] = salary 
		return salaryTable,idTable
try:
	cal = Calculator(argv[1:])
	salaryTable,idTable = cal.income()
	for tmp in idTable:
		print('%s:%.2f'%(tmp,salaryTable[tmp]))
except(ValueError) as e :
	print('Parameters Error')
