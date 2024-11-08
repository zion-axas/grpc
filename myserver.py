from concurrent import futures

from generated import (
    my_pb2,  # содержит месседжи
    my_pb2_grpc,  # содержит сервисы MySrv, MySrvStub, MySrvServicer
)

import grpc

"""Все поля:
1. Необязательные
2. НИКОГДА не бывают null
3. Инициализируются значениями по умолчанию (0, пустая строка и т. д.) 
"""


class My(my_pb2_grpc.MySrv):
    "реализация методов сервиса MySrv"

    def Send(self, request: my_pb2.Req, context):
        print("request.counter:", request.counter, request.products, request.subdata)
        # request.counter: 0 [] - если не передать аргументы

        return my_pb2.Res(answer="ok")

    def SendStream(self, request: my_pb2.Req, context):
        "для возврата потока должен возвращать итератор"

        print("request.counter:", request.counter, request.products, request.subdata)

        for i in ["a", "b", "c"]:
            yield my_pb2.Res(answer=i)

        # return (my_pb2.Res(answer=i) for i in ["a", "b", "c"])  # OR возврат итератора

    def GetStream(self, stream_iterator, context):
        "итератор для получения потока принимает итератор"

        i: my_pb2.Req
        for i in stream_iterator:
            print(i.counter)
            yield my_pb2.Res(answer=str(i.counter * 5))


def serve():
    port = "50051"
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    my_pb2_grpc.add_MySrvServicer_to_server(My(), server)

    server.add_insecure_port("[::]:" + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination(timeout=60)


if __name__ == "__main__":
    serve()
