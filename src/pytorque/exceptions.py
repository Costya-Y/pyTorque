class TorqueError(Exception):
    """Base exception for pyTorque."""

class AuthenticationError(TorqueError):
    pass

class NotFoundError(TorqueError):
    pass

class RateLimitError(TorqueError):
    pass

class ServerError(TorqueError):
    pass
