"""Dictionary Utils: Exercise 6"""

__author__: str = "730748249"


def invert(input_dict: dict[str, str]) -> dict[str, str]:
    temp1: str = ""
    temp2: str = ""
    output_dict: dict[str, str] = {}
    for item in input_dict:
        temp1 = item
        temp2 = input_dict[item]
        has_item: bool = temp2 in output_dict
        if has_item:
            raise KeyError("Cannot have duplicate keys!")
        else:
            output_dict[temp2] = temp1
    return output_dict


def favorite_color(color_dictionary: dict[str, str]) -> str:
    color: str = ""
    values_list: list[str] = []
    tally: int = 0
    for vote in color_dictionary:
        values_list.append(color_dictionary[vote])
    temporary_color: str = color_dictionary[vote]  # type: ignore
    for item in values_list:
        temp_tally: int = 0
        if temporary_color == item:
            temp_tally += 1
            if temp_tally > tally:
                tally = temp_tally
                color = temporary_color

    return color


def count(input_list: list[str]) -> dict[str, int]:
    count_dictionary: dict[str, int] = {}
    for item in input_list:
        if item in count_dictionary:
            count_dictionary[item] = count_dictionary[item] + 1
        else:
            count_dictionary[item] = 1
    return count_dictionary


def alphabetizer(unalphabetized: list[str]) -> dict[str, list[str]]:
    alphabetized: dict[str, list[str]] = {}
    first_letter: str = ""
    temp_list: list[str] = []
    for item in unalphabetized:
        first_letter = item[0].lower()
        temp_list.append(item)
        for item2 in unalphabetized:
            if first_letter == item2[0] and item != item2:
                temp_list.append(item2)
        if first_letter not in alphabetized:
            alphabetized[first_letter] = temp_list
        temp_list = []
    return alphabetized


def update_attendance(
    attendance_dict: dict[str, list[str]], day: str, student: str
) -> None:
    if day in attendance_dict:
        temp_list: list[str] = attendance_dict[day]
        temp_list.append(student)
        attendance_dict[day] = temp_list
    else:
        temp_list: list[str] = []
        temp_list.append(student)
        attendance_dict[day] = temp_list
