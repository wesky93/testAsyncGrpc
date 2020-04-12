# condition
| Config      | Value       |
|-------------|-------------|
| Time Out    | 0(no limit) |
| Concurrency | 50          |
| Total       | 200         |
```bash
./ghz -t 0 -c 50 -n 200 --insecure --proto ./src/hellow_server/helloworld.proto --call helloworld.Greeter.SayHello -d '{"name":"sinsky"}' 0.0.0.0:50051
```

# summary
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


# raw data

#### sync - grpcio server(max 1 worker)
```bash
./ghz -t 0 -c 50 -n 200 --insecure --proto ./src/hellow_server/helloworld.proto --call helloworld.Greeter.SayHello -d '{"name":"sinsky"}' 0.0.0.0:50051


Summary:
  Count:	200
  Total:	91.47 ms
  Slowest:	29.61 ms
  Fastest:	2.75 ms
  Average:	20.92 ms
  Requests/sec:	2186.54

Response time histogram:
  2.752 [1]	|∎
  5.438 [2]	|∎∎
  8.124 [2]	|∎∎
  10.810 [6]	|∎∎∎∎∎∎
  13.496 [11]	|∎∎∎∎∎∎∎∎∎∎
  16.182 [27]	|∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎
  18.868 [23]	|∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎
  21.554 [30]	|∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎
  24.241 [26]	|∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎
  26.927 [29]	|∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎
  29.613 [43]	|∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎

Latency distribution:
  10 % in 13.42 ms
  25 % in 16.40 ms
  50 % in 21.45 ms
  75 % in 26.21 ms
  90 % in 28.32 ms
  95 % in 28.92 ms
  99 % in 29.55 ms

Status code distribution:
  [OK]   200 responses
```
#### sync - grpcio server(max 10 worker)
```bash
./ghz -t 0 -c 50 -n 200 --insecure --proto ./src/hellow_server/helloworld.proto --call helloworld.Greeter.SayHello -d '{"name":"sinsky"}' 0.0.0.0:50051


Summary:
  Count:	200
  Total:	82.80 ms
  Slowest:	32.31 ms
  Fastest:	1.61 ms
  Average:	18.94 ms
  Requests/sec:	2415.41

Response time histogram:
  1.608 [1]	|∎
  4.678 [7]	|∎∎∎∎
  7.747 [3]	|∎∎
  10.817 [10]	|∎∎∎∎∎∎
  13.887 [10]	|∎∎∎∎∎∎
  16.957 [27]	|∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎
  20.027 [64]	|∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎
  23.097 [32]	|∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎
  26.166 [22]	|∎∎∎∎∎∎∎∎∎∎∎∎∎∎
  29.236 [13]	|∎∎∎∎∎∎∎∎
  32.306 [11]	|∎∎∎∎∎∎∎

Latency distribution:
  10 % in 10.68 ms
  25 % in 16.59 ms
  50 % in 18.70 ms
  75 % in 22.43 ms
  90 % in 26.53 ms
  95 % in 29.49 ms
  99 % in 32.13 ms

Status code distribution:
  [OK]   200 responses
```
#### async - grpclib server
```bash
./ghz -t 0 -c 50 -n 200 --insecure --proto ./src/hellow_server/helloworld.proto --call helloworld.Greeter.SayHello -d '{"name":"sinsky"}' 0.0.0.0:50051


Summary:
  Count:	200
  Total:	178.29 ms
  Slowest:	53.31 ms
  Fastest:	16.19 ms
  Average:	38.58 ms
  Requests/sec:	1121.76

Response time histogram:
  16.186 [1]	|
  19.899 [8]	|∎∎∎
  23.612 [6]	|∎∎
  27.325 [6]	|∎∎
  31.037 [5]	|∎∎
  34.750 [5]	|∎∎
  38.463 [21]	|∎∎∎∎∎∎∎
  42.176 [113]	|∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎
  45.888 [21]	|∎∎∎∎∎∎∎
  49.601 [11]	|∎∎∎∎
  53.314 [3]	|∎

Latency distribution:
  10 % in 26.63 ms
  25 % in 38.37 ms
  50 % in 40.34 ms
  75 % in 41.58 ms
  90 % in 44.32 ms
  95 % in 47.71 ms
  99 % in 53.04 ms

Status code distribution:
  [OK]   200 responses

```
#### async - grpclib server with uvloop 
```bash
./ghz -t 0 -c 50 -n 200 --insecure --proto ./src/hellow_server/helloworld.proto --call helloworld.Greeter.SayHello -d '{"name":"sinsky"}' 0.0.0.0:50051


Summary:
  Count:	200
  Total:	140.22 ms
  Slowest:	37.37 ms
  Fastest:	11.96 ms
  Average:	32.78 ms
  Requests/sec:	1426.31

Response time histogram:
  11.958 [1]	|
  14.500 [14]	|∎∎∎∎∎∎
  17.041 [0]	|
  19.583 [0]	|
  22.124 [0]	|
  24.666 [0]	|
  27.208 [0]	|
  29.749 [0]	|
  32.291 [34]	|∎∎∎∎∎∎∎∎∎∎∎∎∎∎
  34.832 [52]	|∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎
  37.374 [99]	|∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎

Latency distribution:
  10 % in 31.32 ms
  25 % in 32.34 ms
  50 % in 34.83 ms
  75 % in 35.50 ms
  90 % in 36.76 ms
  95 % in 37.15 ms
  99 % in 37.36 ms

Status code distribution:
  [OK]   200 responses
```