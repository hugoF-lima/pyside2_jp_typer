import random
import datetime


class Flashcard:
    def __init__(self, question, answer, english, hiragana, interval=1, easiness=2.5):
        self.question = question
        self.answer = answer
        self.english = english
        self.hiragana = hiragana
        self.interval = interval
        self.easiness = easiness
        self.next_review = datetime.datetime.now() + datetime.timedelta(days=interval)

    def update_interval(self, grade):
        if grade >= 3:
            self.interval = int(self.interval * self.easiness)
            self.easiness = min(self.easiness + 0.1, 2.5)
        else:
            self.interval = int(self.interval / self.easiness)
            self.easiness = max(self.easiness - 0.1, 1.3)
        self.next_review = datetime.datetime.now() + datetime.timedelta(
            days=self.interval
        )


class SRS:
    def __init__(self, flashcards: Flashcard):
        self.flashcards = flashcards

    def review(self):
        flashcard = random.choice(self.flashcards)

        return flashcard


items = [
    ["Question 1", "Answer 1", "Info1", "Info2"],
    ["Question 2", "Answer 2", "Info1", "Info2"],
    ["Question 3", "Answer 3", "Info1", "Info2"],
]


# print(flashing)
""" flashcards = [
    Flashcard("Question 1", "Answer 1"),
    Flashcard("Question 2", "Answer 2"),
    Flashcard("Question 3", "Answer 3"),
] """

""" srs = SRS(flashcards)

for i in range(10):
    nani = srs.review()
    string_it = "shitsumon"
    srs.review_return(string_it) """
