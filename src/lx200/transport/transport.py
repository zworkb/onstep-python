
from typing import Protocol, runtime_checkable


@runtime_checkable
class Transport(Protocol):
    def send(self, msg: str) -> None:
        ...
    
    def recv(self) -> str:
        ...