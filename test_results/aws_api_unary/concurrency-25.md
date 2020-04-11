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

```
#### sync - grpcio server(max 10 worker)
```bash

```
#### async - grpclib server
```bash


```
#### async - grpclib server with uvloop 
```bash

```