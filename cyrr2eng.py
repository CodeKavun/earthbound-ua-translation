from charconf import CYRILLIC_TO_LATIN


while True:
    user_input = input("Enter cyrrilic text to interpretate: ")

    result = ""
    for char in user_input:
        if (char in CYRILLIC_TO_LATIN): result += CYRILLIC_TO_LATIN[char]
        else: result += char


    print(result)
