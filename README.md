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


## How to test?
1. [download ghz](https://github.com/bojand/ghz/releases) 
2. start server
3. start ghz

## results
### hellow server
#### sync server
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

#### async server