from proto import (
    my_pb2,  # содержит месседжи
    my_pb2_grpc,  # содержит сервисы MySrv, MySrvStub, MySrvServicer
)

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

        request = my_pb2.Req(counter=123, subdata={"id": 1})

        response: my_pb2.Res = stub.Send(request)
        print("response:", response.answer)

        # async
        # response_future = stub.Send.future(req)
        # response = response_future.result()


def run_stream():
    "принимает итератор"

    with grpc.insecure_channel("localhost:50051") as channel:
        stub = my_pb2_grpc.MySrvStub(channel)

        request = my_pb2.Req(counter=456, subdata={"id": 2})

        response: my_pb2.Res  # type iterator
        for response in stub.SendStream(request):
            print("stream response:", response.answer)


def run_bidirect():
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = my_pb2_grpc.MySrvStub(channel)

        stream_iterator = (my_pb2.Req(counter=i) for i in (1, 2, 3))

        response: my_pb2.Res  # type iterator
        for response in stub.GetStream(stream_iterator):
            print("bidirect response:", response.answer)

        # async
        # response_future = stub.GetStream.future(stream_iterator)
        # response = route_summary_future.result()


if __name__ == "__main__":
    run()
    run_stream()
    run_bidirect()
