with open("./2015/2015-16/input.txt", "r") as inputText:
    aunts = inputText.readlines()

aunt_identifier = 0
for aunt in aunts:
    words = aunt.split()
    children, cats, samoyeds, pomerians, akitas, vizslas, goldfish, trees, cars, perfumes = None, None, None, None, None, None, None, None, None, None
    if "children:" in words and int((words[words.index("children:") + 1]).removesuffix(",")) != 3:
        continue
    if "cats:" in words and int((words[words.index("cats:") + 1]).removesuffix(",")) <= 7:
        continue
    if "samoyeds:" in words and int((words[words.index("samoyeds:") + 1]).removesuffix(",")) != 2:
        continue
    if "pomeranians:" in words and int((words[words.index("pomeranians:") + 1]).removesuffix(",")) >= 3:
        continue
    if "akitas:" in words and int((words[words.index("akitas:") + 1]).removesuffix(",")) != 0:
        continue
    if "vizslas:" in words and int((words[words.index("vizslas:") + 1]).removesuffix(",")) != 0:
        continue
    if "goldfish:" in words and int((words[words.index("goldfish:") + 1]).removesuffix(",")) >= 5:
        continue
    if "trees:" in words and int((words[words.index("trees:") + 1]).removesuffix(",")) <= 3:
        continue
    if "cars:" in words and int((words[words.index("cars:") + 1]).removesuffix(",")) != 2:
        continue
    if "perfumes:" in words and int((words[words.index("perfumes:") + 1]).removesuffix(",")) != 2:
        continue

    aunt_identifier = int(words[1][:-1])
    break  # Only one possible answer, no need to continue parsing

print(aunt_identifier)
