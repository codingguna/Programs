import os
def new_file():
    return""
def open_file():
    filename=input("enter the filename to open: ")
    if os.path.exists(filename):
        with open(filename,'r') as file:
            content=file.read()
        print(f"file '{filename}' opened scussfully.")
        return content
    else:
        print(f"file '{filename}' not found." )
        return ""

def save_file(content):
    filename=input('enter the filename to save:')
    with open(filename,'w') as file:
        file.write(content)
    print(f"file saved in '{filename}'.")
def help_menu():
    print("\n---HELP MENU---")
    print('\n1.NEW: Create a new text.')
    print('\n2.OPEN: Open an existing file.')
    print('\n3.SAVE: Save currrent text to file.')
    print("\n4.INSERT: Insert text.")
    print('\n5.DELETE: Delete text.')
    print("\n6.QUIT: Exit editor.")
    print('--------------------\n')

def insert_text(content):
    insert_type=input("insert word/sentense/character :").lower()
    if insert_type=='word' or insert_type=='sentense':
        position=int(input('enter the position to insert at: '))
        text_to_insert=input(f"enter the '{insert_type}' to insert: ")
        content=content[:position]+text_to_insert+content[position:]
    elif insert_type=='character':
        position=int(input('entre the position to insert character: '))
        char_to_insert=input('enter the character to insert: ')
        content=content[:position]+char_to_insert+content[position:]
    else:
        print("Invalid insert type.")
    return content

def delete(content):
    delete_type=input("delete word/sentense/character :").lower()
    if delete_type=='word' or delete_type=='sentense':
        start_pos=int(input(f'enter the starting position of {delete_type} to delete: '))
        end_pos=int(input(f'enter end position of {delete_type} to delete: '))
        content=content[:start_pos]+content[end_pos:]
    elif delete_type=='character':
        position=int(input("enter position of character to delete: "))
        content=content[:position]+content[position+1:]
    else:
        print('invalid delete type.')
    return content

def main():
    content=''
    while True:
        print('\n Options: NEW, OPEN, SAVE, INSERT, DELETE, HELP, QUIT')
        choise=input("enter your choise: ").lower()
        if choise=='new':
            content=new_file()
            print('new text file created.')
        elif choise=='open':
            content=open_file()
            print("current content:\n"+content)
        elif choise=='save':
            save_file(content)
        elif choise=='insert':
            content=insert_text(content)
            print('updated content:\n'+content)
        elif choise=='delete':
            content=delete(content)
            print('deleted content:\n'+content)
        elif choise=='help':
            help_menu()
        elif choise=='quit':
            print('exiting the text editor.')
            break
        else:
            print("invalid choise. Type 'HELP' to see available options.")

main()