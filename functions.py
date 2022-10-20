import elo


def teaminit(elostore):
    with open("rounds/r1.txt", "r") as round:
        for line in round:
            words = line.split("\t")
            elostore.addPlayer(str(words[0]))
            elostore.addPlayer(str(words[1]))
        round.close()


def doRounds(rounds):
    eloMaster = elo.Elo(k=32)
    teaminit(eloMaster)
    for i in range(rounds):
        with open(f"rounds/r{i + 1}.txt", "r") as round:
            for line in round:
                words = line.split("\t")
                words[3] = words[3].rstrip("\n")
                eloMaster.gameOver(winner=str(words[0]), loser=str(words[1]), winnerHome=words[3])
    return eloMaster

def predictions(round, show=False, funny=False):
    print(f"Round number: {round}")
    thisElo = doRounds(round - 1)
    with open(f"rounds/r{round}.txt", "r") as round1:
        for line in round1:
            line = line.split("\t")
            if show:
                print(
                    f'The Chance of {line[0]} beating {line[1]} is: {int(100*thisElo.expectResult(thisElo.getElo(line[0]), thisElo.getElo(line[1])))}%')
        round1.close()
    total = 0
    succ = 0
    with open(f"rounds/r{round}.txt", "r") as round2:
        for line in round2:
            total += 1
            line = line.split("\t")
            if show:
                print(f'{line[0]} beat {line[1]}, I predicted a {int(100*thisElo.expectResult(thisElo.getElo(line[0]), thisElo.getElo(line[1])))}% chance of this')
            if funny:
                print(f'{line[0]} ({int(thisElo.getElo(line[0]))}) beat {line[1]} ({int(thisElo.getElo(line[1]))}), I predicted a {int(100*thisElo.expectResult(thisElo.getElo(line[0]), thisElo.getElo(line[1])))}% chance of this')
            if int(100*thisElo.expectResult(thisElo.getElo(line[0]), thisElo.getElo(line[1]))) > 50:
                succ += 1
        if show:
            print(f"That's roughly {succ} out of {total}")
        if funny:
            print(f"That's roughly {succ} out of {total}")
    return f"{succ}, {total}"

def shouldbet(round, margin=False):
    print(f"Round number: {round}")
    thisElo = doRounds(round - 1)
    with open(f"rounds/r{round}.txt", "r") as round1:
        for line in round1:
            line = line.split("\t")
            if int(100 * thisElo.expectResult(thisElo.getElo(line[0]), thisElo.getElo(line[1]))) > 70:
                print(f"{line[0]} ({int(thisElo.getElo(line[0]))}) has a {int(100 * thisElo.expectResult(thisElo.getElo(line[0]), thisElo.getElo(line[1])))}"
                      f"% chance of beating {line[1]}({int(thisElo.getElo(line[1]))}), you should bet")
            if int(100 * thisElo.expectResult(thisElo.getElo(line[0]), thisElo.getElo(line[1]))) < 30:
                print(f"{line[0]} has a {int(100 * thisElo.expectResult(thisElo.getElo(line[0]), thisElo.getElo(line[1])))}"
                      f"% chance of beating {line[1]}, you should bet")
    total = 0
    succ = 0
    with open(f"rounds/r{round}.txt", "r") as round2:
        for line in round2:
            line = line.split("\t")
            if int(100 * thisElo.expectResult(thisElo.getElo(line[0]), thisElo.getElo(line[1]))) > 70:
                total += 1
                succ += 1
            if int(100 * thisElo.expectResult(thisElo.getElo(line[0]), thisElo.getElo(line[1]))) < 30:
                total += 1
    return f"{succ}, {total}"