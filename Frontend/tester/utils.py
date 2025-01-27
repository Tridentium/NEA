import re
def validateEmail(email):
    emailPattern = "(([A-Z]|[a-z]|[0-9])+(!|#|\|$|%|&|'|\*|\+|-|/|=|\?|\^|_|`|\{|\||\}|~)?)+@([A-Z]|[a-z]|[0-9]|-)+(.[a-z]([a-z])+)+"
    if re.fullmatch(emailPattern, email):
        return True
    else:
        return False
