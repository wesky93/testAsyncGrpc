# Grpc server bencmarking


## sync server(originer)
### lib
- [grpcio](https://pypi.org/project/grpcio/) == 1.28.1
- boto3

## async server(originer)
### lib
- grpclib
- aioboto

## performance test tool
- [ghz](https://github.com/bojand/ghz)

## scenario
1. example server 
2. request s3 objects list
3. request s3 objects & save monogoDB


## How to test?
1. [download ghz](https://github.com/bojand/ghz/releases) 
2. start server
3. start ghz

## result