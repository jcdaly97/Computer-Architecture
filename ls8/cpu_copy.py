"""CPU functionality."""

import sys
LDI = 0b10000010
class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""
        self.mem = [0] * 256
        self.pc = 0
        self.running = False

    def load(self, arr = None):
        """Load a program into memory."""
        address = 0
        
        if arr:
            for inst in arr:
                self.mem[address] = inst
                address +=1
        """
        print('loading')
        if len(sys.argv) != 2:
            print(f"usage: {sys.argv[0]} filename")
            sys.exit(1)
        try:
            with open(sys.argv[1]) as f:
                for line in f:
                    num = line.split('#', 1)[0]
                    if num.strip() == '':  # ignore comment only lines
                        continue
                    num = int(num, 2)
                    self.mem[address] = num
                    address += 1
        except FileNotFoundError:
            print(f"{sys.argv[0]}: {sys.argv[1]} not found")
            sys.exit(2)
        """
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
            print(" %02X" % self.mem[i], end='')

        print()
    def ram_read(self, addr):
        return self.mem[addr]
    
    def ram_write(self, value, addr):
        self.mem[addr] = value
    
    def run(self):
        """Run the CPU."""
        reg = [0]*8
        sp = 7
        running = True
        while running:
            self.trace()
            inst = self.ram_read(self.pc)
            if inst == 1:
                running = False
            elif inst == 130:
                reg_index = self.mem[self.pc + 1]
                reg_value = self.mem[self.pc + 2]
                self.mem[reg_index] = reg_value
                self.pc += 3
            elif inst == 71:
                
                print(self.pc + 1)
                print(self.mem)
                print(reg)
                self.pc += 2
            elif inst == 162:
                num_1 = self.mem[self.ram_read(self.pc + 1)]
                num_2 = self.mem[self.ram_read(self.pc + 2)]
                print(num_1 * num_2)
                self.pc += 3
            elif inst == 69:
                print("push")
                reg[sp] -= 1
                reg[sp] &= 255
                reg_num = self.mem[self.pc +1]
                value = reg[reg_num]
                push_address = reg[sp]
                self.mem[push_address] = value
                self.pc +=2
            elif inst == 70:
                pop_index = reg[sp]
                value = self.mem[pop_index]
                reg_num = self.mem[self.pc+1]
                reg[reg_num] = value
                reg[sp] +=1
                self.pc+= 2