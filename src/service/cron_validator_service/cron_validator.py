from src.service.cron_definition_service.cron_definition import CronDefinitionService


class CronValidatorService:

    def __init__(self, expression: str):
        self.expression = expression
        self.cron_definition_service = CronDefinitionService()

    def validate(self, cron_pattern: list[str]):

        # get field names for each field
        field_names = self.cron_definition_service.get_cron_field_names()

        # length check of cron based on fields we understand
        if len(cron_pattern) != len(field_names):
            raise ValueError(
                f"Invalid cron pattern length, cron pattern length should be {len(field_names)} not {len(cron_pattern)}")
            # return False

        # Iterate and validate value for each field
        for iter in range(len(field_names)):
            if not self._validate_field(cron_pattern[iter], field_names[iter]):
                return False
        return True

    def _validate_field(self, field_value, field_name):
        try:

            # get min and max value based on field
            min_value = self.cron_definition_service.get_min_value(field_name)
            max_value = self.cron_definition_service.get_max_value(field_name)

            # handling for ',' operator
            if self.cron_definition_service.get_value_list_seperator_operator() in field_value:
                # If there are multiple values separated by comma
                self._validate_comma_operator(field_value, min_value, max_value, field_name)

            # handling for '-' operator
            elif self.cron_definition_service.get_range_of_values_operator() in field_value:
                # If there's a range
                self._validate_hyphen_operator(field_value, min_value, max_value, field_name)

            # handling for '/' operator
            elif self.cron_definition_service.get_step_values_operator() in field_value:
                # If there's a step value
                self._validate_slash_operator(field_value, min_value, max_value, field_name)

            else:
                # Single value
                self._validate_single_value(min_value, max_value, field_name, field_value)

            return True
        except ValueError as ve:
            print(ve)
            return False

    def _validate_single_value(self, min_value, max_value, field_name, field_value):
        if self.cron_definition_service.get_any_value_operator() == field_value:
            return True
        try:
            num_value = int(field_value)
        except Exception as e:
            raise ValueError(f"Invalid cron field value for {field_name}: {field_value}")

        if num_value < min_value or num_value > max_value:
            raise ValueError(f"Invalid cron field value for {field_name}: {field_value}")
        return True

    def get_cron_pattern(self):
        # split fields based on space
        cron_values = self.expression.split(" ")

        # length check of cron based on fields we understand
        if len(cron_values) < len(self.cron_definition_service.get_cron_field_names()):
            return []

        cron_pattern = cron_values[:len(self.cron_definition_service.get_cron_field_names())]
        return cron_pattern

    def get_operations(self):
        # split fields based on space
        cron_values = self.expression.split(" ")

        # length check of cron based on fields we understand
        if len(cron_values) < len(self.cron_definition_service.get_cron_field_names()):
            return []

        # Get operations to trigger
        operations = cron_values[len(self.cron_definition_service.get_cron_field_names()):]
        return operations

    def _validate_comma_operator(self, field_value, min_value, max_value, field_name):
        res = True
        values = field_value.split(self.cron_definition_service.get_value_list_seperator_operator())
        for value in values:
            res &= self._validate_single_value(min_value, max_value, field_name, value)
            if not res:
                raise ValueError(f"Invalid cron field value for {field_name}: {field_value}")

    def _validate_hyphen_operator(self, field_value, min_value, max_value, field_name):
        start, end = map(int, field_value.split(self.cron_definition_service.get_range_of_values_operator()))
        if start < min_value or start > max_value or end < min_value or end > max_value or start >= end:
            raise ValueError(f"Invalid cron field value for {field_name}: {field_value}")

    def _validate_slash_operator(self, field_value, min_value, max_value, field_name):
        step = int(field_value.split(self.cron_definition_service.get_step_values_operator())[1])
        if step < min_value or step > max_value:
            raise ValueError(f"Invalid cron field value for {field_name}: {field_value}")
