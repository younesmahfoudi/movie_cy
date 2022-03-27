from __future__ import annotations
from typing import TypeVar, Generic, Sequence

from fastapi_pagination import Params
from fastapi_pagination.bases import AbstractPage, AbstractParams

T = TypeVar("T")


class Page(AbstractPage[T], Generic[T]):
    results: Sequence[T]

    __params_type__ = Params  # Set params related to Page

    @classmethod
    def create(
            cls,
            items: Sequence[T],
            total: int,
            params: AbstractParams,
    ) -> Page[T]:
        return cls(results=items)