import sqlite3


conScore = sqlite3.connect('game.db')
curScore = conScore.cursor()


def batscore(pl, mt):
    curScore.execute("select * from match where name ='"+mt+"' and player = '"+pl+"';")
    record = curScore.fetchall()
    runs = int(record[0][1])
    balls = int(record[0][2])
    four = int(record[0][3])
    six = int(record[0][12])
    field = int(record[0][8]) + int(record[0][9]) + int(record[0][10])
    point = 0
    point += int(runs / 2)
    if runs > 100:
        point += 10
    elif runs > 50 and runs < 100:
        point += 5
    strike = (runs / balls) * 100
    if strike > 100:
        point += 4
    elif strike >= 80 and strike <= 100:
        point += 2
    point += (four + (six * 2) + (field * 10))
    return int(point)


def bowlscore(pl, mt):
    curScore.execute("select * from match where name ='" + mt + "' and player = '" + pl + "';")
    record = curScore.fetchall()
    wkts = int(record[0][7])
    overs = int(record[0][4])
    runs = int(record[0][6])
    field = int(record[0][8]) + int(record[0][9]) + int(record[0][10])
    point = 0
    point += (wkts * 10)
    if wkts >= 5:
        point += 10
    elif wkts == 3:
        point += 5
    ecorate = runs / overs
    if ecorate > 3.5 and ecorate <= 4.5:
        point += 4
    elif ecorate > 2 and ecorate <= 3.5:
        point += 7
    elif ecorate <= 2:
        point += 10
    point += (field * 10)
    return int(point)


def allscore(pl, mt):
    curScore.execute("select * from match where name ='" + mt + "' and player = '" + pl + "';")
    record = curScore.fetchall()
    runs = int(record[0][1])
    balls = int(record[0][2])
    four = int(record[0][3])
    six = int(record[0][12])
    field = int(record[0][8]) + int(record[0][9]) + int(record[0][10])
    wkts = int(record[0][7])
    overs = int(record[0][4])
    given = int(record[0][6])
    point = 0
    point += int(runs / 2)
    if runs > 100:
        point += 10
    elif runs > 50 and runs < 100:
        point += 5
    strike = (runs / balls) * 100
    if strike > 100:
        point += 4
    elif strike >= 80 and strike <= 100:
        point += 2
    point += (four + (six * 2) + (field * 10))
    point += (wkts * 10)
    if wkts >= 5:
        point += 10
    elif wkts == 3:
        point += 5
    ecorate = given / overs
    if ecorate > 3.5 and ecorate <= 4.5:
        point += 4
    elif ecorate > 2 and ecorate <= 3.5:
        point += 7
    elif ecorate <= 2:
        point += 10
    return int(point)

