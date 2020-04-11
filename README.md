# Grpc server bencmarking


## sync server(originer)
### lib
- [grpcio](https://pypi.org/project/grpcio/) == 1.28.1
- boto3

## async server(originer)
### lib
- grpclib
- aioboto

## performance test tool
- [ghz](https://github.com/bojand/ghz)

## scenario
1. example server 
2. request s3 objects list
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

## results
### hello server
#### sync server - max 10 worker
```bash
./ghz --insecure --proto ./src/hellow_server/helloworld.proto --call helloworld.Greeter.SayHello -d '{"name":"sinsky"}' 0.0.0.0:50051

Summary:
  Count:	200
  Total:	91.11 ms
  Slowest:	28.59 ms
  Fastest:	10.06 ms
  Average:	19.60 ms
  Requests/sec:	2195.03

Response time histogram:
  10.059 [1]	|∎
  11.912 [4]	|∎∎∎
  13.764 [5]	|∎∎∎
  15.617 [15]	|∎∎∎∎∎∎∎∎∎∎
  17.470 [29]	|∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎
  19.322 [32]	|∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎
  21.175 [59]	|∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎
  23.027 [25]	|∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎
  24.880 [14]	|∎∎∎∎∎∎∎∎∎
  26.732 [11]	|∎∎∎∎∎∎∎
  28.585 [5]	|∎∎∎

Latency distribution:
  10 % in 14.83 ms
  25 % in 17.22 ms
  50 % in 19.90 ms
  75 % in 21.47 ms
  90 % in 24.41 ms
  95 % in 25.57 ms
  99 % in 27.98 ms

Status code distribution:
  [OK]   200 responses
```
#### sync server - max 1 worker
```bash

Summary:
  Count:	200
  Total:	110.36 ms
  Slowest:	30.88 ms
  Fastest:	4.59 ms
  Average:	24.34 ms
  Requests/sec:	1812.29

Response time histogram:
  4.592 [1]	|∎
  7.221 [1]	|∎
  9.849 [5]	|∎∎∎
  12.478 [5]	|∎∎∎
  15.106 [6]	|∎∎∎∎
  17.735 [4]	|∎∎
  20.363 [16]	|∎∎∎∎∎∎∎∎∎∎
  22.992 [15]	|∎∎∎∎∎∎∎∎∎
  25.620 [42]	|∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎
  28.249 [67]	|∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎
  30.877 [38]	|∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎

Latency distribution:
  10 % in 16.90 ms
  25 % in 22.57 ms
  50 % in 26.59 ms
  75 % in 27.93 ms
  90 % in 28.81 ms
  95 % in 29.39 ms
  99 % in 30.38 ms

Status code distribution:
  [OK]   200 responses

```
#### async server
```bash
./ghz --insecure --proto ./src/hellow_server/helloworld.proto --call helloworld.Greeter.SayHello -d '{"name":"sinsky"}' 0.0.0.0:50051

Summary:
  Count:	200
  Total:	215.40 ms
  Slowest:	68.36 ms
  Fastest:	16.49 ms
  Average:	48.46 ms
  Requests/sec:	928.52

Response time histogram:
  16.491 [1]	|
  21.679 [7]	|∎∎∎
  26.866 [7]	|∎∎∎
  32.053 [7]	|∎∎∎
  37.240 [6]	|∎∎
  42.428 [9]	|∎∎∎∎
  47.615 [27]	|∎∎∎∎∎∎∎∎∎∎∎
  52.802 [35]	|∎∎∎∎∎∎∎∎∎∎∎∎∎∎
  57.989 [99]	|∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎
  63.177 [0]	|
  68.364 [2]	|∎

Latency distribution:
  10 % in 31.21 ms
  25 % in 46.98 ms
  50 % in 53.15 ms
  75 % in 55.63 ms
  90 % in 56.62 ms
  95 % in 56.84 ms
  99 % in 67.86 ms

Status code distribution:
  [OK]   200 responses
```