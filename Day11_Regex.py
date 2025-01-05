import re

#Task 1 Extract all email addresses from a given text.
text = "test.email@example.com , some-random_email@example.org , hello@vello.co are valid email address, whereas kk@kj and kkk@cc.c is not a valid email address"
emails = re.findall(r'\b[A-Za-z0-9._+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b', text)
print(emails)

#Task 2 Validate if a phone number is in the format XXX-XXX-XXXX (e.g., 123-456-7890).
text1 = "test.email@example.com , some-random_email@example.org , hello@vello.co are valid email address, whereas kk@kj and kkk@cc.c is not a valid email address , 408-888-1234 , 415-362-9900 are valid phone numbers and 444-111-222 , 1234567 are invalid phone numbers"
phone1 = re.findall(r'\d{3}-\d{3}-\d{4}', text1)
print(phone1)

#Task 3 Find all words in a string that starts with a vowel 

text2 ="innn this is a test message orange is both color and food , Texas university is one of the best , Elephant is a mammal"

vowel = re.findall(r'\b[aeiouAEIOU][A-Za-z0-9_]*\b', text2)
print(vowel)
