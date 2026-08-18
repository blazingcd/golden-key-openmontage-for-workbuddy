"""WorkBuddy Shell V2 public API."""

from .package_registration import (
    PackageRegistrationError,
    activate_package,
    locate_active_package,
    recover_active_package,
    register_package,
)
from .runtime_prepare import prepare_optional_capabilities

__version__ = "0.1.0a0"

__all__ = [
    "PackageRegistrationError",
    "register_package",
    "activate_package",
    "recover_active_package",
    "locate_active_package",
    "prepare_optional_capabilities",
    "__version__",
]
