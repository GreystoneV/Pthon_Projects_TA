# some_var = 'string'
# some_ml_var = '''string
#     over
#     lines
# '''
# var2 = some_var[1:3]
# print(var2)
# print(len(vars()))
#
# var3 = '    no spaces      '
# print(var3.strip())
#
# print(var3.upper())
# if 's' in var3:
#     print(var3)
#
# print(var2 + var3 + 'weeee')
#
# print('to print a \\ you have to use a \\')
#
# dict1 = {'Fname': 'Ben', 'Lname': 'Pritchard'}
#
# print(dict1.get("id123"))
# x = {'key1', 'key2', 'key3'}
# y = 0
# thisdict = dict.fromkeys(x, y)
#
# print(thisdict)

# import random
# print(random.randint(1, 100))


# def get_info():
#     var1 = input()
#     var2 = input()
#     return var1, var2
#
#
# def compute():
#     go = True
#     while go:
#         var1, var2 = get_info()
#         try:
#             var3 = int(var1) + int(var2)
#             go = False
#         except ValueError:
#             print("You did not provide a numeric value!")
#     print(f"{var1} + {var2} = {var3}")
#
#
#
#
# if __name__ == "__main__":
#     compute()

# import os
# print(os.getcwd())
#
#
# def write_data():
#     with open('README.md', 'a') as f:
#         user_input = input('Add something to the file: \n')
#         f.write(user_input)
#         f.close()
#
#
# def open_file():
#     with open('README.md', 'r') as f:
#         data = f.read()
#         print(data)
#         f.close()
#
#
# def choose_r_or_w(some_string):
#     if some_string == 'read':
#         open_file()
#     elif some_string == 'write':
#         write_data()
#     else:
#         print('Try running the program again.')
#         exit()
#
#
# answer = input('Would you like to "read" or "write"?:')
# choose_r_or_w(answer)

import os

file_name = 'Hello.txt'
file_path = 'C:'

ab_path = os.path.join(file_path, file_name)

print(ab_path)
