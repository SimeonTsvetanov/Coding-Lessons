class EmailValidator:
    def __init__(self, min_length: int, mails: list, domains: list):
        self.min_length = min_length
        self.mails = mails
        self.domains = domains

    def __validate_name(self, name):
        """Private Method - returns whether the name is greater than or equal to the min_length (True/False)"""
        return len(name) >= self.min_length

    def __validate_mail(self, mail):
        """Private Method - returns whether the mail is in the possible mails list (True/False)"""
        return mail in self.mails

    def __validate_domain(self, domain):
        """Private Method - returns whether the domain is in the possible domains list (True/False)"""
        return domain in self.domains

    def validate(self, email):
        """Public Method - using the three private methods returns whether the email is valid (True/False)"""
        name = email.split("@")[0]
        mail = (email.split("@")[1]).split(".")[0]
        domain = (email.split("@")[1]).split(".")[1]
        return self.__validate_name(name) and self.__validate_mail(mail) and self.__validate_domain(domain)


mails = ["gmail", "softuni"]
domains = ["com", "bg"]
email_validator = EmailValidator(6, mails, domains)
print(email_validator.validate("pe77er@gmail.com"))
print(email_validator.validate("georgios@gmail.net"))
print(email_validator.validate("stamatito@abv.net"))
print(email_validator.validate("abv@softuni.bg"))
