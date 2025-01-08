"""Main module."""

from typing import TypeAlias, List, Optional, Any


Page: TypeAlias = List[str]
Book: TypeAlias = tuple[int, str, List[Page], Optional[int]]
# A Book is structure:
# book(id, title, pages, last_page) -> Book
# is_book -> bool
# book_id -> int
# book_title -> str
# book_pages -> List[Page]
# book_last_page -> Optional[int]
# examples:
pages = [
    "This is a page from a book. Please imagine this book has multiple sentences.",
    "This is the second page, though it'll be indexed as 1",
    "And this is the final page.",
]
a_book = (1, "The fake story", pages, 1)  # on the second page, indexed 1
another_book = (2, "Some empty story", list(), 0)

# NOTES
# - id, and last_page should be automated


# constructor
def book(id, title, pages, last_page) -> Book:
    return (id, title, pages, last_page)


# validator/predicate
def is_book(thing: Any) -> bool:
    """True if thing is a book."""

    def is_pages(thing: Any) -> bool:
        """True if thing is a list of page."""

        def is_page(thing: Any) -> bool:
            """True if thing is a page."""
            return isinstance(thing, str)

        return isinstance(thing, list) and all(map(is_page, thing))

    return (
        isinstance(thing, tuple)
        and isinstance(thing[0], int)
        and isinstance(thing[1], str)
        and is_pages(thing[2])
        and isinstance(thing[3], Optional[int])
    )


# selectors
def book_id(book: Book) -> int:
    return book[0]


def book_title(book: Book) -> str:
    return book[1]


def book_pages(book: Book) -> List[Page]:
    return book[2]


def book_last_page(book: Book) -> Optional[int]:
    return book[3]


BookCollection: TypeAlias = dict[int, Book]  # start from 1
Library: TypeAlias = tuple[BookCollection, Optional[int]]
# A Library is a structure:
# library(collection, active_book) -> Library
# is_library -> bool
# library_collection -> BookCollection
# library_active_book_id -> Optional[int]
# library_active_book -> Optional[Book]
# examples
a_book_collection = {1: a_book, 2: another_book}
a_library = (a_book_collection, 1)


# constructor
def library(collection, active_book) -> Library:
    return (collection, active_book)


# validator
def is_library(thing) -> bool:
    def is_book_collection(thing) -> bool:
        return all(
            map(
                lambda maybe_record: (
                    isinstance(maybe_record[0], int) and is_book(maybe_record[1])
                ),
                thing.items(),
            )
        )

    return (
        isinstance(thing, tuple)
        and is_book_collection(thing[0])
        and isinstance(thing[1], Optional[int])
    )


# selectors
def library_book_collection(library: Library) -> BookCollection:
    return library[0]


def library_active_book_id(library: Library) -> Optional[int]:
    return library[1]


def library_active_book(library: Library) -> Optional[Book]:
    book_id = library_active_book_id(library)

    if book_id:
        return library_book_collection(library).get(book_id)


# ------------- level 2
# add book


def library_add_book(l: Library, b: Book) -> Library:
    c = library_book_collection(l)
    c[book_id(b)] = b

    return library(c, library_active_book_id(l))


# def library_set_active_book(l: Library, b: Book) -> Library:
#     pass
