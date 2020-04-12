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

#### concurrency - 10 [raw data](/test_results/hellow_server/concurrency-10.md)
|                  | sync grpcio server(max 1 worker) | sync grpcio server(max 10 worker) | async grpclib server | async grpclib server(with uvloop) |
|------------------|----------------------------------|-----------------------------------|----------------------|-----------------------------------|
| Count            | 200                              | 200                               | 200                  | 200                               |
| OK               | 200                              | 200                               | 200                  | 200                               |
| DeadlineExceeded | 0                                | 0                                 | 0                    | 0                                 |
| Total            | 75.77 ms                         | 94.25 ms                          | 175.66 ms            | 160.04 ms                         |
| Slowest          | 5.30 ms                          | 8.97 ms                           | 14.21 ms             | 9.88 ms                           |
| Fastest          | 2.27 ms                          | 0.97 ms                           | 6.79 ms              | 3.80 ms                           |
| Average          | 3.50 ms                          | 4.49 ms                           | 8.55 ms              | 7.79 ms                           |
| Requests/sec     | 2639.73                          | 2122.06                           | 1138.54              | 1249.68                           |

#### concurrency - 25 [raw data](/test_results/hellow_server/concurrency-25.md)
|                  | sync grpcio server(max 1 worker) | sync grpcio server(max 10 worker) | async grpclib server | async grpclib server(with uvloop) |
|------------------|----------------------------------|-----------------------------------|----------------------|-----------------------------------|
| Count            | 200                              | 200                               | 200                  | 200                               |
| OK               | 200                              | 200                               | 200                  | 200                               |
| DeadlineExceeded | 0                                | 0                                 | 0                    | 0                                 |
| Total            | 89.54 ms                         | 96.46 ms                          | 162.01 ms            | 145.08 ms                         |
| Slowest          | 16.17 ms                         | 20.22 ms                          | 30.13 ms             | 23.37 ms                          |
| Fastest          | 3.64 ms                          | 2.24 ms                           | 9.69 ms              | 10.88 ms                          |
| Average          | 10.58 ms                         | 10.60 ms                          | 19.24 ms             | 17.40 ms                          |
| Requests/sec     | 2233.59                          | 2073.41                           | 1234.46              | 1378.53                           |

#### concurrency - 50 [raw data](/test_results/hellow_server/concurrency-50.md)
|                  | sync grpcio server(max 1 worker) | sync grpcio server(max 10 worker) | async grpclib server | async grpclib server(with uvloop) |
|------------------|----------------------------------|-----------------------------------|----------------------|-----------------------------------|
| Count            | 200                              | 200                               | 200                  | 200                               |
| OK               | 200                              | 200                               | 200                  | 200                               |
| DeadlineExceeded | 0                                | 0                                 | 0                    | 0                                 |
| Total            | 91.47 ms                         | 82.80 ms                          | 178.29 ms            | 140.22 ms                         |
| Slowest          | 29.61 ms                         | 32.31 ms                          | 53.31 ms             | 37.37 ms                          |
| Fastest          | 2.75 ms                          | 1.61 ms                           | 16.19 ms             | 11.96 ms                          |
| Average          | 20.92 ms                         | 18.94 ms                          | 38.58 ms             | 32.78 ms                          |
| Requests/sec     | 2186.54                          | 2415.41                           | 1121.76              | 1426.31                           |


### aws api unary
#### concurrency - 2 [raw data](/test_results/aws_api_unary/concurrency-2.md)
|                  | sync grpcio server(max 1 worker) | sync grpcio server(max 10 worker) | async grpclib server | async grpclib server(with uvloop) |
|------------------|----------------------------------|-----------------------------------|----------------------|-----------------------------------|
| Count            | 200                              | 200                               | 200                  | 200                               |
| OK               | 200                              | 200                               | 200                  | 200                               |
| DeadlineExceeded | 0                                | 0                                 | 0                    | 0                                 |
| Total            | 117.34 s                         | 82.58 s                           | 84.09 s              | 84.39 s                           |
| Slowest          | 2.76 s                           | 1.75 s                            | 2.77 s               | 1.92 s                            |
| Fastest          | 687.63 ms                        | 505.74 ms                         | 518.04 ms            | 495.28 ms                         |
| Average          | 1.17 s                           | 824.79 ms                         | 839.97 ms            | 836.05 ms                         |
| Requests/sec     | 1.70                             | 2.42                              | 2.38                 | 2.37                              |

#### concurrency - 10 [raw data](/test_results/aws_api_unary/concurrency-10.md)
|                  | sync grpcio server(max 1 worker) | sync grpcio server(max 10 worker) | async grpclib server | async grpclib server(with uvloop) |
|------------------|----------------------------------|-----------------------------------|----------------------|-----------------------------------|
| Count            | 200                              | 200                               | 200                  | 200                               |
| OK               | 200                              | 200                               | 200                  | 200                               |
| DeadlineExceeded | 0                                | 0                                 | 0                    | 0                                 |
| Total            | 116.32 s                         | 65.58 s                           | 62.34 s              | 60.03 s                           |
| Slowest          | 7.27 s                           | 4.89 s                            | 5.04 s               | 5.12 s                            |
| Fastest          | 644.39 ms                        | 886.42 ms                         | 1.28 s               | 1.30 s                            |
| Average          | 5.69 s                           | 3.22 s                            | 3.08 s               | 2.99 s                            |
| Requests/sec     | 1.72                             | 3.05                              | 3.21                 | 3.33                              |

#### concurrency - 25 [raw data](/test_results/aws_api_unary/concurrency-25.md)
|                  | sync grpcio server(max 1 worker) | sync grpcio server(max 10 worker) | async grpclib server | async grpclib server(with uvloop) |
|------------------|----------------------------------|-----------------------------------|----------------------|-----------------------------------|
| Count            | 200                              | 200                               | 200                  | 200                               |
| OK               | 200                              | 200                               | 200                  | 200                               |
| DeadlineExceeded | 0                                | 0                                 | 0                    | 0                                 |
| Total            | 109.31 s                         | 68.52 s                           | 57.39 s              | 56.57 s                           |
| Slowest          | 15.41 s                          | 12.40 s                           | 12.30 s              | 13.05 s                           |
| Fastest          | 1.13 s                           | 3.78 s                            | 1.55 s               | 1.89 s                            |
| Average          | 12.88 s                          | 8.20 s                            | 6.91 s               | 6.96 s                            |
| Requests/sec     | 1.83                             | 2.92                              | 3.49                 | 3.54                              |

#### concurrency - 50 [raw data](/test_results/aws_api_unary/concurrency-50.md)
|                  | sync grpcio server(max 1 worker) | sync grpcio server(max 10 worker) | async grpclib server | async grpclib server(with uvloop) |
|------------------|----------------------------------|-----------------------------------|----------------------|-----------------------------------|
| Count            | 200                              | 200                               | 200                  | 200                               |
| OK               | 200                              | 200                               | 200                  | 200                               |
| DeadlineExceeded | 0                                | 0                                 | 0                    | 0                                 |
| Total            | 109.84 s                         | 66.75 s                           | 59.68 s              | 58.43 s                           |
| Slowest          | 29.53 s                          | 19.92 s                           | 27.24 s              | 24.32 s                           |
| Fastest          | 513.20 ms                        | 3.35 s                            | 3.87 s               | 5.14 s                            |
| Average          | 23.92 s                          | 15.02 s                           | 13.84 s              | 14.24 s                           |
| Requests/sec     | 1.82                             | 3.00                              | 3.35                 | 3.543.42                          |

### aws api stream
#### concurrency - 2 [raw data](/test_results/aws_api_stream/concurrency-2.md)
|              | sync grpcio server(max 1 worker) | sync grpcio server(max 10 worker) | async grpclib server | async grpclib server(with uvloop) |
|--------------|----------------------------------|-----------------------------------|----------------------|-----------------------------------|
| Count        | 200                              | 200                               | 200                  | 200                               |
| OK           | 200                              | 200                               | 200                  | 109                               |
| Unavailable  | 0                                | 0                                 | 0                    | 91                                |
| Total        | 121.00 s                         | 90.31 s                           | 85.28 s              | 48.39 s                           |
| Slowest      | 2.40 s                           | 2.18 s                            | 2.08 s               | 1.72 s                            |
| Fastest      | 654.55 ms                        | 552.69 ms                         | 500.94 ms            | 451.07 ms                         |
| Average      | 1.21 s                           | 900.35 ms                         | 851.79 ms            | 483.83 ms                         |
| Requests/sec | 1.65                             | 2.21                              | 2.35                 | 4.13                              |

#### concurrency - 10 [raw data](/test_results/aws_api_stream/concurrency-10.md)
|              | sync grpcio server(max 1 worker) | sync grpcio server(max 10 worker) | async grpclib server | async grpclib server(with uvloop) |
|--------------|----------------------------------|-----------------------------------|----------------------|-----------------------------------|
| Count        | 200                              | 200                               | 200                  | 200                               |
| OK           | 200                              | 200                               | 55                   | 57                                |
| Unavailable  | 0                                | 0                                 | 145                  | 143                               |
| Total        | 122.18 s                         | 72.01 s                           | 52.96 s              | 51.04 s                           |
| Slowest      | 8.62 s                           | 5.03 s                            | 4.06 s               | 3.57 s                            |
| Fastest      | 659.90 ms                        | 1.59 s                            | 574.99 ms            | 1.52 s                            |
| Average      | 5.98 s                           | 3.54 s                            | 2.49 s               | 2.41 s                            |
| Requests/sec | 1.64                             | 2.78                              | 3.78                 | 3.92                              |

#### concurrency - 25 [raw data](/test_results/aws_api_stream/concurrency-25.md)
|              | sync grpcio server(max 1 worker) | sync grpcio server(max 10 worker) | async grpclib server | async grpclib server(with uvloop) |
|--------------|----------------------------------|-----------------------------------|----------------------|-----------------------------------|
| Count        | 200                              | 200                               | 200                  | 200                               |
| OK           | 200                              | 200                               | 34                   | 39                                |
| Unavailable  | 0                                | 0                                 | 166                  | 161                               |
| Total        | 116.13 s                         | 74.96 s                           | 56.88 s              | 57.44 s                           |
| Slowest      | 16.84 s                          | 14.34 s                           | 9.16 s               | 9.61 s                            |
| Fastest      | 1.08 s                           | 2.48 s                            | 2.60 s               | 2.05 s                            |
| Average      | 13.69 s                          | 8.90 s                            | 6.63 s               | 6.79 s                            |
| Requests/sec | 1.72                             | 2.67                              | 3.52                 | 3.48                              |

#### concurrency - 50 [raw data](/test_results/aws_api_stream/concurrency-50.md)
|              | sync grpcio server(max 1 worker) | sync grpcio server(max 10 worker) | async grpclib server | async grpclib server(with uvloop) |
|--------------|----------------------------------|-----------------------------------|----------------------|-----------------------------------|
| Count        | 200                              | 200                               | 200                  | 200                               |
| OK           | 200                              | 200                               | 50                   | 51                                |
| Unavailable  | 0                                | 0                                 | 150                  | 149                               |
| Total        | 116.42 s                         | 72.87 s                           | 51.91 s              | 48.47 s                           |
| Slowest      | 30.51 s                          | 19.55 s                           | 15.30 s              | 14.42 s                           |
| Fastest      | 566.16 ms                        | 3.51 s                            | 4.71 s               | 5.03 s                            |
| Average      | 25.48 s                          | 16.44 s                           | 11.94 s              | 11.31 s                           |
| Requests/sec | 1.72                             | 2.74                              | 3.85                 | 4.13                              |