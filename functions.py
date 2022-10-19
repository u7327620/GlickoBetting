import elo

eloMaster = elo.Elo(k=32)

def teaminit() :
    with open("rounds/r1.txt", "r") as round:
        for line in round:
            words = line.split("\t")
            eloMaster.addPlayer(str(words[0]))
            eloMaster.addPlayer(str(words[1]))
        round.close()

def doRounds(rounds):
    for i in range(rounds):
        with open(f"rounds/r{i+1}.txt", "r") as round:
            for line in round:
                words = line.split("\t")
                words[3] = words[3].rstrip("\n")
                eloMaster.gameOver(winner=str(words[0]), loser=str(words[1]), winnerHome=words[3])
    return eloMaster.listResult()