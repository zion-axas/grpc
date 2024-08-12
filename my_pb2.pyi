from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Req(_message.Message):
    __slots__ = ("counter",)
    COUNTER_FIELD_NUMBER: _ClassVar[int]
    counter: int
    def __init__(self, counter: _Optional[int] = ...) -> None: ...

class Res(_message.Message):
    __slots__ = ("answer",)
    ANSWER_FIELD_NUMBER: _ClassVar[int]
    answer: str
    def __init__(self, answer: _Optional[str] = ...) -> None: ...
