def is_palindrome(s):
	"""Check whether s reads the same forward and backward.

	Args:
		s: The string to check.

	Returns:
		True if s is a palindrome, otherwise False.
	"""
	return s == s[::-1]


def count_words(text):
	"""Count the words in text.

	Args:
		text: The text whose words should be counted.

	Returns:
		The number of words in text.
	"""
	return len(text.split())


def celsius_to_fahrenheit(c):
	"""Convert a temperature from Celsius to Fahrenheit.

	Args:
		c: The temperature in Celsius.

	Returns:
		The converted temperature in Fahrenheit.
	"""
	return (c * 9 / 5) + 32
print(is_palindrome("madam"))
print(count_words("Python is easy to learn"))
print(celsius_to_fahrenheit(25))