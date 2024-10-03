"""Test for loader.py ."""
from datetime import datetime
from pathlib import Path

from growi_salvage.dataclass import GrowiRevisionData
from growi_salvage.loader import load_growi_revision


def test_loader() -> None:
    """Test for load_growi_revision using revisions-sample.json ."""
    growi_revision_path = Path("./data/revisions-sample.json")
    growi_revision_data = load_growi_revision(path=growi_revision_path)
    assert len(growi_revision_data) == 5
    assert growi_revision_data[0] == GrowiRevisionData(
            _id="799A7AAC88A62C47135C2BF1",
            format="markdown",
            createdAt=datetime.fromisoformat("2020-02-19T08:32:27.266Z"),
            path="/user/Altair626/monthly",
            body="# Altair626\nThis is Altair626's page",
            author="1C1530A7F529961756E5081A",
            _v=0,
    )
    assert growi_revision_data[1] == GrowiRevisionData(
            _id="799A7AAC88A62C47135C2BF2",
            format="markdown",
            createdAt=datetime.fromisoformat("2020-02-21T08:32:27.266Z"),
            path="/user/Altair626/monthly",
            body="# Altair626\nHi! This is Altair626's page:)",
            author="1C1530A7F529961756E5081A",
            _v=0,
    )
