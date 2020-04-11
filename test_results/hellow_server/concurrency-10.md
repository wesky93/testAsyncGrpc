# condition
| Config      | Value       |
|-------------|-------------|
| Time Out    | 0(no limit) |
| Concurrency | 10          |
| Total       | 200         |
```bash
./ghz -t 0 -c 10 -n 200 --insecure --proto ./src/hellow_server/helloworld.proto --call helloworld.Greeter.SayHello -d '{"name":"sinsky"}' 0.0.0.0:50051
```

# summary


# raw data

#### sync - grpcio server(max 1 worker)
```bash
./ghz -t 0 -c 10 -n 200 --insecure --proto ./src/hellow_server/helloworld.proto --call helloworld.Greeter.SayHello -d '{"name":"sinsky"}' 0.0.0.0:50051


Summary:
  Count:	200
  Total:	75.77 ms
  Slowest:	5.30 ms
  Fastest:	2.27 ms
  Average:	3.50 ms
  Requests/sec:	2639.73

Response time histogram:
  2.273 [1]	|∎
  2.576 [4]	|∎∎
  2.878 [5]	|∎∎∎
  3.181 [33]	|∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎
  3.484 [69]	|∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎
  3.787 [37]	|∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎
  4.090 [29]	|∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎
  4.393 [15]	|∎∎∎∎∎∎∎∎∎
  4.696 [5]	|∎∎∎
  4.999 [1]	|∎
  5.301 [1]	|∎

Latency distribution:
  10 % in 3.06 ms
  25 % in 3.21 ms
  50 % in 3.42 ms
  75 % in 3.83 ms
  90 % in 4.13 ms
  95 % in 4.33 ms
  99 % in 4.87 ms

Status code distribution:
  [OK]   200 responses
```
#### sync - grpcio server(max 10 worker)
```bash
./ghz -t 0 -c 10 -n 200 --insecure --proto ./src/hellow_server/helloworld.proto --call helloworld.Greeter.SayHello -d '{"name":"sinsky"}' 0.0.0.0:50051


Summary:
  Count:	200
  Total:	94.25 ms
  Slowest:	8.97 ms
  Fastest:	0.97 ms
  Average:	4.49 ms
  Requests/sec:	2122.06

Response time histogram:
  0.973 [1]	|∎
  1.773 [2]	|∎
  2.572 [4]	|∎∎∎
  3.371 [27]	|∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎
  4.171 [55]	|∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎
  4.970 [54]	|∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎
  5.769 [32]	|∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎
  6.569 [12]	|∎∎∎∎∎∎∎∎∎
  7.368 [8]	|∎∎∎∎∎∎
  8.167 [2]	|∎
  8.967 [3]	|∎∎

Latency distribution:
  10 % in 3.16 ms
  25 % in 3.73 ms
  50 % in 4.37 ms
  75 % in 5.13 ms
  90 % in 6.11 ms
  95 % in 6.94 ms
  99 % in 8.86 ms

Status code distribution:
  [OK]   200 responses
```
#### async - grpclib server
```bash
./ghz -t 0 -c 10 -n 200 --insecure --proto ./src/hellow_server/helloworld.proto --call helloworld.Greeter.SayHello -d '{"name":"sinsky"}' 0.0.0.0:50051


Summary:
  Count:	200
  Total:	175.66 ms
  Slowest:	14.21 ms
  Fastest:	6.79 ms
  Average:	8.55 ms
  Requests/sec:	1138.54

Response time histogram:
  6.790 [1]	|∎
  7.533 [52]	|∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎
  8.275 [49]	|∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎
  9.017 [45]	|∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎
  9.759 [18]	|∎∎∎∎∎∎∎∎∎∎∎∎∎∎
  10.502 [13]	|∎∎∎∎∎∎∎∎∎∎
  11.244 [11]	|∎∎∎∎∎∎∎∎
  11.986 [7]	|∎∎∎∎∎
  12.728 [2]	|∎∎
  13.471 [1]	|∎
  14.213 [1]	|∎

Latency distribution:
  10 % in 7.11 ms
  25 % in 7.49 ms
  50 % in 8.24 ms
  75 % in 9.13 ms
  90 % in 10.53 ms
  95 % in 11.30 ms
  99 % in 13.07 ms

Status code distribution:
  [OK]   200 responses
```
#### async - grpclib server with uvloop 
```bash
./ghz -t 0 -c 10 -n 200 --insecure --proto ./src/hellow_server/helloworld.proto --call helloworld.Greeter.SayHello -d '{"name":"sinsky"}' 0.0.0.0:50051


Summary:
  Count:	200
  Total:	160.04 ms
  Slowest:	9.88 ms
  Fastest:	3.80 ms
  Average:	7.79 ms
  Requests/sec:	1249.68

Response time histogram:
  3.801 [1]	|∎
  4.409 [4]	|∎∎∎
  5.017 [0]	|
  5.626 [1]	|∎
  6.234 [10]	|∎∎∎∎∎∎∎∎
  6.843 [19]	|∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎
  7.451 [40]	|∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎
  8.059 [48]	|∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎
  8.668 [31]	|∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎
  9.276 [22]	|∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎
  9.885 [24]	|∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎

Latency distribution:
  10 % in 6.54 ms
  25 % in 7.17 ms
  50 % in 7.84 ms
  75 % in 8.55 ms
  90 % in 9.40 ms
  95 % in 9.68 ms
  99 % in 9.84 ms

Status code distribution:
  [OK]   200 responses
```