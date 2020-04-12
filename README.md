# Grpc server bencmarking


## sync server(originer)
### lib
- [grpcio](https://pypi.org/project/grpcio/) == 1.28.1
- boto3

## async server(originer)
### lib
- grpclib
- aioboto
- uvloop

## performance test tool
- [ghz](https://github.com/bojand/ghz)

## scenario
1. example server - no i/o only computing logic
2. request s3 objects list - network i/o
    - bucket have 893 objects
3. request s3 objects & save monogoDB
    - bucket have 893 objects


## generate proto file
you must add two option
- `grpc_python_out=.` - grpcio sync stubs
- `python_grpc_out=.` - grpclib async stubs

```bash
python -m grpc_tools.protoc -I. --python_out=. --python_grpc_out=. --grpc_python_out=. helloworld.proto
```

## How to test?
1. [download ghz](https://github.com/bojand/ghz/releases) 
2. start server
    - python sync_server.py -w 1 
    - python sync_server.py -w 10 
    - python async_server.py
    - python async_server.py -l uvloop
3. run ghz

## summary
### hello server
#### concurrency - 2 [raw data](/test_results/hellow_server/concurrency-2.md)
|                  | sync grpcio server(max 1 worker) | sync grpcio server(max 10 worker) | async grpclib server | async grpclib server(with uvloop) |
|------------------|----------------------------------|-----------------------------------|----------------------|-----------------------------------|
| Count            | 200                              | 200                               | 200                  | 200                               |
| OK               | 200                              | 200                               | 200                  | 200                               |
| DeadlineExceeded | 0                                | 0                                 | 0                    | 0                                 |
| Total            | 71.90 ms                         | 118.74 ms                         | 182.37 ms            | 178.11 ms                         |
| Slowest          | 7.51 ms                          | 7.97 ms                           | 4.61 ms              | 4.55 ms                           |
| Fastest          | 0.41 ms                          | 0.55 ms                           | 1.13 ms              | 0.88 ms                           |
| Average          | 0.62 ms                          | 1.09 ms                           | 1.73 ms              | 1.69 ms                           |
| Requests/sec     | 2781.69                          | 1684.29                           | 1096.66              | 1122.91                           |

#### concurrency - 10


#### concurrency - 25


#### concurrency - 50

### aws api unary
#### concurrency - 2
|
#### concurrency - 10


#### concurrency - 25


#### concurrency - 50


### aws api stream
#### concurrency - 2


#### concurrency - 10


#### concurrency - 25


#### concurrency - 50