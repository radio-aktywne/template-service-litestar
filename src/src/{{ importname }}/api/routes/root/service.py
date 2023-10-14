from typing import Literal


class Service:
    """Service for the root endpoint."""

    async def foo(self) -> Literal["bar"]:
        """Get 'bar'."""

        return "bar"
