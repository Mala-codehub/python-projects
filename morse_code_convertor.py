# Morse code dictionary
morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.', '0': '-----',
    ' ': '/'
}

def text_to_morse(text):
    morse_code = ''
    for char in text.upper():
        if char in morse_code_dict:
            morse_code += morse_code_dict[char] + ' '
        else:
            morse_code += ' '
    return morse_code

def morse_to_text(morse_code):
    text = ''
    morse_code += ' '  # Add space at the end to split the last character
    morse_char = ''
    for char in morse_code:
        if char != ' ':
            morse_char += char
        else:
            for key, value in morse_code_dict.items():
                if value == morse_char:
                    text += key
                    break
            morse_char = ''
    return text

def morse_code_converter():
    print("Welcome to Morse Code Converter!")
    print("Select conversion:")
    print("1. Text to Morse Code")
    print("2. Morse Code to Text")

    choice = input("Enter choice (1/2): ")

    if choice == '1':
        text = input("Enter text to convert to Morse code: ")
        print("Morse code:", text_to_morse(text))
    elif choice == '2':
        morse_code = input("Enter Morse code to convert to text: ")
        print("Text:", morse_to_text(morse_code))
    else:
        print("Invalid choice")

if __name__ == "__main__":
    morse_code_converter()
