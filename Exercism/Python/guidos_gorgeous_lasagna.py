#TODO: define the 'EXPECTED_BAKE_TIME' constant.
EXPECTED_BAKE_TIME: int = 40
    

#TODO: Remove 'pass' and complete the 'bake_time_remaining()' function below.
def bake_time_remaining(time_in_the_oven: int) -> int:
    """"""
    return EXPECTED_BAKE_TIME - time_in_the_oven

def preparation_time_in_minutes(layers: int) -> int:
    """"""
    return layers * 2
#TODO: define the 'elapsed_time_in_minutes()' function below.
# Remember to add a docstring (you can copy and then alter the one from bake_time_remaining.)
def elapsed_time_in_minutes(number_of_layers: int, elapsed_bake_time: int) -> int:
    """"""
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time