"""Fail closed when an offline Golden Key Tool launches a Python subprocess."""

from __future__ import annotations

import os
import socket


if os.environ.get("GOLDEN_KEY_WORKBUDDY_OFFLINE_GUARD") == "1":

    def _blocked(*args, **kwargs):
        raise RuntimeError(
            "local-only Tool subprocess network access is blocked by the "
            "WorkBuddy runtime"
        )

    socket.create_connection = _blocked
    socket.getaddrinfo = _blocked
    socket.socket.connect = _blocked
    socket.socket.connect_ex = _blocked
    socket.socket.sendto = _blocked
