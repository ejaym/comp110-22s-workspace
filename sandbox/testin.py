def free_biscuits(lol: dict[str, list[int]]) -> dict[str, bool]:
    returns_dict: dict[str, bool] = {}
    for i in lol:
        if sum(lol[i]) >= 100:
            returns_dict[i] = True
        else: 
            returns_dict[i] = False
    return returns_dict


def multiples(ins: list[int]) -> list[bool]:
    n_list: list[bool] = []
    for i in ins:
        if i == 0:
            n_list.append(ins[i] % ins[(len(ins) - 1)] == 0)
        else:
            n_list.append(ins[i] % ins[i - 1] == 0)
    return n_list

