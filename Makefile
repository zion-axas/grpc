build:
	python -m grpc_tools.protoc -I./protos \
	--python_out=. \
	--pyi_out=. \
	--grpc_python_out=. \
	protos/my.proto

server:
	python3 myserver.py

client:
	python3 myclient.py
