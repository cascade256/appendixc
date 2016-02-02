def handleInterupt(operand, memory, registers):
    if(operand == 128):
        systemCall(memory, registers)
    else:
        print("Not Implemented")

def systemCall(memory, registers):
    call = registers[1]
    if(call == 4): #write
        dest = registers[2]
        if(dest == 1): #screen
            address = registers[3]
            length = registers[4]
            for x in range(length):
                c = chr(memory[address + x])
                print(c)
        else:
            print("Not Implemented")
    else:
        print("Not Implemented")
