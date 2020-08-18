"""CPU functionality."""

import sys

class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""
        self.mem = [0] * 256
        self.address = 0
        self.pc = 0
        self.running = False

    def load(self):
        """Load a program into memory."""

        address = 0

        # For now, we've just hardcoded a program:

        program = [
            # From print8.ls8
            0b10000010, # LDI R0,8
            0b00000000,
            0b00001000,
            0b01000111, # PRN R0
            0b00000000,
            0b00000001, # HLT
        ]

        for instruction in program:
            self.mem[address] = instruction
            address += 1

    """
    def alu(self, op, reg_a, reg_b):

        if op == "ADD":
            self.reg[reg_a] += self.reg[reg_b]
        #elif op == "SUB": etc
        else:
            raise Exception("Unsupported ALU operation")
            """
    def trace(self):
        """
        Handy function to print out the CPU state. You might want to call this
        from run() if you need help debugging.
        """

        print(f"TRACE: %02X | %02X %02X %02X |" % (
            self.pc,
            #self.fl,
            #self.ie,
            self.ram_read(self.pc),
            self.ram_read(self.pc + 1),
            self.ram_read(self.pc + 2)
        ), end='')

        for i in range(8):
            print(" %02X" % self.reg[i], end='')

        print()
    def ram_read(self, addr):
        return self.mem[addr]
    
    def ram_write(self, value, addr):
        self.mem[addr] = value
    
    def run(self):
        """Run the CPU."""
        reg = [0]*8
        running = True
        while running:
            inst = self.ram_read(self.pc)
            if inst == 1:
                running = False
            elif inst == 130:
                reg_index = self.mem[self.pc + 1]
                reg_value = self.mem[self.pc + 2]
                self.mem[reg_index] = reg_value
                self.pc += 3
            elif inst == 71:
                print(self.mem[reg[self.pc + 1]])
                self.pc += 2