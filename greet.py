"""Tiny politely greeting helpers used to practice atomic commits."""

def greet(name: str | None = None) -> str | None:
    return f"Hey Greetingsssss!, {name}."

def shout(name: str) -> str:
    return greet(name).upper()

if __name__ == "__main__":
    print(shout("world"))