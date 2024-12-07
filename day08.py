import ast
with open("inputs/day08.txt") as inp:
    lines = inp.read().splitlines()
    
with open("output_rust.txt") as inp:
    rustoutput = inp.read().splitlines()
    
literal_length = sum([len(x) for x in lines])
normal_length = sum([len(ast.literal_eval(x)) for x in lines])
print(literal_length, normal_length, literal_length-normal_length)
