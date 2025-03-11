class LibraryItem:
    def __init__(self, title, subject, status):
        self.title = title
        self.subject = subject
        self.status = status

    def booking(self):
        return "Your booking is successful"


class Book(LibraryItem):
    def __init__(self, ISBN, author, title, subject, status):
        super().__init__(subject, status)
        self.ISBN = ISBN
        self.author = author
        self.title = title

    def booking(self):
        return f"Your booking of {self.title} is successful"


class Magazine(LibraryItem):
    def __init__(self, journalName, volume, status):
        super().__init__(status)
        self.journalName = journalName
        self.volume = volume
