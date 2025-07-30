import datetime

def days_of_the_week(day, month , year):
    
    days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","sunday"]
    
    if 1971 <= year <=2100:
        targetDate = datetime.date(year, month, day)
        return days[targetDate.weekday()]
    else:
         print("The selected date is out of range")
         
# Enter desire date
print(days_of_the_week(31 ,8, 2019))