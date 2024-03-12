from src.constants.Fields import Fields
from src.service.cron_expression_service.cron_expression import CronExpressionService


class CronController:

    def evaluate(self, expression):
        # evaluate expression
        try:
            cron_evaluation = CronExpressionService(expression).validate_and_evaluate()
        except ValueError as ve:
            print(ve)
            return False

        # print cron in desired format
        return self._format_and_print(cron_evaluation)

        # return True

    def _format_and_print(self, cron_evaluation):
        field_names = [
            Fields.MINUTE,
            Fields.HOUR,
            Fields.DAY_OF_MONTH,
            Fields.MONTH,
            Fields.DAY_OF_WEEK,
            Fields.OPERATIONS
        ]
        output = []
        for each in field_names:
            output.append(f"{each.value:<14}{' '.join(map(str,cron_evaluation[each]))}")

        # print("\n".join(output))
        return "\n".join(output)
