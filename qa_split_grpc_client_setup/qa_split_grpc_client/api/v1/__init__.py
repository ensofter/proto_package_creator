from ozwhc.grpc_clients import BaseGrpc
from qa_split_grpc_client.api.v1 import split_pb2, split_pb2_grpc
from google.protobuf.empty_pb2 import Empty


class WmsGoServiceBatchingSplitV1Split(BaseGrpc):
    grpc_stub = split_pb2_grpc.SplitStub

    def split_posting(self, request: split_pb2.SplitPostingRequest, **kwargs) -> split_pb2.SplitPostingResponse:
        return self._grpc_request(request=request, request_method=self.stub.SplitPosting, **kwargs)
                        
    def split_posting_wh_comm(self, request: split_pb2.SplitPostingWhCommRequest, **kwargs) -> split_pb2.SplitPostingWhCommResponse:
        return self._grpc_request(request=request, request_method=self.stub.SplitPostingWhComm, **kwargs)
                        
    def add_postings_split_reasons(self, request: split_pb2.PostingsSplitReasonsRequest, **kwargs) -> Empty():
        return self._grpc_request(request=request, request_method=self.stub.AddPostingsSplitReasons, **kwargs)
                        
    def split_posting_by_tags(self, request: split_pb2.SplitPostingRequest, **kwargs) -> split_pb2.SplitPostingResponse:
        return self._grpc_request(request=request, request_method=self.stub.SplitPostingByTags, **kwargs)
                        