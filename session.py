import time
from text import Text


class Session:

    def __init__(self, minutes_per_sprint: int,
                 target_wordcount: int, severity: int,
                 text: Text):

        self.minutes_per_sprint = minutes_per_sprint
        self.target_wordcount = target_wordcount
        self.severity = severity
        self.text = text
        self.starttime = time.time()

    def get_minutes_remaining(self) -> int:

        return int((time.time() - self.starttime) / 60)

    
