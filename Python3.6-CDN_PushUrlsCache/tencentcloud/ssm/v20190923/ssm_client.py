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
from taifucloudcloud.ssm.v20190923 import models


class SsmClient(AbstractClient):
    _apiVersion = '2019-09-23'
    _endpoint = 'ssm.taifucloudcloudapi.com'


    def CreateSecret(self, request):
        """創建新的憑據訊息，通過KMS進行加密保護。每個Region最多可創建儲存1000個憑據訊息。

        :param request: Request instance for CreateSecret.
        :type request: :class:`taifucloudcloud.ssm.v20190923.models.CreateSecretRequest`
        :rtype: :class:`taifucloudcloud.ssm.v20190923.models.CreateSecretResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateSecret", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateSecretResponse()
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


    def DeleteSecret(self, request):
        """删除指定的憑據訊息，可以通過RecoveryWindowInDays參數設置立即删除或者計劃删除。對於計劃删除的憑據，在删除日期到達之前狀态爲 PendingDelete，並可以通過RestoreSecret 進行恢複，超出指定删除日期之後會被徹底删除。您必須先通過 DisableSecret 停用憑據後才可以進行（計劃）删除操作。

        :param request: Request instance for DeleteSecret.
        :type request: :class:`taifucloudcloud.ssm.v20190923.models.DeleteSecretRequest`
        :rtype: :class:`taifucloudcloud.ssm.v20190923.models.DeleteSecretResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteSecret", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteSecretResponse()
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


    def DeleteSecretVersion(self, request):
        """該介面用於直接删除指定憑據下的單個版本憑據，删除操作立即生效，對所有狀态下的憑據版本都可以删除。

        :param request: Request instance for DeleteSecretVersion.
        :type request: :class:`taifucloudcloud.ssm.v20190923.models.DeleteSecretVersionRequest`
        :rtype: :class:`taifucloudcloud.ssm.v20190923.models.DeleteSecretVersionResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteSecretVersion", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteSecretVersionResponse()
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


    def DescribeSecret(self, request):
        """獲取憑據的詳細屬性訊息。

        :param request: Request instance for DescribeSecret.
        :type request: :class:`taifucloudcloud.ssm.v20190923.models.DescribeSecretRequest`
        :rtype: :class:`taifucloudcloud.ssm.v20190923.models.DescribeSecretResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeSecret", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeSecretResponse()
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


    def DisableSecret(self, request):
        """停用指定的憑據，停用後狀态爲 Disabled，無法通過介面獲取該憑據的明文。

        :param request: Request instance for DisableSecret.
        :type request: :class:`taifucloudcloud.ssm.v20190923.models.DisableSecretRequest`
        :rtype: :class:`taifucloudcloud.ssm.v20190923.models.DisableSecretResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DisableSecret", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DisableSecretResponse()
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


    def EnableSecret(self, request):
        """該介面用於開啓憑據，狀态爲Enabled。可以通過 GetSecretValue 介面獲取憑據明文。處於PendingDelete狀态的憑據不能直接開啓，需要通過RestoreSecret 恢複後再開啓使用。

        :param request: Request instance for EnableSecret.
        :type request: :class:`taifucloudcloud.ssm.v20190923.models.EnableSecretRequest`
        :rtype: :class:`taifucloudcloud.ssm.v20190923.models.EnableSecretResponse`

        """
        try:
            params = request._serialize()
            body = self.call("EnableSecret", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.EnableSecretResponse()
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


    def GetRegions(self, request):
        """獲取控制台展示region清單

        :param request: Request instance for GetRegions.
        :type request: :class:`taifucloudcloud.ssm.v20190923.models.GetRegionsRequest`
        :rtype: :class:`taifucloudcloud.ssm.v20190923.models.GetRegionsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GetRegions", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetRegionsResponse()
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


    def GetSecretValue(self, request):
        """獲取指定憑據名稱和版本的憑據明文訊息，只能獲取啓用狀态的憑據明文。

        :param request: Request instance for GetSecretValue.
        :type request: :class:`taifucloudcloud.ssm.v20190923.models.GetSecretValueRequest`
        :rtype: :class:`taifucloudcloud.ssm.v20190923.models.GetSecretValueResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GetSecretValue", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetSecretValueResponse()
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


    def GetServiceStatus(self, request):
        """該介面用戶獲取用戶SecretsManager服務開通狀态。

        :param request: Request instance for GetServiceStatus.
        :type request: :class:`taifucloudcloud.ssm.v20190923.models.GetServiceStatusRequest`
        :rtype: :class:`taifucloudcloud.ssm.v20190923.models.GetServiceStatusResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GetServiceStatus", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetServiceStatusResponse()
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


    def ListSecretVersionIds(self, request):
        """該介面用於獲取指定憑據下的版本清單訊息

        :param request: Request instance for ListSecretVersionIds.
        :type request: :class:`taifucloudcloud.ssm.v20190923.models.ListSecretVersionIdsRequest`
        :rtype: :class:`taifucloudcloud.ssm.v20190923.models.ListSecretVersionIdsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ListSecretVersionIds", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ListSecretVersionIdsResponse()
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


    def ListSecrets(self, request):
        """該介面用於獲取所有憑據的詳細清單，可以指定過濾欄位、排序方式等。

        :param request: Request instance for ListSecrets.
        :type request: :class:`taifucloudcloud.ssm.v20190923.models.ListSecretsRequest`
        :rtype: :class:`taifucloudcloud.ssm.v20190923.models.ListSecretsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ListSecrets", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ListSecretsResponse()
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


    def PutSecretValue(self, request):
        """該介面在指定名稱的憑據下增加新版本的憑據内容，一個憑據下最多可以支援10個版本。只能對處於Enabled 和 Disabled 狀态的憑據添加新的版本。

        :param request: Request instance for PutSecretValue.
        :type request: :class:`taifucloudcloud.ssm.v20190923.models.PutSecretValueRequest`
        :rtype: :class:`taifucloudcloud.ssm.v20190923.models.PutSecretValueResponse`

        """
        try:
            params = request._serialize()
            body = self.call("PutSecretValue", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.PutSecretValueResponse()
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


    def RestoreSecret(self, request):
        """該介面用於恢複計劃删除（PendingDelete狀态）中的憑據，取消計劃删除。取消計劃删除的憑據将處於Disabled 狀态，如需恢複使用，通過EnableSecret 介面開啓憑據。

        :param request: Request instance for RestoreSecret.
        :type request: :class:`taifucloudcloud.ssm.v20190923.models.RestoreSecretRequest`
        :rtype: :class:`taifucloudcloud.ssm.v20190923.models.RestoreSecretResponse`

        """
        try:
            params = request._serialize()
            body = self.call("RestoreSecret", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RestoreSecretResponse()
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


    def UpdateDescription(self, request):
        """該介面用於修改指定憑據的描述訊息，僅能修改Enabled 和 Disabled 狀态的憑據。

        :param request: Request instance for UpdateDescription.
        :type request: :class:`taifucloudcloud.ssm.v20190923.models.UpdateDescriptionRequest`
        :rtype: :class:`taifucloudcloud.ssm.v20190923.models.UpdateDescriptionResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UpdateDescription", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpdateDescriptionResponse()
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


    def UpdateSecret(self, request):
        """該介面用於更新指定憑據名稱和版本號的内容，調用該介面會對新的憑據内容加密後函蓋舊的内容。僅允許更新Enabled 和 Disabled 狀态的憑據。

        :param request: Request instance for UpdateSecret.
        :type request: :class:`taifucloudcloud.ssm.v20190923.models.UpdateSecretRequest`
        :rtype: :class:`taifucloudcloud.ssm.v20190923.models.UpdateSecretResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UpdateSecret", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpdateSecretResponse()
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