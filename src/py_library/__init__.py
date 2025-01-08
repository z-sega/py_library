"""Top-level package for py-library."""

__author__ = """Ayo Onipe"""
__email__ = "ayosemail@gmail.com"
__version__ = "0.1.0"

"""
Project Requirements:

Similar to amazon kindle (for short stories)

- Users have a library of books that they can add to or remove from
- Users can set a book from their library as active
- The reading application remembers where a user left off in a given book
- The reading application only displays a page of text at a time in the active book.
"""


"""
Rough

# A Book has
# - id: int
# - title: str
# - pages/content in the book: list of str, index is page-number
# - last page user looked at: int (mind the index)

# A Library has
# - collection of books: { id: Book() }
# - active book: int
"""
