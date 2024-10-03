"""main function."""
from pathlib import Path

from growi_salvage.utils.dump import dump_revisions_as_md
from growi_salvage.utils.loader import load_growi_revision
from growi_salvage.utils.logger import get_logger
from growi_salvage.utils.modifier import get_newest_revision_per_path

logger = get_logger(name=__name__, level=10)


def main(revisions_json_path: str, output_dir: str) -> None:
    """Make markdown files from revision.json ."""
    growi_data = load_growi_revision(Path(revisions_json_path))
    newest_revisions = get_newest_revision_per_path(growi_data)

    logger.info(newest_revisions[:5])
    logger.info("Number of variety of pages: %d", len(newest_revisions))

    if not Path(output_dir).exists():
        Path(output_dir).mkdir()
    dump_revisions_as_md(newest_revisions, Path(output_dir))

if __name__ == "__main__":
    main("./data/revisions.json", "./data/out")
    main("./data/revisions-sample.json", "./data/out-sample")
