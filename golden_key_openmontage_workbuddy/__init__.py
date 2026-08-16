"""WorkBuddy Shell V2 Package Registration API."""

from .package_registration import (
    PackageRegistrationError,
    activate_package,
    locate_active_package,
    recover_active_package,
    register_package,
)

__version__ = "0.1.0a0"

__all__ = [
    "PackageRegistrationError",
    "register_package",
    "activate_package",
    "recover_active_package",
    "locate_active_package",
    "__version__",
]
