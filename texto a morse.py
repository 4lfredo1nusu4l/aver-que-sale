dicionario_a_morse = {
        "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".",
    "F": "..-.", "G": "--.", "H": "....", "I": "..", "J": ".---",
    "K": "-.-", "L": ".-..", "M": "--", "N": "-.", "O": "---",
    "P": ".--.", "Q": "--.-", "R": ".-.", "S": "...", "T": "-",
    "U": "..-", "V": "...-", "W": ".--", "X": "-..-", "Y": "-.--",
    "Z": "--..",
    "0": "-----", "1": ".----", "2": "..---", "3": "...--",
    "4": "....-", "5": ".....", "6": "-....", "7": "--...",
    "8": "---..", "9": "----.",
    ".": ".-.-.-", ",": "--..--", "?": "..--..", "!": "-.-.--",
    "/": "-..-.", "(": "-.--.", ")": "-.--.-", "&": ".-...",
    ":": "---...", ";": "-.-.-.", "=": "-...-", "+": ".-.-.",
    "-": "-....-", "_": "..--.-", '"': ".-..-.", "$": "...-..-",
    "@": ".--.-.", " ": "/"
}

texto = input("Ingresa el tecto a convertir en morse: ").upper() # type: ignore
codifcado_a_morse = []

for letra in texto:
    if letra in dicionario_a_morse:
        codifcado_a_morse.append(dicionario_a_morse[letra])

    else:
        codifcado_a_morse.append([""])

resultado = "".join(codifcado_a_morse)
print("EL resultado es: ",resultado) 


