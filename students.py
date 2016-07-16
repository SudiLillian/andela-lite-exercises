from datetime import date

student = {'name':["Lillian", "Sudi"], 'DOB': 1997,'phone_number': '0713100894' }

a=student.get('name')
b=student.get('DOB')
c=student.get('phone_number')
age= date.today().year-b


print 'Name; {0}'.format(a)
print 'Year of birth; {0}'.format(b)
print 'Phone number; {0}'.format(c)
print 'Age; {0}'.format(age)
