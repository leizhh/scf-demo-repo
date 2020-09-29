# -*- coding: utf8 -*-
# Copyright (c) 2017-2018 THL A29 Limited, a Tencent company. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import json

from taifucloudcloud.common.exception.taifucloud_cloud_sdk_exception import TencentCloudSDKException
from taifucloudcloud.common.abstract_client import AbstractClient
from taifucloudcloud.cam.v20190116 import models


class CamClient(AbstractClient):
    _apiVersion = '2019-01-16'
    _endpoint = 'cam.taifucloudcloudapi.com'


    def AddUser(self, request):
        """添加子用戶

        :param request: Request instance for AddUser.
        :type request: :class:`taifucloudcloud.cam.v20190116.models.AddUserRequest`
        :rtype: :class:`taifucloudcloud.cam.v20190116.models.AddUserResponse`

        """
        try:
            params = request._serialize()
            body = self.call("AddUser", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AddUserResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def AddUserToGroup(self, request):
        """用戶加入到用戶組

        :param request: Request instance for AddUserToGroup.
        :type request: :class:`taifucloudcloud.cam.v20190116.models.AddUserToGroupRequest`
        :rtype: :class:`taifucloudcloud.cam.v20190116.models.AddUserToGroupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("AddUserToGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AddUserToGroupResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def AttachGroupPolicy(self, request):
        """本介面（AttachGroupPolicy）可用於綁定策略到用戶組。

        :param request: Request instance for AttachGroupPolicy.
        :type request: :class:`taifucloudcloud.cam.v20190116.models.AttachGroupPolicyRequest`
        :rtype: :class:`taifucloudcloud.cam.v20190116.models.AttachGroupPolicyResponse`

        """
        try:
            params = request._serialize()
            body = self.call("AttachGroupPolicy", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AttachGroupPolicyResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def AttachRolePolicy(self, request):
        """本介面（AttachRolePolicy）用於綁定策略到角色。

        :param request: Request instance for AttachRolePolicy.
        :type request: :class:`taifucloudcloud.cam.v20190116.models.AttachRolePolicyRequest`
        :rtype: :class:`taifucloudcloud.cam.v20190116.models.AttachRolePolicyResponse`

        """
        try:
            params = request._serialize()
            body = self.call("AttachRolePolicy", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AttachRolePolicyResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def AttachUserPolicy(self, request):
        """本介面（AttachUserPolicy）可用於綁定到用戶的策略。

        :param request: Request instance for AttachUserPolicy.
        :type request: :class:`taifucloudcloud.cam.v20190116.models.AttachUserPolicyRequest`
        :rtype: :class:`taifucloudcloud.cam.v20190116.models.AttachUserPolicyResponse`

        """
        try:
            params = request._serialize()
            body = self.call("AttachUserPolicy", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AttachUserPolicyResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ConsumeCustomMFAToken(self, request):
        """驗證自定義多因子Token

        :param request: Request instance for ConsumeCustomMFAToken.
        :type request: :class:`taifucloudcloud.cam.v20190116.models.ConsumeCustomMFATokenRequest`
        :rtype: :class:`taifucloudcloud.cam.v20190116.models.ConsumeCustomMFATokenResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ConsumeCustomMFAToken", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ConsumeCustomMFATokenResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateGroup(self, request):
        """創建用戶組

        :param request: Request instance for CreateGroup.
        :type request: :class:`taifucloudcloud.cam.v20190116.models.CreateGroupRequest`
        :rtype: :class:`taifucloudcloud.cam.v20190116.models.CreateGroupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateGroupResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreatePolicy(self, request):
        """本介面（CreatePolicy）可用於創建策略。

        :param request: Request instance for CreatePolicy.
        :type request: :class:`taifucloudcloud.cam.v20190116.models.CreatePolicyRequest`
        :rtype: :class:`taifucloudcloud.cam.v20190116.models.CreatePolicyResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreatePolicy", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreatePolicyResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreatePolicyVersion(self, request):
        """該介面（CreatePolicyVersion）用於新增策略版本，用戶創建了一個策略版本之後可以方便的通過變更策略版本的方式來變更策略。

        :param request: Request instance for CreatePolicyVersion.
        :type request: :class:`taifucloudcloud.cam.v20190116.models.CreatePolicyVersionRequest`
        :rtype: :class:`taifucloudcloud.cam.v20190116.models.CreatePolicyVersionResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreatePolicyVersion", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreatePolicyVersionResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateRole(self, request):
        """本介面（CreateRole）用於創建角色。

        :param request: Request instance for CreateRole.
        :type request: :class:`taifucloudcloud.cam.v20190116.models.CreateRoleRequest`
        :rtype: :class:`taifucloudcloud.cam.v20190116.models.CreateRoleResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateRole", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateRoleResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateSAMLProvider(self, request):
        """創建SAML身份提供商

        :param request: Request instance for CreateSAMLProvider.
        :type request: :class:`taifucloudcloud.cam.v20190116.models.CreateSAMLProviderRequest`
        :rtype: :class:`taifucloudcloud.cam.v20190116.models.CreateSAMLProviderResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateSAMLProvider", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateSAMLProviderResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateServiceLinkedRole(self, request):
        """創建服務相關角色

        :param request: Request instance for CreateServiceLinkedRole.
        :type request: :class:`taifucloudcloud.cam.v20190116.models.CreateServiceLinkedRoleRequest`
        :rtype: :class:`taifucloudcloud.cam.v20190116.models.CreateServiceLinkedRoleResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateServiceLinkedRole", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateServiceLinkedRoleResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteGroup(self, request):
        """删除用戶組

        :param request: Request instance for DeleteGroup.
        :type request: :class:`taifucloudcloud.cam.v20190116.models.DeleteGroupRequest`
        :rtype: :class:`taifucloudcloud.cam.v20190116.models.DeleteGroupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteGroupResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeletePolicy(self, request):
        """本介面（DeletePolicy）可用於删除策略。

        :param request: Request instance for DeletePolicy.
        :type request: :class:`taifucloudcloud.cam.v20190116.models.DeletePolicyRequest`
        :rtype: :class:`taifucloudcloud.cam.v20190116.models.DeletePolicyResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeletePolicy", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeletePolicyResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeletePolicyVersion(self, request):
        """本介面（DeletePolicyVersion）可用於删除一個策略的策略版本。

        :param request: Request instance for DeletePolicyVersion.
        :type request: :class:`taifucloudcloud.cam.v20190116.models.DeletePolicyVersionRequest`
        :rtype: :class:`taifucloudcloud.cam.v20190116.models.DeletePolicyVersionResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeletePolicyVersion", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeletePolicyVersionResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteRole(self, request):
        """本介面（DeleteRole）用於删除指定角色。

        :param request: Request instance for DeleteRole.
        :type request: :class:`taifucloudcloud.cam.v20190116.models.DeleteRoleRequest`
        :rtype: :class:`taifucloudcloud.cam.v20190116.models.DeleteRoleResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteRole", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteRoleResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteSAMLProvider(self, request):
        """删除SAML身份提供商

        :param request: Request instance for DeleteSAMLProvider.
        :type request: :class:`taifucloudcloud.cam.v20190116.models.DeleteSAMLProviderRequest`
        :rtype: :class:`taifucloudcloud.cam.v20190116.models.DeleteSAMLProviderResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteSAMLProvider", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteSAMLProviderResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteServiceLinkedRole(self, request):
        """删除服務相關角色

        :param request: Request instance for DeleteServiceLinkedRole.
        :type request: :class:`taifucloudcloud.cam.v20190116.models.DeleteServiceLinkedRoleRequest`
        :rtype: :class:`taifucloudcloud.cam.v20190116.models.DeleteServiceLinkedRoleResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteServiceLinkedRole", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteServiceLinkedRoleResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteUser(self, request):
        """删除子用戶

        :param request: Request instance for DeleteUser.
        :type request: :class:`taifucloudcloud.cam.v20190116.models.DeleteUserRequest`
        :rtype: :class:`taifucloudcloud.cam.v20190116.models.DeleteUserResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteUser", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteUserResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeRoleList(self, request):
        """本介面（DescribeRoleList）用於獲取賬號下的角色清單。

        :param request: Request instance for DescribeRoleList.
        :type request: :class:`taifucloudcloud.cam.v20190116.models.DescribeRoleListRequest`
        :rtype: :class:`taifucloudcloud.cam.v20190116.models.DescribeRoleListResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeRoleList", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeRoleListResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DetachGroupPolicy(self, request):
        """本介面（DetachGroupPolicy）可用於解除綁定到用戶組的策略。

        :param request: Request instance for DetachGroupPolicy.
        :type request: :class:`taifucloudcloud.cam.v20190116.models.DetachGroupPolicyRequest`
        :rtype: :class:`taifucloudcloud.cam.v20190116.models.DetachGroupPolicyResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DetachGroupPolicy", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DetachGroupPolicyResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DetachRolePolicy(self, request):
        """本介面（DetachRolePolicy）用於解除綁定角色的策略。

        :param request: Request instance for DetachRolePolicy.
        :type request: :class:`taifucloudcloud.cam.v20190116.models.DetachRolePolicyRequest`
        :rtype: :class:`taifucloudcloud.cam.v20190116.models.DetachRolePolicyResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DetachRolePolicy", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DetachRolePolicyResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DetachUserPolicy(self, request):
        """本介面（DetachUserPolicy）可用於解除綁定到用戶的策略。

        :param request: Request instance for DetachUserPolicy.
        :type request: :class:`taifucloudcloud.cam.v20190116.models.DetachUserPolicyRequest`
        :rtype: :class:`taifucloudcloud.cam.v20190116.models.DetachUserPolicyResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DetachUserPolicy", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DetachUserPolicyResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def GetCustomMFATokenInfo(self, request):
        """獲取自定義多因子Token關聯訊息

        :param request: Request instance for GetCustomMFATokenInfo.
        :type request: :class:`taifucloudcloud.cam.v20190116.models.GetCustomMFATokenInfoRequest`
        :rtype: :class:`taifucloudcloud.cam.v20190116.models.GetCustomMFATokenInfoResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GetCustomMFATokenInfo", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetCustomMFATokenInfoResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def GetGroup(self, request):
        """查詢用戶組詳情

        :param request: Request instance for GetGroup.
        :type request: :class:`taifucloudcloud.cam.v20190116.models.GetGroupRequest`
        :rtype: :class:`taifucloudcloud.cam.v20190116.models.GetGroupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GetGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetGroupResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def GetPolicy(self, request):
        """本介面（GetPolicy）可用於查詢檢視策略詳情。

        :param request: Request instance for GetPolicy.
        :type request: :class:`taifucloudcloud.cam.v20190116.models.GetPolicyRequest`
        :rtype: :class:`taifucloudcloud.cam.v20190116.models.GetPolicyResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GetPolicy", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetPolicyResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def GetPolicyVersion(self, request):
        """該介面（GetPolicyVersion）用於查詢策略版本詳情

        :param request: Request instance for GetPolicyVersion.
        :type request: :class:`taifucloudcloud.cam.v20190116.models.GetPolicyVersionRequest`
        :rtype: :class:`taifucloudcloud.cam.v20190116.models.GetPolicyVersionResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GetPolicyVersion", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetPolicyVersionResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def GetRole(self, request):
        """本介面（GetRole）用於獲取指定角色的詳細訊息。

        :param request: Request instance for GetRole.
        :type request: :class:`taifucloudcloud.cam.v20190116.models.GetRoleRequest`
        :rtype: :class:`taifucloudcloud.cam.v20190116.models.GetRoleResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GetRole", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetRoleResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def GetSAMLProvider(self, request):
        """查詢SAML身份提供商詳情

        :param request: Request instance for GetSAMLProvider.
        :type request: :class:`taifucloudcloud.cam.v20190116.models.GetSAMLProviderRequest`
        :rtype: :class:`taifucloudcloud.cam.v20190116.models.GetSAMLProviderResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GetSAMLProvider", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetSAMLProviderResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def GetServiceLinkedRoleDeletionStatus(self, request):
        """根據删除TaskId獲取服務相關角色删除狀态

        :param request: Request instance for GetServiceLinkedRoleDeletionStatus.
        :type request: :class:`taifucloudcloud.cam.v20190116.models.GetServiceLinkedRoleDeletionStatusRequest`
        :rtype: :class:`taifucloudcloud.cam.v20190116.models.GetServiceLinkedRoleDeletionStatusResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GetServiceLinkedRoleDeletionStatus", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetServiceLinkedRoleDeletionStatusResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def GetUser(self, request):
        """查詢子用戶

        :param request: Request instance for GetUser.
        :type request: :class:`taifucloudcloud.cam.v20190116.models.GetUserRequest`
        :rtype: :class:`taifucloudcloud.cam.v20190116.models.GetUserResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GetUser", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetUserResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ListAttachedGroupPolicies(self, request):
        """本介面（ListAttachedGroupPolicies）可用於查詢用戶組關聯的策略清單。

        :param request: Request instance for ListAttachedGroupPolicies.
        :type request: :class:`taifucloudcloud.cam.v20190116.models.ListAttachedGroupPoliciesRequest`
        :rtype: :class:`taifucloudcloud.cam.v20190116.models.ListAttachedGroupPoliciesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ListAttachedGroupPolicies", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ListAttachedGroupPoliciesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ListAttachedRolePolicies(self, request):
        """本介面（ListAttachedRolePolicies）用於獲取角色綁定的策略清單。

        :param request: Request instance for ListAttachedRolePolicies.
        :type request: :class:`taifucloudcloud.cam.v20190116.models.ListAttachedRolePoliciesRequest`
        :rtype: :class:`taifucloudcloud.cam.v20190116.models.ListAttachedRolePoliciesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ListAttachedRolePolicies", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ListAttachedRolePoliciesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ListAttachedUserPolicies(self, request):
        """本介面（ListAttachedUserPolicies）可用於查詢子賬號關聯的策略清單。

        :param request: Request instance for ListAttachedUserPolicies.
        :type request: :class:`taifucloudcloud.cam.v20190116.models.ListAttachedUserPoliciesRequest`
        :rtype: :class:`taifucloudcloud.cam.v20190116.models.ListAttachedUserPoliciesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ListAttachedUserPolicies", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ListAttachedUserPoliciesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ListCollaborators(self, request):
        """獲取協作者清單

        :param request: Request instance for ListCollaborators.
        :type request: :class:`taifucloudcloud.cam.v20190116.models.ListCollaboratorsRequest`
        :rtype: :class:`taifucloudcloud.cam.v20190116.models.ListCollaboratorsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ListCollaborators", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ListCollaboratorsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ListEntitiesForPolicy(self, request):
        """本介面（ListEntitiesForPolicy）可用於查詢策略關聯的實體清單。

        :param request: Request instance for ListEntitiesForPolicy.
        :type request: :class:`taifucloudcloud.cam.v20190116.models.ListEntitiesForPolicyRequest`
        :rtype: :class:`taifucloudcloud.cam.v20190116.models.ListEntitiesForPolicyResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ListEntitiesForPolicy", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ListEntitiesForPolicyResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ListGroups(self, request):
        """查詢用戶組清單

        :param request: Request instance for ListGroups.
        :type request: :class:`taifucloudcloud.cam.v20190116.models.ListGroupsRequest`
        :rtype: :class:`taifucloudcloud.cam.v20190116.models.ListGroupsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ListGroups", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ListGroupsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ListGroupsForUser(self, request):
        """列出用戶關聯的用戶組

        :param request: Request instance for ListGroupsForUser.
        :type request: :class:`taifucloudcloud.cam.v20190116.models.ListGroupsForUserRequest`
        :rtype: :class:`taifucloudcloud.cam.v20190116.models.ListGroupsForUserResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ListGroupsForUser", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ListGroupsForUserResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ListPolicies(self, request):
        """本介面（ListPolicies）可用於查詢策略清單。

        :param request: Request instance for ListPolicies.
        :type request: :class:`taifucloudcloud.cam.v20190116.models.ListPoliciesRequest`
        :rtype: :class:`taifucloudcloud.cam.v20190116.models.ListPoliciesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ListPolicies", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ListPoliciesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ListPolicyVersions(self, request):
        """該介面（ListPolicyVersions）用於獲取策略版本清單

        :param request: Request instance for ListPolicyVersions.
        :type request: :class:`taifucloudcloud.cam.v20190116.models.ListPolicyVersionsRequest`
        :rtype: :class:`taifucloudcloud.cam.v20190116.models.ListPolicyVersionsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ListPolicyVersions", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ListPolicyVersionsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ListSAMLProviders(self, request):
        """查詢SAML身份提供商清單

        :param request: Request instance for ListSAMLProviders.
        :type request: :class:`taifucloudcloud.cam.v20190116.models.ListSAMLProvidersRequest`
        :rtype: :class:`taifucloudcloud.cam.v20190116.models.ListSAMLProvidersResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ListSAMLProviders", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ListSAMLProvidersResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ListUsers(self, request):
        """拉取子用戶

        :param request: Request instance for ListUsers.
        :type request: :class:`taifucloudcloud.cam.v20190116.models.ListUsersRequest`
        :rtype: :class:`taifucloudcloud.cam.v20190116.models.ListUsersResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ListUsers", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ListUsersResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ListUsersForGroup(self, request):
        """查詢用戶組關聯的用戶清單

        :param request: Request instance for ListUsersForGroup.
        :type request: :class:`taifucloudcloud.cam.v20190116.models.ListUsersForGroupRequest`
        :rtype: :class:`taifucloudcloud.cam.v20190116.models.ListUsersForGroupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ListUsersForGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ListUsersForGroupResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def RemoveUserFromGroup(self, request):
        """從用戶組删除用戶

        :param request: Request instance for RemoveUserFromGroup.
        :type request: :class:`taifucloudcloud.cam.v20190116.models.RemoveUserFromGroupRequest`
        :rtype: :class:`taifucloudcloud.cam.v20190116.models.RemoveUserFromGroupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("RemoveUserFromGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RemoveUserFromGroupResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def SetDefaultPolicyVersion(self, request):
        """本介面（SetDefaultPolicyVersion）可用於設置生效的策略版本。

        :param request: Request instance for SetDefaultPolicyVersion.
        :type request: :class:`taifucloudcloud.cam.v20190116.models.SetDefaultPolicyVersionRequest`
        :rtype: :class:`taifucloudcloud.cam.v20190116.models.SetDefaultPolicyVersionResponse`

        """
        try:
            params = request._serialize()
            body = self.call("SetDefaultPolicyVersion", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.SetDefaultPolicyVersionResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def UpdateAssumeRolePolicy(self, request):
        """本介面（UpdateAssumeRolePolicy）用於修改角色信任策略的策略文件。

        :param request: Request instance for UpdateAssumeRolePolicy.
        :type request: :class:`taifucloudcloud.cam.v20190116.models.UpdateAssumeRolePolicyRequest`
        :rtype: :class:`taifucloudcloud.cam.v20190116.models.UpdateAssumeRolePolicyResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UpdateAssumeRolePolicy", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpdateAssumeRolePolicyResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def UpdateGroup(self, request):
        """更新用戶組

        :param request: Request instance for UpdateGroup.
        :type request: :class:`taifucloudcloud.cam.v20190116.models.UpdateGroupRequest`
        :rtype: :class:`taifucloudcloud.cam.v20190116.models.UpdateGroupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UpdateGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpdateGroupResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def UpdatePolicy(self, request):
        """本介面（UpdatePolicy ）可用於更新策略。
        如果已存在策略版本，本介面會直接更新策略的預設版本，不會創建新版本，如果不存在任何策略版本，則直接創建一個預設版本。

        :param request: Request instance for UpdatePolicy.
        :type request: :class:`taifucloudcloud.cam.v20190116.models.UpdatePolicyRequest`
        :rtype: :class:`taifucloudcloud.cam.v20190116.models.UpdatePolicyResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UpdatePolicy", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpdatePolicyResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def UpdateRoleConsoleLogin(self, request):
        """本介面（UpdateRoleConsoleLogin）用於修改角色是否可登入。

        :param request: Request instance for UpdateRoleConsoleLogin.
        :type request: :class:`taifucloudcloud.cam.v20190116.models.UpdateRoleConsoleLoginRequest`
        :rtype: :class:`taifucloudcloud.cam.v20190116.models.UpdateRoleConsoleLoginResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UpdateRoleConsoleLogin", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpdateRoleConsoleLoginResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def UpdateRoleDescription(self, request):
        """本介面（UpdateRoleDescription）用於修改角色的描述訊息。

        :param request: Request instance for UpdateRoleDescription.
        :type request: :class:`taifucloudcloud.cam.v20190116.models.UpdateRoleDescriptionRequest`
        :rtype: :class:`taifucloudcloud.cam.v20190116.models.UpdateRoleDescriptionResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UpdateRoleDescription", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpdateRoleDescriptionResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def UpdateSAMLProvider(self, request):
        """更新SAML身份提供商訊息

        :param request: Request instance for UpdateSAMLProvider.
        :type request: :class:`taifucloudcloud.cam.v20190116.models.UpdateSAMLProviderRequest`
        :rtype: :class:`taifucloudcloud.cam.v20190116.models.UpdateSAMLProviderResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UpdateSAMLProvider", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpdateSAMLProviderResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def UpdateUser(self, request):
        """更新子用戶

        :param request: Request instance for UpdateUser.
        :type request: :class:`taifucloudcloud.cam.v20190116.models.UpdateUserRequest`
        :rtype: :class:`taifucloudcloud.cam.v20190116.models.UpdateUserResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UpdateUser", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpdateUserResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)