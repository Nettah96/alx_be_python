class Calculator:
    # Class attribute
    calculation_type = "Arithmetic Operations"

    # Static method: doesn't use self or cls
    @staticmethod
    def add(a, b):
        return a + b

    # Class method: has access to class attributes
    @classmethod
    def multiply(cls, a, b):
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
