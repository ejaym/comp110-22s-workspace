lauren: str = "a friend"


def global_access() -> None:
    print(lauren)


global_access()