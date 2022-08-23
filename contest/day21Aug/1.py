initialEnergy = 5
initialExperience = 3
energy = [1, 4, 3, 2]

experience = [2, 6, 3, 1]

add_energy = max(0, sum(energy) + 1 - initialEnergy)
add_experience = max(0, experience[0] - initialExperience + 1)
res = add_energy + add_experience


initialExperience = initialExperience + add_experience


for i in range(len(experience)):
    if initialExperience > experience[i]:
        initialExperience += experience[i]

    else:
        res += (experience[i] - initialExperience + 1)
        initialExperience += (experience[i] - initialExperience + 1)


print(res)
