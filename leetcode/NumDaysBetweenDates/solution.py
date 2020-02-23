from datetime import date
def daysBetweenDates(self, date1: str, date2: str) -> int:
   date1 = date1.split('-')
   date2 = date2.split('-')
   for i in range(len(date1)):
       date1[i] = int(date1[i])
       date2[i] = int(date2[i])
           
   y1,m1,d1 = date1
   y2,m2,d2 = date2
   
   d1 = date(y1,m1,d1)
   d2 = date(y2,m2,d2)
   diff = d1 - d2
   return abs(diff.days)
        
