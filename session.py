import time
from text import Text


class Session:

    def __init__(self, minutes_per_sprint: int,
                 target_wordcount: int, severity: int,
                 text: Text):

        self.severity = severity
        self.text = text

        self.minutes_per_sprint = minutes_per_sprint
        self.minutes_remaining = minutes_per_sprint
        self.seconds_remaining = minutes_per_sprint * 60
        self.perc_time_remaining = 100

        self.starttime = time.time()
        self.finishtime = self.starttime + self.minutes_per_sprint * 60

        self.target_wordcount = target_wordcount
        self.words_remaining = target_wordcount
        self.perc_wc_achieved = 0

    def update_session_status(self, current_text_string: str):

        self.text.update_wordcount_info(current_text_string)

        self.calc_minutes_remaining()

        self.calc_word_stats()

    def calc_minutes_remaining(self):

        self.seconds_remaining = self.finishtime - time.time()
        self.minutes_remaining = round(self.seconds_remaining / 60)
        self.minutes_remaining = max(self.minutes_remaining, 0)

        if self.minutes_per_sprint > 0:
            self.perc_time_remaining = int(self.minutes_remaining / self.minutes_per_sprint * 100)
        else:
            self.perc_time_remaining = 0

    def calc_word_stats(self):

        self.words_remaining = self.target_wordcount - self.text.added_wordcount

        if self.target_wordcount > 0:
            self.perc_wc_achieved = int(self.text.added_wordcount / self.target_wordcount * 100)
        else:
            self.perc_wc_achieved = 0