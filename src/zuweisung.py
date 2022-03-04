# coding=utf-8
import datetime
from random import randrange

bewohner = ["Karyna", "B", "Amjad", "Johannes", "Nikita", "Ana", "Chris", "Lena", "Luise", "Simon"]
dienste = ["Bad", "WCs", "Kueche", "Gr Saal", "Kl Saal"]

def generatePutzplan(bewohner, dienste):
     vWoche = [None] * 5
     Woche1 = [None] * 5
     Woche2 = [None] * 5
     my_date = datetime.date.today()
     year, week_num, day_of_week = my_date.isocalendar()
     dienste2 = list(dienste)
     if (int(week_num)%2 == 1):
          for i in range(5):
                    pRand = randrange(len(bewohner))
                    rRand = randrange(len(dienste))
                    Woche1[i] = bewohner[pRand] + ": " + dienste[rRand]
                    vWoche[i] = bewohner[pRand]
                    del bewohner[pRand]
                    del dienste[rRand]
          for i in range(5):
               if (len(bewohner) > 0):
                    pRand = randrange(len(bewohner))
                    rRand = randrange(len(dienste2))
                    Woche2[i] = bewohner[pRand]  + ": " + dienste2[rRand] 
                    del bewohner[pRand]
                    del dienste2[rRand]
               else:
                    pRand = randrange(len(vWoche))
                    rRand = randrange(len(dienste2))
                    Woche2[i] = vWoche[pRand]  + ": " + dienste2[rRand]
                    del vWoche[pRand]
                    del dienste2[rRand]
     return week_num, my_date, Woche1, Woche2


print(generatePutzplan(bewohner, dienste))