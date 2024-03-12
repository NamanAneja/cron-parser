from src.constants.Fields import Fields
from src.service.cron_evaluator_service.cron_evaluator import CronEvaluatorService
from src.service.cron_validator_service.cron_validator import CronValidatorService


class CronExpressionService:

    def __init__(self, expression: str):
        self.expression = expression
        self.cron_validator_service = CronValidatorService(expression)
        self.cron_evaluator_service = CronEvaluatorService(expression)

    def validate_cron(self, cron_pattern: list[str]):
        if self.cron_validator_service.validate(cron_pattern):
            return True

        return False

    def evaluate_cron(self, cron_pattern: list[str]):
        return self.cron_evaluator_service.evaluate(cron_pattern)

    def validate_and_evaluate(self):
        # get cron pattern and operations from expression
        cron_pattern = self.cron_validator_service.get_cron_pattern()
        cron_operations = self.cron_validator_service.get_operations()

        if len(cron_pattern) == 0 or len(cron_operations) == 0:
            raise ValueError(f"Invalid cron expression {self.expression}")
            # return False

        triggers = {}
        if self.validate_cron(cron_pattern):
            triggers = self.evaluate_cron(cron_pattern)
        else:
            raise ValueError(f"Invalid cron expression {self.expression}")
            # return False

        triggers[Fields.OPERATIONS] = cron_operations
        return triggers
