# condition
| Config      | Value       |
|-------------|-------------|
| Time Out    | 0(no limit) |
| Concurrency | 25          |
| Total       | 200         |
```bash
./ghz -t 0 -c 25 -n 200 --insecure --proto ./src/aws_api_unary/AwsAPI.proto --call AwsAPI.S3.GetObjects -d '{"bucket":"storybook.spaceone.dev"}' 0.0.0.0:50051
```

# summary


# raw data

#### sync - grpcio server(max 1 worker)
```bash
./ghz -t 0 -c 25 -n 200 --insecure --proto ./src/aws_api_unary/AwsAPI.proto --call AwsAPI.S3.GetObjects -d '{"bucket":"storybook.spaceone.dev"}' 0.0.0.0:50051


Summary:
  Count:	200
  Total:	109.31 s
  Slowest:	15.41 s
  Fastest:	1.13 s
  Average:	12.88 s
  Requests/sec:	1.83

Response time histogram:
  1128.586 [1]	|
  2557.032 [2]	|∎
  3985.478 [3]	|∎
  5413.924 [2]	|∎
  6842.370 [3]	|∎
  8270.816 [3]	|∎
  9699.262 [2]	|∎
  11127.708 [3]	|∎
  12556.154 [3]	|∎
  13984.600 [127]	|∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎
  15413.046 [51]	|∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎

Latency distribution:
  10 % in 11.81 s
  25 % in 12.84 s
  50 % in 13.19 s
  75 % in 14.20 s
  90 % in 14.95 s
  95 % in 15.32 s
  99 % in 15.38 s

Status code distribution:
  [OK]   200 responses
```
#### sync - grpcio server(max 10 worker)
```bash
./ghz -t 0 -c 25 -n 200 --insecure --proto ./src/aws_api_unary/AwsAPI.proto --call AwsAPI.S3.GetObjects -d '{"bucket":"storybook.spaceone.dev"}' 0.0.0.0:50051


Summary:
  Count:	200
  Total:	68.52 s
  Slowest:	12.40 s
  Fastest:	3.78 s
  Average:	8.20 s
  Requests/sec:	2.92

Response time histogram:
  3778.314 [1]	|
  4640.832 [10]	|∎∎∎∎∎
  5503.349 [0]	|
  6365.867 [5]	|∎∎
  7228.384 [18]	|∎∎∎∎∎∎∎∎
  8090.901 [32]	|∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎
  8953.419 [86]	|∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎
  9815.936 [28]	|∎∎∎∎∎∎∎∎∎∎∎∎∎
  10678.454 [8]	|∎∎∎∎
  11540.971 [9]	|∎∎∎∎
  12403.488 [3]	|∎

Latency distribution:
  10 % in 6.52 s
  25 % in 8.00 s
  50 % in 8.22 s
  75 % in 8.89 s
  90 % in 9.92 s
  95 % in 10.81 s
  99 % in 12.39 s

Status code distribution:
  [OK]   200 responses
```
#### async - grpclib server
```bash
./ghz -t 0 -c 25 -n 200 --insecure --proto ./src/aws_api_unary/AwsAPI.proto --call AwsAPI.S3.GetObjects -d '{"bucket":"storybook.spaceone.dev"}' 0.0.0.0:50051


Summary:
  Count:	200
  Total:	57.39 s
  Slowest:	12.30 s
  Fastest:	1.55 s
  Average:	6.91 s
  Requests/sec:	3.49

Response time histogram:
  1553.060 [1]	|∎
  2628.086 [0]	|
  3703.113 [6]	|∎∎∎∎∎
  4778.140 [20]	|∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎
  5853.166 [30]	|∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎
  6928.193 [43]	|∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎
  8003.220 [46]	|∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎
  9078.247 [26]	|∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎
  10153.273 [21]	|∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎
  11228.300 [6]	|∎∎∎∎∎
  12303.327 [1]	|∎

Latency distribution:
  10 % in 4.42 s
  25 % in 5.54 s
  50 % in 6.94 s
  75 % in 8.17 s
  90 % in 9.44 s
  95 % in 9.89 s
  99 % in 10.88 s

Status code distribution:
  [OK]   200 responses

```
#### async - grpclib server with uvloop 
```bash
./ghz -t 0 -c 25 -n 200 --insecure --proto ./src/aws_api_unary/AwsAPI.proto --call AwsAPI.S3.GetObjects -d '{"bucket":"storybook.spaceone.dev"}' 0.0.0.0:50051


Summary:
  Count:	200
  Total:	56.57 s
  Slowest:	13.05 s
  Fastest:	1.89 s
  Average:	6.96 s
  Requests/sec:	3.54

Response time histogram:
  1887.035 [1]	|∎
  3002.898 [8]	|∎∎∎∎∎∎
  4118.760 [14]	|∎∎∎∎∎∎∎∎∎∎∎
  5234.623 [23]	|∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎
  6350.486 [22]	|∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎
  7466.348 [50]	|∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎
  8582.211 [40]	|∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎
  9698.073 [24]	|∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎
  10813.936 [11]	|∎∎∎∎∎∎∎∎∎
  11929.799 [5]	|∎∎∎∎
  13045.661 [2]	|∎∎

Latency distribution:
  10 % in 4.02 s
  25 % in 5.45 s
  50 % in 7.38 s
  75 % in 7.97 s
  90 % in 9.46 s
  95 % in 10.74 s
  99 % in 12.06 s

Status code distribution:
  [OK]   200 responsess

```