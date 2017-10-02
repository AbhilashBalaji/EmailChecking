import csv
import AnotherMethod as an
from validate_email import validate_email
def check(a):
	
	with open('E:\Repos\EmailChecking\EmailsCsV.csv', 'rt')	as c:
		reader=csv.reader(c)
		for lines in reader:
			if a in lines:
				#print("not in")
				return False
				
	return True
			
				
	print("working")		
	return True		


with open('E:\Repos\EmailChecking\Bengaluru.txt', 'rt') as f :
	
	reader=csv.reader(f)
	Emails=[]
	c=0		
	for line in reader:
		a=str(line)[1:-1]
		a=a[1:-1] #ghetto fkn method 
		Emails.append(a)
#print(Emails)		

with open('E:\Repos\EmailChecking\EmailsCsV.csv', 'a')	as c:
	EmailWriter = csv.writer(c, delimiter=',' ,skipinitialspace=True,lineterminator='\n')	
	#EmailWriter.writerow(('Email','legit?'))
	for email in Emails:
		if check(email) == True:
			b=an.getSuccess(email)
			EmailWriter.writerow((email,str(b)))
			print("Added ",email,"And ",str(b))


'''

	
	a=[]

	
'''