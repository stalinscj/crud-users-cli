import re
from typing import Any

from src.types.BaseType import BaseType


class EmailType(BaseType, str):

    def is_valid(self, value: Any) -> bool:

        if not isinstance(value, str):
            return False

        regex = r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+"

        match = re.fullmatch(regex, value)

        return True if match else False
