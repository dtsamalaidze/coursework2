class BaseAppExceptions(Exception):
    code = 404


class FileNotFound(BaseAppExceptions):
    code = 404


class FileTypeError(BaseAppExceptions):
    code = 500
