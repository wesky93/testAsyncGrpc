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
3. request s3 objects & save monogoDB

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
3. run ghz

## summary
### hello server
|                  | sync<br>grpcio server(max 1 worker) | sync<br>grpcio server(max 10 worker) | async<br>grpclib server | async<br>grpclib server(with uvloop) |
|------------------|-------------------------------------|--------------------------------------|-------------------------|--------------------------------------|
| Count            | 200                                 | 200                                  | 200                     | 200                                  |
| OK               | 200                                 | 200                                  | 200                     | 200                                  |
| DeadlineExceeded | 0                                   | 0                                    | 0                       | 0                                    |
| Total            | 110.36 ms                           | 91.11 ms                             | 215.40 ms               | 152.43 ms                            |
| Slowest          | 30.88 ms                            | 28.59 ms                             | 68.36 ms                | 40.99 ms                             |
| Fastest          | 4.59 ms                             | 10.06 ms                             | 16.49 ms                | 8.06 ms                              |
| Average          | 24.34 ms                            | 19.60 ms                             | 48.46 ms                | 34.86 ms                             |
| Requests/sec     | 1812.29                             | 2195.03                              | 928.52                  | 1312.04                              |


### get s3 objects
|                  | sync<br>grpcio server(max 1 worker) | sync<br>grpcio server(max 10 worker) | async<br>grpclib server | async<br>grpclib server(with uvloop) |
|------------------|-------------------------------------|--------------------------------------|-------------------------|--------------------------------------|
| Count            | 200                                 | 200                                  | 200                     | 200                                  |
| OK               | 42                                  | 200                                  | 200                     | 200                                  |
| DeadlineExceeded | 158                                 | 0                                    | 0                       | 0                                    |
| Total            | 80.02 s                             | 60.87 s                              | 44.50 s                 | 41.66 s                              |
| Slowest          | 20.00 s                             | 17.62 s                              | 16.57 s                 | 19.62 s                              |
| Fastest          | 1.22 s                              | 3.97 s                               | 1.78 s                  | 1.32 s                               |
| Average          | 19.16 s                             | 13.74 s                              | 9.96 s                  | 10.21 s                              |
| Requests/sec     | 2.50                                | 3.29                                 | 4.49                    | 4.80                                 |

# raw result
