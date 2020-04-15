
def grep(pattern, flags, files):
    n, l, i, v, x  = "-n" in flags, "-l" in flags, "-i" in flags ,"-v" in flags, "-x" in flags

    pattern = pattern.lower() if i else pattern
    b = len(files) > 1
    res = ""
    for file in files:
        with open(file, 'r') as f:
            for num, line in enumerate(f.readlines()):
                case_i = line.lower() if i else line
                if v ^ (not x and pattern in case_i
                        or pattern + '\n' == case_i):
                    if l:
                        res += file + "\n"
                        break
                    res += (f"{file}:" if b else '') + \
                        (f"{num +1}:" if n else '') + line
    return res
