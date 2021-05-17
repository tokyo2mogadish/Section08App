from fpdf import FPDF
import webbrowser
import os
from filestack import Client

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
        
        os.chdir('files') #changing directory to files where pdf is stored in previous line
        pdf.output(self.filename)
        webbrowser.open(self.filename) #to open file   in browser or default pdf viewer automatically #on linux webbrowser.open('file://' + os.path.realpath(self.filename))
    
class FileSharer:
    
    def __init__(self, filepath, api_key = 'ALQrtAB9RYGBNfFQjYJN6z'):
        self.filepath = filepath
        self.api_key = api_key
    
    def share(self):
        client = Client(self.api_key)
        new_filelink = client.upload(filepath = self.filepath)

        return (new_filelink.url)
                
        