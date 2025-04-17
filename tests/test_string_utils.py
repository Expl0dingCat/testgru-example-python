import pytest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.string_utils import StringProcessor

def test_reverse_words_empty_string():
    assert StringProcessor.reverse_words("") == ""

def test_reverse_words_single_word():
    assert StringProcessor.reverse_words("hello") == "olleh"

def test_reverse_words_multiple_words():
    assert StringProcessor.reverse_words("hello world") == "olleh dlrow"

def test_reverse_words_with_spaces():
    assert StringProcessor.reverse_words("  hello   world  ") == "olleh dlrow"

def test_count_word_frequency_empty():
    assert StringProcessor.count_word_frequency("") == {}

def test_count_word_frequency_single_word():
    assert StringProcessor.count_word_frequency("hello") == {"hello": 1}

def test_count_word_frequency_repeated_words():
    text = "hello world hello HELLO World"
    expected = {"hello": 3, "world": 2}
    assert StringProcessor.count_word_frequency(text) == expected

def test_count_word_frequency_with_punctuation():
    text = "hello, world! hello? world."
    expected = {"hello": 2, "world": 2}
    assert StringProcessor.count_word_frequency(text) == expected

def test_find_palindromes_empty():
    assert StringProcessor.find_palindromes("") == []

def test_find_palindromes_no_palindromes():
    assert StringProcessor.find_palindromes("hello world") == []

def test_find_palindromes_with_palindromes():
    text = "level radar hello deed"
    expected = ["level", "radar", "deed"]
    assert StringProcessor.find_palindromes(text) == expected

def test_find_palindromes_case_insensitive():
    text = "Level Radar DEED"
    expected = ["level", "radar", "deed"]
    assert StringProcessor.find_palindromes(text) == expected

def test_find_palindromes_single_char():
    # Single character words should not be included
    assert StringProcessor.find_palindromes("a b c level") == ["level"]

def test_truncate_text_empty():
    assert StringProcessor.truncate_text("", 10) == ""

def test_truncate_text_negative_length():
    assert StringProcessor.truncate_text("hello", -1) == ""

def test_truncate_text_no_truncation_needed():
    assert StringProcessor.truncate_text("hello", 10) == "hello"

def test_truncate_text_with_truncation():
    assert StringProcessor.truncate_text("hello world", 8) == "hello..."

def test_truncate_text_custom_suffix():
    assert StringProcessor.truncate_text("hello world", 7, "..") == "hello.."

def test_truncate_text_max_length_less_than_suffix():
    assert StringProcessor.truncate_text("hello", 2, "...") == ".."
