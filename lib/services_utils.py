import dataclasses
from typing import Any


@dataclasses.dataclass
class Errors:
    errors: dict[str, list[str]] = dataclasses.field(default_factory=dict)

    def add(self, attr: str, message: str):
        if attr not in self.errors:
            self.errors[attr] = []
        self.errors[attr].append(message)

    def get(self, attr):
        return self.errors.get(attr, [])

    def is_any(self) -> bool:
        return len(self.errors) > 0

    def all(self):
        return self.errors

    def __str__(self):
        return "\n".join(
            f"{attr.title()}: {error}"
            for attr, errors in self.errors.items()
            for error in errors
        )


@dataclasses.dataclass
class ServiceResult:
    SUCCESS = 200
    FAIL = 422

    _data: dict[str, Any] = None
    errors: Errors = dataclasses.field(default_factory=Errors)

    @property
    def response(self):
        if self.is_success():
            return self._data
        return self.errors.all()

    def set_data(self, data: dict[str, Any]):
        self._data = data

    @property
    def status(self):
        return self.SUCCESS if self.is_success() else self.FAIL

    def is_success(self) -> bool:
        return not self.is_fail()

    def is_fail(self) -> bool:
        return self.errors.is_any()


class BaseService:
    result: ServiceResult

    def call(self) -> ServiceResult:
        self.result = ServiceResult()
        self._execute()
        return self.result

    def _execute(self):
        raise NotImplementedError("must be redefined in subclass")

    def _add_error(self, attr: str, message: str):
        self.result.errors.add(attr, message)

    def _build_result(self, **data):
        self.result.set_data(data)
