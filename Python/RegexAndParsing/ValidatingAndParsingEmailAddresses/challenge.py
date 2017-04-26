import email.utils
import re


def is_valid_username(user):
    match = re.search("^[A-Za-z0-9][-_.A-Za-z0-9]*$", user)
    return True if match else False


def is_valid_domain(s):
    match = re.search("^[A-Za-z]+$", s)
    return True if match else False


def is_valid_extension(e):
    if len(e) < 1 or len(e) > 3:
        return False
    return is_valid_domain(e)  # domain and extension both alphabetical


def get_proper_emails(list_of_emails):
    valid_emails = []
    for name_email in list_of_emails:
        try:
            name = name_email[0]
            emailaddr = name_email[1]
            username = emailaddr.split('@')[0]
            domain = emailaddr.split('@')[1].split('.')[0]
            extension = emailaddr.split('@')[1].split('.')[1]

            if is_valid_username(username) and is_valid_domain(domain) and is_valid_extension(extension):
                if username + "@" + domain + "." + extension == emailaddr:
                    valid_emails.append(email.utils.formataddr((name, emailaddr)))
        except IndexError:
            pass  # Couldn't parse email

    return valid_emails


if __name__ == "__main__":
    name_email_collection = []
    for _ in range(int(raw_input())):
        line = raw_input()
        name_email_collection.append(email.utils.parseaddr(line))

    valid_emails = get_proper_emails(name_email_collection)
    for i in valid_emails:
        print i
