from src.service.cron_display_service.cron_display import CronDisplayService
from src.service.cron_validator_service.cron_validator import CronValidatorService


class CronExpressionService:

    def __init__(self, expression: str):
        self.expression = expression
        self.cron_validator_service = CronValidatorService(expression)
        self.cron_display_service = CronDisplayService(expression)

    def validate_cron(self):
        if self.cron_validator_service.validate():
            return True

        return False

    def evaluate_cron(self):
        pass
