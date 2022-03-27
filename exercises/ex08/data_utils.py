"""Dictionary related utility functions."""

__author__ = "730477174"


from csv import DictReader


def read_csv_rows(data: str) -> list[dict[str, str]]:
    """Read the rows of a csv into a 'table'."""
    result: list[dict[str, str]] = []
    file_handle = open(data, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close()
    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column."""
    result: list[str] = []
    for row in table: 
        item: str = row[column]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table to a column-oriented table."""
    result: dict[str, list[str]] = {}
    
    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)

    return result


def head(input: dict[str, list[str]], row_number: int) -> dict[str, list[str]]: 
    """Produce a new column-based table with only the second parameter rows of data for each column."""
    result: dict[str, list[str]] = {}
    if row_number >= len(input):
        row_number = len(input)
    for column in input:
        result_list_2: list[str] = []
        i: int = 0
        while i < row_number:
            result_list_2.append(input[column][i])
            i += 1
        result[column] = result_list_2
    return result


def select(input: dict[str, list[str]], column_names: list[str]) -> dict[str, list[str]]: 
    """Produce a new column-based table with only a specific subset of the original columns."""
    result_dict: dict[str, list[str]] = {}
    for names in column_names:
        result_dict[names] = input[names]
    return result_dict


def concat(first_dict: dict[str, list[str]], second_dict: dict[str, list[str]]) -> dict[str, list[str]]: 
    """Produce a new column-bsaed table with two column-based tables combined."""
    result: dict[str, list[str]] = {}
    for column in first_dict:
        result[column] = first_dict[column]
    for column in second_dict:
        if column in result:
            result[column] += second_dict[column]
        else:
            result[column] = second_dict[column]
    return result


def count(value_frequency: list[str]) -> dict[str, int]:
    """Produce a new dictionary which counts the amount of times a key appears within the data."""
    result: dict[str, int] = {}
    for item in value_frequency:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1
    return result


def upper_lower(input: dict[str, list[str]]) -> None:
    upper_classmen: int = 0
    lower_classmen: int = 0
    new_list: list[str] = []
    i: int = 0
    for grad_year_list in input:
        for grad_year in input[grad_year_list]:
            new_list.append(grad_year)
        while i < len(new_list):
            if new_list[i] == "22":
                upper_classmen += 1
            elif new_list[i] == "23":
                upper_classmen += 1
            elif new_list[i] == "24":
                lower_classmen += 1
            elif new_list[i] == "25":
                lower_classmen += 1
            elif new_list[i] == "26":
                lower_classmen += 1
            i += 1
    print(f"Upperclassmen: {upper_classmen}") 
    print(f"Lowerclassmen: {lower_classmen}")