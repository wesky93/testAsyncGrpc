# condition
| Config      | Value       |
|-------------|-------------|
| Time Out    | 0(no limit) |
| Concurrency | 10          |
| Total       | 200         |
```bash
./ghz -t 0 -c 10 -n 200 --insecure --proto ./src/aws_api_unary/AwsAPI.proto --call AwsAPI.S3.GetObjects -d '{"bucket":"storybook.spaceone.dev"}' 0.0.0.0:50051
```

# summary
|                  | sync grpcio server(max 1 worker) | sync grpcio server(max 10 worker) | async grpclib server | async grpclib server(with uvloop) |
|------------------|----------------------------------|-----------------------------------|----------------------|-----------------------------------|
| Count            | 200                              | 200                               | 200                  | 200                               |
| OK               | 200                              | 200                               | 200                  | 200                               |
| DeadlineExceeded | 0                                | 0                                 | 0                    | 0                                 |
| Total            | 116.32 s                         | 65.58 s                           | 62.34 s              | 60.03 s                           |
| Slowest          | 7.27 s                           | 4.89 s                            | 5.04 s               | 5.12 s                            |
| Fastest          | 644.39 ms                        | 886.42 ms                         | 1.28 s               | 1.30 s                            |
| Average          | 5.69 s                           | 3.22 s                            | 3.08 s               | 2.99 s                            |
| Requests/sec     | 1.72                             | 3.05                              | 3.21                 | 3.33                              |


# raw data

#### sync - grpcio server(max 1 worker)
```bash
./ghz -t 0 -c 10 -n 200 --insecure --proto ./src/aws_api_unary/AwsAPI.proto --call AwsAPI.S3.GetObjects -d '{"bucket":"storybook.spaceone.dev"}' 0.0.0.0:50051


Summary:
  Count:	200
  Total:	116.32 s
  Slowest:	7.27 s
  Fastest:	644.39 ms
  Average:	5.69 s
  Requests/sec:	1.72

Response time histogram:
  644.386 [1]	|
  1307.105 [1]	|
  1969.824 [1]	|
  2632.543 [1]	|
  3295.261 [1]	|
  3957.980 [1]	|
  4620.699 [2]	|∎
  5283.418 [10]	|∎∎∎
  5946.137 [148]	|∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎
  6608.856 [6]	|∎∎
  7271.574 [28]	|∎∎∎∎∎∎∎∎

Latency distribution:
  10 % in 5.30 s
  25 % in 5.47 s
  50 % in 5.61 s
  75 % in 5.78 s
  90 % in 7.07 s
  95 % in 7.17 s
  99 % in 7.22 s

Status code distribution:
  [OK]   200 responses
```
#### sync - grpcio server(max 10 worker)
```bash
./ghz -t 0 -c 10 -n 200 --insecure --proto ./src/aws_api_unary/AwsAPI.proto --call AwsAPI.S3.GetObjects -d '{"bucket":"storybook.spaceone.dev"}' 0.0.0.0:50051


Summary:
  Count:	200
  Total:	65.58 s
  Slowest:	4.89 s
  Fastest:	886.42 ms
  Average:	3.22 s
  Requests/sec:	3.05

Response time histogram:
  886.421 [1]	|
  1286.953 [2]	|∎
  1687.484 [7]	|∎∎∎
  2088.016 [0]	|
  2488.547 [4]	|∎∎
  2889.079 [14]	|∎∎∎∎∎∎
  3289.610 [93]	|∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎
  3690.142 [51]	|∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎
  4090.673 [15]	|∎∎∎∎∎∎
  4491.205 [10]	|∎∎∎∎
  4891.737 [3]	|∎

Latency distribution:
  10 % in 2.82 s
  25 % in 3.01 s
  50 % in 3.20 s
  75 % in 3.52 s
  90 % in 3.94 s
  95 % in 4.37 s
  99 % in 4.70 s

Status code distribution:
  [OK]   200 responses
```
#### async - grpclib server
```bash
./ghz -t 0 -c 10 -n 200 --insecure --proto ./src/aws_api_unary/AwsAPI.proto --call AwsAPI.S3.GetObjects -d '{"bucket":"storybook.spaceone.dev"}' 0.0.0.0:50051


Summary:
  Count:	200
  Total:	62.34 s
  Slowest:	5.04 s
  Fastest:	1.28 s
  Average:	3.08 s
  Requests/sec:	3.21

Response time histogram:
  1277.006 [1]	|∎
  1653.251 [9]	|∎∎∎∎∎∎∎∎∎∎∎
  2029.495 [15]	|∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎
  2405.740 [18]	|∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎
  2781.984 [30]	|∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎
  3158.229 [30]	|∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎
  3534.473 [32]	|∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎
  3910.718 [31]	|∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎
  4286.962 [18]	|∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎
  4663.206 [13]	|∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎
  5039.451 [3]	|∎∎∎∎

Latency distribution:
  10 % in 1.89 s
  25 % in 2.51 s
  50 % in 3.12 s
  75 % in 3.69 s
  90 % in 4.14 s
  95 % in 4.42 s
  99 % in 4.99 s

Status code distribution:
  [OK]   200 responses

```
#### async - grpclib server with uvloop 
```bash
./ghz -t 0 -c 10 -n 200 --insecure --proto ./src/aws_api_unary/AwsAPI.proto --call AwsAPI.S3.GetObjects -d '{"bucket":"storybook.spaceone.dev"}' 0.0.0.0:50051


Summary:
  Count:	200
  Total:	60.03 s
  Slowest:	5.12 s
  Fastest:	1.30 s
  Average:	2.99 s
  Requests/sec:	3.33

Response time histogram:
  1296.504 [1]	|
  1679.244 [11]	|∎∎∎∎
  2061.985 [10]	|∎∎∎∎
  2444.726 [5]	|∎∎
  2827.466 [21]	|∎∎∎∎∎∎∎∎
  3210.207 [109]	|∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎
  3592.948 [19]	|∎∎∎∎∎∎∎
  3975.688 [3]	|∎
  4358.429 [8]	|∎∎∎
  4741.170 [11]	|∎∎∎∎
  5123.910 [2]	|∎

Latency distribution:
  10 % in 1.91 s
  25 % in 2.83 s
  50 % in 2.97 s
  75 % in 3.15 s
  90 % in 4.08 s
  95 % in 4.45 s
  99 % in 4.77 s

Status code distribution:
  [OK]   200 responses
```