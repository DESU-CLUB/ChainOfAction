```python
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        # 1: Initialize a set to store unique email addresses.
        unique_emails = set()

        # 2: Loop through the list of emails.
        for email in emails:
            # 3: For each email, split the local name and domain name by the '@' character.
            local, domain = email.split('@')

            # 4: Remove all periods ('.') from the local name.
            local = local.replace('.', '')

            # 5: Discard everything after the first plus ('+') in the local name.
            local = local.split('+')[0]

            # 6: Concatenate the processed local name with the domain name.
            clean_email = local + '@' + domain

            # 7: Add the resulting email address to the set.
            unique_emails.add(clean_email)

        # 8: Return the size of the set as the number of unique email addresses.
        return len(unique_emails)
```