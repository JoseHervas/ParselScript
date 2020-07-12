import sys, re
sym = ('sss','sha','sas','shs','saa','ssh','sah','shh')
inf = sys.argv[1]
instr = ' '.join(sys.argv[2:])

# Check args
if len(sys.argv) < 2:
    print('''Usage:
    python3 parsel.py <Sourcefile.ps>
    ''')
    sys.exit(0)

# Memory structure
A = [0]
n = 0
ptr = 0
loop = []
skipFlag = False
inBuffer = list(' '.join(sys.argv[2:]))
inBuffer.reverse()

# Input read
with open(inf, 'r') as codeFile:
    codeSource=codeFile.read()
    # @ is the symbol for comments in this language
    codeSource=re.sub('@.*\n', '', codeSource)
    codeSource=codeSource.replace('\n', '').replace(' ', '')
code = [codeSource[i:i+3] for i in range(0, len(codeSource), 3)]
for i in code:
    if i not in sym:
        code.remove(i)
code.append('/0')

# Abstract Syntax Tree
while True:
    if skipFlag and code[ptr] != sym[7]:
        if code[ptr] == '/0':
            raise BufferError
            sys.exit(1)
        ptr += 1
        continue
    if code[ptr] == sym[0]:
        if len(A) <= n+1:
            A.append(0)
        n+=1
        ptr += 1
    elif code[ptr] == sym[1]:
        if n > 0:
            n-=1
        ptr += 1
    elif code[ptr] == sym[2]:
        A[n]+=1
        ptr += 1
    elif code[ptr] == sym[3]:
        A[n]-=1
        ptr += 1
    elif code[ptr] == sym[4]:
        try:
            print(chr(A[n]), end="")
        except ValueError:
            pass
        ptr += 1
    elif code[ptr] == sym[5]:
        try:
            inChar = inBuffer.pop()
            A[n] = int(inChar)
        except ValueError:
            print('Error reading char')
        except IndexError:
            pass
        ptr += 1
    elif code[ptr] == sym[6]:
        if A[n] != 0:
            loop.append(ptr)
        else:
            skipFlag = True
        ptr += 1
    elif code[ptr] == sym[7]:
        try:
            ptr = loop.pop()
        except IndexError:
            ptr += 1
            skipFlag = False
    elif code[ptr] == '/0':
        sys.exit(0)
    else:
        ptr += 1
