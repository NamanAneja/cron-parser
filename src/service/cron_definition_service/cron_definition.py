from src.constants.Fields import Fields


class CronDefinitionService:

    def __init__(self):
        self.field_min_map = {
            Fields.MINUTE: 0,
            Fields.MONTH: 1,
            Fields.HOUR: 0,
            Fields.DAY_OF_WEEK: 0,
            Fields.DAY_OF_MONTH: 1
        }
        self.field_max_map = {
            Fields.MINUTE: 59,
            Fields.MONTH: 12,
            Fields.HOUR: 23,
            Fields.DAY_OF_WEEK: 6,
            Fields.DAY_OF_MONTH: 31
        }
        self.num_of_fields = 5
        self.cron_field_names = [
            Fields.MINUTE,
            Fields.HOUR,
            Fields.DAY_OF_MONTH,
            Fields.MONTH,
            Fields.DAY_OF_WEEK
        ]
        self.ANY_VALUE = '*'
        self.VALUE_LIST_SEPARATOR = ','
        self.RANGE_OF_VALUES = '-'
        self.STEP_VALUES = '/'

    def get_number_of_fields(self):
        return self.num_of_fields

    def get_min_value(self, field: Fields):
        return self.field_min_map[field]

    def get_max_value(self, field: Fields):
        return self.field_max_map[field]

    def get_cron_field_names(self):
        return self.cron_field_names

    def get_any_value_operator(self):
        return self.ANY_VALUE

    def get_value_list_seperator_operator(self):
        return self.VALUE_LIST_SEPARATOR

    def get_range_of_values_operator(self):
        return self.RANGE_OF_VALUES

    def get_step_values_operator(self):
        return self.STEP_VALUES

    def get_operators(self):
        return [self.RANGE_OF_VALUES, self.ANY_VALUE, self.STEP_VALUES, self.VALUE_LIST_SEPARATOR]
