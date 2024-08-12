from concurrent import futures

import grpc
import my_pb2
import my_pb2_grpc


class My(my_pb2_grpc.MySrv):
    "реализация методов сервиса MySrv"

    def Send(self, request, context):
        print("request.counter:", request.counter)
        return my_pb2.Res(answer="ok")


def serve():
    port = "50051"
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    my_pb2_grpc.add_MySrvServicer_to_server(My(), server)
    server.add_insecure_port("[::]:" + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination(timeout=30)


if __name__ == "__main__":
    serve()
