import re 

with open("inputs/day09.txt") as inp:
    lines = inp.read().splitlines()
    
    
cities = set()

distances = {}
    
    
for line in lines:
    source, destination, distance = re.match("([A-Za-z]{1,}) to ([A-Za-z]{1,}) = ([0-9]{1,})", line).groups()
    
    cities.add(source)
    cities.add(destination)
    
    distances[(source, destination)] = int(distance)
    distances[(destination, source)] = int(distance)
    
DP_matrix = {}

for city in cities:
    DP_matrix[(city)] = 0
    
def dp(S, i):
    pass
