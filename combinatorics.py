#!/usr/bin/env python3

def tucker_5_1_37():
    faces = [1, 2, 3, 4, 5, 6]
    rolls = lambda: ((i, j, k)
                for i in faces
                for j in faces
                for k in faces
                if min(i, j, k) == max(i, j, k) / 2)

    rolls_2 = [roll for roll in rolls()
               if len(set(roll)) == 2]

    rolls_3 = [roll for roll in rolls()
               if len(set(roll)) == 3]

    for roll in sorted(map(sorted, rolls_2)):
        print(sorted(roll))

    print()

    for roll in sorted(map(sorted, rolls_3)):
        print(sorted(roll))

    print()

    numer = len(rolls_2) + len(rolls_3)

    denom = 6**3
    return (numer, denom)

print(tucker_5_1_37())
