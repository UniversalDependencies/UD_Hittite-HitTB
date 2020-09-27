import os
import re
from collections import Counter


variant_strs = ['OH', 'MH', 'NH', 'OS', 'MS', 'NS', 'OH/NS', 'MH/NS', 'OH/MS', 'OH/OS', 'NH/NS', 'MH/MS', 'NH/NS']

if __name__ == "__main__":
    input_file = os.path.join(os.path.curdir, "hit_hittb-ud-test.conllu")
    with open(input_file, "r", encoding="utf-8") as f:
        file_lines = f.readlines()
        pos_count = Counter()
        deprel_count = Counter()
        deprel_pos_count = Counter()
        variant_counts = Counter()
        sources = []
        for line in file_lines:
            if line[0] == '#' or line == '\n':
                if 'source' in line:
                    sources.append(line.strip())
                    print(line)
                    for x in variant_strs:
                        if x in line:
                            variant_counts[x] += 1
                            break
                continue
            line_split = line.split("\t")
            if "-" in line_split[0]:
                continue
            pos_tag = line_split[3]
            dep_rel = line_split[7]
            dep_pos = (pos_tag, dep_rel)
            pos_count[pos_tag] += 1
            deprel_count[dep_rel] += 1
            deprel_pos_count[dep_pos] += 1
    for (k, v) in sorted(pos_count.items(), key=lambda t:t[1]):
        print(k + ": " + str(v) + " " + str(v/sum(pos_count.values())))
    for (k, v) in sorted(deprel_count.items(), key=lambda t:t[1]):
        print(k + ": " + str(v))
    for (k, v) in sorted(deprel_pos_count.items(), key=lambda t:t[0]):
        print(str(k) + ": " + str(v))
    print(sum(pos_count.values()))
    print(sum(deprel_count.values()))
    print(sum(deprel_pos_count.values()))
    for item in sorted(sources):
        print(item)
    print(len(sources))
    for (k, v) in variant_counts.items():
        print(k + ": " + str(v))
    
            

