# condition
| Config      | Value       |
|-------------|-------------|
| Time Out    | 0(no limit) |
| Concurrency | 25          |
| Total       | 200         |
```bash
./ghz -t 0 -c 25 -n 200 --insecure --proto ./src/hellow_server/helloworld.proto --call helloworld.Greeter.SayHello -d '{"name":"sinsky"}' 0.0.0.0:50051
```

# summary

# raw data

#### sync - grpcio server(max 1 worker)
```bash
./ghz -t 0 -c 25 -n 200 --insecure --proto ./src/hellow_server/helloworld.proto --call helloworld.Greeter.SayHello -d '{"name":"sinsky"}' 0.0.0.0:50051


Summary:
  Count:	200
  Total:	89.54 ms
  Slowest:	16.17 ms
  Fastest:	3.64 ms
  Average:	10.58 ms
  Requests/sec:	2233.59

Response time histogram:
  3.644 [1]	|∎
  4.896 [0]	|
  6.148 [1]	|∎
  7.400 [8]	|∎∎∎∎∎∎
  8.652 [20]	|∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎
  9.904 [51]	|∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎
  11.156 [54]	|∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎
  12.409 [23]	|∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎
  13.661 [28]	|∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎
  14.913 [10]	|∎∎∎∎∎∎∎
  16.165 [4]	|∎∎∎

Latency distribution:
  10 % in 8.53 ms
  25 % in 9.19 ms
  50 % in 10.51 ms
  75 % in 12.16 ms
  90 % in 13.39 ms
  95 % in 14.00 ms
  99 % in 15.89 ms

Status code distribution:
  [OK]   200 responses
```
#### sync - grpcio server(max 10 worker)
```bash
./ghz -t 0 -c 25 -n 200 --insecure --proto ./src/hellow_server/helloworld.proto --call helloworld.Greeter.SayHello -d '{"name":"sinsky"}' 0.0.0.0:50051


Summary:
  Count:	200
  Total:	96.46 ms
  Slowest:	20.22 ms
  Fastest:	2.24 ms
  Average:	10.60 ms
  Requests/sec:	2073.41

Response time histogram:
  2.241 [1]	|∎
  4.040 [3]	|∎∎
  5.838 [2]	|∎
  7.636 [21]	|∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎
  9.434 [43]	|∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎
  11.233 [45]	|∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎
  13.031 [54]	|∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎
  14.829 [15]	|∎∎∎∎∎∎∎∎∎∎∎
  16.627 [12]	|∎∎∎∎∎∎∎∎∎
  18.426 [3]	|∎∎
  20.224 [1]	|∎

Latency distribution:
  10 % in 7.30 ms
  25 % in 8.56 ms
  50 % in 10.72 ms
  75 % in 12.24 ms
  90 % in 14.25 ms
  95 % in 15.90 ms
  99 % in 17.73 ms

Status code distribution:
  [OK]   200 responses
```
#### async - grpclib server
```bash
./ghz -t 0 -c 25 -n 200 --insecure --proto ./src/hellow_server/helloworld.proto --call helloworld.Greeter.SayHello -d '{"name":"sinsky"}' 0.0.0.0:50051


Summary:
  Count:	200
  Total:	162.01 ms
  Slowest:	30.13 ms
  Fastest:	9.69 ms
  Average:	19.24 ms
  Requests/sec:	1234.46

Response time histogram:
  9.692 [1]	|
  11.736 [4]	|∎∎
  13.779 [7]	|∎∎∎
  15.823 [9]	|∎∎∎∎
  17.867 [17]	|∎∎∎∎∎∎∎∎
  19.911 [81]	|∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎
  21.954 [55]	|∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎
  23.998 [20]	|∎∎∎∎∎∎∎∎∎∎
  26.042 [2]	|∎
  28.085 [2]	|∎
  30.129 [2]	|∎

Latency distribution:
  10 % in 15.76 ms
  25 % in 18.10 ms
  50 % in 19.05 ms
  75 % in 21.18 ms
  90 % in 22.21 ms
  95 % in 22.85 ms
  99 % in 28.78 ms

Status code distribution:
  [OK]   200 responses

```
#### async - grpclib server with uvloop 
```bash
./ghz -t 0 -c 25 -n 200 --insecure --proto ./src/hellow_server/helloworld.proto --call helloworld.Greeter.SayHello -d '{"name":"sinsky"}' 0.0.0.0:50051


Summary:
  Count:	200
  Total:	145.08 ms
  Slowest:	23.37 ms
  Fastest:	10.88 ms
  Average:	17.40 ms
  Requests/sec:	1378.53

Response time histogram:
  10.877 [1]	|
  12.126 [16]	|∎∎∎∎∎∎∎
  13.376 [0]	|
  14.625 [0]	|
  15.875 [21]	|∎∎∎∎∎∎∎∎∎
  17.124 [90]	|∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎
  18.374 [14]	|∎∎∎∎∎∎
  19.624 [8]	|∎∎∎∎
  20.873 [28]	|∎∎∎∎∎∎∎∎∎∎∎∎
  22.123 [5]	|∎∎
  23.372 [17]	|∎∎∎∎∎∎∎∎

Latency distribution:
  10 % in 15.66 ms
  25 % in 16.10 ms
  50 % in 16.79 ms
  75 % in 20.17 ms
  90 % in 20.88 ms
  95 % in 23.18 ms
  99 % in 23.37 ms

Status code distribution:
  [OK]   200 responses
```