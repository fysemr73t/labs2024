import mailbox
import os
import email
from email.policy import default
from email import message_from_bytes
from email.header import decode_header
from pathlib import Path
import sys

# Configuration
email_file = sys.argv[1]

# Helper function to decode headers
def decode_header_value(value):
    if value:
        decoded = decode_header(value)
        return "".join(
            part.decode(encoding or "utf-8") if isinstance(part, bytes) else part
            for part, encoding in decoded
        )
    return ""


# Extract the first email
html_file = email_file+".html"
with open(email_file,'rb') as f:
    msg = email.message_from_binary_file(f, policy=default)
    for part in msg.walk():
        print(part.get_content_type())
        if part.get_content_type()=='text/html':
            with open(html_file, "wb") as f:
                f.write(part.get_payload(decode=True))
