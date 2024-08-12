from concurrent import futures

import my_pb2  # содержит месседжи
import my_pb2_grpc  # содержит сервисы MySrv, MySrvStub, MySrvServicer

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

        return iter([my_pb2.Res(answer=i) for i in ["a", "b", "c"]])

        def foo(r):
            for i in r:
                yield my_pb2.Res(answer=i)

        return foo(["a", "b", "c"])


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
