import re
from typing import Dict


def compare_two_strings(first: str, second: str) -> float:
    first = re.sub("\s", "", first)
    second = re.sub("\s", "", second)
    if len(first) == 0 and len(second) == 0:
        return 1
    if len(first) == 0 or len(second) == 0:
        return 0
    if first == second:
        return 1
    if len(first) == 1 and len(second) == 1:
        return 0
    if len(first) < 2 or len(second) < 2:
        return 0

    first_bigrams: Dict[str, int] = {}
    for i in range(0, len(first) - 1):
        bigram = first[i : i + 2]
        count = first_bigrams[bigram] + 1 if bigram in first_bigrams.keys() else 1
        first_bigrams[bigram] = count

    intersection_size = 0
    for i in range(0, len(second) - 1):
        bigram = second[i : i + 2]
        count = first_bigrams[bigram] if bigram in first_bigrams.keys() else 0

        if count > 0:
            first_bigrams[bigram] = count - 1
            intersection_size += 1
    print(first_bigrams)
    return (2.0 * intersection_size) / (len(first) + len(second) - 2)


def find_best_match(main_string: str, target_strings: list):
    if are_args_valid(main_string, target_strings) != True:
        raise Exception(
            "Bad arguments: First argument should be a string, second should be an array of strings"
        )

    ratings = []
    best_match_index = 0

    for i in range(len(target_strings)):
        current_target_string = target_strings[i]
        current_rating = compare_two_strings(main_string, current_target_string)
        ratings.append({"target": current_target_string, "rating": current_rating})
        if current_rating > ratings[best_match_index]["rating"]:
            best_match_index = i

    best_match = ratings[best_match_index]
    return ratings, best_match, best_match_index


def flatten_deep(arr: list):
    return (
        [item for sublist in arr for item in sublist]
        if isinstance(arr, list)
        else [arr]
    )


def are_args_valid(main_string: str, target_strings: list) -> bool:
    if not isinstance(main_string, str):
        return False
    if not isinstance(target_strings, list):
        return False
    if len(target_strings) == 0:
        return False
    if [x for x in target_strings if not isinstance(x, str)] != []:
        return False
    return True


def letter_pairs(str: str) -> list:
    pairs = []
    for i in range(0, len(str) - 1):
        pairs.append(str[i : i + 2])
    return pairs


def word_letter_pairs(str: str):
    pairs = list(map(letter_pairs, str.upper().split(" ")))
    return flatten_deep(pairs)

