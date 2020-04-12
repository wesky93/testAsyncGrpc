# condition
| Config      | Value       |
|-------------|-------------|
| Time Out    | 0(no limit) |
| Concurrency | 2           |
| Total       | 200         |
```bash
./ghz -t 0 -c 2 -n 200 --insecure --proto ./src/aws_api_stream/AwsAPI.proto --call AwsAPI.S3.GetObjects -d '{"bucket":"storybook.spaceone.dev"}' 0.0.0.0:50051
```

# summary
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

# raw data

#### sync - grpcio server(max 1 worker)
```bash
./ghz --connect-timeout 120s -t 0 -c 2 -n 200 --insecure --proto ./src/aws_api_stream/AwsAPI.proto --call AwsAPI.S3.GetObjects -d '{"bucket":"storybook.spaceone.dev"}' 0.0.0.0:50051


Summary:
  Count:	200
  Total:	121.00 s
  Slowest:	2.40 s
  Fastest:	654.55 ms
  Average:	1.21 s
  Requests/sec:	1.65

Response time histogram:
  654.547 [1]	|
  829.423 [0]	|
  1004.299 [0]	|
  1179.175 [110]	|∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎
  1354.051 [74]	|∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎
  1528.927 [8]	|∎∎∎
  1703.803 [1]	|
  1878.678 [2]	|∎
  2053.554 [2]	|∎
  2228.430 [0]	|
  2403.306 [2]	|∎

Latency distribution:
  10 % in 1.09 s
  25 % in 1.14 s
  50 % in 1.17 s
  75 % in 1.22 s
  90 % in 1.32 s
  95 % in 1.44 s
  99 % in 2.40 s

Status code distribution:
  [OK]   200 responses
```
#### sync - grpcio server(max 10 worker)
```bash
./ghz -t 0 -c 2 -n 200 --insecure --proto ./src/aws_api_stream/AwsAPI.proto --call AwsAPI.S3.GetObjects -d '{"bucket":"storybook.spaceone.dev"}' 0.0.0.0:50051


Summary:
  Count:	200
  Total:	90.31 s
  Slowest:	2.18 s
  Fastest:	552.69 ms
  Average:	900.35 ms
  Requests/sec:	2.21

Response time histogram:
  552.687 [1]	|
  715.720 [1]	|
  878.754 [115]	|∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎
  1041.787 [72]	|∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎
  1204.821 [5]	|∎∎
  1367.854 [0]	|
  1530.888 [1]	|
  1693.921 [2]	|∎
  1856.955 [1]	|
  2019.988 [1]	|
  2183.022 [1]	|

Latency distribution:
  10 % in 812.44 ms
  25 % in 840.98 ms
  50 % in 867.72 ms
  75 % in 903.92 ms
  90 % in 976.20 ms
  95 % in 1.06 s
  99 % in 1.96 s

Status code distribution:
  [OK]   200 responses
```
#### async - grpclib server
```bash
./ghz -t 0 -c 2 -n 200 --insecure --proto ./src/aws_api_stream/AwsAPI.proto --call AwsAPI.S3.GetObjects -d '{"bucket":"storybook.spaceone.dev"}' 0.0.0.0:50051


Summary:
  Count:	200
  Total:	85.28 s
  Slowest:	2.08 s
  Fastest:	500.94 ms
  Average:	851.79 ms
  Requests/sec:	2.35

Response time histogram:
  500.941 [1]	|∎
  658.910 [32]	|∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎
  816.878 [59]	|∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎
  974.847 [62]	|∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎
  1132.815 [38]	|∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎
  1290.784 [3]	|∎∎
  1448.752 [2]	|∎
  1606.720 [1]	|∎
  1764.689 [1]	|∎
  1922.657 [0]	|
  2080.626 [1]	|∎

Latency distribution:
  10 % in 628.46 ms
  25 % in 766.43 ms
  50 % in 823.33 ms
  75 % in 956.64 ms
  90 % in 1.05 s
  95 % in 1.09 s
  99 % in 1.74 s

Status code distribution:
  [OK]   200 responses
```
#### async - grpclib server with uvloop 
```bash
./ghz -t 0 -c 2 -n 200 --insecure --proto ./src/aws_api_stream/AwsAPI.proto --call AwsAPI.S3.GetObjects -d '{"bucket":"storybook.spaceone.dev"}' 0.0.0.0:50051


Summary:
  Count:	200
  Total:	48.39 s
  Slowest:	1.72 s
  Fastest:	451.07 ms
  Average:	483.83 ms
  Requests/sec:	4.13

Response time histogram:
  451.074 [1]	|∎
  577.877 [3]	|∎∎
  704.679 [1]	|∎
  831.481 [67]	|∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎
  958.284 [27]	|∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎
  1085.086 [7]	|∎∎∎∎
  1211.888 [0]	|
  1338.691 [2]	|∎
  1465.493 [0]	|
  1592.295 [0]	|
  1719.098 [1]	|∎

Latency distribution:
  10 % in 721.01 ms
  25 % in 737.08 ms
  50 % in 777.07 ms
  75 % in 869.34 ms
  90 % in 994.60 ms
  95 % in 1.04 s
  99 % in 1.72 s

Status code distribution:
  [OK]            109 responses
  [Unavailable]   91 responses

Error distribution:
  [91]   rpc error: code = Unavailable desc = transport is closing
```