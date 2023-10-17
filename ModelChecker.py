class ModalChecker:
    def __init__(self, selection_technique, use_case):
        self.selection_technique = selection_technique
        self.use_case = use_case
        self.conditions = set()
        self.actions = {}

    def parse_conditions_and_actions(self, description):
        conditions_actions = [condition.strip() for condition in description.split(';')]
        for condition_action in conditions_actions:
            condition, action = condition_action.split('->')
            self.conditions.add(condition)
            self.actions[condition] = action

    def model_check(self, condition_to_check):
        if condition_to_check not in self.conditions:
            print(f"Condition {condition_to_check} is not defined in the descriptions.")
            return None

        possible_values = set()

        for condition, selected_value in zip(self.conditions, self.actions.values()):
            if condition == condition_to_check:
                possible_values.add(selected_value)

        print(f"Possible values for {condition_to_check}: {possible_values}")
        return possible_values
