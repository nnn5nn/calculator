from sys import argv
class Calculator():
	def __init__(self,cash):
		self.cash = cash
	def computation(self):
		cash = int(self.cash)
		taxbase = cash -3500
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
		format(tax,'.2f')
		return tax
try:
	if len(argv) == 2:
		cal = Calculator(argv[1])
		print(cal.computation())
	else:
		print('Parameters Error')
except(ValueError) as e :
	print('Parameters Error')
