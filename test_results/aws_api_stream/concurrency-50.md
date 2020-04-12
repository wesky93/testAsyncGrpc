# condition
| Config      | Value       |
|-------------|-------------|
| Time Out    | 0(no limit) |
| Concurrency | 50          |
| Total       | 200         |
```bash
./ghz -t 0 -c 50 -n 200 --insecure --proto ./src/aws_api_stream/AwsAPI.proto --call AwsAPI.S3.GetObjects -d '{"bucket":"storybook.spaceone.dev"}' 0.0.0.0:50051
```

# summary
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

# raw data

#### sync - grpcio server(max 1 worker)
```bash
./ghz -t 0 -c 50 -n 200 --insecure --proto ./src/aws_api_stream/AwsAPI.proto --call AwsAPI.S3.GetObjects -d '{"bucket":"storybook.spaceone.dev"}' 0.0.0.0:50051


Summary:
  Count:	200
  Total:	116.42 s
  Slowest:	30.51 s
  Fastest:	566.16 ms
  Average:	25.48 s
  Requests/sec:	1.72

Response time histogram:
  566.161 [1]	|
  3560.148 [5]	|∎∎
  6554.134 [5]	|∎∎
  9548.121 [5]	|∎∎
  12542.108 [4]	|∎
  15536.094 [2]	|∎
  18530.081 [6]	|∎∎
  21524.067 [5]	|∎∎
  24518.054 [6]	|∎∎
  27512.041 [30]	|∎∎∎∎∎∎∎∎∎
  30506.027 [131]	|∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎

Latency distribution:
  10 % in 13.15 s
  25 % in 27.35 s
  50 % in 27.65 s
  75 % in 29.60 s
  90 % in 29.87 s
  95 % in 30.38 s
  99 % in 30.49 s

Status code distribution:
  [OK]   200 responses
```
#### sync - grpcio server(max 10 worker)
```bash
./ghz -t 0 -c 50 -n 200 --insecure --proto ./src/aws_api_stream/AwsAPI.proto --call AwsAPI.S3.GetObjects -d '{"bucket":"storybook.spaceone.dev"}' 0.0.0.0:50051


Summary:
  Count:	200
  Total:	72.87 s
  Slowest:	19.55 s
  Fastest:	3.51 s
  Average:	16.44 s
  Requests/sec:	2.74

Response time histogram:
  3513.441 [1]	|
  5116.999 [9]	|∎∎∎
  6720.556 [0]	|
  8324.113 [10]	|∎∎∎∎
  9927.670 [0]	|
  11531.228 [10]	|∎∎∎∎
  13134.785 [0]	|
  14738.342 [11]	|∎∎∎∎
  16341.899 [8]	|∎∎∎
  17945.456 [40]	|∎∎∎∎∎∎∎∎∎∎∎∎∎∎
  19549.014 [111]	|∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎

Latency distribution:
  10 % in 10.55 s
  25 % in 16.94 s
  50 % in 18.02 s
  75 % in 18.89 s
  90 % in 19.39 s
  95 % in 19.46 s
  99 % in 19.55 s

Status code distribution:
  [OK]   200 responses
```
#### async - grpclib server
```bash
./ghz -t 0 -c 50 -n 200 --insecure --proto ./src/aws_api_stream/AwsAPI.proto --call AwsAPI.S3.GetObjects -d '{"bucket":"storybook.spaceone.dev"}' 0.0.0.0:50051


Summary:
  Count:	200
  Total:	51.91 s
  Slowest:	15.30 s
  Fastest:	4.71 s
  Average:	11.94 s
  Requests/sec:	3.85

Response time histogram:
  4707.853 [1]	|∎∎
  5766.897 [2]	|∎∎∎∎
  6825.942 [2]	|∎∎∎∎
  7884.986 [1]	|∎∎
  8944.030 [1]	|∎∎
  10003.075 [0]	|
  11062.119 [0]	|
  12121.163 [0]	|
  13180.208 [1]	|∎∎
  14239.252 [22]	|∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎
  15298.296 [20]	|∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎

Latency distribution:
  10 % in 7.29 s
  25 % in 13.54 s
  50 % in 14.05 s
  75 % in 14.60 s
  90 % in 15.05 s
  95 % in 15.26 s
  0 % in 0 ns

Status code distribution:
  [OK]            50 responses
  [Unavailable]   150 responses

Error distribution:
  [150]   rpc error: code = Unavailable desc = transport is closing

```
#### async - grpclib server with uvloop 
```bash
./ghz -t 0 -c 50 -n 200 --insecure --proto ./src/aws_api_stream/AwsAPI.proto --call AwsAPI.S3.GetObjects -d '{"bucket":"storybook.spaceone.dev"}' 0.0.0.0:50051


Summary:
  Count:	200
  Total:	48.47 s
  Slowest:	14.42 s
  Fastest:	5.03 s
  Average:	11.31 s
  Requests/sec:	4.13

Response time histogram:
  5030.181 [1]	|∎
  5969.617 [2]	|∎∎∎
  6909.054 [3]	|∎∎∎∎
  7848.490 [0]	|
  8787.927 [0]	|
  9727.363 [1]	|∎
  10666.800 [0]	|
  11606.236 [1]	|∎
  12545.673 [9]	|∎∎∎∎∎∎∎∎∎∎∎∎
  13485.109 [30]	|∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎
  14424.546 [4]	|∎∎∎∎∎

Latency distribution:
  10 % in 9.49 s
  25 % in 12.45 s
  50 % in 12.87 s
  75 % in 13.25 s
  90 % in 13.46 s
  95 % in 14.10 s
  0 % in 0 ns

Status code distribution:
  [Unavailable]   149 responses
  [OK]            51 responses

Error distribution:
  [149]   rpc error: code = Unavailable desc = transport is closing
```