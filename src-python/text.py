class Text:

    def __init__(self, initial_text_string=''):

        self.text_string = initial_text_string
        self.initial_wordcount = self.count_words(initial_text_string)
        self.current_wordcount = self.initial_wordcount
        self.added_wordcount = self.get_added_wordcount()

    def update_wordcount_info(self, current_text_string: str):

        self.text_string = current_text_string

        self.current_wordcount = self.count_words(self.text_string)
        self.added_wordcount = self.get_added_wordcount()

    @staticmethod
    def count_words(text_string: str) -> int:
        """Counts words using same method as linux wc"""

        # TODO
        wc = len(text_string.split())

        return wc

    def get_added_wordcount(self) -> int:

        return self.current_wordcount - self.initial_wordcount