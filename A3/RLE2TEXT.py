def decode(rleString, setRowLength):
    decodedLine = ""
    digits = ""
    rowLength = 0
    for char in rleString:
        # If we encounter a digit, append to the 'digits' string
        if char.isdigit():
            digits += char
        # If we encounter a 'b' or 'o' append it
        elif char == 'b' or char == 'o':
            if digits == "":
                decodedLine += ('O' if char == 'o' else '.')
                rowLength += 1
            else:
        # Cast 'digits' and append 'digits' # of characters
                decodedLine += int(digits) * ('O' if char == 'o' else '.')
                rowLength += int(digits)
                digits = ""
        # New line break, calculate line offset
        elif char == '$': 
            if digits == "":
                decodedLine += (setRowLength - rowLength) * '.'
                decodedLine += '\n'
            else:
        # Append empty lines
                decodedLine += (setRowLength - rowLength) * '.'
                decodedLine += '\n'
                decodedLine += (int(digits) - 1) * ((setRowLength * '.')  + '\n')
            rowLength = 0
            digits = ""
        elif char == '!':
            decodedLine += (setRowLength - rowLength) * '.'
            break
        
    return decodedLine
        


LINELEN = 2219

with open("in", "r") as inp:
    data = inp.read()
    decodedLine = decode(data, LINELEN)
    with open("out", "w") as out:
        out.write(decodedLine)













        

