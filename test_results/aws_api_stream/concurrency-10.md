# condition
| Config      | Value       |
|-------------|-------------|
| Time Out    | 0(no limit) |
| Concurrency | 10          |
| Total       | 200         |
```bash
./ghz -t 0 -c 10 -n 200 --insecure --proto ./src/aws_api_stream/AwsAPI.proto --call AwsAPI.S3.GetObjects -d '{"bucket":"storybook.spaceone.dev"}' 0.0.0.0:50051
```

# summary


# raw data

#### sync - grpcio server(max 1 worker)
```bash
./ghz -t 0 -c 10 -n 200 --insecure --proto ./src/aws_api_stream/AwsAPI.proto --call AwsAPI.S3.GetObjects -d '{"bucket":"storybook.spaceone.dev"}' 0.0.0.0:50051


Summary:
  Count:	200
  Total:	122.18 s
  Slowest:	8.62 s
  Fastest:	659.90 ms
  Average:	5.98 s
  Requests/sec:	1.64

Response time histogram:
  659.898 [1]	|
  1456.247 [1]	|
  2252.596 [0]	|
  3048.946 [1]	|
  3845.295 [1]	|
  4641.644 [0]	|
  5437.993 [34]	|∎∎∎∎∎∎∎∎∎∎∎∎
  6234.343 [112]	|∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎
  7030.692 [10]	|∎∎∎∎
  7827.041 [31]	|∎∎∎∎∎∎∎∎∎∎∎
  8623.391 [9]	|∎∎∎

Latency distribution:
  10 % in 5.36 s
  25 % in 5.48 s
  50 % in 5.63 s
  75 % in 6.27 s
  90 % in 7.62 s
  95 % in 7.80 s
  99 % in 8.62 s

Status code distribution:
  [OK]   200 responses
```
#### sync - grpcio server(max 10 worker)
```bash
./ghz -t 0 -c 10 -n 200 --insecure --proto ./src/aws_api_stream/AwsAPI.proto --call AwsAPI.S3.GetObjects -d '{"bucket":"storybook.spaceone.dev"}' 0.0.0.0:50051


Summary:
  Count:	200
  Total:	72.01 s
  Slowest:	5.03 s
  Fastest:	1.59 s
  Average:	3.54 s
  Requests/sec:	2.78

Response time histogram:
  1585.423 [1]	|∎
  1929.562 [6]	|∎∎∎
  2273.701 [0]	|
  2617.840 [1]	|∎
  2961.979 [4]	|∎∎
  3306.118 [38]	|∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎
  3650.257 [80]	|∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎
  3994.396 [40]	|∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎
  4338.535 [15]	|∎∎∎∎∎∎∎∎
  4682.674 [10]	|∎∎∎∎∎
  5026.813 [5]	|∎∎∎

Latency distribution:
  10 % in 3.12 s
  25 % in 3.32 s
  50 % in 3.53 s
  75 % in 3.79 s
  90 % in 4.23 s
  95 % in 4.51 s
  99 % in 4.90 s

Status code distribution:
  [OK]   200 responses
```
#### async - grpclib server
```bash
./ghz -t 0 -c 10 -n 200 --insecure --proto ./src/aws_api_stream/AwsAPI.proto --call AwsAPI.S3.GetObjects -d '{"bucket":"storybook.spaceone.dev"}' 0.0.0.0:50051


Summary:
  Count:	200
  Total:	52.96 s
  Slowest:	4.06 s
  Fastest:	574.99 ms
  Average:	2.49 s
  Requests/sec:	3.78

Response time histogram:
  574.986 [1]	|∎
  923.870 [2]	|∎∎∎
  1272.755 [1]	|∎
  1621.639 [4]	|∎∎∎∎∎∎
  1970.524 [2]	|∎∎∎
  2319.409 [0]	|
  2668.293 [3]	|∎∎∎∎
  3017.178 [6]	|∎∎∎∎∎∎∎∎
  3366.062 [29]	|∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎
  3714.947 [4]	|∎∎∎∎∎∎
  4063.832 [3]	|∎∎∎∎

Latency distribution:
  10 % in 1.48 s
  25 % in 2.90 s
  50 % in 3.10 s
  75 % in 3.23 s
  90 % in 3.46 s
  95 % in 4.02 s
  0 % in 0 ns

Status code distribution:
  [OK]            55 responses
  [Unavailable]   145 responses

Error distribution:
  [145]   rpc error: code = Unavailable desc = transport is closing

```
#### async - grpclib server with uvloop 
```bash
./ghz -t 0 -c 10 -n 200 --insecure --proto ./src/aws_api_stream/AwsAPI.proto --call AwsAPI.S3.GetObjects -d '{"bucket":"storybook.spaceone.dev"}' 0.0.0.0:50051


Summary:
  Count:	200
  Total:	51.04 s
  Slowest:	3.57 s
  Fastest:	1.52 s
  Average:	2.41 s
  Requests/sec:	3.92

Response time histogram:
  1518.703 [1]	|∎∎
  1723.842 [2]	|∎∎∎
  1928.981 [0]	|
  2134.120 [1]	|∎∎
  2339.259 [0]	|
  2544.397 [6]	|∎∎∎∎∎∎∎∎∎∎
  2749.536 [3]	|∎∎∎∎∎
  2954.675 [9]	|∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎
  3159.814 [23]	|∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎
  3364.953 [8]	|∎∎∎∎∎∎∎∎∎∎∎∎∎∎
  3570.092 [4]	|∎∎∎∎∎∎∎

Latency distribution:
  10 % in 2.36 s
  25 % in 2.86 s
  50 % in 3.03 s
  75 % in 3.15 s
  90 % in 3.35 s
  95 % in 3.48 s
  0 % in 0 ns

Status code distribution:
  [OK]            57 responses
  [Unavailable]   143 responses

Error distribution:
  [143]   rpc error: code = Unavailable desc = transport is closing
```