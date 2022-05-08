import datetime
from collections.abc import Callable
from typing import Any, TypeVar, overload

from huey.api import (
    Huey,
    Result,
    ResultGroup,
    Task,
    TaskLock,
    TaskWrapper,
    _OnShutdownHandler,
    _OnStartupHandler,
    _PostExecuteHandler,
    _PreExecuteHandler,
    _SignalHandler,
)
from huey.signals import _SIGNAL
from typing_extensions import ParamSpec

from django_huey.config import DjangoHueySettingsReader as DjangoHueySettingsReader

DJANGO_HUEY: dict
config: DjangoHueySettingsReader

_T = TypeVar("_T")
_P = ParamSpec("_P")

def get_close_db_for_queue(
    queue: str | None = ...,
) -> Callable[[Callable[_P, _T]], Callable[_P, _T]]: ...
def get_queue(queue: str | None = ...) -> Huey: ...
def get_queue_name(queue: str | None) -> str: ...

# When changing these functions, also change the corresponding functions in
# huey-stubs/api.pyi
# huey-stubs/contrib/djhuey/__init__.pyi
def task(
    retries: int = ...,
    retry_delay: int = ...,
    priority: int | None = ...,
    context: bool = ...,
    name: str | None = ...,
    expires: int | datetime.timedelta | datetime.datetime | None = ...,
    *,
    queue: str | None = ...,
    **kwargs: Any,
) -> Callable[[Callable[_P, _T]], TaskWrapper[_T, _P]]: ...
def periodic_task(
    validate_datetime,
    retries: int = ...,
    retry_delay: int = ...,
    priority: int | None = ...,
    context: bool = ...,
    name: str | None = ...,
    expires: int | datetime.timedelta | datetime.datetime | None = ...,
    *,
    queue: str | None = ...,
    **kwargs: Any,
) -> Callable[[Callable[_P, _T]], TaskWrapper[_T, _P]]: ...
def lock_task(lock_name: str, *, queue: str | None = ...) -> TaskLock: ...
@overload
def enqueue(task: Task[_T, None]) -> Result[_T, None]: ...
@overload
def enqueue(task: Task[_T, Task]) -> ResultGroup: ...
def restore(task: Task, *, queue: str | None = ...) -> bool: ...
def restore_all(task_class: type[Task], *, queue: str | None = ...) -> bool: ...
def restore_by_id(id: str, *, queue: str | None = ...) -> bool: ...
def revoke(
    task: Task,
    revoke_until: datetime.datetime | None = ...,
    revoke_once: bool = ...,
    *,
    queue: str | None = ...,
) -> None: ...
def revoke_all(
    task_class: type[Task],
    revoke_until: datetime.datetime | None = ...,
    revoke_once: bool = ...,
    *,
    queue: str | None = ...,
) -> None: ...
def revoke_by_id(
    id: str,
    revoke_until: datetime.datetime | None = ...,
    revoke_once: bool = ...,
    *,
    queue: str | None = ...,
) -> None: ...
def is_revoked(
    task: Task | str,
    timestamp: datetime.datetime | None = ...,
    peek: bool = ...,
    *,
    queue: str | None = ...,
) -> bool: ...
def result(
    id: str,
    blocking: bool = ...,
    timeout: int | None = ...,
    backoff: float = ...,
    max_delay: float = ...,
    revoke_on_timeout: bool = ...,
    preserve: bool = ...,
    *,
    queue: str | None = ...,
) -> Any: ...
def scheduled(limit: int | None = ..., *, queue: str | None = ...) -> list[Task]: ...
def on_startup(
    name: str | None = ..., *, queue: str | None = ...
) -> Callable[[_OnStartupHandler], _OnStartupHandler]: ...
def on_shutdown(
    name: str | None = ..., *, queue: str | None = ...
) -> Callable[[_OnShutdownHandler], _OnShutdownHandler]: ...
def pre_execute(
    name: str | None = ..., *, queue: str | None = ...
) -> Callable[[_PreExecuteHandler], _PreExecuteHandler]: ...
def post_execute(
    name: str | None = ..., *, queue: str | None = ...
) -> Callable[[_PostExecuteHandler], _PostExecuteHandler,]: ...

_H = TypeVar("_H", bound=_SignalHandler)

def signal(*signals: _SIGNAL, queue: str | None = ...) -> Callable[[_H], _H]: ...
def disconnect_signal(
    receiver: _SignalHandler, *signals: _SIGNAL, queue: str | None = ...
) -> None: ...
def db_task(
    retries: int = ...,
    retry_delay: int = ...,
    priority: int | None = ...,
    context: bool = ...,
    name: str | None = ...,
    expires: int | datetime.timedelta | datetime.datetime | None = ...,
    *,
    queue: str | None = ...,
    **kwargs: Any,
) -> Callable[[Callable[_P, _T]], TaskWrapper[_T, _P]]: ...
def db_periodic_task(
    validate_datetime,
    retries: int = ...,
    retry_delay: int = ...,
    priority: int | None = ...,
    context: bool = ...,
    name: str | None = ...,
    expires: int | datetime.timedelta | datetime.datetime | None = ...,
    *,
    queue: str | None = ...,
    **kwargs: Any,
) -> Callable[[Callable[_P, _T]], TaskWrapper[_T, _P]]: ...
