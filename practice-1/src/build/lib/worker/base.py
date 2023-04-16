from abc import ABC, abstractmethod
from typing import Any, Union


class WorkerBase(ABC):

    @abstractmethod
    def serialize(self, data: Any) -> Union[str, bytes]:
        pass

    @abstractmethod
    def deserialize(self, data: Union[str, bytes]) -> Any:
        pass

    @staticmethod
    @abstractmethod
    def MODE():
        pass

    def calc_perf_info(self):
        ...

    @property
    def perf_test_case(self) -> Any:
        return {
            'str_key': 'str_value',
            'int_key': 42,
            'float_key': 13.37,
            'array_key': ['val1', 'val2', 'val3'],
            'map_key': {
                'k': 'v',
                'hello': 'world',
            },
        }
