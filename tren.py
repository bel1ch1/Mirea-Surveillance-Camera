from typing import List


def get_full_name(first_name: str, last_name: str):
    fullname = first_name.upper() + " " + last_name.lower()
    return fullname


def get_name_with_age(name: str, age: int):
    name_with_age = name + " is this old: " + str(age)
    return name_with_age


def process_items(items: List[str]):
    for item in items:
        print(item)

process_items(["first", "sec", "tre"])
