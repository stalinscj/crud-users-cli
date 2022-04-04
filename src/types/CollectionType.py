import json
from typing import Any

from src.types.BaseType import BaseType


class CollectionType(BaseType, list):

    def is_valid(self, value: Any) -> bool:
        return True if isinstance(value, list) else False

    def __str__(self) -> str:
        return json.dumps([str(x) for x in self], indent=2)
