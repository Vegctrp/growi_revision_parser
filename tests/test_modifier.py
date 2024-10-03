"""Test for modifier.py ."""
from datetime import datetime
from pathlib import Path

from growi_salvage.dataclass import GrowiRevisionData
from growi_salvage.loader import load_growi_revision
from growi_salvage.modifier import get_newest_revision_per_path


def test_get_newest_revision_per_path() -> None:
    """Test for get_newest_revision_per_path using revisions-sample.json ."""
    growi_revision_path = Path("./data/revisions-sample.json")
    growi_revision_data = load_growi_revision(path=growi_revision_path)
    newest_revision_data = get_newest_revision_per_path(growi_revision_data)
    assert len(newest_revision_data) == 3
    assert newest_revision_data[0] == GrowiRevisionData(
            _id="799A7AAC88A62C47135C2BF3",
            format="markdown",
            createdAt=datetime.fromisoformat("2020-02-21T08:33:27.266Z"),
            path="/user/Altair626/monthly",
            body="# Altair626\nHi! This is Altair626's page:) (This is the newest page!!!!!)",  # noqa: E501
            author="1C1530A7F529961756E5081A",
            _v=0,
    )
