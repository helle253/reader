
from io import TextIOWrapper
import os
from multiprocessing import Process, Queue, Value
from ctypes import c_bool
import smart_open


class S3UploadProcess:
  data_incoming: Value
  fd: TextIOWrapper
  queue: Queue
  uri: str

  def __init__(self, key):
    self.queue = Queue()
    self.uri = f's3://{os.getenv("S3_BUCKLET")}/{key}'
    self.fd = smart_open.smart_open(self.uri, 'wb')
    self.data_incoming = Value(c_bool, False)

  def no_more_incoming_data(self):
    self.data_incoming.value = False

  def spawn_worker(self):
    Process(target=self.worker, args=(self.queue, self.fd), daemon=True).start()

  def worker(self, queue, fd):
    while self.data_incoming or not queue.empty():
      chunk = queue.get()
      fd.write(chunk)
    fd.close()
