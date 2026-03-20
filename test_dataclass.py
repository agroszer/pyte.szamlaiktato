from dataclasses import dataclass
from typing import Optional, Any

@dataclass
class MyResponse:
    type: Optional[str] = None
    list: Optional[__builtins__.list[dict[str, Any]]] = None

print(MyResponse(type="hello", list=[{"a": 1}]))
