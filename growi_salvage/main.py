from pathlib import Path

from growi_salvage.utils.loader import load_growi_revision
from growi_salvage.utils.logger import get_logger
from growi_salvage.utils.modifier import get_newest_revision_per_path

logger = get_logger(name=__name__, level=10)

def main(path: str) -> None:
    """Make markdown files from revision.json ."""
    growi_revision_path = Path(path)
    growi_data = load_growi_revision(growi_revision_path)
    newest_revisions = get_newest_revision_per_path(growi_data)

    logger.info(newest_revisions[:5])
    logger.info("Number of variety of pages: %d", len(newest_revisions))

    # TODO: add dump

if __name__ == "__main__":
    main("./data/revisions.json")
