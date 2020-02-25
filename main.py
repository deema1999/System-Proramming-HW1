import numpy as np
array = np.genfromtxt('code.txt',dtype='str',delimiter=(8,1,5,2,17,30))

length = len(array) 

#Declare lists for labels,blanks, opcodes, operands, comments, comment lines
label = [] 
blank1 = []
opcode = []
blank2 = []
operand = []
noOfCommentLines = 0
comment = []
directive=[]
linesWithIndexedAddressing = []
#Declare a variable to hold number of indexed instructions
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

    #if array[l][0].startswith('.'):
        #commentLine.append(array[l][0])

    if array[l][1] != '\n' :
        if  array[l][1] != '':
            blank1.append(array[l][1])
           
    if array[l][2] != '\n':
        if  array[l][2] != '':
            if array[l][2].strip() in {'START','END','RESW','RESB','BYTE','WORD'}:
                #directive.append(array[l][2].strip()) 
                noOfDirectives = noOfDirectives + 1
            else:
                noOfInst = noOfInst + 1
        opcode.append(array[l][2].strip())
        
    if array[l][3] != '\n' :
        if  array[l][3] != '':
            blank2.append(array[l][3])
        
    if array[l][4] != '\n' :
        if array[l][4] != '':
            if ',x' in array[l][4]:
                linesWithIndexedAddressing.append((l+1)*5)
               #noOfIndexInst = noOfIndexInst + 1
               #operand.append(array[l][4].strip()[-len(array[l][4].strip()):-2])
            operand.append(array[l][4].strip())
       
    if array[l][5] != '\n':
        if  array[l][5] != '':
            comment.append(array[l][5].strip())
     
programName = label[0]
#print(programName)
#print(label)
#print(blank1)
#print(opcode)
#print(directive)
#print(operand)

#print(comment)
#print(commentLine)
#print(noOfIndexInst)

while True:
    print('1.What is the name of the program?\n2.Separate each column as a list.\n3.How many lines are comments?\n4.How many directives in the source code?')
    print('5.How many instructions in the source code?\n6.Which lines contain indexed addressing?')
    choice = input("Enter your choice: ") 
    if choice == '1':
        print(programName)
                
    if choice == '2': 
        print('Label column:', label)
        print('Blank column:', blank1)
        print('Opcode column:', opcode)
        print('Operand column:', operand)
        print('comment column:', comment)
                
    if choice == '3':
        print(noOfCommentLines)
                
    if choice == '4': 
        print(noOfDirectives)
                
    if choice == '5':
        print(noOfInst)
               
    if choice == '6':
        print(linesWithIndexedAddressing)
               