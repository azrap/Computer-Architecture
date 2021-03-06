"""CPU functionality."""

import sys


class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""
        self.ram = [0] * 16
        self.reg = [0] * 8
        self.pc = 0
        self.stack = 0

    def load(self):

        address = 0
        try:

            with open(sys.argv[1]) as f:
                for line in f:
                    # ignore comments & white space
                    comment_split = line.split("#")
                    num = comment_split[0].strip()
                    if num == "":
                        continue
                    value = int(num, 2)  # binary
                    self.ram[address] = value
                    address += 1

        except FileNotFoundError:
            print(f'{sys.argv[0]}: {sys.argv[1]} not found')
            sys.exit(2)

        print(self.ram)

    # def load(self):
    #     """Load a program into memory."""

    #     address = 0

    #     # For now, we've just hardcoded a program:

    #     program = [
    #         # From print8.ls8
    #         0b10000010,  # LDI R0,8
    #         0b00000000,
    #         0b00001000,
    #         0b01000111,  # PRN R0
    #         0b00000000,
    #         0b00000001,  # HLT
    #     ]

    #     for instruction in program:
    #         self.ram[address] = instruction
    #         address += 1

    def alu(self, op, reg_a, reg_b):
        """ALU operations."""

        if op == "ADD":
            self.reg[reg_a] += self.reg[reg_b]
        elif op == 'MUL':
            self.reg[reg_a] *= self.reg[reg_b]
        else:
            raise Exception("Unsupported ALU operation")

    def ram_read(self, address):
        return self.ram[address]

    def ram_write(self, address, value):
        self.ram[address] = value

    def trace(self):
        """
        Handy function to print out the CPU state. You might want to call this
        from run() if you need help debugging.
        """

        print(f"TRACE: %02X | %02X %02X %02X |" % (
            self.pc,
            # self.fl,
            # self.ie,
            self.ram_read(self.pc),
            self.ram_read(self.pc + 1),
            self.ram_read(self.pc + 2)
        ), end='')

        for i in range(8):
            print(" %02X" % self.reg[i], end='')

        print()

    def run(self):
        """Run the CPU."""
        # IR = self.ram_read(self.pc)
        # operand_a = self.ram_read(self.pc+1)
        # operand_b = self.ram_read(self.pc+2)
        HLT = 0b00000001
        LDI = 0b10000010
        PRN = 0b01000111
        MUL = 0b10100010

        running = True

        while running:

            IR = self.ram_read(self.pc)  # loads the instruction

            operand_a = self.ram_read(self.pc+1)
            operand_b = self.ram_read(self.pc+2)

            if IR == LDI:  # loads the 8 into the register

                self.reg[operand_a] = operand_b
                self.pc += 3

            elif IR == PRN:
                index = self.ram_read(self.pc+1)
                print(self.reg[index])
                self.pc += 2

            elif IR == MUL:
                self.alu('MUL', operand_a, operand_b)
                self.pc += 3

            elif IR == HLT:
                running = False
                self.pc += 1

            else:
                print(f"unknown instruction at index {self.pc}")
                sys.exit(1)
