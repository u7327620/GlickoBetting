homeField = {
    'Adelaide': 'Adelaide Oval',
    'Brisbane Lions': 'GABBA, ' 'Brisbane Oval',
    'Carlton': 'Docklands, ' 'M.C.G.',
    'Collingwood': 'M.C.G., ' 'Melbourne',
    'Essendon': 'Docklands, ' 'M.C.G.',
    'Fremantle': 'Optus Stadium, ' 'Subiaco',
    'Geelong': 	'Kardinia Park, ' 'Geelong',
    'Gold Coast': 'Carrara',
    'Greater Western Sydney': 'Sydney Showground Stadium, ' 'Manuka Oval',
    'Hawthorn': 'M.C.G.',
    'North Melbourne': 'Docklands, ' 'Bellerive Oval',
    'Melbourne': 'M.C.G.',
    'Richmond': 'M.C.G.',
    'St Kilda': 'Docklands',
    'Sydney': 	'S.C.G., ' 'Stadium Australia, ' 'Sydney Showground',
    'West Coast': 'Subiaco, ' 'Optus Stadium',
    'Western Bulldogs': 'Docklands',
    'Port Adelaide': 'Adelaide Oval'
}

def convert(file):
    # step 1, removing useless information
    with open(f"rounds/{file}", "r") as f:
        # 1st line is odd
        lineodd = True
        outlines = []
        for line in f:
            words = line.split("\t")
            words.pop(1)
            if lineodd:
                venue = words[2].split("Venue: ")
                date = venue[0].split("2015")
                date = date[0].rstrip("-")
                venue[1] = venue[1].replace("\n", "")
                words.pop(2)
                words.append(venue[1])
                words.append(date)
                lineodd = False
            else:
                words.pop(2)
                lineodd = True
            print(words)
            words = "\t".join(words)
            outlines.append(f'{words}\n')
        f.close()
    with open(f"rounds/{file}", "w") as f:
        f.writelines(outlines)
        f.close()

    # step 2, converting for the other file
    with open(f"rounds/{file}", 'r') as f:
        secondline = False
        final = []
        for line in f:
            out = []
            line = line.split('\t')
            line[len(line)-1] = line[len(line)-1].rstrip("\n")

            if secondline:
                if int(lastline[1]) > int(line[1]):
                    out.append(lastline[0])
                    out.append(line[0])
                    out.append(int(lastline[1]) - int(line[1]))
                elif int(lastline[1]) == int(line[1]):
                    pass
                else:
                    out.append(line[0])
                    out.append(lastline[0])
                    out.append(int(line[1]) - int(lastline[1]))

                if lastline[2] in homeField[out[0]].split(", "):
                    out.append("True")
                else:
                    out.append("False")
                secondline = False
                final.append(out)

            else:
                lastline = line
                secondline = True
        f.close()
    with open(f"rounds/{file}", 'w') as f:
        for list in final:
            i = 0
            for item in list:
                list[i] = str(item)
                i += 1
            print(list)
            tmp = "\t".join(list)
            f.writelines(f'{tmp}\n')
        f.close()
convert("r23.txt")
