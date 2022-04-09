import time
from text import Text


class Session:

    def __init__(self, minutes_per_sprint: int,
                 target_wordcount: int, severity: int,
                 text: Text):

        print('new session')

        self.minutes_per_sprint = minutes_per_sprint
        self.target_wordcount = target_wordcount
        self.severity = severity
        self.text = text
        self.starttime = time.time()
        self.finishtime = self.starttime + self.minutes_per_sprint * 60

    def get_minutes_remaining(self) -> (int, int):

        seconds_remaining = self.finishtime - time.time()
        minutes_remaining = round(seconds_remaining / 60)
        minutes_remaining = max(minutes_remaining, 0)

        if self.minutes_per_sprint > 0:
            perc_time_remaining = int(minutes_remaining / self.minutes_per_sprint * 100)
        else:
            perc_time_remaining = 0

        return minutes_remaining, perc_time_remaining

    def get_perc_wc_achieved(self, current_wordcount: int) -> int:

        if self.target_wordcount > 0:
            perc_wc_achieved = int(current_wordcount / self.target_wordcount * 100)
        else:
            perc_wc_achieved = 0

        return perc_wc_achieved
    
