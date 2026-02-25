"""A simple Python example script."""


def greet(name: str) -> str:
    """Return a greeting message for the given name."""
    return f"Hello, {name}!"


if __name__ == "__main__":
    # run a quick demonstration
    user = "Zenitsu"
    print(greet(user))
