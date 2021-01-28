from openff.units._version import get_versions  # type: ignore
from openff.units.units import DEFAULT_UNIT_REGISTRY

unit = DEFAULT_UNIT_REGISTRY

# Handle versioneer
versions = get_versions()
__version__ = versions["version"]
__git_revision__ = versions["full-revisionid"]
del get_versions, versions
