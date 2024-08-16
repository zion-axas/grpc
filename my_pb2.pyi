from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Medal(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    zero: _ClassVar[Medal]
    gold: _ClassVar[Medal]
    silver: _ClassVar[Medal]
    bronze: _ClassVar[Medal]
zero: Medal
gold: Medal
silver: Medal
bronze: Medal

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

class MapType(_message.Message):
    __slots__ = ("projects", "medal", "smart", "beauty")
    class ProjectsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: int
        def __init__(self, key: _Optional[str] = ..., value: _Optional[int] = ...) -> None: ...
    PROJECTS_FIELD_NUMBER: _ClassVar[int]
    MEDAL_FIELD_NUMBER: _ClassVar[int]
    SMART_FIELD_NUMBER: _ClassVar[int]
    BEAUTY_FIELD_NUMBER: _ClassVar[int]
    projects: _containers.ScalarMap[str, int]
    medal: Medal
    smart: str
    beauty: str
    def __init__(self, projects: _Optional[_Mapping[str, int]] = ..., medal: _Optional[_Union[Medal, str]] = ..., smart: _Optional[str] = ..., beauty: _Optional[str] = ...) -> None: ...
