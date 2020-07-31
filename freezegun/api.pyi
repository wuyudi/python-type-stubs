import datetime
import numbers
import types
from typing import Any, Callable, NoReturn, Optional, Sequence, Tuple, Type, Union

class TickingDateTimeFactory(object):
    def __init__(
        self, time_to_freeze: datetime.datetime, start: datetime.datetime
    ) -> NoReturn:
        self.time_to_freeze: datetime.datetime = ...
        self.start: datetime.datetime = ...
    def __call__(self) -> datetime.datetime: ...

class FrozenDateTimeFactory(object):
    def __init__(self, time_to_freeze: datetime.datetime) -> NoReturn:
        self.time_to_freeze: datetime.datetime = ...
    def __call__(self) -> datetime.datetime: ...
    def tick(
        self, delta: Union[float, numbers.Real, datetime.timedelta] = ...
    ) -> NoReturn: ...
    def move_to(
        self,
        target_datetime: Optional[
            Union[str, datetime.datetime, datetime.date, datetime.timedelta]
        ],
    ) -> NoReturn:
        """Moves frozen datetime.date to the given ``target_datetime``"""
        ...

class StepTickTimeFactory(object):
    def __init__(
        self, time_to_freeze: datetime.datetime, step_width: float
    ) -> NoReturn:
        self.time_to_freeze = ...
        self.step_width = ...
    def __call__(self) -> datetime.datetime: ...
    def tick(self, delta: Optional[datetime.timedelta] = ...) -> NoReturn: ...
    def update_step_width(self, step_width: float) -> NoReturn:
        self.step_width = ...
    def move_to(
        self,
        target_datetime: Optional[
            Union[str, datetime.datetime, datetime.date, datetime.timedelta]
        ],
    ) -> NoReturn:
        """Moves frozen datetime.date to the given ``target_datetime``"""
        ...

class _freeze_time:
    time_to_freeze: datetime.datetime = ...
    tz_offset: float = ...
    ignore: Sequence[str] = ...
    tick: bool = ...
    auto_tick_seconds: float = ...
    undo_changes: Sequence[Tuple[types.ModuleType, str, Any]] = ...
    modules_at_start: Sequence[str] = ...
    as_arg: bool = ...
    def __init__(
        self,
        time_to_freeze_str: Union[
            None, str, datetime.datetime, datetime.date, datetime.timedelta
        ],
        tz_offset: float,
        ignore: Sequence[str],
        tick: bool,
        as_arg: bool,
        auto_tick_seconds: float,
    ) -> NoReturn: ...
    def __call__(self, func: Any) -> Any: ...
    def __enter__(
        self,
    ) -> Union[StepTickTimeFactory, TickingDateTimeFactory, FrozenDateTimeFactory]: ...
    def __exit__(self, *args: Any) -> NoReturn: ...
    def start(
        self,
    ) -> Union[StepTickTimeFactory, TickingDateTimeFactory, FrozenDateTimeFactory]: ...
    def stop(self) -> NoReturn: ...
    def decorate_class(self, klass: Any) -> Any: ...
    def decorate_coroutine(self, coroutine: Any) -> Any: ...
    def decorate_callable(self, func: Callable[..., Any],) -> Callable[..., Any]: ...

def freeze_time(
    time_to_freeze: Optional[
        Union[
            str,
            datetime.datetime,
            datetime.date,
            datetime.timedelta,
            types.FunctionType,
            types.GeneratorType,
        ]
    ] = ...,
    tz_offset: Optional[float] = ...,
    ignore: Optional[Sequence[str]] = ...,
    tick: Optional[bool] = ...,
    as_arg: Optional[bool] = ...,
    auto_tick_seconds: Optional[float] = ...,
) -> _freeze_time: ...
