class Text:

    def ___init__(self, initial_text=''):

        self.text = initial_text
        self.initial_wordcount = self.count_words(initial_text)
        self.current_wordcount = initial_wordcount
        self.delta_wordcount = self.get_delta_wordcount()

    def update_text(self, text: str):

        self.text = text
        self.update_wordcount()

    def update_wordcount(self):

        self.current_wordcount = self.count_words(self.text)
        self.delta_wordcount = self.get_delta_wordcount()

    @staticmethod
    def count_words(text):
        """Counts words using same method as linux wc"""

        # TODO

        return wc

    def get_delta_wordcount(self):

        return self.current_wordcount - self.initial_wordcount
