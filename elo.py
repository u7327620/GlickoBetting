class Elo:

    def __init__(self, k, g=1, homefield=100):
        self.ratingDict = {}
        self.k = k
        self.g = g
        self.homefield = homefield

    def addPlayer(self, name, rating=1500):
        self.ratingDict[name] = rating

    def gameOver(self, winner, loser, winnerHome):
        if winnerHome == "True":
            result = self.expectResult(self.ratingDict[winner] + self.homefield, self.ratingDict[loser])
        else:
            result = self.expectResult(self.ratingDict[winner], self.ratingDict[loser] + self.homefield)

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