import email
from email.policy import default

def parse_email(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        message = email.message_from_file(file, policy=default)

    email_content = {
        "headers": dict(message.items()),
        "body": "",
        "attachments": []
    }

    if message.is_multipart():
        for part in message.iter_parts():
            content_disposition = part.get("Content-Disposition", "")
            if "attachment" in content_disposition:
                attachment = {
                    "filename": part.get_filename(),
                    "content": part.get_payload(decode=True),
                    "content_type": part.get_content_type()
                }
                email_content["attachments"].append(attachment)
            elif part.get_content_type() == "text/plain":
                email_content["body"] += part.get_content().strip()
            elif part.get_content_type() == "text/html":
                email_content["body"] += part.get_content().strip()
    else:
        email_content["body"] = message.get_content()

    return email_content

# Usage
email_file = "msg3.txt"
parsed_email = parse_email(email_file)

# Print parsed data
print("Headers:", parsed_email["headers"])
print("Body:", parsed_email["body"])
print("Attachments:", [(att['filename'], att['content_type']) for att in parsed_email["attachments"]])
