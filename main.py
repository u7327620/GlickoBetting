import functions
import elo

# M value section
"""
modeled = [0, 0]
for i in range(23):
    total = 0
    succ = 0
    x = functions.doRounds(i+1)
    print(f"Round number: {i+1}")
    with open(f'rounds/r{i+1}.txt', 'r') as round:
        for lines in round:
            lines = lines.split("\t")
            string, out = x.mValue(lines[0], lines[1], currRound=i+1)
            total += 1
            modeled[1] += 1
            print(string)
            out = out.split(" to ")
            out[0] = int(out[0])
            out[1] = int(out[1])
            lines[2] = int(lines[2])
            if lines[2] > out[0] and lines[2] < out[1]:
                succ += 1
                modeled[0] += 1
    print(f"M value succesfully modeled {succ} out of {total}")
print(f"A total of {modeled[0]} out of {modeled[1]} or {int(modeled[0]/modeled[1]*100)}% were modeled correctly")

"""

"""
bets = [0, 0]
first = True
for i in range(10, 23):
    x = functions.shouldbet(i+1, first)
    first = False
    x = x.split(", ")
    print(x)
    if int(x[0]) > 0:
        bets[0] += int(x[0]) 
        bets[1] += int(x[1])
percentCorrect = bets[0]/bets[1]
print(f"{int(percentCorrect*100)}% are correct or {bets[0]} out of {bets[1]}")

"""
out=[]
first = True
for i in range(23):
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

