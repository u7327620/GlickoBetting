import functions
import elo

# M value section

for i in range(23):
    x = functions.doRounds(i+1)
    print(f"Round number: {i}")
    with open(f'rounds/r{i+1}.txt', 'r') as round:
        for lines in round:
            lines = lines.split("\t")
            print(x.mValue(lines[0], lines[1]))

"""
bets = [0, 0]
first = True
for i in range(23):
    x = functions.shouldbet(i+1, first)
    first = False
    x = x.split(", ")
    print(x)
    if int(x[0]) > 0:
        bets[0] += int(x[0]) 
        bets[1] += int(x[1])
percentCorrect = bets[0]/bets[1]
print(f"{int(percentCorrect*100)}% are correct or {bets[0]} out of {bets[1]}")


out=[]
first = True
for i in range(10, 23):
    x, thiselo = functions.predictions(i+1, funny=True, first=first)
    first = False
    x = x.split(", ")
    out.append(int(x[0])/int(x[1]))
percentRight = 0
for percent in out:
    percentRight += percent
percentRight = percentRight/int(len(out))
print(int(percentRight*100), "% correct")
thiselo.listResult()
"""
