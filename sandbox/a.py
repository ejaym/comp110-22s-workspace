def input_char(x: str) -> int:
    return len(x)


def remove_ws(x: str) -> str:
    """Removes white space."""
    x.strip()
    return x


def delete_ws(x: str) -> str:
    x.strip()
    return x


def multiple(x: str, y: int) -> str:
    """Get letters within the word to multiply by y."""
    i: int = 0
    result: str = ""
    while i < len(x):
        j: int = y
        while j > 0:
            result += x[i]
            j -= 1
        i += 1
        j == y
    return result
        
        
