from ozwhc.grpc_clients import BaseGrpc
from qa_split_grpc_client.api.system_v1 import system_v1_pb2, system_v1_pb2_grpc
from google.protobuf.empty_pb2 import Empty


class WmsGoServiceBatchingSplitSystemV1SystemV1(BaseGrpc):
    grpc_stub = system_v1_pb2_grpc.SystemV1Stub

    def get_feature_flag_list(self, request: system_v1_pb2.GetFeatureFlagListRequest, **kwargs) -> system_v1_pb2.GetFeatureFlagListResponse:
        return self._grpc_request(request=request, request_method=self.stub.GetFeatureFlagList, **kwargs)
                        
    def link_feature_flag(self, request: system_v1_pb2.LinkFeatureFlagRequest, **kwargs) -> system_v1_pb2.LinkFeatureFlagResponse:
        return self._grpc_request(request=request, request_method=self.stub.LinkFeatureFlag, **kwargs)
                        
    def unlink_feature_flag(self, request: system_v1_pb2.UnlinkFeatureFlagRequest, **kwargs) -> system_v1_pb2.UnlinkFeatureFlagResponse:
        return self._grpc_request(request=request, request_method=self.stub.UnlinkFeatureFlag, **kwargs)
                        
    def v1_get_split_restrictions(self, request: system_v1_pb2.V1GetSplitRestrictionsRequest, **kwargs) -> system_v1_pb2.V1GetSplitRestrictionsResponse:
        return self._grpc_request(request=request, request_method=self.stub.V1GetSplitRestrictions, **kwargs)
                        
    def v1_create_split_restrictions(self, request: system_v1_pb2.V1CreateSplitRestrictionsRequest, **kwargs) -> system_v1_pb2.V1CreateSplitRestrictionsResponse:
        return self._grpc_request(request=request, request_method=self.stub.V1CreateSplitRestrictions, **kwargs)
                        
    def v1_update_split_restrictions(self, request: system_v1_pb2.V1UpdateSplitRestrictionsRequest, **kwargs) -> system_v1_pb2.V1UpdateSplitRestrictionsResponse:
        return self._grpc_request(request=request, request_method=self.stub.V1UpdateSplitRestrictions, **kwargs)
                        