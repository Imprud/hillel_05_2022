from email.generator import Generator

FILE_NAME = "./lesson_4/generators/rockyou.txt"
SEARCH_KEYWORD = "admin"


# def read_lines_find_admin() -> list:

#     with open(FILE_NAME, encoding='utf-8') as file:
#         return [word for word in file.readlines() if SEARCH_KEYWORD in word]


# # print(f'Lines: {len(read_lines_find_admin())}')


def read_lines_find_admin_generator() -> Generator:
    with open(FILE_NAME, encoding="utf-8") as file:
        while True:
            line = file.readline()
            if not line:
                break
            if SEARCH_KEYWORD in line:
                yield line.replace("\n", "")


# print(f'Lines2: {read_lines_find_admin_generator()}')

for line in read_lines_find_admin_generator():
    print(line)
