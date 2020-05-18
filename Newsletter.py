import smtplib, ssl,csv


port = 465  
smtp_server = "smtp.gmail.com"
sender_email = "sample_sender_email@gmail.com"  

password = "sample_pass"
message = """\
Subject: Hi there

This message is sent from Python."""



with open('C:\\Program Files\\Sublime Text 3\\sample.csv') as csv_file:
	csv_reader = csv.reader(csv_file, delimiter=',')
	line_count = 0
	for row in csv_reader:
		if line_count == 0:
			print(f'Column names are {", ".join(row)}')
			line_count += 1
		else:
			print(f'\tSent Email to {row[1]}')
			receiver_email = "sample_recieving_email@gmail.com" 
			context = ssl.create_default_context()
			with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
				server.login(sender_email, password)
				server.sendmail(sender_email, receiver_email, message)
                      
			line_count += 1
	print(f'Processed {line_count} lines.')