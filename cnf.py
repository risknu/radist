from __future__ import annotations

from os import environ
from dotenv import load_dotenv; load_dotenv()

from dataclasses import dataclass
from typing import Optional

@dataclass
class cnf:
    token: Optional[str] = environ.get('TOKEN')
    