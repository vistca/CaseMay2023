
# A custom Error used when the connection to the API fails
class MyAPIError(Exception):
    pass


# a custom Error used when the API do not have the requested data available
class MyInfoAccessError(Exception):
    pass
