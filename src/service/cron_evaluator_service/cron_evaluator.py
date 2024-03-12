from src.service.cron_definition_service.cron_definition import CronDefinitionService
from src.utils.utils import get_step_values, get_range_values


class CronEvaluatorService():

    def __init__(self, expression: str):
        self.expression = expression
        self.cron_definition = CronDefinitionService()

    def evaluate(self, cron_pattern: list[str]):
        res = {}
        # iterate for all values in cron_pattern
        for iter, field_str in enumerate(cron_pattern):

            # get field name associated with that index of cron pattern
            field_name = self.cron_definition.get_cron_field_names()[iter]

            # find the values of trigger for that particular field name nd add in dict
            res[field_name] = self._parse(field_name, field_str)

        return res

    def _parse(self, field_name, field_str):
        # get min and max value for a particular field name
        min_value = self.cron_definition.get_min_value(field_name)
        max_value = self.cron_definition.get_max_value(field_name)

        # store values based on field string
        values = []

        if field_str == self.cron_definition.get_any_value_operator():
            # Any value case
            values = list(range(min_value, max_value + 1))

        elif self.cron_definition.get_value_list_seperator_operator() in field_str:
            # List of values case
            values = []
            parts = field_str.split(self.cron_definition.get_value_list_seperator_operator())
            for part in parts:
                if part == self.cron_definition.get_any_value_operator():
                    continue  # Skip the "*" character
                if self.cron_definition.get_step_values_operator() in part:
                    step_parts = part.split(self.cron_definition.get_step_values_operator())
                    if len(step_parts) == 2:
                        if int(step_parts[1]) > min_value:
                            raise ValueError(f"Invalid cron field value for {field_name}: {field_str}")
                        range_values = get_step_values(step_parts[1], min_value, max_value)
                        values.extend(range_values)
                    else:
                        raise ValueError(f"Invalid cron field value for {field_name}: {field_str}")
                elif self.cron_definition.get_range_of_values_operator() in part:
                    range_values = get_range_values(part)
                    values.extend(range_values)
                else:
                    values.append(int(part))

        elif self.cron_definition.get_range_of_values_operator() in field_str:
            # Range value case
            values = get_range_values(field_str)

        elif self.cron_definition.get_step_values_operator() in field_str:
            # Step value case
            step_parts = field_str.split(self.cron_definition.get_step_values_operator())
            if len(step_parts) == 2:
                if int(step_parts[1]) > max_value:
                    raise ValueError(f"Invalid cron field value for {field_name}: {field_str}")
                values = get_step_values(step_parts[1], min_value, max_value)
            else:
                raise ValueError(f"Invalid cron field value for {field_name}: {field_str}")
        else:
            # Single value case
            values = [int(field_str)]

        return values
