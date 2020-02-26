#import numpy which is general-purpose array-processing library
import numpy as np

#importing data with genformtxt from a file and use The delimiter keyword to define how each line will be splitted
array = np.genfromtxt('code.txt',dtype='str',delimiter=(8,1,5,2,17,30))
length = len(array) 

#Declare lists for labels, blanks, opcodes, operands, comments, comment lines columns
label = [] 
blank1 = []
opcode = []
blank2 = []
operand = []
comment = []
directive=[]
linesWithIndexedAddressing = []
noOfCommentLines = 0
noOfIndexInst = 0
noOfDirectives = 0
noOfInst = 0
programName = ''

# Iterating the array
for l in range(length):
    if array[l][0] != '':
        if array[l][0].startswith('.'):
            noOfCommentLines = noOfCommentLines + 1    
    label.append(array[l][0].strip())

    if array[l][1] != '\n' :
            blank1.append(array[l][1])
           
    if array[l][2] != '\n':
        if array[l][2].strip() in {'START','END','RESW','RESB','BYTE','WORD'}:
            noOfDirectives = noOfDirectives + 1
        else:
            noOfInst = noOfInst + 1
    opcode.append(array[l][2].strip())
        
    if array[l][3] != '\n' :
        blank2.append(array[l][3])
        
    if array[l][4] != '\n' :
        if ',x' in array[l][4]:
            linesWithIndexedAddressing.append((l+1)*5)
        operand.append(array[l][4].strip())
    
    if array[l][5] != '\n':
        comment.append(array[l][5].strip())
     
while True:
    print('1.What is the name of the program?\n2.Separate each column as a list.\n3.How many lines are comments?')
    print('4.How many directives in the source code?\n5.How many instructions in the source code?\n6.Which lines contain indexed addressing?')
    choice = input("Enter your choice: ") 
    if choice == '1':
        programName = label[0]
        print(programName)
                
    if choice == '2': 
        print('Label column:', label)
        print('Blank1 column:', blank1)
        print('Opcode column:', opcode)
        print('Blank2 column:', blank2)
        print('Operand column:', operand)
        print('comment column:', comment)
                
    if choice == '3':
        print(noOfCommentLines)
                
    if choice == '4': 
        print(noOfDirectives)
                
    if choice == '5':
        print(noOfInst)
               
    if choice == '6':
        [print('line',i) for i in linesWithIndexedAddressing]
               