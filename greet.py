"""Tiny politely greeting helpers used to practice atomic commits."""

def greet(name: str) -> str:
    return f"Greetings, {name}."

def shout(name: str) -> str:
    return greet(name).upper()

if __name__ == "__main__":
    print(shout("world"))