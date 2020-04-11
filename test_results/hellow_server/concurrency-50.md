# condition
| Config      | Value       |
|-------------|-------------|
| Time Out    | 0(no limit) |
| Concurrency | 50          |
| Total       | 200         |
```bash
./ghz -t 0 -c 50 -n 200 --insecure --proto ./src/hellow_server/helloworld.proto --call helloworld.Greeter.SayHello -d '{"name":"sinsky"}' 0.0.0.0:50051
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