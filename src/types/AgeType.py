from typing import Any

from src.types.BaseType import BaseType


class AgeType(BaseType, int):

    def is_valid(self, value: Any) -> bool:
        try:
            if isinstance(value, str):
                value = int(value)

            if isinstance(value, int) and value >= 0:
                return True
        except:
            pass

        return False
