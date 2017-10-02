import csv
import AnotherMethod as an
from validate_email import validate_email
with open('E:\Repos\EmailChecking\Bengaluru.txt', 'rt') as f :
	with open('E:\Repos\EmailChecking\EmailsCsv.csv','w') as c:
		reader=csv.reader(f)
		EmailWriter = csv.writer(c, delimiter=',' ,skipinitialspace=True,lineterminator='\n')
		EmailWriter.writerow(('Email','legit?'))
		Emails={}
		c=0		
		for line in reader:
			for email in line:		
				a=str(line)[1:-1]
				a=a[1:-1] #ghetto fkn method 
				EmailWriter.writerow((a,str(an.getSuccess(email))))
				c+=1
				print("done"+" ",c)


		
		
		
			
		

	


