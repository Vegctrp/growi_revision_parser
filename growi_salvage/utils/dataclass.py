"""define dataclasses."""

from datetime import datetime

from pydantic.dataclasses import dataclass


@dataclass
class GrowiRevisionData:
    """Growiのrevisionデータを表すクラス."""

    _id: str
    format: str
    createdAt: datetime  # noqa: N815
    path: str
    body: str
    author: str
    _v: int

    def get_markdown_body(self) -> str:
        """Get markdown_format body string."""
        return self.body  # TODO: handle if body is not markdown-format
