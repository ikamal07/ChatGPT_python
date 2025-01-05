# Example with word boundaries
import re
text = "test.email@example.com and some-random_email@example.org are valid."
emails = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b', text)
print(emails)  # ['test.email@example.com', 'some-random_email@example.org']

print("================================")

# Without \b (matches partial patterns)
text = "notanemail-12345@example.comwrong_format"
emails = re.findall(r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}', text)
print(emails)  # ['notanemail-12345@example.comwrong_format']