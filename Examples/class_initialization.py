from dataclasses import dataclass


@dataclass
class ClassExample:
    name: str
    age: int = 0
    height: float = 0.0
    weight: float = 0.0

    def __post_init__(self):
        self.height = self.height * 2.54
        self.weight = self.weight * 0.453592

    def __str__(self):
        return f'Name: {self.name}, Age: {self.age}, Height: {self.height}, Weight: {self.weight}'

    def __repr__(self):
        return f'ClassExample(name={self.name}, age={self.age}, height={self.height}, weight={self.weight})'

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age and self.height == other.height and self.weight == other.weight

    def __ne__(self, other):
        return not self == other

    def __lt__(self, other):
        return self.name < other.name

    def __le__(self, other):
        return self.name <= other.name

    def __gt__(self, other):
        return self.name > other.name

    def __ge__(self, other):
        return self.name >= other.name

    def __hash__(self):
        return hash((self.name, self.age, self.height, self.weight))

    def __format__(self, format_spec):
        if format_spec == 'name':
            return self.name
        elif format_spec == 'age':
            return str(self.age)
        elif format_spec == 'height':
            return str(self.height)
        elif format_spec == 'weight':
            return str(self.weight)
        else:
            return str(self)

    def __bool__(self):
        return self.name != '' and self.age != 0 and self.height != 0.0 and self.weight != 0.0

    def __len__(self):
        return len(self.name)

    def __getitem__(self, item):
        return self.name[item]

    def __setitem__(self, key, value):
        self.name = self.name[:key] + value + self.name[key + 1:]

    def __delitem__(self, key):
        self.name = self.name[:key] + self.name[key + 1:]

    def __iter__(self):
        return iter(self.name)

    def __contains__(self, item):
        return item in self.name
