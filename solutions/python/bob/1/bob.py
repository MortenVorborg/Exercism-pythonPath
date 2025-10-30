import re

def response(hey_bob):

    stripped = hey_bob.strip()

    # 1. Empty or only whitespace
    if not stripped:
        return "Fine. Be that way!"


    if not re.search(r'[A-Za-z]', stripped):
        if stripped.endswith("?"):
            return "Sure."
        else:
            return "Whatever."

    # 3. All uppercase letters
    if stripped.isupper():
        if stripped.endswith("?"):
            return "Calm down, I know what I'm doing!"
        else:
            return "Whoa, chill out!"

    # 4. Lowercase or mixed case
    if stripped.endswith("?"):
        return "Sure."
    else:
        return "Whatever."
