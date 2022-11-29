from ozwhc.grpc_clients import BaseGrpc
from qa_split_grpc_client.api.qa import qa_pb2, qa_pb2_grpc
from google.protobuf.empty_pb2 import Empty


class OzonWmsGoServiceBatchingSplitApiQaQa(BaseGrpc):
    grpc_stub = qa_pb2_grpc.QaStub

    def remove_oldest(self, request: qa_pb2.RemoveOldestRequest, **kwargs) -> qa_pb2.RemoveOldestResponse:
        return self._grpc_request(request=request, request_method=self.stub.RemoveOldest, **kwargs)
                        