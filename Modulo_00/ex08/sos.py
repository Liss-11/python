import sys
import string

CHARS_TO_MORSE_CODE_MAPPING = {
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    '0': '-----',
    ' ': '/',
}

if __name__=='__main__':
    if len(sys.argv) < 2:
        print("ERROR: You must pass at least one String as a parameter")
        exit(1)
    i = 1
    params = ""
    while i < len(sys.argv):
        if i > 1:
            params += ' '
        for char in sys.argv[i]:
            if not char == ' ':
                if char.isalnum() == False:
                    print("ERROR: String must contain only alphanumeric characters or spaces")
                    exit(1)
        params = params + sys.argv[i]
        i += 1
    print(params)
    code = ""
    code += CHARS_TO_MORSE_CODE_MAPPING[params[0].upper()]
    for char in params[1:]:
        code += ' '
        code += CHARS_TO_MORSE_CODE_MAPPING[char.upper()]
    print(code)