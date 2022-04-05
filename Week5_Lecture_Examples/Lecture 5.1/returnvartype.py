def get_secret_code(password):
    if password != "bicycle":
        raise ValueError
    else:
        return "42"

try:
    secret_code = get_secret_code("bicycle")
    print("The secret code is {}".format(secret_code))
except ValueError:
    print("Wrong password.")
