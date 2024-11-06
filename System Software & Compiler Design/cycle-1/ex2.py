instruction_set={'LDA':0x00,'LDX':0X04,'STA':0X0C,'STX':0X10,'ADD':0X18,'SUB':0X1C,'MUL':0X20,'DIV':0X24}
def process_lines(line):
    parts=line.split()
    if len(parts)==3:
        label,opcode,operand=parts
    elif len(parts)==2:
        label=None
        opcode,operand=parts
    elif len(parts)==1:
        label=None
        opcode=parts[0]
        operand=None
    else:
        raise SyntaxError("invalid instruction format")
    return label,opcode,operand

def pass_one_sic_assembler(source_code,start_addr=0):
    locctr=start_addr
    intermed_file=[]
    symtab={}
    for line in source_code:
        line=line.strip()
        if line.startswith("."):
            continue
        label,opcode,operand=process_lines(line)
        if opcode=='START':
            locctr=int(operand,16)
            intermed_file.append((locctr,label,opcode,operand))
            continue
        if label:
            if label in symtab:
                raise ValueError(f"duplicate symbol: {label}")
            symtab[label]=locctr
        intermed_file.append((locctr,label,opcode,operand))
        if opcode in instruction_set:
            locctr+=3
        elif opcode=='WORD':
            locctr+=3
        elif opcode=='RESW':
            locctr+=3*int(operand)
        elif opcode=='RESB':
            locctr+=int(operand)
        elif opcode=='END':
            break
        else:
            raise ValueError(f"onvalid opcode: {opcode}")
    return intermed_file,symtab

source_code=None
with open('pro.asm','r') as f:
    source_code=f.readlines()
intermediate_file,symtab=pass_one_sic_assembler(source_code)
with open("intermediate.txt",'w') as int_f:
    for entry in intermediate_file:
        locctr,label,opcode,operands=entry
        int_f.write(f"{locctr:04X} {label or ''} {opcode} {operands or ''}\n")

with open("symtab.txt",'w') as sym_f:
    for symbol,addres in symtab.items():
        sym_f.write(f'{symbol} {addres:04X}\n')

print('pass one complete. intermediated file and symtab created.')





