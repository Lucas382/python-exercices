from dataclasses import dataclass

@dataclass
class Pirates:
    name: str = ""
    age: int = 0

    def __str__(self):
        return f'{self.name}, {self.age}'
