import re
# Define email validation function that compares email to valid regex string and returns true if it matches
def validateEmail(email):
    emailPattern = "(([A-Z]|[a-z]|[0-9])+(!|#|\|$|%|&|'|\*|\+|-|/|=|\?|\^|_|`|\{|\||\}|~)?)+@([A-Z]|[a-z]|[0-9]|-)+(.[a-z]([a-z])+)+"
    if re.fullmatch(emailPattern, email):
        return True
    else:
        return False
