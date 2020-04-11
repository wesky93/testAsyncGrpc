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

## summary
### hello server


### get s3 objects

## raw results
### hello server
#### sync - grpcio server(max 1 worker)
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
#### sync - grpcio server(max 10 worker)
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

#### async - grpclib server
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
#### async - grpclib server with uvloop
```bash
./ghz --insecure --proto ./src/hellow_server/helloworld.proto --call helloworld.Greeter.SayHello -d '{"name":"sinsky"}' 0.0.0.0:50051

Summary:
  Count:	200
  Total:	152.43 ms
  Slowest:	40.99 ms
  Fastest:	8.06 ms
  Average:	34.86 ms
  Requests/sec:	1312.04

Response time histogram:
  8.060 [1]	|
  11.353 [7]	|∎∎
  14.646 [0]	|
  17.938 [0]	|
  21.231 [0]	|
  24.524 [0]	|
  27.816 [0]	|
  31.109 [0]	|
  34.401 [24]	|∎∎∎∎∎∎
  37.694 [150]	|∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎
  40.987 [18]	|∎∎∎∎∎

Latency distribution:
  10 % in 34.14 ms
  25 % in 35.15 ms
  50 % in 36.04 ms
  75 % in 36.50 ms
  90 % in 37.42 ms
  95 % in 38.29 ms
  99 % in 39.51 ms

Status code distribution:
  [OK]   200 responses
```

### aws api server
#### sync - grpcio server(max 1 worker)
```bash
./ghz --insecure --proto ./src/get_s3_objects_server/AwsAPI.proto --call AwsAPI.S3.GetObjects -d '{"bucket":"storybook.spaceone.dev"}' 0.0.0.0:50051

Summary:
  Count:	200
  Total:	80.02 s
  Slowest:	20.00 s
  Fastest:	1.22 s
  Average:	19.16 s
  Requests/sec:	2.50

Response time histogram:
  1220.703 [1]	|∎
  3098.594 [1]	|∎
  4976.484 [2]	|∎∎∎
  6854.374 [1]	|∎
  8732.264 [2]	|∎∎∎
  10610.155 [1]	|∎
  12488.045 [2]	|∎∎∎
  14365.935 [2]	|∎∎∎
  16243.825 [1]	|∎
  18121.716 [1]	|∎
  19999.606 [28]	|∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎

Latency distribution:
  10 % in 6.93 s
  25 % in 14.19 s
  50 % in 19.34 s
  75 % in 19.80 s
  90 % in 19.93 s
  95 % in 19.99 s
  0 % in 0 ns

Status code distribution:
  [OK]                 42 responses
  [DeadlineExceeded]   158 responses

Error distribution:
  [134]   rpc error: code = DeadlineExceeded desc = context deadline exceeded
  [24]    rpc error: code = DeadlineExceeded desc = Deadline Exceeded
```
#### sync - grpcio server(max 10 worker)
```bash
./ghz --insecure --proto ./src/get_s3_objects_server/AwsAPI.proto --call AwsAPI.S3.GetObjects -d '{"bucket":"storybook.spaceone.dev"}' 0.0.0.0:50051

Summary:
  Count:	200
  Total:	60.87 s
  Slowest:	17.62 s
  Fastest:	3.97 s
  Average:	13.74 s
  Requests/sec:	3.29

Response time histogram:
  3972.114 [1]	|
  5336.826 [9]	|∎∎∎∎
  6701.538 [0]	|
  8066.250 [10]	|∎∎∎∎
  9430.962 [0]	|
  10795.674 [10]	|∎∎∎∎
  12160.386 [0]	|
  13525.098 [13]	|∎∎∎∎∎
  14889.810 [95]	|∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎
  16254.522 [24]	|∎∎∎∎∎∎∎∎∎∎
  17619.235 [38]	|∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎

Latency distribution:
  10 % in 10.27 s
  25 % in 13.78 s
  50 % in 14.41 s
  75 % in 16.14 s
  90 % in 16.49 s
  95 % in 16.76 s
  99 % in 17.29 s

Status code distribution:
  [OK]   200 responses
```
#### async - grpclib server
```bash
./ghz --insecure --proto ./src/get_s3_objects_server/AwsAPI.proto --call AwsAPI.S3.GetObjects -d '{"bucket":"storybook.spaceone.dev"}' 0.0.0.0:50051

Summary:
  Count:	200
  Total:	44.50 s
  Slowest:	16.57 s
  Fastest:	1.78 s
  Average:	9.96 s
  Requests/sec:	4.49

Response time histogram:
  1776.485 [1]	|∎
  3255.347 [8]	|∎∎∎∎∎∎∎∎∎
  4734.209 [8]	|∎∎∎∎∎∎∎∎∎
  6213.071 [14]	|∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎
  7691.933 [17]	|∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎
  9170.795 [22]	|∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎
  10649.657 [35]	|∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎
  12128.520 [36]	|∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎
  13607.382 [34]	|∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎
  15086.244 [18]	|∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎
  16565.106 [7]	|∎∎∎∎∎∎∎∎

Latency distribution:
  10 % in 5.14 s
  25 % in 7.82 s
  50 % in 10.45 s
  75 % in 12.38 s
  90 % in 13.96 s
  95 % in 14.59 s
  99 % in 16.52 s

Status code distribution:
  [OK]   200 responses
```
#### async - grpclib server with uvloop 
```bash
./ghz --insecure --proto ./src/get_s3_objects_server/AwsAPI.proto --call AwsAPI.S3.GetObjects -d '{"bucket":"storybook.spaceone.dev"}' 0.0.0.0:50051

Summary:
  Count:	200
  Total:	41.66 s
  Slowest:	19.62 s
  Fastest:	1.32 s
  Average:	10.21 s
  Requests/sec:	4.80

Response time histogram:
  1316.922 [1]	|∎
  3147.381 [11]	|∎∎∎∎∎∎∎
  4977.840 [4]	|∎∎∎
  6808.298 [23]	|∎∎∎∎∎∎∎∎∎∎∎∎∎∎
  8638.757 [5]	|∎∎∎
  10469.216 [58]	|∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎
  12299.675 [64]	|∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎
  14130.133 [0]	|
  15960.592 [18]	|∎∎∎∎∎∎∎∎∎∎∎
  17791.051 [12]	|∎∎∎∎∎∎∎∎
  19621.510 [4]	|∎∎∎

Latency distribution:
  10 % in 6.34 s
  25 % in 10.21 s
  50 % in 10.24 s
  75 % in 10.73 s
  90 % in 14.38 s
  95 % in 16.83 s
  99 % in 19.21 s

Status code distribution:
  [OK]   200 responses
```