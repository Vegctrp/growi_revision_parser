"""loader module for revisions.json ."""
import json
from pathlib import Path

from growi_salvage.dataclass import GrowiRevisionData
from growi_salvage.logger import get_logger

logger = get_logger(name=__name__, level=10)
DEFAULT_PATH = Path("./data/revisions-sample.json")


def load_growi_revision(path: Path = DEFAULT_PATH) -> list[GrowiRevisionData]:
    """Load Growi Revision data from specified path.

    Args:
        path: pathlib.Path object that refer revisions.json .

    Returns:
        list[GrowiRevisionData]: list of GrowiRevisionData from specified revision.json .

    """
    with Path.open(path) as f:
        data = json.load(f)
    revisions = []
    for d in data:
        d["_v"] = d.pop("__v")
        logger.debug(d)
        revisions.append(GrowiRevisionData(**d))
    return revisions
