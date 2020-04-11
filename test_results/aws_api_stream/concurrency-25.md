# condition
| Config      | Value       |
|-------------|-------------|
| Time Out    | 0(no limit) |
| Concurrency | 25          |
| Total       | 200         |
```bash
./ghz -t 0 -c 25 -n 200 --insecure --proto ./src/aws_api_stream/AwsAPI.proto --call AwsAPI.S3.GetObjects -d '{"bucket":"storybook.spaceone.dev"}' 0.0.0.0:50051
```

# summary


# raw data

#### sync - grpcio server(max 1 worker)
```bash
 ./ghz -t 0 -c 25 -n 200 --insecure --proto ./src/aws_api_stream/AwsAPI.proto --call AwsAPI.S3.GetObjects -d '{"bucket":"storybook.spaceone.dev"}' 0.0.0.0:50051


Summary:
  Count:	200
  Total:	116.13 s
  Slowest:	16.84 s
  Fastest:	1.08 s
  Average:	13.69 s
  Requests/sec:	1.72

Response time histogram:
  1083.882 [1]	|
  2659.197 [1]	|
  4234.513 [2]	|∎
  5809.828 [2]	|∎
  7385.144 [2]	|∎
  8960.459 [2]	|∎
  10535.775 [3]	|∎
  12111.090 [3]	|∎
  13686.406 [54]	|∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎
  15261.721 [93]	|∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎
  16837.037 [37]	|∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎

Latency distribution:
  10 % in 13.36 s
  25 % in 13.55 s
  50 % in 13.81 s
  75 % in 15.08 s
  90 % in 15.45 s
  95 % in 15.59 s
  99 % in 16.33 s

Status code distribution:
  [OK]   200 responses
```
#### sync - grpcio server(max 10 worker)
```bash
./ghz -t 0 -c 25 -n 200 --insecure --proto ./src/aws_api_stream/AwsAPI.proto --call AwsAPI.S3.GetObjects -d '{"bucket":"storybook.spaceone.dev"}' 0.0.0.0:50051


Summary:
  Count:	200
  Total:	74.96 s
  Slowest:	14.34 s
  Fastest:	2.48 s
  Average:	8.90 s
  Requests/sec:	2.67

Response time histogram:
  2484.060 [1]	|∎
  3669.974 [2]	|∎∎
  4855.888 [0]	|
  6041.802 [8]	|∎∎∎∎∎∎∎
  7227.716 [49]	|∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎
  8413.630 [40]	|∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎
  9599.544 [6]	|∎∎∎∎∎
  10785.458 [49]	|∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎
  11971.372 [39]	|∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎
  13157.286 [2]	|∎∎
  14343.200 [4]	|∎∎∎

Latency distribution:
  10 % in 6.92 s
  25 % in 7.16 s
  50 % in 8.78 s
  75 % in 10.70 s
  90 % in 11.41 s
  95 % in 11.71 s
  99 % in 14.28 s

Status code distribution:
  [OK]   200 responses
```
#### async - grpclib server
```bash
./ghz -t 0 -c 25 -n 200 --insecure --proto ./src/aws_api_stream/AwsAPI.proto --call AwsAPI.S3.GetObjects -d '{"bucket":"storybook.spaceone.dev"}' 0.0.0.0:50051


Summary:
  Count:	200
  Total:	56.88 s
  Slowest:	9.16 s
  Fastest:	2.60 s
  Average:	6.63 s
  Requests/sec:	3.52

Response time histogram:
  2598.699 [1]	|∎∎∎∎
  3255.299 [5]	|∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎
  3911.898 [0]	|
  4568.498 [1]	|∎∎∎∎
  5225.097 [2]	|∎∎∎∎∎∎∎∎
  5881.697 [7]	|∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎
  6538.297 [0]	|
  7194.896 [1]	|∎∎∎∎
  7851.496 [10]	|∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎
  8508.095 [3]	|∎∎∎∎∎∎∎∎∎∎∎∎
  9164.695 [4]	|∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎

Latency distribution:
  10 % in 2.77 s
  25 % in 5.37 s
  50 % in 7.29 s
  75 % in 7.82 s
  90 % in 9.12 s
  95 % in 9.16 s
  0 % in 0 ns

Status code distribution:
  [OK]            34 responses
  [Unavailable]   166 responses

Error distribution:
  [166]   rpc error: code = Unavailable desc = transport is closing

```
#### async - grpclib server with uvloop 
```bash
./ghz -t 0 -c 25 -n 200 --insecure --proto ./src/aws_api_stream/AwsAPI.proto --call AwsAPI.S3.GetObjects -d '{"bucket":"storybook.spaceone.dev"}' 0.0.0.0:50051


Summary:
  Count:	200
  Total:	57.44 s
  Slowest:	9.61 s
  Fastest:	2.05 s
  Average:	6.79 s
  Requests/sec:	3.48

Response time histogram:
  2049.108 [1]	|∎∎∎∎∎
  2804.828 [5]	|∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎
  3560.548 [0]	|
  4316.268 [0]	|
  5071.988 [0]	|
  5827.708 [8]	|∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎
  6583.428 [8]	|∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎
  7339.148 [5]	|∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎
  8094.868 [6]	|∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎
  8850.588 [1]	|∎∎∎∎∎
  9606.308 [5]	|∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎

Latency distribution:
  10 % in 2.16 s
  25 % in 5.72 s
  50 % in 6.44 s
  75 % in 7.87 s
  90 % in 9.45 s
  95 % in 9.61 s
  0 % in 0 ns

Status code distribution:
  [OK]            39 responses
  [Unavailable]   161 responses

Error distribution:
  [161]   rpc error: code = Unavailable desc = transport is closing
```