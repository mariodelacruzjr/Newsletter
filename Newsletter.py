import smtplib, ssl, csv

port = 465
smtp_server = "smtp.gmail.com"
# Input sender email
sender_email = "test_email@gmail.com"

# input your unique google apps password
password = "google_apps_password"

# message to be sent
message = """\
Subject: Hi there
This message is sent from Python."""

with open('test.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:

        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            print(f'\tSent Email to {row[1]}')
            receiver_email = row[2]
            context = ssl.create_default_context()

            with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
                server.login(sender_email, password)
                server.sendmail(sender_email, receiver_email, message)

            line_count += 1
    print(f'Processed {line_count} lines.')