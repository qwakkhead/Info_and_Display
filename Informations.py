#Pseudocode first

#Import fontstyle
import fontstyle

#State the users name
name = input("State the users Name")
text_name = fontstyle.apply(name, 
					'bold/Italic/red/UNDERLINE/GREEN_BG')
#State the users Job
job = input("State the users Job")
text_job = fontstyle.apply(job, 
					'bold/Italic/red/UNDERLINE/GREEN_BG')
#Now print it in a fancy way both Name and Job
print (text_name)
print (text_job)

#Add some Informations 
birthday = input("Enter the users Birthday")
gender = input("Enter the users Gender")
status = input("Enter users Status")

#Create some fancy style

text_birthday = fontstyle.apply(birthday, 'blue/bold/underline')
text_gender = fontstyle.apply(gender, 'blue/bold/underline') 
text_status = fontstyle.apply(status, 'blue/bold/underline')

#Now Print

print(text_birthday)
print(text_gender)
print(text_status)
                              
