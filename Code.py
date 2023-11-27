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

    
def morse_to_text(dot):
    if dot == '.-':
        return "A"
    elif dot == '-...':
        return "B"
    elif dot == '-.-.':
        return "C"
    elif dot == '-..':
        return "D"
    elif dot == '.':
        return "E"
    elif dot == '..-.':
        return "F"
    elif dot == '--.':
        return "G"
    elif dot == '....':
        return "H"
    elif dot == '..':
        return "I"
    elif dot == '.---':
        return "J"
    elif dot == '-.-':
        return "K"
    elif dot == '.-..':
        return "L"
    elif dot == '--':
        return "M"
    elif dot == '-.':
        return "N"
    elif dot == '---':
        return "O"
    elif dot == '.--.':
        return "P"
    elif dot == '--.-':
        return "Q"
    elif dot == '.-.':
        return "R"
    elif dot == '...':
        return "S"
    elif dot == '-':
        return "T"
    elif dot == '..-':
        return "U"
    elif dot == '...-':
        return "V"
    elif dot == '.--':
        return "W"
    elif dot == '-..-':
        return "X"
    elif dot == '-.--':
        return "Y"
    elif dot == '--..':
        return "Z"  
    elif dot == " ":
        return " "
    else:
        return "Error What you have entered cant be decrypted"
    
    
 
    
def string_to_morse(text):
    morse_code = ""
    for letter in text:
        morse_code += text_to_morse(letter) + " "
    return morse_code

def morsestr(text):
    morse_code = ""
    for dot in text:
        morse_code += morse_to_text(dot) + " "
    return morse_code

if __name__ == "__main__":
    input_text = input("Enter text to encrypt into Morse code: ")
    encrypted_text = string_to_morse(input_text.upper())
    print("Morse code:", encrypted_text)


    