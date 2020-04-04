import re


class PhoneRegister:
    def __init__(self, number):
        if self.validate(number):
            self.number = str(number)
        else:
            raise ValueError("Telefone inválido!")

    def __str__(self):
        return self.format()

    def validate(self, number):
        standard_model = "([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
        phone = re.findall(standard_model, number)
        if phone:
            return True
        else:
            return False

    def format(self):
        standard_model = "([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
        phone = re.search(standard_model, self.number)
        if phone.group(1) == None:
            return f"({phone.group(2)})" \
                   f"{phone.group(3)}" \
                   f"-{phone.group(4)}"
        else:
            return f"+{phone.group(1)}" \
                   f"({phone.group(2)})" \
                   f"{phone.group(3)}" \
                   f"-{phone.group(4)}"
