import re

def count_valid_emails(emails):
    count = 0
    proper_email_format = r"^[a-zA-Z0-9._%+-]+(?:[^\.\s]+)*@[a-zA-Z0-9-]+\.[a-zA-Z]{2,}$"

    for email in emails:
        if re.match(proper_email_format, email):
            count += 1

    return count
