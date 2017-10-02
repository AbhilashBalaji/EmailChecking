import re
import smtplib
import dns.resolver

def test_conn_open(conn):
    try:
        status = conn.noop()[0]
    except:  # smtplib.SMTPServerDisconnected
        status = -1
    return True if status == 250 else False

def getSuccess(email):
	fromAddress = 'corn@bt.com'
	regex = '^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,})$'
	inputAddress = email
	addressToVerify = str(inputAddress)
	match = re.match(regex, addressToVerify)
	if match == None:
		return False	
	splitAddress = addressToVerify.split('@')
	domain = str(splitAddress[1])
	records = dns.resolver.query(domain, 'MX')
	mxRecord = records[0].exchange
	mxRecord = str(mxRecord)
	server = smtplib.SMTP()
	server.set_debuglevel(0)
	server.connect(mxRecord)
	server.helo(server.local_hostname) ### server.local_hostname(Get local server hostname)
	server.mail(fromAddress)
	code, message = server.rcpt(str(addressToVerify))
	server.quit()
	if code == 250:
		return	True
	else:
		return False 