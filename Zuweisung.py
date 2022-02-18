import datetime
from random import randrange

Gruppe3 = ["Karyna", "B", "Amjad", "Johannes", "Nikita", "Ana", "Chris", "Lena", "Luise", "Simon"]
VWoche = [None] * 5
Putzdienste = ["Bad", "WCs", "Küche", "Gr Saal", "Kl Saal"]


my_date = datetime.date.today()
year, week_num, day_of_week = my_date.isocalendar()


if (int(week_num)%2 == 1):
    for i in range(5):
             pRand = randrange(len(Gruppe3))
             rRand = randrange(len(Putzdienste))
             print(Gruppe3[pRand],Putzdienste[rRand] )
             VWoche[i] = Gruppe3[pRand]
             del Gruppe3[pRand]
             del Putzdienste[rRand]
    Putzdienste = ["Bad", "WCs", "Küche", "Gr Saal", "Kl Saal"]
    for i in range(5):
        if (len(Gruppe3) > 0):
             pRand = randrange(len(Gruppe3))
             rRand = randrange(len(Putzdienste))
             print(Gruppe3[pRand],Putzdienste[rRand] )
             del Gruppe3[pRand]
             del Putzdienste[rRand]
        else:
             pRand = randrange(len(VWoche))
             rRand = randrange(len(Putzdienste))
             print(VWoche[pRand],Putzdienste[rRand])
             del VWoche[pRand]
             del Putzdienste[rRand]