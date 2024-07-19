class BaseAppException(Exception):
    """アプリケーション固有の基本例外クラス"""

    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)


class NotionAPIError(BaseAppException):
    """Notion API関連のエラーを表す例外クラス"""

    def __init__(self, message: str, status_code: int = None):
        self.status_code = status_code
        super().__init__(f"Notion API Error: {message}")


class DatabaseError(BaseAppException):
    """データベース操作に関連するエラーを表す例外クラス"""
    pass


class ValidationError(BaseAppException):
    """データ検証エラーを表す例外クラス"""
    pass


class AuthenticationError(BaseAppException):
    """認証エラーを表す例外クラス"""
    pass


class AuthorizationError(BaseAppException):
    """認可エラーを表す例外クラス"""
    pass


class ResourceNotFoundError(BaseAppException):
    """リソースが見つからない場合のエラーを表す例外クラス"""
    pass


class ConfigurationError(BaseAppException):
    """設定関連のエラーを表す例外クラス"""
    pass
