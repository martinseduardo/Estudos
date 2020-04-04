from validate_docbr import CPF
from validate_docbr import CNPJ

class DocumentRegister:

    @staticmethod
    def create_register(number):
        number = str(number)
        if len(number) == 11:
            return CpfRegister(number)
        elif len(number) == 14:
            return CnpjRegister(number)
        else:
            raise ValueError("Quantidade de digitos inválida!")

class CpfRegister:
    def __init__(self, number):
        if self.validate(number):
            self.cpf = number
            self.document_type = "CPF"
        else:
            raise ValueError("CPF Inválido!")

    def validate(self, cpf):
        validate_cpf = CPF()
        return validate_cpf.validate(cpf)

    def format(self):
        cpf_mask = CPF()
        return cpf_mask.mask(self.cpf)

    def __str__(self):
        return f"{self.document_type}: {self.format()}"

class CnpjRegister:
    def __init__(self, number):
        if self.validate(number):
            self.cnpj = number
            self.document_type = "CNPJ"
        else:
            raise ValueError("CNPJ Inválido!")

    def validate(self, cnpj):
        validate_cnpj = CNPJ()
        return validate_cnpj.validate(cnpj)

    def format(self):
        cnpj_mask = CNPJ()
        return cnpj_mask.mask(self.cnpj)

    def __str__(self):
        return f"{self.document_type}: {self.format()}"