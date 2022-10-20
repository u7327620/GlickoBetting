import functions

bets = [0, 0]
for i in range(10, 23):
    x = functions.shouldbet(i+1)
    x = x.split(", ")
    print(x)
    if int(x[0]) > 0:
        bets[0] += int(x[0]) 
        bets[1] += int(x[1])
percentCorrect = bets[0]/bets[1]
print(f"{int(percentCorrect*100)}% are correct or {bets[0]} out of {bets[1]}")


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
