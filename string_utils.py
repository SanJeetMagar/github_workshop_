#!/usr/bin/env python3
"""
Simple Python program to demonstrate Git workflow
This script performs basic string operations
"""

def greet(name):
    """Greet a person by name"""
    return f"Hello, {name}! Welcome to GitHub Workshop."

def reverse_string(text):
    """Reverse a string"""
    return text[::-1]

def count_characters(text):
    """Count the number of characters in a string"""
    return len(text)

def is_palindrome(text):
    """Check if a string is a palindrome"""
    cleaned = text.replace(" ", "").lower()
    return cleaned == cleaned[::-1]

# Main execution
if __name__ == "__main__":
    print(greet("Student"))
    print(f"Reversed 'Git': {reverse_string('Git')}")
    print(f"Character count in 'GitHub': {count_characters('GitHub')}")
    print(f"Is 'racecar' a palindrome? {is_palindrome('racecar')}")
