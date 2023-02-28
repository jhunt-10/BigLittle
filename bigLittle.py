

"""
1) Run thru frosh, if there exists a 1 to 1 relationship, match, and remove frosh from queue
    a) update the exisiting sophs pref lists, removing any frosh that were filled
2) Run thru frosh, if there exists a 1 to 2 relationship, match, and remove frosh from queue, 
    if a soph has 2 littles, remove them from queue
    a) update exisiting sophs pref lists, removing where any forsh were filled.
    b) update remaining frosh pref lists, removing any sophs that are filled
3) Run thru soph, if there exists 2 to 1 relationship, match, and remove frosh from queue,
    if a soph has 2 littles remove them from the queue
    a) update remaining sophs pref list, removing frosh who were filled.
    b) update remaing frosh pref list, removing sophs who were filled.

1. 
"""
sophies = ["James",
           "Spencer",
           "Remi",
           "Jonty",
           "MP",
           "Wayne",
           "Ethan B",
           "Lucas",
           "Andres",
           "Koch",
           "Bello",
           "Tona",
           "AVL",
           "Eric",
           "Cappy",
           "CJ",
           "Cronin",
           "Luis",
           "Juan GL",
           "Abel",
           "Juanchi A",
           "Jack F"]

sophies1 = ["Karem",
            "Nico",
            "Ted Sod",
            "Carlos P",
            "Teddy N",
            "Banit",
            "Charlie",
            "Charlie",
            "Carlos P",
            "Kellan",
            "Rigby",
            "Chamo",
            "Rigby",
            "Nico",
            "Karem",
            "Karem",
            "Blake",
            "JP",
            "Vidal",
            "Preston",
            "Preston",
            "Preston"]

sophies2 = ["Vidal",
            "Teddy N",
            "Otto",
            "Leo",
            "Blake",
            "Rigby",
            "Dylan C",
            "Karem",
            "Nico",
            "Kahne",
            "Ahnaf",
            "Nico",
            "Banit",
            "Leo",
            "Carlos P",
            "Teddy N",
            "Jake F",
            "Carlos V",
            "Nico",
            "Preston",
            "Preston",
            "Preston"]

sophies3 = ["Charlie",
            "JP",
            "Karam",
            "Chamo",
            "Kupe",
            "Otto",
            "Ben K",
            "Ben K",
            "Leo",
            "Jasper",
            "Karam",
            "Leo",
            "Ahnaf",
            "Carlos P",
            "Dylan R",
            "Charlie",
            "Teddy N",
            "Rigby",
            "Ethan F",
            "Preston",
            "Preston",
            "Preston"]

sophies4 = ["Jake F",
            "Connor",
            "Chase",
            "Vidal",
            "Leo",
            "Ted Sod",
            "Ethan F",
            "JP",
            "Carlos V",
            "Ahnaf",
            "Drew",
            "JP",
            "Ethan F",
            "Ahnaf",
            "Carlos V",
            "Kellan",
            "Kupe",
            "Kupe",
            "Kellan",
            "Preston",
            "Preston",
            "Preston"]

froshies = ["Teddy N",
            "Rigby",
            "Kupe",
            "Carlos P",
            "Otto",
            "Jasper",
            "Carlos V",
            "Charlie",
            "Nico",
            "Alain",
            "Jake F",
            "Ahnaf",
            "Blake",
            "Dylan R",
            "Dylan C",
            "Vidal",
            "JP",
            "Ethan F",
            "Ben K",
            "Leo",
            "Drew",
            "Chamo",
            "Preston",
            "Kellan",
            "Banit",
            "Connor",
            "Karam",
            "Chase",
            "Karem",
            "Ted Sod"]

froshies1 = ["MP",
             "AVL",
             "Luis",
             "Andres",
             "Remi",
             "Jack F",
             "Andres",
             "Ethan B",
             "Eric",
             "Eric",
             "Cronin",
             "MP",
             "Lucas",
             "Cappy",
             "Jack F",
             "Juan GL",
             "Luis",
             "Juan GL",
             "Ethan B",
             "Eric",
             "Koch",
             "Tona",
             "Ethan B",
             "Jack F",
             "Wayne",
             "Spencer",
             "Jonty",
             "Bello",
             "Cappy",
             "Remi"]

froshies2 = ["Juan GL",
             "Jonty",
             "MP",
             "Tona",
             "Jonty",
             "Ethan B",
             "Luis",
             "Koch",
             "Andres",
             "Andres",
             "Jack F",
             "AVL",
             "Cronin",
             "Koch",
             "Koch",
             "Jonty",
             "Juan GL",
             "James",
             "Cappy",
             "Juanchi A",
             "Eric",
             "Juanchi A",
             "Spencer",
             "Koch",
             "Jonty",
             "Ethan B",
             "Andres",
             "Eric",
             "MP",
             "Abel"]

froshies3 = ["James",
             "James",
             "Juanchi A",
             "Jack F",
             "Abel",
             "Koch",
             "Juanchi A",
             "Lucas",
             "Spencer",
             "Koch",
             "James",
             "Juan GL",
             "Jonty",
             "Jack F",
             "Spencer",
             "Juanchi A",
             "Juanchi A",
             "Ethan B",
             "Koch",
             "Jonty",
             "Ethan B",
             "Andres",
             "James",
             "Lucas",
             "AVL",
             "James",
             "Remi",
             "Abel",
             "Cronin",
             "Abel"]


j = 0


frosh_remaining = set()
soph_remaining = set()
froshes = {}
sophs = {}
matches = {}
while True:
    fro = froshies[j]
    frosh_remaining.add(fro)
    froshes[fro] = []
    froshes[fro].append(froshies1[j])
    froshes[fro].append(froshies2[j])
    froshes[fro].append(froshies3[j])
    j += 1
    print(j)
    if j > 29:
        break

j = 0
while True:
    so = sophies[j]
    soph_remaining.add(so)
    sophs[so] = []
    sophs[so].append(sophies1[j])
    sophs[so].append(sophies2[j])
    sophs[so].append(sophies3[j])
    sophs[so].append(sophies4[j])
    sophs[so].append(0)
    j += 1
    if j > 21:
        break

doubles = 0

# 1-1 iteration
f = 0  # frosh pref number
s = 0  # soph pref number

iteration = 0
iterations = [(1, 1), (1, 2), (2, 1), (1, 3), (2, 2), (3, 1),
              (1, 4), (2, 3), (3, 2), (3, 3), (2, 4), (3, 4)]

while iteration < 12:
    f = iterations[iteration][0] - 1
    s = iterations[iteration][1] - 1
    potentials = {}
    for frosh in list(frosh_remaining):
        soph = froshes[frosh][f]  # soph at the fth pref of the current frosh

        # if frosh at sth pref of the soph == frosh and soph doesn't already have 2 littles
        if frosh == sophs[soph][s] and soph in soph_remaining:
            # sophs[soph][-1] points to the number of littles soph has, if soph has 0 littles, give them this frosh
            if sophs[soph][-1] == 0:
                matches[soph] = []
                matches[soph].append(frosh)
                sophs[soph][-1] = sophs[soph][-1] + 1
                frosh_remaining.remove(frosh)
                if sophs[soph][-1] >= 2:
                    soph_remaining.remove(soph)
            elif sophs[soph][-1] == 1:  # if soph already has 1 little,
                # add them to potential so that later we can check to make sure we aren't creating more than 8 double littles
                potentials[soph] = frosh
    # after iterating thru all the remainging frosh
    # check the size of potentials, if doubles + size <= 8, add all potentials
    if len(potentials.keys()) + doubles <= 8 and len(potentials.keys()) != 0:
        doubles += len(potentials.keys())
        for soph, frosh in potentials.items():  # iterate thru all in potentials
            # at each iteration add the frosh to that sophs matches
            matches[soph].append(frosh)
            sophs[soph][-1] = sophs[soph][-1] + 1
            # remove soph now that they have 2 littles
            soph_remaining.remove(soph)
            # remove frosh now that they have a big
            frosh_remaining.remove(frosh)
    elif len(potentials.keys()) + doubles > 8:
        # might have to get creative here
        # this is where randomness might have to come into play
        # if this is the case then there are now more than 8 qualified sophs for a double little
        # let's say that there are 5 soph's with a double little after 1 to 2 checks
        # this is the earliest point after which you could see a double little since you cant see a double little after 1 to 1
        # further, let's assume there are then 4 sophs qualified for a second little after 2 to 1 check
        # now since, we already have 5 sophs with two littles, and thus only 3 more double little spots open, we need to decide how to choose 3 of
        # the 4 qualified sophs after 2 to 1 check
        # the only reasonably fair way it would seem to do this would be to randomly choose 3 of the 4
        pass
    potentials = {}
    iteration += 1

for soph in list(soph_remaining):
    if sophs[soph][-1] == 1:
        soph_remaining.remove(soph)

for k, v in matches.items():
    if len(v) == 1:

        print(f"Big is : {k} -> {v[0]}")
    if len(v) == 2:
        l = 1
        f_rel = None
        s_rel = None
        for s in froshes[v[1]]:
            if s == k:
                f_rel = l
                break
            l += 1
        l = 1
        for f in sophs[k]:
            if f == v[1]:
                s_rel = l
                break
            l += 1
        print(f"Big is : {k} -> {v[0]} and {v[1]} ({f_rel}, {s_rel})")

for frosh in frosh_remaining:
    print(f"{frosh} is left")
for soph in soph_remaining:
    print(f"{soph} is left")
