import re

emails = ['abc@gmail.com', '123$tt*@xyz.com', 'good@bad@uk.in', 'nasa@usa12.space', 'no-reply@domain.in', 'ramhanuman@saketa.lok', 'ruhi.mohan@exter123.123', 'fake@fake123.fakercom']

pattern_for_emil_verification = "^[a-zA-Z].[a-zA-Z0-9_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,3}$"

verified_emails = []
for email in emails:
    if re.match(pattern_for_emil_verification,email):
        verified_emails.append(email)
print(verified_emails)