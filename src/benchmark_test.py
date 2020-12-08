import unittest
from functools import partial
from multiprocessing import Process
from hellow_server.sync_server import serve as sync_server

def fun(name):
    print(f'hello {name}')

def main():

    p = Process(target=fun, args=('Peter',))
    p.start()

class Benchmark(unittest.TestCase):

    def run_grpc_server(self,server):
        p = Process(target=server)
        p.start()
        return p

    def test_sync_server_1_worker(self):
        server_process = self.run_grpc_server(partial(sync_server,1))
        print(server_process)

        return
