with open("inputs/day07.txt") as inp:
    lines = inp.read().splitlines()
    
data = {}
results = {}

for line in lines:
    left, right = line.split(" -> ")
    try:
        data[right] = int(left)
    except Exception:
        data[right] = left
    
i=0
while True:
    i +=1 
    print(i)
    for key, value in data.items():
        if isinstance(value, int):
            if not key in results.keys():
                results[key] = value
        else:
            equation = value.split(" ")
            
            if len(equation) == 1:
                if equation[0] in results:
                    results[key] = int(results[equation[0]])
                continue

            match equation[1]:
                case "AND":
                    if equation[0] in results.keys():
                        data[key] = data[key].replace(equation[0], str(results[equation[0]]))
                    if equation[2] in results.keys():
                        data[key] = data[key].replace(equation[2], str(results[equation[2]]))
                    try:
                        tmp = int(equation[0]) & int(equation[2])
                        results[key] = tmp
                    except Exception:
                        pass
                case "OR":
                    if equation[0] in results.keys():
                        data[key] = data[key].replace(equation[0], str(results[equation[0]]))
                    if equation[2] in results.keys():
                        data[key] = data[key].replace(equation[2], str(results[equation[2]]))
                    try:
                        tmp = int(equation[0]) | int(equation[2])
                        results[key] = tmp
                    except Exception:
                        pass
                case "LSHIFT":
                    if equation[0] in results.keys():
                        data[key] = data[key].replace(equation[0], str(results[equation[0]]))
                    try:
                        tmp = int(equation[0]) << int(equation[2])
                        results[key] = tmp
                    except Exception:
                        pass
                case "RSHIFT":
                    if equation[0] in results.keys():
                        data[key] = data[key].replace(equation[0], str(results[equation[0]]))
                    try:
                        tmp = int(equation[0]) >> int(equation[2])
                        results[key] = tmp
                    except Exception:
                        pass
                case _: # NOT
                    if equation[1] in results.keys():
                        data[key] = data[key].replace(equation[1], str(results[equation[1]]))
                    try:
                        tmp = ~int(equation[1]) & 0xFFFF
                        results[key] = tmp
                    except Exception:
                        pass
                    
    
    if "a" in results.keys():
        break
    
print(results['a'])