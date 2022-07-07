"""In a small town the population is p0 at the beginning of a year. The population regularly increases by a percent per year and moreover 50 new inhabitants (aug) per year come to live in the town. How many years does the town need to see its population greater or equal to p = p inhabitants?"""

def nb_year(p0, percent, aug, p):
    result = p0
    n = 0
    while p > result:
        result = int(result * (1 + (percent / 100)) + aug)
        n +=1
    return n

print(nb_year(1000, 2, 50, 1214))