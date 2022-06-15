import functools


# MODIFY THIS DECORATOR
def mask_data(target_key: str, replace_with: str = "*"):
    """Replace the value of a dictionary with a 'masked' version."""

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # do we need to check if the function returns a dict? or it's good enough?
            func_dict = func(*args, **kwargs)
            func_dict[target_key] = replace_with * len(func_dict[target_key])
            return func_dict

        return wrapper

    return decorator


# TARGET FUNCTIONS
@mask_data(target_key="name", replace_with="*")
def get_user(name: str, age: int):
    return {"name": name, "age": age}


# TEST OUPUT
print(get_user(name="Alice", age=30), get_user(name="Bob", age=25), sep="\n")
