from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SubData(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class Req(_message.Message):
    __slots__ = ("counter", "products", "subdata")
    COUNTER_FIELD_NUMBER: _ClassVar[int]
    PRODUCTS_FIELD_NUMBER: _ClassVar[int]
    SUBDATA_FIELD_NUMBER: _ClassVar[int]
    counter: int
    products: _containers.RepeatedScalarFieldContainer[str]
    subdata: SubData
    def __init__(self, counter: _Optional[int] = ..., products: _Optional[_Iterable[str]] = ..., subdata: _Optional[_Union[SubData, _Mapping]] = ...) -> None: ...

class Res(_message.Message):
    __slots__ = ("answer",)
    ANSWER_FIELD_NUMBER: _ClassVar[int]
    answer: str
    def __init__(self, answer: _Optional[str] = ...) -> None: ...
