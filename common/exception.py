
class AppError(Exception):
    status_code = 400
    detail = "Application error"

    def __init__(self, detail=None):
        if detail:
            self.detail = detail


class UserNotFoudError(AppError):
    status_code = 404
    detail = "User tidak di temukan"

class PermissionDenail(AppError):
    status_code = 403
    detail = "Akses ditolak"

class DatabaseError(AppError):
    status_code = 503
    detail = "Data base error"

class UniqueError(AppError):
    status_code = 400
    detail = "Email telah digunakan"
