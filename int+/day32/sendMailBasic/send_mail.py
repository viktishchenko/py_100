import smtplib

my_email = 'myrealmailaddress@gmail.com'
pswrd = 'qwewqdsfcxvsf'

with smtplib.SMTP('smtp.gmail.com') as connection:
  connection.starttls()
  connection.login(user=my_email, password=pswrd)
  connection.sendmail(
    from_addr=my_email,
    to_addrs='emailtosendaddress@yahoo.com',
    msg='Subject:Hello there!\n\nThis is body of email.'
  )