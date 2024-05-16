class BaseError(Exception):
    def __init__(self, msg):
        self.msg = msg
    
    def __repr__(self):
        return self.msg

    def __str__(self):
        return self.msg

class CardRequiredFieldError(BaseError):
    ...

class CardMissingFieldsError(BaseError):
    ...

class FileFormatError(BaseError):
    ...