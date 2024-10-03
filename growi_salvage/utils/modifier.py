"""modifier modules."""
from growi_salvage.utils.dataclass import GrowiRevisionData


def get_newest_revision_per_path(
        revisions: list[GrowiRevisionData],
) -> list[GrowiRevisionData]:
    """Get newest revisions in each path.

    Args:
        revisions (list[GrowiRevisionData]): list of GrowiRevisionData

    Returns:
        list[GrowiRevisionData]

    """
    newest_revision_per_path: dict[str, GrowiRevisionData] = {}
    for revision in revisions:
        if revision.path in newest_revision_per_path:
            if newest_revision_per_path[revision.path].createdAt < revision.createdAt:
                newest_revision_per_path[revision.path] = revision
        else:
            newest_revision_per_path[revision.path] = revision
    return list(newest_revision_per_path.values())
