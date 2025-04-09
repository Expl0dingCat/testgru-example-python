import pytest
import sys
import os

# Add the src directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

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

def test_count_word_frequency_multiple_words():
    result = StringProcessor.count_word_frequency("hello world hello")
    assert result == {"hello": 2, "world": 1}

def test_count_word_frequency_case_insensitive():
    result = StringProcessor.count_word_frequency("Hello WORLD hello")
    assert result == {"hello": 2, "world": 1}

def test_count_word_frequency_with_punctuation():
    result = StringProcessor.count_word_frequency("hello, world! hello.")
    assert result == {"hello": 2, "world": 1}

def test_find_palindromes_empty():
    assert StringProcessor.find_palindromes("") == []

def test_find_palindromes_no_palindromes():
    assert StringProcessor.find_palindromes("hello world") == []

def test_find_palindromes_single_palindrome():
    assert StringProcessor.find_palindromes("level") == ["level"]

def test_find_palindromes_multiple_palindromes():
    result = StringProcessor.find_palindromes("madam saw level deed")
    assert sorted(result) == ["deed", "level", "madam"]

def test_find_palindromes_case_insensitive():
    assert StringProcessor.find_palindromes("Level Madam") == ["level", "madam"]

def test_find_palindromes_single_letter():
    assert StringProcessor.find_palindromes("a b c") == []

def test_truncate_text_empty():
    assert StringProcessor.truncate_text("", 10) == ""

def test_truncate_text_negative_length():
    assert StringProcessor.truncate_text("hello", -5) == ""

def test_truncate_text_no_truncation_needed():
    assert StringProcessor.truncate_text("hello", 10) == "hello"

def test_truncate_text_exact_length():
    assert StringProcessor.truncate_text("hello", 5) == "hello"

def test_truncate_text_with_truncation():
    assert StringProcessor.truncate_text("hello world", 8) == "hello..."

def test_truncate_text_custom_suffix():
    assert StringProcessor.truncate_text("hello world", 7, "..") == "hello.."

def test_truncate_text_max_length_less_than_suffix():
    assert StringProcessor.truncate_text("hello", 2, "...") == ".."
