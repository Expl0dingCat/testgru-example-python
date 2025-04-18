import pytest
from pathlib import Path
import sys

# Adjust import path for the src module
sys.path.append(str(Path(__file__).resolve().parent.parent))

from src.string_utils import StringProcessor

@pytest.mark.skip(reason="reverse_words method no longer implemented")
def test_reverse_words_empty():
    assert StringProcessor.reverse_words("") == ""

@pytest.mark.skip(reason="reverse_words method no longer implemented")
def test_reverse_words_single_word():
    assert StringProcessor.reverse_words("hello") == "hello"

@pytest.mark.skip(reason="reverse_words method no longer implemented")
def test_reverse_words_multiple_words():
    assert StringProcessor.reverse_words("hello world") == "hello world"

def test_count_word_frequency_empty():
    assert StringProcessor.count_word_frequency("") == {}

def test_count_word_frequency_single_word():
    assert StringProcessor.count_word_frequency("hello") == {"hello": 1}

def test_count_word_frequency_multiple_words():
    assert StringProcessor.count_word_frequency("hello hello world") == {
        "hello": 2,
        "world": 1,
    }

def test_count_word_frequency_case_insensitive():
    assert StringProcessor.count_word_frequency("Hello HELLO world") == {
        "hello": 2,
        "world": 1,
    }

def test_count_word_frequency_punctuation():
    assert StringProcessor.count_word_frequency("hello, world! hello.") == {
        "hello": 2,
        "world": 1,
    }

def test_find_palindromes_empty():
    assert StringProcessor.find_palindromes("") == []

def test_find_palindromes_none():
    assert StringProcessor.find_palindromes("hello world") == []

def test_find_palindromes_single():
    assert StringProcessor.find_palindromes("noon") == ["noon"]

def test_find_palindromes_multiple():
    assert StringProcessor.find_palindromes("noon level radar hello") == [
        "noon",
        "level",
        "radar",
    ]

def test_find_palindromes_case_insensitive():
    assert StringProcessor.find_palindromes("Noon Level") == ["noon", "level"]

def test_find_palindromes_single_char():
    assert StringProcessor.find_palindromes("a b c") == []

def test_truncate_text_empty():
    assert StringProcessor.truncate_text("", 10) == ""

def test_truncate_text_negative_length():
    assert StringProcessor.truncate_text("hello", -1) == ""

def test_truncate_text_no_truncation():
    assert StringProcessor.truncate_text("hello", 10) == "hello"

def test_truncate_text_exact_length():
    assert StringProcessor.truncate_text("hello", 5) == "hello"

def test_truncate_text_with_truncation():
    assert StringProcessor.truncate_text("hello world", 8) == "hello..."

def test_truncate_text_custom_suffix():
    assert StringProcessor.truncate_text("hello world", 8, "***") == "hello***"

def test_truncate_text_small_max_length():
    assert StringProcessor.truncate_text("hello", 2) == ".."
