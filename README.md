### grpc basics tutorial

`https://grpc.io/docs/languages/python/basics/`

### protobuf guide

`https://protobuf.dev/programming-guides/proto3/`

### helloworld.proto

`python -m grpc_tools.protoc -I../../proto --python_out=. --pyi_out=. --grpc_python_out=. ../../protos/helloworld.proto`

### pip install

`pip install grpcio grpcio-tools grpcio-reflection`

### my

```
python3 -m grpc_tools.protoc \
--python_out=. \  # классы для сообщений
--grpc_python_out=. \  # классы для сервисов
--pyi_out=. \  # аннотации типов
--proto_path=. \  # путь к директории файлов .proto
./proto/*.proto
```
--proto_path=IMPORT_PATH OR -I=IMPORT_PATH
