#https://www.udemy.com/course/the-python-mega-course/learn/lecture/4775322#overview
from fpdf import FPDF
import webbrowser

class Bill:
    """
    Object that contains data about the bill, such as 
    total amount and period of the bill
    """

    def __init__(self, amount, period):
        self.amount = amount
        self.period = period

class Flatmate:
    """
    Creates a flatmate person who lives in the flat 
    and pays a share of the bill.
    """

    def __init__(self, days_in_house, name):
        self.days_in_house = days_in_house
        self.name = name

    
    def pays(self, bill, flatmates):
        
        sum_of_days = 0
        for flatmate in flatmates:
            if(flatmate != self):
                sum_of_days += flatmate.days_in_house

        weight = self.days_in_house / (self.days_in_house + sum_of_days) 
        to_pay = bill.amount * weight
        return to_pay

class PdfReport:
    """
    Creates a Pdf file that contains data about 
    the flatmates such as their names, their due amount 
    and the period of the bill
    """

    def __init__(self, filename):
        self.filename = filename
    
    def generate(self, flatmates, bill):
        pdf = FPDF(orientation = 'P', unit = 'pt', format = 'A4')
        pdf.add_page()


        #add icon
        pdf.image('files/house.png', w = 30, h = 30)
        
        #insert title
        pdf.set_font(family = 'Times', size = 24, style = 'B')
        pdf.cell(w = 0, h = 80, txt = 'Flatmates Bill', border = 1 , align = 'C', ln = 1) #in pt units , cell is a rectangle we draw on pdf
        #Insert Period Label and Value
        pdf.set_font(family = 'Times', size = 14, style = 'B')
        pdf.cell(w = 100, h = 40, txt = 'Period:', border = 0)
        pdf.cell(w = 130, h = 40, txt = bill.period, border = 0, ln = 1)        
        
        #Insert Name and due amount for flatmates
        pdf.set_font(family = 'Times', size = 12)
        for flatmate in flatmates:
            pdf.cell(w = 100, h = 25, txt = flatmate.name, border = 0)        
            pdf.cell(w = 130, h = 25, txt = str(round(flatmate.pays(bill, flatmates),2)) , border = 0, ln = 1)
        
        pdf.output(self.filename)
        webbrowser.open(self.filename) #to open file in browser or default pdf viewer automatically #on linux webbrowser.open('file://' + os.path.realpath(self.filename))

the_bill = Bill(amount = 1000, period = "March 2021")
john = Flatmate(name = "John", days_in_house = 15)
marry = Flatmate(name= "Marry", days_in_house = 20)
seb = Flatmate(name= "Seb", days_in_house = 20)

flatmates = [john, marry, seb]
print('JOHN IS DUE: ',john.pays(bill = the_bill, flatmates= flatmates)) 
print('MARRY IS DUE: ',marry.pays(bill = the_bill, flatmates = flatmates))
print('SEB IS DUE: ',seb.pays(bill = the_bill, flatmates = flatmates))

pdf_report = PdfReport(filename = 'bill.pdf')
pdf_report.generate(flatmates = flatmates, bill = the_bill)
