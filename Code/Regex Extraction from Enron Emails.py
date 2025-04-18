import re

sample_email_text = """
Hi John, please contact me at alice@example.com or call 202-555-0143. 
We’ll meet on 12/05/2023 at 10:30 AM. Regards, Alice
"""

def extract_patterns(text):
    emails = re.findall(r"\b[\w.-]+?@\w+?\.\w+?\b", text)
    dates = re.findall(r"\b\d{1,2}/\d{1,2}/\d{2,4}\b", text)
    phones = re.findall(r"\b\d{3}[-.\s]\d{3}[-.\s]\d{4}\b", text)

    print("Emails:", emails)
    print("Dates:", dates)
    print("Phone Numbers:", phones)

if __name__ == "__main__":
    extract_patterns(sample_email_text)
