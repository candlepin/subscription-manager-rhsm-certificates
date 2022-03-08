import datetime
from tito.tagger.main import VersionTagger


class DateVersionTagger(VersionTagger):
    """
    A specialized version tagger that uses a YYYYMMDD format for
    upstream versions.

    Sadly it needs to be hacked by forcing a version (as if
    --use-version was specified), as the logic for determining the
    next version is not part of VersionTagger itself but comes from
    helper functions.
    """

    def _bump_version(self, release=False, zstream=False):
        if not release:
            if not hasattr(self, '_use_version'):
                today = datetime.date.today()
                self._use_version = today.strftime("%Y%m%d")
        return super()._bump_version(release, zstream)
