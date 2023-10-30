from H_5_3_8_ValNamePo import username_validation
from G_5_3_7_ValName import name_validation


def user_validation(**kwargs):
    if len(kwargs) != 3:
        raise KeyError
    last_name = kwargs["last_name"]
    first_name = kwargs["first_name"]
    username = kwargs["username"]
    if not (isinstance(last_name, str) and isinstance(first_name, str)
            and isinstance(username, str)):
        raise TypeError

    _ = name_validation(last_name)
    _ = name_validation(first_name)
    _ = username_validation(username)
    return kwargs


print(user_validation(last_name="Иванов", first_name="Иван", username="ivanych45"))
