"""
A Hello World to be sure all our tools work
"""

from dataclasses import dataclass


@dataclass
class Greeting:
    """_summary_

    Returns:
        _type_: _description_
    """

    greeting: str
    audience: str

    def __str__(self) -> str:
        return f"{self.greeting} {self.audience}"


def main() -> None:
    """main"""
    g = Greeting("hello", "world")
    print(g)


if __name__ == "__main__":
    main()
