import re

ann = re.compile(r"\s+Ann \{")
vector = re.compile(r"  V \{")
loop_open = re.compile(r"  Loop (?P<loop>\d+) ")

cycle_count = 0
with open('sample.stil','r') as f :
    for line in f:
        is_ann = ann.search(line)
        is_loop_open = loop_open.search(line)
        is_vector = vector.search(line)

        if is_ann : 
            print(line,end="")
        if is_loop_open  : 
            cycle_count = cycle_count - 1
        if is_vector :
            print('Ann * Cycle Number:{} *'.format(cycle_count))
            cycle_count = cycle_count + 1

