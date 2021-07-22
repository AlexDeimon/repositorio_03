def print_formatted(number):
    spacePad = len(str(bin(number))) 
    for i in range(1, number + 1): 
        decVar = str(i) 
        octVar = str(oct(i)[2:]) 
        hexVar = str(hex(i)[2:]).upper() 
        binVar = str(bin(i)[2:]) 
        formatDec = ((" " * (spacePad - len(str(decVar)) - 2)) + decVar) 
        formatOct = ((" " * (spacePad - len(str(octVar)) - 2)) + octVar) 
        formatHex = ((" " * (spacePad - len(str(hexVar)) - 2)) + hexVar) 
        formatBin = ((" " * (spacePad - len(str(binVar)) - 2)) + binVar) 
        print(formatDec + " " + formatOct + " " + formatHex + " " + formatBin)
n = int(input())
print_formatted(n)