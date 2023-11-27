def text_to_morse(letter):
    if letter == 'A':
        return ".-"
    elif letter == 'B':
        return "-..."
    elif letter == 'C':
        return "-.-."
    elif letter == 'D':
        return "-.."
    elif letter == 'E':
        return "."
    elif letter == 'F':
        return "..-."
    elif letter == 'G':
        return "--."
    elif letter == 'H':
        return "...."
    elif letter == 'I':
        return ".."
    elif letter == 'J':
        return ".---"
    elif letter == 'K':
        return "-.-"
    elif letter == 'L':
        return ".-.."
    elif letter == 'M':
        return "--"
    elif letter == 'N':
        return "-."
    elif letter == 'O':
        return "---"
    elif letter == 'P':
        return ".--."
    elif letter == 'Q':
        return "--.-"
    elif letter == 'R':
        return ".-."
    elif letter == 'S':
        return "..."
    elif letter == 'T':
        return "-"
    elif letter == 'U':
        return "..-"
    elif letter == 'V':
        return "...-"
    elif letter == 'W':
        return ".--"
    elif letter == 'X':
        return "-..-"
    elif letter == 'Y':
        return "-.--"
    elif letter == 'Z':
        return "--.."  
    elif letter == " ":
        return " "
    else:
        return "Error What you have entered cant be encrypted"
    
def morse_to_text(letter):
    if letter == '.-':
        return "A"
    elif letter == '-...':
        return "B"
    elif letter == '-.-.':
        return "C"
    elif letter == '-..':
        return "D"
    elif letter == '.':
        return "E"
    elif letter == '..-.':
        return "F"
    elif letter == '--.':
        return "G"
    elif letter == '....':
        return "H"
    elif letter == '..':
        return "I"
    elif letter == '.---':
        return "J"
    elif letter == '-.-':
        return "K"
    elif letter == '.-..':
        return "L"
    elif letter == '--':
        return "M"
    elif letter == '-.':
        return "N"
    elif letter == '---':
        return "O"
    elif letter == '.--.':
        return "P"
    elif letter == '--.-':
        return "Q"
    elif letter == '.-.':
        return "R"
    elif letter == '...':
        return "S"
    elif letter == '-':
        return "T"
    elif letter == '..-':
        return "U"
    elif letter == '...-':
        return "V"
    elif letter == '.--':
        return "W"
    elif letter == '-..-':
        return "X"
    elif letter == '-.--':
        return "Y"
    elif letter == '--..':
        return "Z"  
    elif letter == " ":
        return " "
    else:
        return "Error What you have entered cant be encrypted"
    
 
    
    
    