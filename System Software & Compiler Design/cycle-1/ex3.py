instruction_set={'LDA':0x00,'STA':0x0C,'LDX':0x04,'STX':0X10,'ADD':0X18,'SUB':0X1C,'MUL':0X20,'DIV':0X24}
def pass_two_sic_assembler(inter_file,symtab):
    header_record=None
    text_records=[]
    end_record=None
    for line in inter_file:
        locctr,label,opcode,operand=line
        if opcode=='START':
            start_addr=-int(operand,16)
            program_name=label or "DEFAULT"
            header_record=f'H{program_name:<6}{start_addr:06X}{0:06X}'
            continue
        if opcode in instruction_set:
            opcode_hex=instruction_set[opcode]<<16
            if operand in symtab:
                operand_address=symtab[operand]
            else:
                operand_address=0
            instruction_obj_code=opcode_hex+operand_address
            object_code_hex=f'{instruction_obj_code:06X}'
            text_records.append(object_code_hex)
        elif opcode=='RESW' or opcode=='RESB':
            continue
        elif opcode=='END':
            end_record=f'E{symtab[operand]:06X}'
    text_record_str="T{:<06X}{:<02X}".format(start_addr,len(text_records)*3)+''.join(text_records)
    program_len=locctr-start_addr
    header_record=f'H{program_name:<6}{start_addr:06X}{program_len:06X}'
    with open("object_code.txt",'w') as obj:
        obj.write(header_record+"\n")
        obj.write(text_record_str+'\n')
        obj.write(end_record+'\n')
    print("pass two complete. object code generated")

inter_file=[(0x100,'COPY','START','1000'),
            (0x1000,'FIRST','LDA','FIVE'),
            (0x1003,None,'ADD','BETA'),
            (0x1006,None,'SUB','GAMMA'),
            (0x1009,None,'STA','ALPHA'),
            (0x100C,'SECOND','LDX','ALPHA'),
            (0x100F,None,'STX','DELTA'),
            (0x1012,None,'RESW','1'),
            (0x1015,None,'RESB','5'),
            (0x101A,None,'END','FIRST')]

symtab={'COPY':0x1000,'FIRST':0x1000,'SECOND':0x100C,'FIVE':0x1018,'BETA':0x101B,'GAMMA':0x101E,'ALPHA':0x1021,'DELTA':0X1024}

pass_two_sic_assembler(inter_file,symtab)




