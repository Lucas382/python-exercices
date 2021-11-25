import numpy as np
from Pirates import Pirates

Pirates: Pirates
pirates = []


# Testing the new functionality "match/case" of python 3.10
# and messing with user dataclasses
def name_finder(name: str, age: int):
    match name:
        case "Zoro":
            return f"Eu sou o caçador de piratas {name} e tenho {age} anos"

        case "Carla":
            return f"Eu sou a bucaneira {name} e tenho {age} anos"

        case "Mara":
            return f"Eu sou a Navegadora {name} e tenho {age} anos"

        case _:
            return f"Não conheço esse nome! {name}"


def main():

    pirates.append(Pirates("Carla", 30))
    pirates.append(Pirates("Mara", 20))
    pirates.append(Pirates("Zoro", 40))
    pirates.append(Pirates("Igor", 18))

    for pirate in pirates:
        print(name_finder(pirate.name, pirate.age))


if __name__ == '__main__':
    main()

