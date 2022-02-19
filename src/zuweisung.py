import datetime
from random import randrange

bewohner = ["Karyna", "B", "Amjad", "Johannes", "Nikita", "Ana", "Chris", "Lena", "Luise", "Simon"]
vWoche = [None] * 5
dienste = ["Bad", "WCs", "Küche", "Gr Saal", "Kl Saal"]


my_date = datetime.date.today()
year, week_num, day_of_week = my_date.isocalendar()


if (int(week_num)%2 == 1):
    for i in range(5):
             pRand = randrange(len(bewohner))
             rRand = randrange(len(dienste))
             print(bewohner[pRand],dienste[rRand] )
             vWoche[i] = bewohner[pRand]
             del bewohner[pRand]
             del dienste[rRand]
    dienste = ["Bad", "WCs", "Küche", "Gr Saal", "Kl Saal"]
    for i in range(5):
        if (len(bewohner) > 0):
             pRand = randrange(len(bewohner))
             rRand = randrange(len(dienste))
             print(bewohner[pRand],dienste[rRand] )
             del bewohner[pRand]
             del dienste[rRand]
        else:
             pRand = randrange(len(vWoche))
             rRand = randrange(len(dienste))
             print(vWoche[pRand],dienste[rRand])
             del vWoche[pRand]
             del dienste[rRand]
