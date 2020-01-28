import sys

PRINT_BEEJ = 1
HALT = 2
SAVE_REG = 3
PRINT_REG = 4

memory = [
    PRINT_BEEJ,
    SAVE_REG,
    30,
    4,  # save 10 in register space R2
    PRINT_REG,  # print R2 out
    4,
    HALT
]

# like variables there's a fixed # of them, fixed names R0, R1, R2.... R7
register = [0]*8

pc = 0  # Program Counter

halted = False

while not halted:

    instruction = memory[pc]

    if instruction == PRINT_BEEJ:
        print("Beej!")
        pc += 1  # for each instruction we add a byte

    elif instruction == HALT:
        halted = True
        pc += 2

    elif instruction == PRINT_REG:
        reg_num = memory[pc+1]
        print(register[reg_num])
        pc += 2

    elif instruction == SAVE_REG:
        value = memory[pc+1]
        reg_num = memory[pc+2]
        register[reg_num] = value
        pc += 3

    else:
        print(f"unknown instruction at index {pc}")
        sys.exit(1)
