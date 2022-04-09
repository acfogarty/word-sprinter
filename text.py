class Text:

    def __init__(self, initial_text_string=''):

        self.text_string = initial_text_string
        self.initial_wordcount = self.count_words(initial_text_string)
        self.current_wordcount = self.initial_wordcount
        self.delta_wordcount = self.get_delta_wordcount()

    def get_wordcount_info(self, current_text_string: str):
        """
        Returns:
        * current total wordcount
        * delta between current and initial wordcounts
        """

        self.text_string = current_text_string
        self.update_wordcount()

        return self.current_wordcount, self.delta_wordcount

    def update_wordcount(self):

        self.current_wordcount = self.count_words(self.text_string)
        self.delta_wordcount = self.get_delta_wordcount()

    @staticmethod
    def count_words(text_string: str) -> int:
        """Counts words using same method as linux wc"""

        # TODO
        wc = len(text_string.split('\s+'))

        return wc

    def get_delta_wordcount(self) -> int:

        return self.current_wordcount - self.initial_wordcount
