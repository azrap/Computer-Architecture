import sys

# python3 file.py filename

if len(sys.argv) != 2:
    print("Usage: file.py filename", file=sys.stderr)
    sys.exit(1)
try:
    with open(sys.argv[1]) as f:
        commands = []
        for line in f:
            # ignore comments & white space
            comment_split = line.split("#")

            num = comment_split[0].strip()
            x = int(num, 2)
            # print("{:08b}:{:d}".format(x, x))
            # print it out in 8bit string and decimal
            # print(f"{x:08b}:{x:d}")
            commands.append(num)
        print([int(c, 2)for c in commands])

except FileNotFoundError:
    print(f'{sys.argv[0]}: {sys.argv[1]} not found')
