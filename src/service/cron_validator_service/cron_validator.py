class CronValidatorService:

    def __init__(self, expression: str):
        self.expression = expression

    def validate(self):
        print(self.expression)
        return True
