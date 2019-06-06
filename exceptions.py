# user_input = 'a'
# d = {'b': 'valid'}
# try:
#     int(user_input)
#     d[user_input]
# except (KeyError, ValueError) as k:
#     print('Come on man!', k)


# def division(num):
#     try:
#         result = 3.14/num
#         print(result)
#     except ZeroDivisionError:
#         print('Divide by zero error')
#     except ArithmeticError:
#         print('We had a general math error')


# division(56)

# class MyCustomException(Exception):
#     pass


# raise MyCustomException()

# class IncorrectValueError(Exception):
#     def __init__(self, value):
#         message = f'Got a bad value: {value}'
#         super().__init__(message)


# my_val = 9

# if my_val < 10:
#     raise IncorrectValueError(my_val)

# class GitHubApiError(Exception):

#     def __init__(self, status_code):
#         if status_code == 403:
#             message = 'Rate limit reached.'
#         else:
#             message = f'Status code was: {status_code}'

#         super().__init__(message)


# raise GitHubApiError(403)

# class MyError(Exception):
#     pass


# raise MyError()


class MyError(Exception):
    def __init__(self, message):
        new_message = f'!!!!!EORORR !!! system failure: {message}'
        super().__init__(new_message)


# raise MyError('Ohno')

# my_dict = {1: 'true'}

# try:
#     my_dict['random']
# except KeyError as e:
#     print(f'oh no the key doesn\'t exist. error was: {e}')

# my_list = list(range(5, 0, -1))

for num in range(5, -1, -1):
    try:
        5 / num
    except ZeroDivisionError:
        raise MyError('haha you divided by zero, idiot!')


# print(my_list)
