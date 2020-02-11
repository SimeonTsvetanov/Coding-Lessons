# Simeon Tsvetanov - Solution of Email Validator:
class NameTooShortError(Exception):
    """
    This error will be raised when the name is less then or equal to 4 symbols.
    And the given message must be:
    Name must be more than 4 characters
    """


class MustContainAtSymbolError(Exception):
    """
    This error will be raised when the name does not include the symbol "@".
    And the given message must be:
    Email must contain @
    """


class InvalidDomainError(Exception):
    """
    This error will be raised when the domain doesn't end on .com, .bg, .org, .net.
    and the message must be:
    Domain must be one of the following: .com, .bg, .org, .net
    """


while True:
    email = input()
    if email == "End":
        break
    first_part = email.split("@")[0]
    if len(first_part) <= 4:
        raise NameTooShortError("Name must be more than 4 characters")
    if "@" not in email:
        raise MustContainAtSymbolError("Email must contain @")
    valid_domains = [".com", ".bg", ".org", ".net"]
    if not (email.endswith(".com") or email.endswith(".bg") or email.endswith(".net") or email.endswith(".net")):
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")
    print(f"Email is valid")
