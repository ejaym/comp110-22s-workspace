"""Example of a function that searches through a list."""

# Define a function named contains
# Two parameters:
# 1. needle - the string we're searching for
# 2. haystack - the list we're searching through


def main() -> None:
    print(contains("Kevin Bacon", ["Kanye West", "Pete Daividson"]))


def contains(needle: str, haystack: list[str]) -> bool:
    for item in haystack:
        if item == needle:
            return True
    return False


if __name__ == "__main__":
    main()