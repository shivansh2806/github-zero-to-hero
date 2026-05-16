"""Tiny greeting helpers used to practice atomic commits."""

def greet(name: str) -> str:
    return f"Hello, {name}!"

if __name__ == "__main__":
    print(greet("world"))
