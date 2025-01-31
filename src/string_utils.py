from typing import Dict, List
import re

class StringProcessor:
    @staticmethod
    def reverse_words(text: str) -> str:
        """Reverse each word in a text while maintaining word order."""
        if not text:
            return ""
        words = text.split()
        reversed_words = [word[::-1] for word in words]
        return " ".join(reversed_words)

    @staticmethod
    def count_word_frequency(text: str) -> Dict[str, int]:
        """Count frequency of each word in the text."""
        if not text:
            return {}
        
        # Convert to lowercase and split into words
        words = text.lower().split()
        frequency = {}
        
        for word in words:
            # Remove punctuation from word
            clean_word = re.sub(r'[^\w\s]', '', word)
            if clean_word:
                frequency[clean_word] = frequency.get(clean_word, 0) + 1
        
        return frequency

    @staticmethod
    def find_palindromes(text: str) -> List[str]:
        """Find all palindromic words in the text."""
        if not text:
            return []
        
        words = re.findall(r'\b\w+\b', text.lower())
        return [word for word in words if word == word[::-1] and len(word) > 1]

    @staticmethod
    def truncate_text(text: str, max_length: int, suffix: str = "...") -> str:
        """
        Truncate text to max_length and add suffix if truncated.
        
        Args:
            text: Input text to truncate
            max_length: Maximum length of the output text (including suffix)
            suffix: String to append if text is truncated
        """
        if not text or max_length <= 0:
            return ""
        
        if len(text) <= max_length:
            return text
            
        if max_length <= len(suffix):
            return suffix[:max_length]
            
        return text[:max_length - len(suffix)] + suffix 