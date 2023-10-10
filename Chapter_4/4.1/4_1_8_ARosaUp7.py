def is_palindrome(x):
    if isinstance(x, int):
        return str(x)[::-1] == str(x)
    if isinstance(x, str):
        return str(x)[::-1] == str(x)
    if isinstance(x, list | tuple):
        return x[::-1] == str(x)
