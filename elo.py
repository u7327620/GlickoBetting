class Elo:

    def __init__(self, k, g=1, homefield=100):
        self.ratingDict = {}
        self.k = k
        self.g = g
        self.homefield = homefield

    def addPlayer(self, name, rating=1500):
        self.ratingDict[name] = rating

    def gameOver(self, winner, loser, winnerHome, k=0):
        if winnerHome == "True":
            result = self.expectResult(self.ratingDict[winner] + self.homefield, self.ratingDict[loser])
        else:
            result = self.expectResult(self.ratingDict[winner], self.ratingDict[loser] + self.homefield)
        if k:
            self.ratingDict[winner] = self.ratingDict[winner] + (k * self.g) * (1 - result)
            self.ratingDict[loser] = self.ratingDict[loser] + (k * self.g) * (0 - (1 - result))
        else:
            self.ratingDict[winner] = self.ratingDict[winner] + (self.k * self.g) * (1 - result)
            self.ratingDict[loser] = self.ratingDict[loser] + (self.k * self.g) * (0 - (1 - result))

    def getElo(self, team):
        return self.ratingDict[team]

    def expectResult(self, p1, p2):
        exp = (p2 - p1) / 400.0
        return 1.0 / (1.0 + 10.0 ** (exp))

    def listResult(self):
        for player in self.ratingDict:
            print(f'{player} is: {int(self.ratingDict[player])} elo')

    def previousMatchLookup(self, p1, p2, currRound):
        for i in range(currRound):
            with open(f"rounds/r{i+1}.txt", "r") as round:
                for line in round:
                    line = line.split("\t")
                    if line[0] == p1 and line[1] == p2 or line[0] == p2 and line[1] == p1:
                        return int(line[2])
        return 0


    def mValue(self, p1, p2, currRound):
        x = self.previousMatchLookup(p1, p2, currRound)
        p1name = p1
        p2name = p2
        p1 = self.ratingDict[p1]
        p2 = self.ratingDict[p2]
        if p2-p1 > 200:
            p1 = p2-200
            tmp = abs(1 / 5 * (p2 - p1))
        elif p1-p2 > 200:
            p2 = p1-200
            tmp = abs(1 / 5 * (p1 - p2))
        else:
            if p1 > p2:
                tmp = abs(1 / 5 * (p1 - p2))
            elif p2 > p1:
                tmp = abs(1 / 5 * (p2 - p1))
            else:
                tmp = 0
        if x > 0: # it returns 0 if there is no previous match
            out = f"{int(x-tmp/2)} to {int(x+tmp/2)}"
        else:
            out = tmp
        string = f"{p1name} vs {p2name} has a M value of: {out}"
        return string, out