build:
	python -m grpc_tools.protoc -I=./proto \
	--python_out=./generated \
	--pyi_out=./generated \
	--grpc_python_out=./generated \
	./proto/my.proto

server:
	python3 myserver.py

client:
	python3 myclient.py
