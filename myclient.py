import my_pb2
import my_pb2_grpc
import grpc


def run():
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = my_pb2_grpc.MySrvStub(channel)
        response = stub.Send(my_pb2.Req(counter=123))

        print("response:", response)


if __name__ == "__main__":
    run()
