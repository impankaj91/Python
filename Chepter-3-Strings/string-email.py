#Author : Pankaj Shah
#Date : 22-10-2020
# Create A Template .

email_temp=''' Dear Sir/Mam ,
 I am Writing to Apply For <position> as a <Experiance>.I would like to bring more attention to key strenght for the job role:
  #<Enter Your Speciality>
  For more information, i have attached my resume for your reference
  Thank You For Your Valuable time and consideration.
  Sincerely,
  <Name>
  <Phone>'''
position=input("Enter Position:")
exp=input("Enter Experiance:")
spec=input("Enter Your Speciality:")
name=input("Name:")
phone=input("Phone:")
email_temp=email_temp.replace("<position>",position)
email_temp=email_temp.replace("<Experiance>",exp)
email_temp=email_temp.replace("<Enter Your Speciality>",spec)
email_temp=email_temp.replace("<Name>",name)
email_temp=email_temp.replace("<Phone>",phone)
print(email_temp)
  