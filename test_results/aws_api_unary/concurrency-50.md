# condition
| Config      | Value       |
|-------------|-------------|
| Time Out    | 0(no limit) |
| Concurrency | 50          |
| Total       | 200         |
```bash
./ghz -t 0 -c 50 -n 200 --insecure --proto ./src/aws_api_unary/AwsAPI.proto --call AwsAPI.S3.GetObjects -d '{"bucket":"storybook.spaceone.dev"}' 0.0.0.0:50051
```

# summary
|                  | sync grpcio server(max 1 worker) | sync grpcio server(max 10 worker) | async grpclib server | async grpclib server(with uvloop) |
|------------------|----------------------------------|-----------------------------------|----------------------|-----------------------------------|
| Count            | 200                              | 200                               | 200                  | 200                               |
| OK               | 200                              | 200                               | 200                  | 200                               |
| DeadlineExceeded | 0                                | 0                                 | 0                    | 0                                 |
| Total            | 109.84 s                         | 66.75 s                           | 59.68 s              | 58.43 s                           |
| Slowest          | 29.53 s                          | 19.92 s                           | 27.24 s              | 24.32 s                           |
| Fastest          | 513.20 ms                        | 3.35 s                            | 3.87 s               | 5.14 s                            |
| Average          | 23.92 s                          | 15.02 s                           | 13.84 s              | 14.24 s                           |
| Requests/sec     | 1.82                             | 3.00                              | 3.35                 | 3.543.42                          |

# raw data

#### sync - grpcio server(max 1 worker)
```bash
./ghz -t 0 -c 50 -n 200 --insecure --proto ./src/aws_api_unary/AwsAPI.proto --call AwsAPI.S3.GetObjects -d '{"bucket":"storybook.spaceone.dev"}' 0.0.0.0:50051



Summary:
  Count:	200
  Total:	109.84 s
  Slowest:	29.53 s
  Fastest:	513.20 ms
  Average:	23.92 s
  Requests/sec:	1.82

Response time histogram:
  513.199 [1]	|
  3415.105 [5]	|∎∎
  6317.012 [6]	|∎∎∎
  9218.918 [5]	|∎∎
  12120.824 [6]	|∎∎∎
  15022.731 [5]	|∎∎
  17924.637 [5]	|∎∎
  20826.544 [6]	|∎∎∎
  23728.450 [5]	|∎∎
  26630.356 [83]	|∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎
  29532.263 [73]	|∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎

Latency distribution:
  10 % in 11.00 s
  25 % in 25.76 s
  50 % in 26.41 s
  75 % in 28.51 s
  90 % in 29.39 s
  95 % in 29.44 s
  99 % in 29.51 s

Status code distribution:
  [OK]   200 responses
```
#### sync - grpcio server(max 10 worker)
```bash
./ghz -t 0 -c 50 -n 200 --insecure --proto ./src/aws_api_unary/AwsAPI.proto --call AwsAPI.S3.GetObjects -d '{"bucket":"storybook.spaceone.dev"}' 0.0.0.0:50051


Summary:
  Count:	200
  Total:	66.75 s
  Slowest:	19.92 s
  Fastest:	3.35 s
  Average:	15.02 s
  Requests/sec:	3.00

Response time histogram:
  3346.698 [1]	|
  5003.984 [9]	|∎∎∎∎
  6661.271 [0]	|
  8318.557 [11]	|∎∎∎∎∎
  9975.844 [0]	|
  11633.130 [11]	|∎∎∎∎∎
  13290.416 [4]	|∎∎
  14947.703 [31]	|∎∎∎∎∎∎∎∎∎∎∎∎∎∎
  16604.989 [24]	|∎∎∎∎∎∎∎∎∎∎∎
  18262.276 [91]	|∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎
  19919.562 [18]	|∎∎∎∎∎∎∎∎

Latency distribution:
  10 % in 8.01 s
  25 % in 13.91 s
  50 % in 16.67 s
  75 % in 17.14 s
  90 % in 17.50 s
  95 % in 19.75 s
  99 % in 19.89 s

Status code distribution:
  [OK]   200 responses
```
#### async - grpclib server
```bash
./ghz -t 0 -c 50 -n 200 --insecure --proto ./src/aws_api_unary/AwsAPI.proto --call AwsAPI.S3.GetObjects -d '{"bucket":"storybook.spaceone.dev"}' 0.0.0.0:50051


Summary:
  Count:	200
  Total:	59.68 s
  Slowest:	27.24 s
  Fastest:	3.87 s
  Average:	13.84 s
  Requests/sec:	3.35

Response time histogram:
  3867.563 [1]	|∎
  6205.170 [2]	|∎∎
  8542.778 [17]	|∎∎∎∎∎∎∎∎∎∎∎∎∎
  10880.386 [27]	|∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎
  13217.993 [41]	|∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎
  15555.601 [52]	|∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎
  17893.209 [29]	|∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎
  20230.817 [15]	|∎∎∎∎∎∎∎∎∎∎∎∎
  22568.424 [12]	|∎∎∎∎∎∎∎∎∎
  24906.032 [1]	|∎
  27243.640 [3]	|∎∎

Latency distribution:
  10 % in 8.58 s
  25 % in 11.06 s
  50 % in 13.84 s
  75 % in 16.00 s
  90 % in 19.20 s
  95 % in 21.31 s
  99 % in 26.27 s

Status code distribution:
  [OK]   200 responses

```
#### async - grpclib server with uvloop 
```bash
./ghz -t 0 -c 50 -n 200 --insecure --proto ./src/aws_api_unary/AwsAPI.proto --call AwsAPI.S3.GetObjects -d '{"bucket":"storybook.spaceone.dev"}' 0.0.0.0:50051


Summary:
  Count:	200
  Total:	58.43 s
  Slowest:	24.32 s
  Fastest:	5.14 s
  Average:	14.24 s
  Requests/sec:	3.42

Response time histogram:
  5144.400 [1]	|
  7061.525 [14]	|∎∎∎∎∎∎∎
  8978.649 [19]	|∎∎∎∎∎∎∎∎∎
  10895.774 [0]	|
  12812.898 [3]	|∎
  14730.023 [54]	|∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎
  16647.147 [84]	|∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎
  18564.272 [0]	|
  20481.396 [14]	|∎∎∎∎∎∎∎
  22398.521 [3]	|∎
  24315.645 [8]	|∎∎∎∎

Latency distribution:
  10 % in 8.34 s
  25 % in 14.07 s
  50 % in 14.97 s
  75 % in 15.14 s
  90 % in 19.97 s
  95 % in 22.33 s
  99 % in 23.95 s

Status code distribution:
  [OK]   200 responses

```