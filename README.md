python -m grpc_tools.protoc -I../../protos --python_out=. --pyi_out=. --grpc_python_out=. ../../protos/helloworld.proto

pip install grpcio grpcio-tools grpcio-reflection

## my
python -m grpc_tools.protoc -I. --python_out=. --pyi_out=. --grpc_python_out=. my.proto
python -m grpc_tools.protoc -I./protos --python_out=. --pyi_out=. --grpc_python_out=. protos/my.proto
