import os



if __name__ == '__main__':
    filename = "hit_hittb-ud-test.conllu"
    with open(filename) as f:
        for line in f.readlines():
            line_split = line.split("\t")
            if "_\t_\t_" in line and "-" not in line_split[0]:
                print(line)

