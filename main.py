import functions




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
out=[]
for i in range(10, 23):
    x = functions.predictions(i+1, funny=True)
    x = x.split(", ")
    out.append(int(x[0])/int(x[1]))
percentRight = 0
for percent in out:
    percentRight += percent
percentRight = percentRight/int(len(out))
print(int(percentRight*100), "% correct")
"""