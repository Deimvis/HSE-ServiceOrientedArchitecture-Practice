import avro.schema

from serialization.worker.modes import (
    AvroWorker,
    JsonWorker,
    MsgpackWorker,
    ProtobufWorker,
    PythonNativeWorker,
    XMLWorker,
)


class WorkersManager:
    def __init__(self):
        self.workers = [
            self.init_AvroWorker(),
            JsonWorker(),
            MsgpackWorker(),
            ProtobufWorker(),
            PythonNativeWorker(),
            XMLWorker(),
        ]
        self._mode2worker = {
            worker.MODE: worker for worker in self.workers
        }

    def init_AvroWorker(self):
        with open('schemas/perf_test_case.avsc', 'rb') as f:
            return AvroWorker(avro.schema.parse(f.read()))

    @property
    def mode2worker(self):
        return self._mode2worker
 