class ServiceError(Exception):
    """Base class for service errors."""

    pass


class FooError(ServiceError):
    """Example error."""

    pass
