VOWELS = dict([
    ("а", "я"),
    ("у", "е"),
    ("о", "е"),
    ("", "я"),
    ("и", "и"),
    ("э", "е"),
    ("я", "я"),
    ("ю", "ю"),
    ("е", "ю"),

])


PREFIX = "ху"


def replace(source: str) -> str:
    for position, letter in enumerate(source):
        if letter in VOWELS:
            return PREFIX + VOWELS[letter] + source[position+1:]
    raise NotImplementedError()


if __name__ == '__main__':
    try:
        print(replace(input()))
    except NotImplementedError:
        print("ы,ё не реализовано")
