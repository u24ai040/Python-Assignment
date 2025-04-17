#QUESTION 1

import pandas as pd

date_object=pd.Timestamp('2012-01-15')
print("Date time object for Jan 15 2012:", date_object)

date_object=pd.Timestamp('2012-01-15 21:20')
print("Specific date and time of 9:20 pm:", date_object)    

date_object=pd.Timestamp.now()
print("Local date and time:", date_object)  

date_object=pd.Timestamp('2007-04-02').date()
print("A specific date without time:", date_object)

date_object=pd.Timestamp.now().date()
print("A current date without time:", date_object)

date_object=pd.Timestamp('2012-01-15 21:20').time()
print("Time from a date time:", date_object)

date_object=pd.Timestamp.now().time().replace(microsecond=0)
print("A current local time:", date_object)