import my_pb2  # содержит месседжи
import my_pb2_grpc  # содержит сервисы MySrv, MySrvStub, MySrvServicer

import grpc

"""Все поля:
1. Необязательные
2. НИКОГДА не бывают null
3. Инициализируются значениями по умолчанию (0, пустая строка и т. д.) 
"""

# стаб - объект содержащий удаленные методы


def run():
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = my_pb2_grpc.MySrvStub(channel)

        response: my_pb2.Res = stub.Send(my_pb2.Req(counter=123, subdata={"id": 1}))
        print("response:", response.answer)


def run_stream():
    "принимает итератор"

    with grpc.insecure_channel("localhost:50051") as channel:
        stub = my_pb2_grpc.MySrvStub(channel)

        response: my_pb2.Res  # iterator
        for response in stub.SendStream(my_pb2.Req(counter=456, subdata={"id": 2})):
            print("response:", response.answer)


def run_bidirect():
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = my_pb2_grpc.MySrvStub(channel)

        stream_iterator = (my_pb2.Req(counter=i) for i in (1, 2, 3))

        response: my_pb2.Res
        for response in stub.GetStream(stream_iterator):
            print("response:", response.answer)


if __name__ == "__main__":
    run()
    run_stream()
    run_bidirect()
