# 1

def read_file(name_file, lines):
    with open(f"{name_file}",'r',encoding= 'utf-8') as file:
        for i, line in enumerate(file):
            if (i + 1) <= lines:
                print(line.strip())
            else:
                break

read_file("./data/text.txt",4)

# 2 - Alternative
print("-"*40)
def file_read_from_line(fname, nlines):
        from itertools import islice
        with open(fname, encoding="utf-8") as f:
                for line in islice(f, nlines):
                        print(line.strip())
file_read_from_line('./data/text.txt',2)
