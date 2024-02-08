import secrets
import string
import random
# Storng password consists of ascii_characters, digits and proper punctation(special characters)
letters = string.ascii_letters # concatenations of lowercase and uppercase letters.
digits = string.digits
special = string.punctuation # special characters.
selection_list = letters+digits+special

# password len.
password_len = 10
password = ''
for i in range(password_len):
    password+=''.join(secrets.choice(selection_list))

print(password)

# This line imports the secrets module, which provides functions for generating cryptographically secure random numbers and strings. It's commonly used for generating secure tokens, passwords, etc.