#https://www.udemy.com/course/the-python-mega-course/learn/lecture/4775322#overview
'''
greska Failed to connect to github.com port 443 resena sa
git config --global http.proxy http://smilojevic:Okoro13!!@192.168.11.5:8080
'''
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

    def pays(self, bill):
        pass

class PdfReport:
    """
    Creates a Pdf file that contains data about 
    the flatmates such as their names, their due amount 
    and the period of the bill
    """

    def __init__(self, filename):
        self.filename = filename
    
    def generate(self, flatmates, bill):
        pass
    