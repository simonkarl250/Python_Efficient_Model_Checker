import ModelChecker;

# using the model checker:
selection_technique = "A->T,F; B->T,F; C->T,F"
use_case = "A->B, C; T->T, T"

modal_checker = ModelChecker.ModalChecker(selection_technique, use_case)

# getting the required conditions and actions from the descriptions
modal_checker.parse_conditions_and_actions(selection_technique)
modal_checker.parse_conditions_and_actions(use_case)

# verifying and Solving for A 
result_A = modal_checker.model_check('K')