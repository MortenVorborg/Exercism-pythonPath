import re

def response(hey_bob):

    stripped = hey_bob.strip()

    if not stripped:
        return "Fine. Be that way!"

    if not re.search(r'[A-Za-z]', stripped):
        if stripped.endswith("?"):
            return "Sure."
        else:
            return "Whatever."

    if stripped.isupper():
        if stripped.endswith("?"):
            return "Calm down, I know what I'm doing!"
        else:
            return "Whoa, chill out!"

    if stripped.endswith("?"):
        return "Sure."
    else:
        return "Whatever."
