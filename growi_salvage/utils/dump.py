"""dump module."""
from pathlib import Path

from growi_salvage.utils.dataclass import GrowiRevisionData
from growi_salvage.utils.logger import get_logger

logger = get_logger(name=__name__, level=10)


def dump_revision_as_md(revision: GrowiRevisionData, directory: Path) -> None:
    """Dump GrowiRevisionData as markdown file."""
    filename = revision.path.replace("/", "_") + ".md"
    filepath = directory.joinpath(filename)
    markdown_body = revision.get_markdown_body()
    logger.debug("start dumping %s", filepath)
    with Path.open(filepath, "w") as f:
        f.write(markdown_body)


def dump_revisions_as_md(revisions: list[GrowiRevisionData], directory: Path) -> None:
    """Dump all GrowiRevisionData as markdown file."""
    for revision in revisions:
        dump_revision_as_md(revision, directory)
