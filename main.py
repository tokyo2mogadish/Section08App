#https://www.udemy.com/course/the-python-mega-course/learn/lecture/4775322#overview
from flat import Bill, Flatmate
from reports import PdfReport, FileSharer

amount = float(input('Hey user, please enter the bill amount: '))
period = input('What is the bill period? E.g. December 2021: ')

flatmates = []
track = True
while track == True:
    answer = input('Do you wanna enter flatmate? Y/N: ')
    if(answer.lower() == 'y'):
        name = input('Enter the flatmates name: ')
        days_in_house = int(input(f'Enter {name}\'s days in house: '))
        flatmate = Flatmate(name = name, days_in_house = days_in_house)
        flatmates.append(flatmate)
    else:
        track = False

the_bill = Bill(amount = amount , period = period)

if ( len(flatmates) > 0 ):
    for flatmate in flatmates:
        print(f'{flatmate.name} is due: ', flatmate.pays(bill = the_bill, flatmates = flatmates))

    pdf_report = PdfReport(filename = (f'{the_bill.period}.pdf'))
    pdf_report.generate(flatmates = flatmates, bill = the_bill)
else:
    print('You didnt provide even one flatmate.')

file_sharer = FileSharer(filepath = pdf_report.filename)
print (file_sharer.share())