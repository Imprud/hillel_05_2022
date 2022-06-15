import functools


# MODIFY THIS DECORATOR
def reverse_string(func):
    """If output is a string, reverse it. Otherwise, return None."""

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        university_name = func(*args, **kwargs)
        # if type(university_name) == str:
        if isinstance(university_name, str):
            return university_name[::-1]
        else:
            return None

    return wrapper


# TARGET FUNCTIONS
@reverse_string
def get_university_name() -> str:
    return "Western Institute of Technology and Higher Education"


@reverse_string
def get_university_founding_year() -> int:
    return 1957


# TEST OUPUT
print(get_university_name(), get_university_founding_year(), sep="\n")
