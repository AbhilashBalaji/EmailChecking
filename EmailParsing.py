import csv
from validate_email import validate_email
with open('Bengaluru.txt', 'rt') as f:
	reader=csv.reader(f)
	Emails={}
	for line in reader:
		for email in line:
			Emails[str(line)]=validate_email(email)
with open('EmailsCsv.csv','w') as f:
	EmailWriter = csv.writer(f, delimiter=',' ,skipinitialspace=True,lineterminator='\n')
	EmailWriter.writerow(('Email','legit?'))
	for Email,check in Emails.items():
		a=Email[1:-1]
		b=a[1:-1] #ghetto fkn method 
		EmailWriter.writerow((b,str(check)))

		

	


