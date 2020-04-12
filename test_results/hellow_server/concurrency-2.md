# condition
| Config      | Value       |
|-------------|-------------|
| Time Out    | 0(no limit) |
| Concurrency | 2           |
| Total       | 200         |
```bash
./ghz -t 0 -c 2 -n 200 --insecure --proto ./src/hellow_server/helloworld.proto --call helloworld.Greeter.SayHello -d '{"name":"sinsky"}' 0.0.0.0:50051
```

# summary
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

# raw data

#### sync - grpcio server(max 1 worker)
```bash
./ghz -t 0 -c 2 -n 200 --insecure --proto ./src/hellow_server/helloworld.proto --call helloworld.Greeter.SayHello -d '{"name":"sinsky"}' 0.0.0.0:50051


Summary:
  Count:	200
  Total:	71.90 ms
  Slowest:	7.51 ms
  Fastest:	0.41 ms
  Average:	0.62 ms
  Requests/sec:	2781.69

Response time histogram:
  0.405 [1]	|
  1.116 [196]	|∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎
  1.826 [1]	|
  2.536 [0]	|
  3.247 [0]	|
  3.957 [0]	|
  4.667 [0]	|
  5.378 [0]	|
  6.088 [0]	|
  6.798 [0]	|
  7.509 [2]	|

Latency distribution:
  10 % in 0.47 ms
  25 % in 0.50 ms
  50 % in 0.54 ms
  75 % in 0.60 ms
  90 % in 0.67 ms
  95 % in 0.76 ms
  99 % in 7.24 ms

Status code distribution:
  [OK]   200 responses


```
#### sync - grpcio server(max 10 worker)
```bash
Summary:
  Count:	200
  Total:	118.74 ms
  Slowest:	7.97 ms
  Fastest:	0.55 ms
  Average:	1.09 ms
  Requests/sec:	1684.29

Response time histogram:
  0.553 [1]	|
  1.294 [167]	|∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎
  2.036 [21]	|∎∎∎∎∎
  2.777 [8]	|∎∎
  3.519 [1]	|
  4.261 [0]	|
  5.002 [0]	|
  5.744 [0]	|
  6.485 [0]	|
  7.227 [0]	|
  7.968 [2]	|

Latency distribution:
  10 % in 0.67 ms
  25 % in 0.78 ms
  50 % in 0.91 ms
  75 % in 1.12 ms
  90 % in 1.48 ms
  95 % in 2.31 ms
  99 % in 7.86 ms

Status code distribution:
  [OK]   200 responses
```
#### async - grpclib server
```bash
./ghz -t 0 -c 2 -n 200 --insecure --proto ./src/hellow_server/helloworld.proto --call helloworld.Greeter.SayHello -d '{"name":"sinsky"}' 0.0.0.0:50051


Summary:
  Count:	200
  Total:	182.37 ms
  Slowest:	4.61 ms
  Fastest:	1.13 ms
  Average:	1.73 ms
  Requests/sec:	1096.66

Response time histogram:
  1.129 [1]	|
  1.477 [83]	|∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎
  1.826 [44]	|∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎
  2.174 [39]	|∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎
  2.523 [23]	|∎∎∎∎∎∎∎∎∎∎∎
  2.872 [5]	|∎∎
  3.220 [3]	|∎
  3.569 [0]	|
  3.917 [0]	|
  4.266 [0]	|
  4.614 [2]	|∎

Latency distribution:
  10 % in 1.31 ms
  25 % in 1.36 ms
  50 % in 1.58 ms
  75 % in 1.98 ms
  90 % in 2.39 ms
  95 % in 2.52 ms
  99 % in 4.54 ms

Status code distribution:
  [OK]   200 responses


```
#### async - grpclib server with uvloop 
```bash
./ghz -t 0 -c 2 -n 200 --insecure --proto ./src/hellow_server/helloworld.proto --call helloworld.Greeter.SayHello -d '{"name":"sinsky"}' 0.0.0.0:50051


Summary:
  Count:	200
  Total:	178.11 ms
  Slowest:	4.55 ms
  Fastest:	0.88 ms
  Average:	1.69 ms
  Requests/sec:	1122.91

Response time histogram:
  0.880 [1]	|∎
  1.247 [34]	|∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎
  1.614 [74]	|∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎
  1.981 [43]	|∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎
  2.348 [29]	|∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎
  2.715 [10]	|∎∎∎∎∎
  3.082 [1]	|∎
  3.449 [5]	|∎∎∎
  3.816 [1]	|∎
  4.183 [0]	|
  4.550 [2]	|∎

Latency distribution:
  10 % in 1.19 ms
  25 % in 1.32 ms
  50 % in 1.54 ms
  75 % in 1.97 ms
  90 % in 2.23 ms
  95 % in 2.67 ms
  99 % in 4.52 ms

Status code distribution:
  [OK]   200 responses
```