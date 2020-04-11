# condition
| Config      | Value       |
|-------------|-------------|
| Time Out    | 0(no limit) |
| Concurrency | 2           |
| Total       | 200         |
```bash
./ghz -t 0 -c 2 -n 200 --insecure --proto ./src/aws_api_unary/AwsAPI.proto --call AwsAPI.S3.GetObjects -d '{"bucket":"storybook.spaceone.dev"}' 0.0.0.0:50051
```

# summary


# raw data

#### sync - grpcio server(max 1 worker)
```bash
./ghz -t 0 -c 2 -n 200 --insecure --proto ./src/aws_api_unary/AwsAPI.proto --call AwsAPI.S3.GetObjects -d '{"bucket":"storybook.spaceone.dev"}' 0.0.0.0:50051


Summary:
  Count:	200
  Total:	117.34 s
  Slowest:	2.76 s
  Fastest:	687.63 ms
  Average:	1.17 s
  Requests/sec:	1.70

Response time histogram:
  687.630 [1]	|
  895.281 [0]	|
  1102.931 [64]	|∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎
  1310.582 [120]	|∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎
  1518.233 [8]	|∎∎∎
  1725.884 [2]	|∎
  1933.534 [1]	|
  2141.185 [0]	|
  2348.836 [2]	|∎
  2556.487 [1]	|
  2764.137 [1]	|

Latency distribution:
  10 % in 1.06 s
  25 % in 1.09 s
  50 % in 1.13 s
  75 % in 1.18 s
  90 % in 1.28 s
  95 % in 1.34 s
  99 % in 2.44 s

Status code distribution:
  [OK]   200 responses
```
#### sync - grpcio server(max 10 worker)
```bash
./ghz -t 0 -c 2 -n 200 --insecure --proto ./src/aws_api_unary/AwsAPI.proto --call AwsAPI.S3.GetObjects -d '{"bucket":"storybook.spaceone.dev"}' 0.0.0.0:50051


Summary:
  Count:	200
  Total:	82.58 s
  Slowest:	1.75 s
  Fastest:	505.74 ms
  Average:	824.79 ms
  Requests/sec:	2.42

Response time histogram:
  505.745 [1]	|
  630.462 [1]	|
  755.179 [25]	|∎∎∎∎∎∎
  879.895 [159]	|∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎
  1004.612 [6]	|∎∎
  1129.329 [0]	|
  1254.046 [0]	|
  1378.763 [2]	|∎
  1503.480 [3]	|∎
  1628.197 [0]	|
  1752.914 [3]	|∎

Latency distribution:
  10 % in 745.48 ms
  25 % in 770.43 ms
  50 % in 797.41 ms
  75 % in 835.22 ms
  90 % in 860.28 ms
  95 % in 919.10 ms
  99 % in 1.72 s

Status code distribution:
  [OK]   200 responses

```
#### async - grpclib server
```bash
./ghz -t 0 -c 2 -n 200 --insecure --proto ./src/aws_api_unary/AwsAPI.proto --call AwsAPI.S3.GetObjects -d '{"bucket":"storybook.spaceone.dev"}' 0.0.0.0:50051


Summary:
  Count:	200
  Total:	84.09 s
  Slowest:	2.77 s
  Fastest:	518.04 ms
  Average:	839.97 ms
  Requests/sec:	2.38

Response time histogram:
  518.042 [1]	|
  743.715 [63]	|∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎
  969.388 [99]	|∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎
  1195.061 [30]	|∎∎∎∎∎∎∎∎∎∎∎∎
  1420.733 [2]	|∎
  1646.406 [1]	|
  1872.079 [0]	|
  2097.752 [2]	|∎
  2323.425 [1]	|
  2549.098 [0]	|
  2774.771 [1]	|

Latency distribution:
  10 % in 623.68 ms
  25 % in 708.07 ms
  50 % in 798.54 ms
  75 % in 943.89 ms
  90 % in 1.02 s
  95 % in 1.08 s
  99 % in 2.23 s

Status code distribution:
  [OK]   200 responses

```
#### async - grpclib server with uvloop 
```bash
./ghz -t 0 -c 2 -n 200 --insecure --proto ./src/aws_api_unary/AwsAPI.proto --call AwsAPI.S3.GetObjects -d '{"bucket":"storybook.spaceone.dev"}' 0.0.0.0:50051


Summary:
  Count:	200
  Total:	84.39 s
  Slowest:	1.92 s
  Fastest:	495.28 ms
  Average:	836.05 ms
  Requests/sec:	2.37

Response time histogram:
  495.283 [1]	|∎
  637.309 [27]	|∎∎∎∎∎∎∎∎∎∎∎∎∎∎
  779.336 [42]	|∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎
  921.362 [80]	|∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎
  1063.388 [40]	|∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎
  1205.415 [4]	|∎∎
  1347.441 [2]	|∎
  1489.468 [0]	|
  1631.494 [0]	|
  1773.521 [2]	|∎
  1915.547 [2]	|∎

Latency distribution:
  10 % in 624.96 ms
  25 % in 737.55 ms
  50 % in 818.34 ms
  75 % in 922.49 ms
  90 % in 1.02 s
  95 % in 1.06 s
  99 % in 1.84 s

Status code distribution:
  [OK]   200 responses
```