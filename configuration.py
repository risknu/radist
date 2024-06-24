from __future__ import annotations

from packaging.version import Version
from typing import Optional

from disnake import Status

from dataclasses import dataclass
from dotenv import load_dotenv
from os import environ, path
from sys import exit, version_info

import functools

MIN_PYTHON_VERSION: Version = Version("3.11")
FILES_TO_CHECK: list[str] = ['cogs/', '.env']


@functools.cache
def check_project_valid() -> None:
    if MIN_PYTHON_VERSION > Version(f"{version_info.major}.{version_info.minor}.{version_info.micro}"):
        exit(1)
    for filename in FILES_TO_CHECK:
        if not path.exists(filename):
            exit(1)
    load_dotenv('.env')


check_project_valid()


@dataclass
class ENV:
    TOKEN: Optional[str] = environ.get('TOKEN')
    
@dataclass
class Conf:
    MODEL: str = "llama3"
    
    BOT_ACTIVITY_TYPE: str = "watch"
    BOT_ACTIVITY_STRING: str = "risknu pencil"
    BOT_STATUS: Status = Status.idle
