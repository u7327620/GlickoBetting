import functions



""" use this for betting tips
roundslist = []
for i in range(10, 22):
    x = functions.shouldbet(i+1)
    x = x.split(", ")
    if int(x[0]) > 0:
        tmp = int(x[0])/int(x[1])
        roundslist.append(tmp)
print(roundslist)
tmp = 0
for float in roundslist:
    tmp += float
tmp = tmp/len(roundslist)
print(int(tmp*100), "% of bets will win money")
"""
""" use this for pure elo percentaging
percentRight = 50.0
for i in range(10, 22):
    x = functions.predictions(i+1, funny=True)
    x = x.split(", ")
    percentRight = (percentRight + int(x[0])/int(x[1]))/2
print(int(percentRight*100), "% correct")
"""