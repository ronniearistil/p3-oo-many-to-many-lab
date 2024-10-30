# lib/author.py
class Author:
    all_authors = []  # Track all authors

    def __init__(self, name):
        self.name = name
        Author.all_authors.append(self)

    def contracts(self):
        """Returns a list of contracts for this author."""
        return [contract for contract in Contract.all_contracts if contract.author == self]

    def books(self):
        """Returns a list of books using contracts as intermediary."""
        return [contract.book for contract in self.contracts()]

    def sign_contract(self, book, date, royalties):
        """Creates and returns a new contract."""
        return Contract(self, book, date, royalties)

    def total_royalties(self):
        """Calculates total royalties earned by the author."""
        return sum(contract.royalties for contract in self.contracts())

    def __repr__(self):
        return f"<Author: {self.name}>"


# lib/book.py
class Book:
    all_books = []  # Track all books

    def __init__(self, title):
        self.title = title
        Book.all_books.append(self)

    def contracts(self):
        """Returns a list of contracts for this book."""
        return [contract for contract in Contract.all_contracts if contract.book == self]

    def authors(self):
        """Returns a list of authors for this book."""
        return [contract.author for contract in self.contracts()]

    def __repr__(self):
        return f"<Book: {self.title}>"


# lib/contract.py

class Contract:
    all_contracts = []  # Store all contracts

    def __init__(self, author, book, date, royalties):
        # Validate inputs
        if not isinstance(author, Author):
            raise Exception("Invalid author")
        if not isinstance(book, Book):
            raise Exception("Invalid book")
        if not isinstance(date, str):
            raise Exception("Date must be a string")
        if not isinstance(royalties, int):
            raise Exception("Royalties must be an integer")

        # Initialize attributes
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties

        # Track the contract
        Contract.all_contracts.append(self)

    @classmethod
    def reset_contracts(cls):
        """Resets the list of all contracts."""
        cls.all_contracts = []

    @classmethod
    def contracts_by_date(cls, date):
        """Returns contracts signed on a specific date."""
        return [contract for contract in cls.all_contracts if contract.date == date]

    def __repr__(self):
        """Ensure proper string representation."""
        return f"<Contract: {self.author.name} - {self.book.title} on {self.date}>"

    def __eq__(self, other):
        """Compares two contracts for equality."""
        if isinstance(other, Contract):
            return (
                self.author == other.author and
                self.book == other.book and
                self.date == other.date and
                self.royalties == other.royalties
            )
        return False
