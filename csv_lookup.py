import json
import codecs
import random
import pandas as pd

from flashcard_srs import Flashcard, SRS

full_data = r"n5_first_50_quotes.csv"


def access_csv():
    mapping_first = ["name"]
    mapping_second = ["japanese_quote", "english", " with_hiragana"]

    df = pd.read_csv(full_data, sep=";", encoding="utf-8-sig")

    wrapped_list = []
    for key, group in df.groupby(mapping_first):
        for jp_quote, english, hiragana in zip(
            group["japanese_quote"], group["english"], group["with_hiragana"]
        ):
            sub_item = [f"{str(jp_quote)}", f"{english}", f"{hiragana}"]
            # sub_item_k = {f"{key}": [f"Merc = {merc}", f"ICMS = {icms}", f"ST = {st}"]}

            # sub_item_a = {f"{key}": [f"'Merc' : {merc} , 'ICMS' : {icms}, 'ST' : {st}"]}
            wrapped_list.append(sub_item)

    return wrapped_list


assign = access_csv()

flashcard_list = []


def access_flashcard():
    for item in assign:
        flashcard_list.append([Flashcard(item[0], item[0], item[1], item[2])])

    return flashcard_list


# flashcard_list = access_flashcard(flashcard_list)


def call_flashcard(input_widget):
    value = ""
    srs = SRS(flashcards=flashcard_list)
    for val in range(len(flashcard_list)):
        value = srs.review(input_widget)
        # value = ["", "", ""]
    return value


"""
val = call_flashcard()

print(val)


def srs_evaluate(widget_val):
    srs = SRS(flashcard_list)
    for i in range(len(flashcard_list)):
        srs.review_return(widget_val)
 """


# TODO: This is where the spaced repetition logic should be applied
def random_quote():
    return assign[random.randint(1, 50)]


# kanji quiz: I've thought about keeping a progress marker for each N category i guess.
