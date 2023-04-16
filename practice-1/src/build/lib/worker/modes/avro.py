import avro.schema
from avro.io import DatumReader, DatumWriter
from io import StringIO

from typing import Any, Union

from serialization.worker.base import WorkerBase


class AvroWorker(WorkerBase):
    MODE = 'avro'

    def __init__(self, schema=None):
        self.schema = None
        self.writer = None
        self.reader = None
        self.reset(schema)

    def serialize(self, data: Any) -> Union[str, bytes]:
        bytes_io = StringIO()
        self.writer.write(data, avro.io.BinaryEncoder(bytes_io))
        return bytes_io.getvalue()

    def deserialize(self, data: Union[str, bytes]) -> Any:
        bytes_io = StringIO(data)
        return self.reader.read(avro.io.BinaryDecoder(bytes_io))

    @property
    def perf_test_case(self) -> Any:
        with open('schemas/perf_test_case.avsc', 'rb') as f:
            self.reset(avro.schema.parse(f.read()))
        return super().perf_test_case

    def reset(self, schema):
        self.schema = schema
        self.writer = DatumWriter(self.schema)
        self.reader = DatumReader(schema)
