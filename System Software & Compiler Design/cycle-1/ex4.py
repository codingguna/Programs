source_code = [
    "MACRO ADD &X,&Y",
    "LOAD &X",
    "ADD &Y",
    "STORE &X",
    "MEND",
    "START",
    "ADD A,B",
    "END"
]

mnt = {}
mdt = []

def pass_one(source_code):
    """Pass One: Identify macros and populate MNT and MDT."""
    is_macro_def = False
    macro_name = ""
    
    for line in source_code:
        tokens = line.split()
        
        if tokens[0] == "MACRO":
            is_macro_def = True
            macro_name = tokens[1]
            # Store macro name with its starting index in MDT
            mnt[macro_name] = len(mdt)
            # Extract parameters and store them in MDT
            params = tokens[2].split(',')
            mdt.append((macro_name, params))
        
        elif tokens[0] == "MEND":
            is_macro_def = False
            
        elif is_macro_def:
            # Add lines in macro body to MDT
            mdt.append(line)

# Run Pass One
pass_one(source_code)

print("Macro Name Table (MNT):", mnt)
print("Macro Definition Table (MDT):", mdt)
