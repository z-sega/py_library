#!/usr/bin/env python

"""Tests for `py_library` package."""

import pytest


from src.py_library import py_library


@pytest.fixture
def a_book():
    return py_library.a_book


@pytest.fixture
def another_book():
    return py_library.another_book


@pytest.fixture
def a_book_collection():
    return py_library.a_book_collection


@pytest.fixture
def a_library():
    return py_library.a_library


# Test Book
def test_book(a_book):
    id = a_book[0]
    title = a_book[1]
    pages = a_book[2]
    last_page = a_book[3]

    assert (
        py_library.book(id, title, pages, last_page) == a_book
    ), "Cannot construct a book."


def test_is_book(a_book):
    assert (
        py_library.is_book(
            10,
        )
        == False
    ), "'(10,)' should not be a book."
    assert py_library.is_book(a_book) == True, "Fixture book should be a book."


def test_book_id(a_book):
    book_id = a_book[0]
    assert py_library.book_id(a_book) == book_id, "Cannot select id of book."


def test_book_title(a_book):
    book_title = a_book[1]
    assert py_library.book_title(a_book) == book_title, "Cannot select title of book."


def test_book_pages(a_book):
    book_pages = a_book[2]
    assert py_library.book_pages(a_book) == book_pages, "Cannot select pages of book."


def test_book_last_page(a_book):
    book_last_page = a_book[3]
    assert (
        py_library.book_last_page(a_book) == book_last_page
    ), "Cannot select last page of book."


# Test Library
def test_library(a_library):
    book_collection = a_library[0]
    active_book_id = a_library[1]

    assert (
        py_library.library(book_collection, active_book_id) == a_library
    ), "Cannot construct library."


def test_is_library(a_library):
    assert (
        py_library.is_library(a_library) == True
    ), "Fixture library should be a library."
    assert (
        py_library.is_library(
            10,
        )
        == False
    ), "'(10,)' should not be a library."


def test_library_book_collection(a_library):
    book_collection = a_library[0]

    assert (
        py_library.library_book_collection(a_library) == book_collection
    ), "Cannot select book collection of library."


def test_library_active_book_id(a_library, a_book_collection):
    active_book_id = a_library[1]
    a_library_without_active_book = (a_book_collection, None)

    assert (
        py_library.library_active_book_id(a_library) == active_book_id
    ), "Cannot select active book id of library."
    assert (
        py_library.library_active_book_id(a_library_without_active_book) == None
    ), "Library with no active book should be None."


def test_library_active_book(a_library, a_book_collection):
    active_book = a_book_collection.get(a_library[1])
    a_library_without_active_book = (a_book_collection, None)

    assert (
        py_library.library_active_book(a_library) == active_book
    ), "Cannot select active book of library."
    assert (
        py_library.library_active_book(a_library_without_active_book) == None
    ), "Library with no active book should be None."
