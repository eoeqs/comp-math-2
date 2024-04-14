import os


def validate_filename(name):
    if os.path.isfile(name):
        return True
    else:
        return False


def validate_input_data(lower_limit, upper_limit, epsilon):
    if lower_limit >= upper_limit:
        return False, "Lower limit should be less than upper limit."
    if epsilon <= 0:
        return False, "Epsilon should be greater than zero."
    return True, None


def validate_input_data_system(epsilon):
    if epsilon <= 0:
        return False, "Epsilon should be greater than zero."
    return True, None
