import re
import pyperclip

# Get text from clipboard
text = pyperclip.paste()

# Regex for emails
email_regex = re.compile(r'''
	[a-zA-Z0-9._%+-]+      # username
	@
	[a-zA-Z0-9.-]+         # domain
	\.[a-zA-Z]{2,}         # dot-something
''', re.VERBOSE)

# Regex for phone numbers
phone_regex = re.compile(r'''
	(
		(\+?\d{1,3}[\s.-]?)?        # optional country code
		(\(?\d{3}\)?[\s.-]?)        # area code
		(\d{3}[\s.-]?)              # first 3 digits
		(\d{4})                     # last 4 digits
	)
''', re.VERBOSE)

# Find matches
emails = email_regex.findall(text)
phones = phone_regex.findall(text)

# phone_regex returns tuples; extract the full match
phones_clean = [match[0] for match in phones]

# Combine results
results = "\n".join(emails + phones_clean)

# Copy back to clipboard
pyperclip.copy(results)

print("Done! Extracted items copied to clipboard:")
print(results)

