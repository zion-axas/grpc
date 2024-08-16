build:
	python -m grpc_tools.protoc -I=./proto \
	--python_out=. \
	--pyi_out=. \
	--grpc_python_out=. \
	proto/my.proto

server:
	python3 myserver.py

client:
	python3 myclient.py
