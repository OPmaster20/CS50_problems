from datetime import date,timedelta
import sys
import inflect
import re
p = inflect.engine()
class Date:
    def __init__(self,year,month,date):
        self.year=year
        self.month=month
        self.date=date
        self.now=0
        self.sum=timedelta(days=365)
    def __sub__(self):
        today=date.today()
        toyear,tomonth,todate=today.split('-')
        self.now=toyear-self.year
        return p.number_to_words(p.ordinal(int(self.now)*365*int(self.date)*24*60))
    def __str__(self):
        return p.number_to_words(p.ordinal(int(self.now)*365*int(self.date)*24*60))
    @classmethod
    def get_today(cls):
        return date.today()

def main():
    get=input("Date of Birth: ").strip()
    if re.search('^[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]$',get):
        year,month,date=get.split('-')
        Get=Date()
        print(Get(year,month,date))
    else:
        sys.exit('Invalid date')
if __name__ == "__main__":
    main()