FILE_NAME = "./lesson_4/generators/rockyou.txt"
SEARCH_KEYWORD = "user"


def read_lines_find_user_generator(search_keyword) -> tuple:
    results = []
    with open(FILE_NAME, encoding="utf-8") as file:
        while True:
            line = file.readline()
            if not line:
                break
            if search_keyword in line:
                line = line.replace("\n", "")
                added = input(
                    f"Add the word '{line}' in the results? Type 'yes'/'no' or 'exit': "
                )
                if added == "yes":
                    results.append(line)
                elif added == "exit":
                    print("Stopped reading the file.")
                    break
    print(f"Result: {results} \nLength: {len(results)} ")
    return results, len(
        results
    )  # the task requires to return value of results and results' length


print(read_lines_find_user_generator("user"))
