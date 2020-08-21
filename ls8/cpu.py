"""CPU functionality."""

import sys

class CPU:
    """Main CPU class."""
    

    def __init__(self):
        """Construct a new CPU."""
        self.ram = [0]* 256
        self.pc = 0
        self.address = 0
        self.reg = [0]*8
        self.fl = [0]*8

    def load(self, filename):
        """Load a program into memory."""
        path = fr'C:\Users\joelc\desktop\lambda-cs\computer-architecture\ls8\examples\{filename}'
        print(path)
        address = 0
        with open(path) as f:
            for line in f:
                num = line.split("#", 1)[0]
                if num.strip() == '':
                    continue
                self.ram[address] = int(num, 2)
                address += 1
        print(self.ram)
        # For now, we've just hardcoded a program:
        """
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
            self.ram[address] = instruction
            address += 1
        """

    def alu(self, op, reg_a, reg_b):
        """ALU operations."""

        if op == "ADD":
            self.reg[reg_a] += self.reg[reg_b]
        #elif op == "SUB": etc
        else:
            raise Exception("Unsupported ALU operation")

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

        
        return self.ram[addr]
        
    
    def ram_write(self, addr, val):
        self.ram[addr] = val

    def compare(self, a, b):
        if 1 in self.fl:
            self.fl = [0]*8
        if a < b:
            self.fl[5] = 1
        elif a > b:
            self.fl[6] = 1
        elif a == b:
            self.fl[7] = 1

    def run(self):
        """Run the CPU."""
        running = True
        sp = 7
        self.reg[sp] = 255
        while running:
            
            #self.trace()
            inst = self.ram_read(self.pc)

            if inst == 1:   #Halt
                running = False
                break

            elif inst == 130: #ldi
                reg_index = self.ram[self.pc + 1]
                reg_value = self.ram[self.pc + 2]
                self.reg[reg_index] = reg_value
                self.pc += 3

            elif inst == 71: #print register
                reg_num = self.ram[self.pc +1]
                print(self.reg[reg_num])
                self.pc += 2

            elif inst == 162: #multiply
                print(self.reg[self.ram[self.pc+1]] * self.reg[self.ram[self.pc+2]])  
                self.pc +=3         
            
            elif inst == 69: #push
                self.reg[sp] -= 1
                reg_num = self.ram[self.pc +1]
                value = self.reg[reg_num]
                top_o_stack = self.reg[sp]
                self.ram[top_o_stack] = value

                self.pc += 2

            elif inst == 70: #pop
                top_o_stack = self.reg[sp]
                value = self.ram[top_o_stack]
                reg_num = self.ram[self.pc + 1]
                self.reg[reg_num] = value
                self.reg[sp] += 1
                self.pc += 2
            
            elif inst == 80: #call
                ret_address = self.pc + 2
                self.reg[sp] -= 1
                self.ram[self.reg[sp]] = ret_address
                reg_num = self.ram[self.pc +1]
                self.pc = self.reg[reg_num]
            
            elif inst == 17: #return
                ret_address = self.ram[self.reg[sp]]
                self.reg[sp] += 1
                self.pc = ret_address
           
            elif inst == 160: #add
                self.reg[self.ram[self.pc+1]] += self.reg[self.ram[self.pc+2]]
                self.pc += 3
            
            elif inst == 84: #unconditional jump
                self.pc = self.reg[self.ram[self.pc+1]]
            
            elif inst == 167: #compare
                a = self.reg[self.ram[self.pc +1]]
                b = self.reg[self.ram[self.pc +2]]
                self.compare(a,b)
                self.pc += 3
            
            elif inst == 85: #jeq
                if self.fl[7] == 1:
                    self.pc = self.reg[self.ram[self.pc + 1]]
                else:
                    self.pc += 2

            elif inst == 86: #jne
                if self.fl[7] == 0:
                    self.pc = self.reg[self.ram[self.pc + 1]]
                else:
                    self.pc += 2