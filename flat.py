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