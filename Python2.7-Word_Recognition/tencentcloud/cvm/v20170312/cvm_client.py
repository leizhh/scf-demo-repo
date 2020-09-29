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
from taifucloudcloud.cvm.v20170312 import models


class CvmClient(AbstractClient):
    _apiVersion = '2017-03-12'
    _endpoint = 'cvm.taifucloudcloudapi.com'


    def AllocateHosts(self, request):
        """本介面 (AllocateHosts) 用於創建一個或多個指定配置的CDH實例。
        * 當HostChargeType爲PREPAID時，必須指定HostChargePrepaid參數。

        :param request: 調用AllocateHosts所需參數的結構體。
        :type request: :class:`taifucloudcloud.cvm.v20170312.models.AllocateHostsRequest`
        :rtype: :class:`taifucloudcloud.cvm.v20170312.models.AllocateHostsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("AllocateHosts", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AllocateHostsResponse()
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


    def AssociateInstancesKeyPairs(self, request):
        """本介面 (AssociateInstancesKeyPairs) 用於将金鑰綁定到實例上。

        * 将金鑰的公鑰寫入到實例的`SSH`配置當中，用戶就可以通過該金鑰的私鑰來登入實例。
        * 如果實例原來綁定過金鑰，那麽原來的金鑰将失效。
        * 如果實例原來是通過密碼登入，綁定金鑰後無法使用密碼登入。
        * 支援批次操作。每次請求批次實例的上限爲100。如果批次實例存在不允許操作的實例，操作會以特定錯誤碼返回。

        :param request: 調用AssociateInstancesKeyPairs所需參數的結構體。
        :type request: :class:`taifucloudcloud.cvm.v20170312.models.AssociateInstancesKeyPairsRequest`
        :rtype: :class:`taifucloudcloud.cvm.v20170312.models.AssociateInstancesKeyPairsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("AssociateInstancesKeyPairs", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AssociateInstancesKeyPairsResponse()
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


    def AssociateSecurityGroups(self, request):
        """本介面 (AssociateSecurityGroups) 用於綁定安全組到指定實例。

        :param request: 調用AssociateSecurityGroups所需參數的結構體。
        :type request: :class:`taifucloudcloud.cvm.v20170312.models.AssociateSecurityGroupsRequest`
        :rtype: :class:`taifucloudcloud.cvm.v20170312.models.AssociateSecurityGroupsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("AssociateSecurityGroups", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AssociateSecurityGroupsResponse()
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


    def CreateDisasterRecoverGroup(self, request):
        """本介面 (CreateDisasterRecoverGroup)用於創建[分散置放群組](https://cloud.taifucloud.com/document/product/213/15486)。創建好的置放群組，可在[創建實例](https://cloud.taifucloud.com/document/api/213/15730)時指定。

        :param request: 調用CreateDisasterRecoverGroup所需參數的結構體。
        :type request: :class:`taifucloudcloud.cvm.v20170312.models.CreateDisasterRecoverGroupRequest`
        :rtype: :class:`taifucloudcloud.cvm.v20170312.models.CreateDisasterRecoverGroupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateDisasterRecoverGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateDisasterRecoverGroupResponse()
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


    def CreateImage(self, request):
        """本介面(CreateImage)用於将實例的系統盤制作爲新映像，創建後的映像可以用於創建實例。

        :param request: 調用CreateImage所需參數的結構體。
        :type request: :class:`taifucloudcloud.cvm.v20170312.models.CreateImageRequest`
        :rtype: :class:`taifucloudcloud.cvm.v20170312.models.CreateImageResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateImage", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateImageResponse()
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


    def CreateKeyPair(self, request):
        """本介面 (CreateKeyPair) 用於創建一個 `OpenSSH RSA` 金鑰對，可以用於登入 `Linux` 實例。

        * 開發者只需指定金鑰對名稱，即可由系統自動創建金鑰對，並返回所生成的金鑰對的 `ID` 及其公鑰、私鑰的内容。
        * 金鑰對名稱不能和已經存在的金鑰對的名稱重複。
        * 私鑰的内容可以保存到文件中作爲 `SSH` 的一種認證方式。
        * Top Cloud 不會保存用戶的私鑰，請妥善保管。

        :param request: 調用CreateKeyPair所需參數的結構體。
        :type request: :class:`taifucloudcloud.cvm.v20170312.models.CreateKeyPairRequest`
        :rtype: :class:`taifucloudcloud.cvm.v20170312.models.CreateKeyPairResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateKeyPair", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateKeyPairResponse()
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


    def DeleteDisasterRecoverGroups(self, request):
        """本介面 (DeleteDisasterRecoverGroups)用於删除[分散置放群組](https://cloud.taifucloud.com/document/product/213/15486)。只有空的置放群組才能被删除，非空的群組需要先銷毀組内所有雲主機，才能執行删除操作，不然會産生删除置放群組失敗的錯誤。

        :param request: 調用DeleteDisasterRecoverGroups所需參數的結構體。
        :type request: :class:`taifucloudcloud.cvm.v20170312.models.DeleteDisasterRecoverGroupsRequest`
        :rtype: :class:`taifucloudcloud.cvm.v20170312.models.DeleteDisasterRecoverGroupsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteDisasterRecoverGroups", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteDisasterRecoverGroupsResponse()
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


    def DeleteImages(self, request):
        """本介面（DeleteImages）用於删除一個或多個映像。

        * 當[映像狀态](https://cloud.taifucloud.com/document/api/213/9452#image_state)爲`創建中`和`使用中`時, 不允許删除。映像狀态可以通過[DescribeImages](https://cloud.taifucloud.com/document/api/213/9418)獲取。
        * 每個地域最多只支援創建10個自定義映像，删除映像可以釋放帳戶的配額。
        * 當映像正在被其它帳戶分享時，不允許删除。

        :param request: 調用DeleteImages所需參數的結構體。
        :type request: :class:`taifucloudcloud.cvm.v20170312.models.DeleteImagesRequest`
        :rtype: :class:`taifucloudcloud.cvm.v20170312.models.DeleteImagesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteImages", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteImagesResponse()
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


    def DeleteKeyPairs(self, request):
        """本介面 (DeleteKeyPairs) 用於删除已在Top Cloud 托管的金鑰對。

        * 可以同時删除多個金鑰對。
        * 不能删除已被實例或映像引用的金鑰對，所以需要獨立判斷是否所有金鑰對都被成功删除。

        :param request: 調用DeleteKeyPairs所需參數的結構體。
        :type request: :class:`taifucloudcloud.cvm.v20170312.models.DeleteKeyPairsRequest`
        :rtype: :class:`taifucloudcloud.cvm.v20170312.models.DeleteKeyPairsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteKeyPairs", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteKeyPairsResponse()
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


    def DescribeDisasterRecoverGroupQuota(self, request):
        """本介面 (DescribeDisasterRecoverGroupQuota)用於查詢[分散置放群組](https://cloud.taifucloud.com/document/product/213/15486)配額。

        :param request: 調用DescribeDisasterRecoverGroupQuota所需參數的結構體。
        :type request: :class:`taifucloudcloud.cvm.v20170312.models.DescribeDisasterRecoverGroupQuotaRequest`
        :rtype: :class:`taifucloudcloud.cvm.v20170312.models.DescribeDisasterRecoverGroupQuotaResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDisasterRecoverGroupQuota", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDisasterRecoverGroupQuotaResponse()
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


    def DescribeDisasterRecoverGroups(self, request):
        """本介面 (DescribeDisasterRecoverGroups)用於查詢[分散置放群組](https://cloud.taifucloud.com/document/product/213/15486)訊息。

        :param request: 調用DescribeDisasterRecoverGroups所需參數的結構體。
        :type request: :class:`taifucloudcloud.cvm.v20170312.models.DescribeDisasterRecoverGroupsRequest`
        :rtype: :class:`taifucloudcloud.cvm.v20170312.models.DescribeDisasterRecoverGroupsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDisasterRecoverGroups", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDisasterRecoverGroupsResponse()
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


    def DescribeHosts(self, request):
        """本介面 (DescribeHosts) 用於獲取一個或多個CDH實例的詳細訊息。

        :param request: 調用DescribeHosts所需參數的結構體。
        :type request: :class:`taifucloudcloud.cvm.v20170312.models.DescribeHostsRequest`
        :rtype: :class:`taifucloudcloud.cvm.v20170312.models.DescribeHostsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeHosts", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeHostsResponse()
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


    def DescribeImageQuota(self, request):
        """本介面(DescribeImageQuota)用於查詢用戶帳號的映像配額。

        :param request: 調用DescribeImageQuota所需參數的結構體。
        :type request: :class:`taifucloudcloud.cvm.v20170312.models.DescribeImageQuotaRequest`
        :rtype: :class:`taifucloudcloud.cvm.v20170312.models.DescribeImageQuotaResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeImageQuota", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeImageQuotaResponse()
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


    def DescribeImageSharePermission(self, request):
        """本介面（DescribeImageSharePermission）用於查詢映像分享訊息。

        :param request: 調用DescribeImageSharePermission所需參數的結構體。
        :type request: :class:`taifucloudcloud.cvm.v20170312.models.DescribeImageSharePermissionRequest`
        :rtype: :class:`taifucloudcloud.cvm.v20170312.models.DescribeImageSharePermissionResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeImageSharePermission", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeImageSharePermissionResponse()
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


    def DescribeImages(self, request):
        """本介面(DescribeImages) 用於檢視映像清單。

        * 可以通過指定映像ID來查詢指定映像的詳細訊息，或通過設定過濾器來查詢滿足過濾條件的映像的詳細訊息。
        * 指定偏移(Offset)和限制(Limit)來選擇結果中的一部分，預設返回滿足條件的前20個映像訊息。

        :param request: 調用DescribeImages所需參數的結構體。
        :type request: :class:`taifucloudcloud.cvm.v20170312.models.DescribeImagesRequest`
        :rtype: :class:`taifucloudcloud.cvm.v20170312.models.DescribeImagesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeImages", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeImagesResponse()
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


    def DescribeImportImageOs(self, request):
        """檢視可以導入的映像作業系統訊息。

        :param request: 調用DescribeImportImageOs所需參數的結構體。
        :type request: :class:`taifucloudcloud.cvm.v20170312.models.DescribeImportImageOsRequest`
        :rtype: :class:`taifucloudcloud.cvm.v20170312.models.DescribeImportImageOsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeImportImageOs", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeImportImageOsResponse()
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


    def DescribeInstanceFamilyConfigs(self, request):
        """本介面（DescribeInstanceFamilyConfigs）查詢當前用戶和地域所支援的機型族清單訊息。

        :param request: 調用DescribeInstanceFamilyConfigs所需參數的結構體。
        :type request: :class:`taifucloudcloud.cvm.v20170312.models.DescribeInstanceFamilyConfigsRequest`
        :rtype: :class:`taifucloudcloud.cvm.v20170312.models.DescribeInstanceFamilyConfigsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeInstanceFamilyConfigs", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeInstanceFamilyConfigsResponse()
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


    def DescribeInstanceInternetBandwidthConfigs(self, request):
        """本介面 (DescribeInstanceInternetBandwidthConfigs) 用於查詢實例頻寬配置。

        * 只支援查詢`BANDWIDTH_PREPAID`計費模式的頻寬配置。
        * 介面返回實例的所有頻寬配置訊息（包含曆史的頻寬配置訊息）。

        :param request: 調用DescribeInstanceInternetBandwidthConfigs所需參數的結構體。
        :type request: :class:`taifucloudcloud.cvm.v20170312.models.DescribeInstanceInternetBandwidthConfigsRequest`
        :rtype: :class:`taifucloudcloud.cvm.v20170312.models.DescribeInstanceInternetBandwidthConfigsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeInstanceInternetBandwidthConfigs", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeInstanceInternetBandwidthConfigsResponse()
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


    def DescribeInstanceTypeConfigs(self, request):
        """本介面 (DescribeInstanceTypeConfigs) 用於查詢實例機型配置。

        * 可以根據`zone`、`instance-family`來查詢實例機型配置。過濾條件詳見過濾器`Filter`。
        * 如果參數爲空，返回指定地域的所有實例機型配置。

        :param request: 調用DescribeInstanceTypeConfigs所需參數的結構體。
        :type request: :class:`taifucloudcloud.cvm.v20170312.models.DescribeInstanceTypeConfigsRequest`
        :rtype: :class:`taifucloudcloud.cvm.v20170312.models.DescribeInstanceTypeConfigsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeInstanceTypeConfigs", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeInstanceTypeConfigsResponse()
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


    def DescribeInstanceVncUrl(self, request):
        """本介面 ( DescribeInstanceVncUrl ) 用於查詢實例管理終端網址。

        * 處於 `STOPPED` 狀态的機器無法使用此功能。
        * 管理終端網址的有效期爲 15 秒，調用介面成功後如果 15 秒内不使用該連結進行訪問，管理終端網址自動失效，您需要重新查詢。
        * 管理終端網址一旦被訪問，将自動失效，您需要重新查詢。
        * 如果連接斷開，每分鍾内重新連接的次數不能超過 30 次。
        * 獲取到 `InstanceVncUrl` 後，您需要在在連結 <https://img.qcloud.com/qcloud/app/active_vnc/index.html?> 末尾加上參數 `InstanceVncUrl=xxxx`  。
          - 參數 `InstanceVncUrl` ：調用介面成功後會返回的 `InstanceVncUrl` 的值。

            最後組成的 URL 格式如下：

        ```
        https://img.qcloud.com/qcloud/app/active_vnc/index.html?InstanceVncUrl=wss%3A%2F%2Fbjvnc.qcloud.com%3A26789%2Fvnc%3Fs%3DaHpjWnRVMFNhYmxKdDM5MjRHNlVTSVQwajNUSW0wb2tBbmFtREFCTmFrcy8vUUNPMG0wSHZNOUUxRm5PMmUzWmFDcWlOdDJIbUJxSTZDL0RXcHZxYnZZMmRkWWZWcEZia2lyb09XMzdKNmM9
        ```

        :param request: 調用DescribeInstanceVncUrl所需參數的結構體。
        :type request: :class:`taifucloudcloud.cvm.v20170312.models.DescribeInstanceVncUrlRequest`
        :rtype: :class:`taifucloudcloud.cvm.v20170312.models.DescribeInstanceVncUrlResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeInstanceVncUrl", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeInstanceVncUrlResponse()
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


    def DescribeInstances(self, request):
        """本介面 (DescribeInstances) 用於查詢一個或多個實例的詳細訊息。

        * 可以根據實例`ID`、實例名稱或者實例計費模式等訊息來查詢實例的詳細訊息。過濾訊息詳細請見過濾器`Filter`。
        * 如果參數爲空，返回當前用戶一定數量（`Limit`所指定的數量，預設爲20）的實例。

        :param request: 調用DescribeInstances所需參數的結構體。
        :type request: :class:`taifucloudcloud.cvm.v20170312.models.DescribeInstancesRequest`
        :rtype: :class:`taifucloudcloud.cvm.v20170312.models.DescribeInstancesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeInstances", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeInstancesResponse()
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


    def DescribeInstancesOperationLimit(self, request):
        """本介面（DescribeInstancesOperationLimit）用於查詢實例操作限制。

        * 目前支援調整配置操作限制次數查詢。

        :param request: 調用DescribeInstancesOperationLimit所需參數的結構體。
        :type request: :class:`taifucloudcloud.cvm.v20170312.models.DescribeInstancesOperationLimitRequest`
        :rtype: :class:`taifucloudcloud.cvm.v20170312.models.DescribeInstancesOperationLimitResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeInstancesOperationLimit", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeInstancesOperationLimitResponse()
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


    def DescribeInstancesStatus(self, request):
        """本介面 (DescribeInstancesStatus) 用於查詢一個或多個實例的狀态。

        * 可以根據實例`ID`來查詢實例的狀态。
        * 如果參數爲空，返回當前用戶一定數量（Limit所指定的數量，預設爲20）的實例狀态。

        :param request: 調用DescribeInstancesStatus所需參數的結構體。
        :type request: :class:`taifucloudcloud.cvm.v20170312.models.DescribeInstancesStatusRequest`
        :rtype: :class:`taifucloudcloud.cvm.v20170312.models.DescribeInstancesStatusResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeInstancesStatus", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeInstancesStatusResponse()
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


    def DescribeInternetChargeTypeConfigs(self, request):
        """本介面（DescribeInternetChargeTypeConfigs）用於查詢網絡的計費類型。

        :param request: 調用DescribeInternetChargeTypeConfigs所需參數的結構體。
        :type request: :class:`taifucloudcloud.cvm.v20170312.models.DescribeInternetChargeTypeConfigsRequest`
        :rtype: :class:`taifucloudcloud.cvm.v20170312.models.DescribeInternetChargeTypeConfigsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeInternetChargeTypeConfigs", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeInternetChargeTypeConfigsResponse()
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


    def DescribeKeyPairs(self, request):
        """本介面 (DescribeKeyPairs) 用於查詢金鑰對訊息。

        * 金鑰對是通過一種算法生成的一對金鑰，在生成的金鑰對中，一個向外界公開，稱爲公鑰；另一個用戶自己保留，稱爲私鑰。金鑰對的公鑰内容可以通過這個介面查詢，但私鑰内容系統不保留。

        :param request: 調用DescribeKeyPairs所需參數的結構體。
        :type request: :class:`taifucloudcloud.cvm.v20170312.models.DescribeKeyPairsRequest`
        :rtype: :class:`taifucloudcloud.cvm.v20170312.models.DescribeKeyPairsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeKeyPairs", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeKeyPairsResponse()
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


    def DescribeRegions(self, request):
        """本介面(DescribeRegions)用於查詢地域訊息。

        :param request: 調用DescribeRegions所需參數的結構體。
        :type request: :class:`taifucloudcloud.cvm.v20170312.models.DescribeRegionsRequest`
        :rtype: :class:`taifucloudcloud.cvm.v20170312.models.DescribeRegionsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeRegions", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeRegionsResponse()
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


    def DescribeZoneInstanceConfigInfos(self, request):
        """本介面(DescribeZoneInstanceConfigInfos) 獲取可用區的機型訊息。

        :param request: 調用DescribeZoneInstanceConfigInfos所需參數的結構體。
        :type request: :class:`taifucloudcloud.cvm.v20170312.models.DescribeZoneInstanceConfigInfosRequest`
        :rtype: :class:`taifucloudcloud.cvm.v20170312.models.DescribeZoneInstanceConfigInfosResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeZoneInstanceConfigInfos", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeZoneInstanceConfigInfosResponse()
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


    def DescribeZones(self, request):
        """本介面(DescribeZones)用於查詢可用區訊息。

        :param request: 調用DescribeZones所需參數的結構體。
        :type request: :class:`taifucloudcloud.cvm.v20170312.models.DescribeZonesRequest`
        :rtype: :class:`taifucloudcloud.cvm.v20170312.models.DescribeZonesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeZones", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeZonesResponse()
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


    def DisassociateInstancesKeyPairs(self, request):
        """本介面 (DisassociateInstancesKeyPairs) 用於解除實例的金鑰綁定關系。

        * 只支援[`STOPPED`](https://cloud.taifucloud.com/document/api/213/9452#INSTANCE_STATE)狀态的`Linux`作業系統的實例。
        * 解綁金鑰後，實例可以通過原來設置的密碼登入。
        * 如果原來沒有設置密碼，解綁後将無法使用 `SSH` 登入。可以調用 [ResetInstancesPassword](https://cloud.taifucloud.com/document/api/213/15736) 介面來設置登入密碼。
        * 支援批次操作。每次請求批次實例的上限爲100。如果批次實例存在不允許操作的實例，操作會以特定錯誤碼返回。

        :param request: 調用DisassociateInstancesKeyPairs所需參數的結構體。
        :type request: :class:`taifucloudcloud.cvm.v20170312.models.DisassociateInstancesKeyPairsRequest`
        :rtype: :class:`taifucloudcloud.cvm.v20170312.models.DisassociateInstancesKeyPairsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DisassociateInstancesKeyPairs", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DisassociateInstancesKeyPairsResponse()
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


    def DisassociateSecurityGroups(self, request):
        """本介面 (DisassociateSecurityGroups) 用於解綁實例的指定安全組。

        :param request: 調用DisassociateSecurityGroups所需參數的結構體。
        :type request: :class:`taifucloudcloud.cvm.v20170312.models.DisassociateSecurityGroupsRequest`
        :rtype: :class:`taifucloudcloud.cvm.v20170312.models.DisassociateSecurityGroupsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DisassociateSecurityGroups", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DisassociateSecurityGroupsResponse()
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


    def ImportImage(self, request):
        """本介面(ImportImage)用於導入映像，導入後的映像可用於創建實例。

        :param request: 調用ImportImage所需參數的結構體。
        :type request: :class:`taifucloudcloud.cvm.v20170312.models.ImportImageRequest`
        :rtype: :class:`taifucloudcloud.cvm.v20170312.models.ImportImageResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ImportImage", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ImportImageResponse()
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


    def ImportKeyPair(self, request):
        """本介面 (ImportKeyPair) 用於導入金鑰對。

        * 本介面的功能是将金鑰對導入到用戶帳戶，並不會自動綁定到實例。如需綁定可以使用[AssociasteInstancesKeyPair](https://cloud.taifucloud.com/document/api/213/9404)介面。
        * 需指定金鑰對名稱以及該金鑰對的公鑰文本。
        * 如果用戶只有私鑰，可以通過 `SSL` 工具将私鑰轉換成公鑰後再導入。

        :param request: 調用ImportKeyPair所需參數的結構體。
        :type request: :class:`taifucloudcloud.cvm.v20170312.models.ImportKeyPairRequest`
        :rtype: :class:`taifucloudcloud.cvm.v20170312.models.ImportKeyPairResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ImportKeyPair", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ImportKeyPairResponse()
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


    def InquiryPriceModifyInstancesChargeType(self, request):
        """本介面 (InquiryPriceModifyInstancesChargeType) 用於切換實例的計費模式詢價。

        * 只支援從 `POSTPAID_BY_HOUR` 計費模式切換爲`PREPAID`計費模式。
        * 關機不收費的實例、`BC1`和`BS1`機型族的實例、設置定時銷毀的實例不支援該操作。

        :param request: 調用InquiryPriceModifyInstancesChargeType所需參數的結構體。
        :type request: :class:`taifucloudcloud.cvm.v20170312.models.InquiryPriceModifyInstancesChargeTypeRequest`
        :rtype: :class:`taifucloudcloud.cvm.v20170312.models.InquiryPriceModifyInstancesChargeTypeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("InquiryPriceModifyInstancesChargeType", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.InquiryPriceModifyInstancesChargeTypeResponse()
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


    def InquiryPriceRenewInstances(self, request):
        """本介面 (InquiryPriceRenewInstances) 用於續約包年包月實例詢價。

        * 只支援查詢包年包月實例的續約價格。

        :param request: 調用InquiryPriceRenewInstances所需參數的結構體。
        :type request: :class:`taifucloudcloud.cvm.v20170312.models.InquiryPriceRenewInstancesRequest`
        :rtype: :class:`taifucloudcloud.cvm.v20170312.models.InquiryPriceRenewInstancesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("InquiryPriceRenewInstances", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.InquiryPriceRenewInstancesResponse()
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


    def InquiryPriceResetInstance(self, request):
        """本介面 (InquiryPriceResetInstance) 用於重裝實例詢價。* 如果指定了`ImageId`參數，則使用指定的映像進行重裝詢價；否則按照當前實例使用的映像進行重裝詢價。* 目前只支援[系統盤類型](/document/api/213/9452#block_device)是`CLOUD_BASIC`、`CLOUD_PREMIUM`、`CLOUD_SSD`類型的實例使用該介面實現`Linux`和`Windows`作業系統切換的重裝詢價。* 目前不支援海外地域的實例使用該介面實現`Linux`和`Windows`作業系統切換的重裝詢價。

        :param request: 調用InquiryPriceResetInstance所需參數的結構體。
        :type request: :class:`taifucloudcloud.cvm.v20170312.models.InquiryPriceResetInstanceRequest`
        :rtype: :class:`taifucloudcloud.cvm.v20170312.models.InquiryPriceResetInstanceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("InquiryPriceResetInstance", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.InquiryPriceResetInstanceResponse()
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


    def InquiryPriceResetInstancesInternetMaxBandwidth(self, request):
        """本介面 (InquiryPriceResetInstancesInternetMaxBandwidth) 用於調整實例公網頻寬上限詢價。

        * 不同機型頻寬上限範圍不一緻，具體限制詳見[購買網絡頻寬](https://cloud.taifucloud.com/document/product/213/509)。
        * 對於`BANDWIDTH_PREPAID`計費方式的頻寬，需要輸入參數`StartTime`和`EndTime`，指定調整後的頻寬的生效時間段。在這種場景下目前不支援調小頻寬，會涉及扣費，請确保帳戶餘額充足。可通過[`DescribeAccountBalance`](https://cloud.taifucloud.com/document/product/378/4397)介面查詢帳戶餘額。
        * 對於 `TRAFFIC_POSTPAID_BY_HOUR`、 `BANDWIDTH_POSTPAID_BY_HOUR` 和 `BANDWIDTH_PACKAGE` 計費方式的頻寬，使用該介面調整頻寬上限是實時生效的，可以在頻寬允許的範圍内調大或者調小頻寬，不支援輸入參數 `StartTime` 和 `EndTime` 。
        * 介面不支援調整`BANDWIDTH_POSTPAID_BY_MONTH`計費方式的頻寬。
        * 介面不支援批次調整 `BANDWIDTH_PREPAID` 和 `BANDWIDTH_POSTPAID_BY_HOUR` 計費方式的頻寬。
        * 介面不支援批次調整混合計費方式的頻寬。例如不支援同時調整`TRAFFIC_POSTPAID_BY_HOUR`和`BANDWIDTH_PACKAGE`計費方式的頻寬。

        :param request: 調用InquiryPriceResetInstancesInternetMaxBandwidth所需參數的結構體。
        :type request: :class:`taifucloudcloud.cvm.v20170312.models.InquiryPriceResetInstancesInternetMaxBandwidthRequest`
        :rtype: :class:`taifucloudcloud.cvm.v20170312.models.InquiryPriceResetInstancesInternetMaxBandwidthResponse`

        """
        try:
            params = request._serialize()
            body = self.call("InquiryPriceResetInstancesInternetMaxBandwidth", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.InquiryPriceResetInstancesInternetMaxBandwidthResponse()
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


    def InquiryPriceResetInstancesType(self, request):
        """本介面 (InquiryPriceResetInstancesType) 用於調整實例的機型詢價。

        * 目前只支援[系統盤類型](https://cloud.taifucloud.com/document/api/213/9452#block_device)是`CLOUD_BASIC`、`CLOUD_PREMIUM`、`CLOUD_SSD`類型的實例使用該介面進行調整機型詢價。
        * 目前不支援[CDH](https://cloud.taifucloud.com/document/product/416)實例使用該介面調整機型詢價。
        * 對於包年包月實例，使用該介面會涉及扣費，請确保帳戶餘額充足。可通過[`DescribeAccountBalance`](https://cloud.taifucloud.com/document/product/378/4397)介面查詢帳戶餘額。

        :param request: 調用InquiryPriceResetInstancesType所需參數的結構體。
        :type request: :class:`taifucloudcloud.cvm.v20170312.models.InquiryPriceResetInstancesTypeRequest`
        :rtype: :class:`taifucloudcloud.cvm.v20170312.models.InquiryPriceResetInstancesTypeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("InquiryPriceResetInstancesType", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.InquiryPriceResetInstancesTypeResponse()
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


    def InquiryPriceResizeInstanceDisks(self, request):
        """本介面 (InquiryPriceResizeInstanceDisks) 用於擴容實例的數據盤詢價。

        * 目前只支援擴容非彈性數據盤（[`DescribeDisks`](https://cloud.taifucloud.com/document/api/362/16315)介面返回值中的`Portable`爲`false`表示非彈性）詢價，且[數據盤類型](/document/api/213/9452#block_device)爲：`CLOUD_BASIC`、`CLOUD_PREMIUM`、`CLOUD_SSD`。
        * 目前不支援[CDH](https://cloud.taifucloud.com/document/product/416)實例使用該介面擴容數據盤詢價。* 僅支援包年包月實例随機器購買的數據盤。* 目前只支援擴容一塊數據盤詢價。

        :param request: 調用InquiryPriceResizeInstanceDisks所需參數的結構體。
        :type request: :class:`taifucloudcloud.cvm.v20170312.models.InquiryPriceResizeInstanceDisksRequest`
        :rtype: :class:`taifucloudcloud.cvm.v20170312.models.InquiryPriceResizeInstanceDisksResponse`

        """
        try:
            params = request._serialize()
            body = self.call("InquiryPriceResizeInstanceDisks", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.InquiryPriceResizeInstanceDisksResponse()
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


    def InquiryPriceRunInstances(self, request):
        """本介面(InquiryPriceRunInstances)用於創建實例詢價。本介面僅允許針對購買限制範圍内的實例配置進行詢價, 詳見：[創建實例](https://cloud.taifucloud.com/document/api/213/15730)。

        :param request: 調用InquiryPriceRunInstances所需參數的結構體。
        :type request: :class:`taifucloudcloud.cvm.v20170312.models.InquiryPriceRunInstancesRequest`
        :rtype: :class:`taifucloudcloud.cvm.v20170312.models.InquiryPriceRunInstancesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("InquiryPriceRunInstances", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.InquiryPriceRunInstancesResponse()
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


    def ModifyDisasterRecoverGroupAttribute(self, request):
        """本介面 (ModifyDisasterRecoverGroupAttribute)用於修改[分散置放群組](https://cloud.taifucloud.com/document/product/213/15486)屬性。

        :param request: 調用ModifyDisasterRecoverGroupAttribute所需參數的結構體。
        :type request: :class:`taifucloudcloud.cvm.v20170312.models.ModifyDisasterRecoverGroupAttributeRequest`
        :rtype: :class:`taifucloudcloud.cvm.v20170312.models.ModifyDisasterRecoverGroupAttributeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyDisasterRecoverGroupAttribute", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyDisasterRecoverGroupAttributeResponse()
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


    def ModifyHostsAttribute(self, request):
        """本介面（ModifyHostsAttribute）用於修改CDH實例的屬性，如實例名稱和續約標記等。參數HostName和RenewFlag必須設置其中一個，但不能同時設置。

        :param request: 調用ModifyHostsAttribute所需參數的結構體。
        :type request: :class:`taifucloudcloud.cvm.v20170312.models.ModifyHostsAttributeRequest`
        :rtype: :class:`taifucloudcloud.cvm.v20170312.models.ModifyHostsAttributeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyHostsAttribute", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyHostsAttributeResponse()
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


    def ModifyImageAttribute(self, request):
        """本介面（ModifyImageAttribute）用於修改映像屬性。

        * 已分享的映像無法修改屬性。

        :param request: 調用ModifyImageAttribute所需參數的結構體。
        :type request: :class:`taifucloudcloud.cvm.v20170312.models.ModifyImageAttributeRequest`
        :rtype: :class:`taifucloudcloud.cvm.v20170312.models.ModifyImageAttributeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyImageAttribute", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyImageAttributeResponse()
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


    def ModifyImageSharePermission(self, request):
        """本介面（ModifyImageSharePermission）用於修改映像分享訊息。

        * 分享映像後，被分享帳戶可以通過該映像創建實例。
        * 每個自定義映像最多可共享給50個帳戶。
        * 分享映像無法更改名稱，描述，僅可用於創建實例。
        * 只支援分享到對方帳戶相同地域。

        :param request: 調用ModifyImageSharePermission所需參數的結構體。
        :type request: :class:`taifucloudcloud.cvm.v20170312.models.ModifyImageSharePermissionRequest`
        :rtype: :class:`taifucloudcloud.cvm.v20170312.models.ModifyImageSharePermissionResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyImageSharePermission", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyImageSharePermissionResponse()
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


    def ModifyInstancesAttribute(self, request):
        """本介面 (ModifyInstancesAttribute) 用於修改實例的屬性（目前只支援修改實例的名稱和關聯的安全組）。

        * “實例名稱”僅爲方便用戶自己管理之用，Top Cloud 並不以此名稱作爲提交工單或是進行實例管理操作的依據。
        * 支援批次操作。每次請求批次實例的上限爲100。
        * 修改關聯安全組時，子機原來關聯的安全組會被解綁。

        :param request: 調用ModifyInstancesAttribute所需參數的結構體。
        :type request: :class:`taifucloudcloud.cvm.v20170312.models.ModifyInstancesAttributeRequest`
        :rtype: :class:`taifucloudcloud.cvm.v20170312.models.ModifyInstancesAttributeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyInstancesAttribute", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyInstancesAttributeResponse()
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


    def ModifyInstancesChargeType(self, request):
        """本介面 (ModifyInstancesChargeType) 用於切換實例的計費模式。

        * 只支援從 `POSTPAID_BY_HOUR` 計費模式切換爲`PREPAID`計費模式。
        * 關機不收費的實例、`BC1`和`BS1`機型族的實例、設置定時銷毀的實例不支援該操作。

        :param request: 調用ModifyInstancesChargeType所需參數的結構體。
        :type request: :class:`taifucloudcloud.cvm.v20170312.models.ModifyInstancesChargeTypeRequest`
        :rtype: :class:`taifucloudcloud.cvm.v20170312.models.ModifyInstancesChargeTypeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyInstancesChargeType", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyInstancesChargeTypeResponse()
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


    def ModifyInstancesProject(self, request):
        """本介面 (ModifyInstancesProject) 用於修改實例所屬項目。

        * 項目爲一個虛拟概念，用戶可以在一個帳戶下面建立多個項目，每個項目中管理不同的資源；将多個不同實例分屬到不同項目中，後續使用 [`DescribeInstances`](https://cloud.taifucloud.com/document/api/213/9388)介面查詢實例，項目ID可用於過濾結果。
        * 綁定負載均衡的實例不支援修改實例所屬項目，請先使用[`DeregisterInstancesFromLoadBalancer`](https://cloud.taifucloud.com/document/api/214/1258)介面解綁負載均衡。
        * 修改實例所屬項目會自動解關聯實例原來關聯的安全組，修改完成後可能使用[`ModifySecurityGroupsOfInstance`](https://cloud.taifucloud.com/document/api/213/1367)介面關聯安全組。
        * 支援批次操作。每次請求批次實例的上限爲100。

        :param request: 調用ModifyInstancesProject所需參數的結構體。
        :type request: :class:`taifucloudcloud.cvm.v20170312.models.ModifyInstancesProjectRequest`
        :rtype: :class:`taifucloudcloud.cvm.v20170312.models.ModifyInstancesProjectResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyInstancesProject", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyInstancesProjectResponse()
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


    def ModifyInstancesRenewFlag(self, request):
        """本介面 (ModifyInstancesRenewFlag) 用於修改包年包月實例續約標識。

        * 實例被標識爲自動續約後，每次在實例到期時，會自動續約一個月。
        * 支援批次操作。每次請求批次實例的上限爲100。

        :param request: 調用ModifyInstancesRenewFlag所需參數的結構體。
        :type request: :class:`taifucloudcloud.cvm.v20170312.models.ModifyInstancesRenewFlagRequest`
        :rtype: :class:`taifucloudcloud.cvm.v20170312.models.ModifyInstancesRenewFlagResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyInstancesRenewFlag", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyInstancesRenewFlagResponse()
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


    def ModifyInstancesVpcAttribute(self, request):
        """本介面(ModifyInstancesVpcAttribute)用於修改實例vpc屬性，如私有網絡ip。
        * 此操作預設會關閉實例，完成後再啓動。
        * 當指定私有網絡ID和子網ID（子網必須在實例所在的可用區）與指定實例所在私有網絡不一緻時，會将實例遷移至指定的私有網絡的子網下。執行此操作前請确保指定的實例上沒有綁定[彈性網卡](https://cloud.taifucloud.com/document/product/576)和[負載均衡](https://cloud.taifucloud.com/document/product/214)。

        :param request: 調用ModifyInstancesVpcAttribute所需參數的結構體。
        :type request: :class:`taifucloudcloud.cvm.v20170312.models.ModifyInstancesVpcAttributeRequest`
        :rtype: :class:`taifucloudcloud.cvm.v20170312.models.ModifyInstancesVpcAttributeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyInstancesVpcAttribute", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyInstancesVpcAttributeResponse()
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


    def ModifyKeyPairAttribute(self, request):
        """本介面 (ModifyKeyPairAttribute) 用於修改金鑰對屬性。

        * 修改金鑰對ID所指定的金鑰對的名稱和描述訊息。
        * 金鑰對名稱不能和已經存在的金鑰對的名稱重複。
        * 金鑰對ID是金鑰對的唯一標識，不可修改。

        :param request: 調用ModifyKeyPairAttribute所需參數的結構體。
        :type request: :class:`taifucloudcloud.cvm.v20170312.models.ModifyKeyPairAttributeRequest`
        :rtype: :class:`taifucloudcloud.cvm.v20170312.models.ModifyKeyPairAttributeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyKeyPairAttribute", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyKeyPairAttributeResponse()
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


    def RebootInstances(self, request):
        """本介面 (RebootInstances) 用於重啓實例。

        * 只有狀态爲`RUNNING`的實例才可以進行此操作。
        * 介面調用成功時，實例會進入`REBOOTING`狀态；重啓實例成功時，實例會進入`RUNNING`狀态。
        * 支援強制重啓。強制重啓的效果等同於關閉物理電腦的電源開關再重新啓動。強制重啓可能會導緻數據丢失或文件系統損壞，請僅在服務器不能正常重啓時使用。
        * 支援批次操作，每次請求批次實例的上限爲100。

        :param request: 調用RebootInstances所需參數的結構體。
        :type request: :class:`taifucloudcloud.cvm.v20170312.models.RebootInstancesRequest`
        :rtype: :class:`taifucloudcloud.cvm.v20170312.models.RebootInstancesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("RebootInstances", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RebootInstancesResponse()
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


    def RenewHosts(self, request):
        """本介面 (RenewHosts) 用於續約包年包月CDH實例。

        * 只支援操作包年包月實例，否則操作會以特定[錯誤碼](#4.-.E9.94.99.E8.AF.AF.E7.A0.81)返回。
        * 續約時請确保帳戶餘額充足。可通過[`DescribeAccountBalance`](https://cloud.taifucloud.com/document/product/378/4397)介面查詢帳戶餘額。

        :param request: 調用RenewHosts所需參數的結構體。
        :type request: :class:`taifucloudcloud.cvm.v20170312.models.RenewHostsRequest`
        :rtype: :class:`taifucloudcloud.cvm.v20170312.models.RenewHostsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("RenewHosts", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RenewHostsResponse()
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


    def RenewInstances(self, request):
        """本介面 (RenewInstances) 用於續約包年包月實例。

        * 只支援操作包年包月實例。
        * 續約時請确保帳戶餘額充足。可通過[`DescribeAccountBalance`](https://cloud.taifucloud.com/document/product/378/4397)介面查詢帳戶餘額。

        :param request: 調用RenewInstances所需參數的結構體。
        :type request: :class:`taifucloudcloud.cvm.v20170312.models.RenewInstancesRequest`
        :rtype: :class:`taifucloudcloud.cvm.v20170312.models.RenewInstancesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("RenewInstances", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RenewInstancesResponse()
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


    def ResetInstance(self, request):
        """本介面 (ResetInstance) 用於重裝指定實例上的作業系統。

        * 如果指定了`ImageId`參數，則使用指定的映像重裝；否則按照當前實例使用的映像進行重裝。
        * 系統盤将會被格式化，並重置；請确保系統盤中無重要文件。
        * `Linux`和`Windows`系統互相切換時，該實例系統盤`ID`将發生變化，系統盤關聯快照将無法回滾、恢複數據。
        * 密碼不指定将會通過站内信下發随機密碼。
        * 目前只支援[系統盤類型](https://cloud.taifucloud.com/document/api/213/9452#block_device)是`CLOUD_BASIC`、`CLOUD_PREMIUM`、`CLOUD_SSD`類型的實例使用該介面實現`Linux`和`Windows`作業系統切換。
        * 目前不支援海外地域的實例使用該介面實現`Linux`和`Windows`作業系統切換。

        :param request: 調用ResetInstance所需參數的結構體。
        :type request: :class:`taifucloudcloud.cvm.v20170312.models.ResetInstanceRequest`
        :rtype: :class:`taifucloudcloud.cvm.v20170312.models.ResetInstanceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ResetInstance", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ResetInstanceResponse()
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


    def ResetInstancesInternetMaxBandwidth(self, request):
        """本介面 (ResetInstancesInternetMaxBandwidth) 用於調整實例公網頻寬上限。

        * 不同機型頻寬上限範圍不一緻，具體限制詳見[購買網絡頻寬](https://cloud.taifucloud.com/document/product/213/509)。
        * 對於 `BANDWIDTH_PREPAID` 計費方式的頻寬，需要輸入參數 `StartTime` 和 `EndTime` ，指定調整後的頻寬的生效時間段。在這種場景下目前不支援調小頻寬，會涉及扣費，請确保帳戶餘額充足。可通過 [`DescribeAccountBalance`](https://cloud.taifucloud.com/document/product/378/4397) 介面查詢帳戶餘額。
        * 對於 `TRAFFIC_POSTPAID_BY_HOUR` 、 `BANDWIDTH_POSTPAID_BY_HOUR` 和 `BANDWIDTH_PACKAGE` 計費方式的頻寬，使用該介面調整頻寬上限是實時生效的，可以在頻寬允許的範圍内調大或者調小頻寬，不支援輸入參數 `StartTime` 和 `EndTime` 。
        * 介面不支援調整 `BANDWIDTH_POSTPAID_BY_MONTH` 計費方式的頻寬。
        * 介面不支援批次調整 `BANDWIDTH_PREPAID` 和 `BANDWIDTH_POSTPAID_BY_HOUR` 計費方式的頻寬。
        * 介面不支援批次調整混合計費方式的頻寬。例如不支援同時調整 `TRAFFIC_POSTPAID_BY_HOUR` 和 `BANDWIDTH_PACKAGE` 計費方式的頻寬。

        :param request: 調用ResetInstancesInternetMaxBandwidth所需參數的結構體。
        :type request: :class:`taifucloudcloud.cvm.v20170312.models.ResetInstancesInternetMaxBandwidthRequest`
        :rtype: :class:`taifucloudcloud.cvm.v20170312.models.ResetInstancesInternetMaxBandwidthResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ResetInstancesInternetMaxBandwidth", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ResetInstancesInternetMaxBandwidthResponse()
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


    def ResetInstancesPassword(self, request):
        """本介面 (ResetInstancesPassword) 用於将實例作業系統的密碼重置爲用戶指定的密碼。

        * 只修改管理員帳號的密碼。實例的作業系統不同，管理員帳號也會不一樣(`Windows`爲`Administrator`，`Ubuntu`爲`ubuntu`，其它系統爲`root`)。
        * 重置處於運作中狀态的實例，需要顯式指定強制關機參數`ForceStop`。如果沒有顯式指定強制關機參數，則只有處於關機狀态的實例才允許執行重置密碼操作。
        * 支援批次操作。将多個實例作業系統的密碼重置爲相同的密碼。每次請求批次實例的上限爲100。

        :param request: 調用ResetInstancesPassword所需參數的結構體。
        :type request: :class:`taifucloudcloud.cvm.v20170312.models.ResetInstancesPasswordRequest`
        :rtype: :class:`taifucloudcloud.cvm.v20170312.models.ResetInstancesPasswordResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ResetInstancesPassword", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ResetInstancesPasswordResponse()
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


    def ResetInstancesType(self, request):
        """本介面 (ResetInstancesType) 用於調整實例的機型。
        * 目前只支援[系統盤類型](/document/api/213/9452#block_device)是`CLOUD_BASIC`、`CLOUD_PREMIUM`、`CLOUD_SSD`類型的實例使用該介面進行機型調整。
        * 目前不支援[CDH](https://cloud.taifucloud.com/document/product/416)實例使用該介面調整機型。對於包年包月實例，使用該介面會涉及扣費，請确保帳戶餘額充足。可通過[`DescribeAccountBalance`](https://cloud.taifucloud.com/document/product/378/4397)介面查詢帳戶餘額。

        :param request: 調用ResetInstancesType所需參數的結構體。
        :type request: :class:`taifucloudcloud.cvm.v20170312.models.ResetInstancesTypeRequest`
        :rtype: :class:`taifucloudcloud.cvm.v20170312.models.ResetInstancesTypeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ResetInstancesType", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ResetInstancesTypeResponse()
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


    def ResizeInstanceDisks(self, request):
        """本介面 (ResizeInstanceDisks) 用於擴容實例的數據盤。

        * 目前只支援擴容非彈性數據盤（[`DescribeDisks`](https://cloud.taifucloud.com/document/api/362/16315)介面返回值中的`Portable`爲`false`表示非彈性），且[數據盤類型](/document/api/213/9452#block_device)爲：`CLOUD_BASIC`、`CLOUD_PREMIUM`、`CLOUD_SSD`。
        * 目前不支援[CDH](https://cloud.taifucloud.com/document/product/416)實例使用該介面擴容數據盤。
        * 對於包年包月實例，使用該介面會涉及扣費，請确保帳戶餘額充足。可通過[`DescribeAccountBalance`](https://cloud.taifucloud.com/document/product/378/4397)介面查詢帳戶餘額。
        * 目前只支援擴容一塊數據盤。

        :param request: 調用ResizeInstanceDisks所需參數的結構體。
        :type request: :class:`taifucloudcloud.cvm.v20170312.models.ResizeInstanceDisksRequest`
        :rtype: :class:`taifucloudcloud.cvm.v20170312.models.ResizeInstanceDisksResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ResizeInstanceDisks", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ResizeInstanceDisksResponse()
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


    def RunInstances(self, request):
        """本介面 (RunInstances) 用於創建一個或多個指定配置的實例。

        * 實例創建成功後将自動開機啓動，[實例狀态](/document/api/213/9452#instance_state)變爲“運作中”。
        * 預付費實例的購買會預先扣除本次實例購買所需金額，按小時後付費實例購買會預先鎖定本次實例購買一小時内所需金額，在調用本介面前請确保帳戶餘額充足。
        * 本介面允許購買的實例數量遵循[CVM實例購買限制](https://cloud.taifucloud.com/document/product/213/2664)，所創建的實例和官網入口創建的實例共用配額。
        * 本介面爲異步介面，當創建請求下發成功後會返回一個實例`ID`清單，此時實例的創建並立即未完成。在此期間實例的狀态将會處於“準備中”，可以通過調用 [DescribeInstances](https://cloud.taifucloud.com/document/api/213/15728) 介面查詢對應實例的狀态，來判斷創建有沒有最終成功。如果實例的狀态由“準備中”變爲“運作中”，則爲創建成功。

        :param request: 調用RunInstances所需參數的結構體。
        :type request: :class:`taifucloudcloud.cvm.v20170312.models.RunInstancesRequest`
        :rtype: :class:`taifucloudcloud.cvm.v20170312.models.RunInstancesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("RunInstances", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RunInstancesResponse()
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


    def StartInstances(self, request):
        """本介面 (StartInstances) 用於啓動一個或多個實例。

        * 只有狀态爲`STOPPED`的實例才可以進行此操作。
        * 介面調用成功時，實例會進入`STARTING`狀态；啓動實例成功時，實例會進入`RUNNING`狀态。
        * 支援批次操作。每次請求批次實例的上限爲100。

        :param request: 調用StartInstances所需參數的結構體。
        :type request: :class:`taifucloudcloud.cvm.v20170312.models.StartInstancesRequest`
        :rtype: :class:`taifucloudcloud.cvm.v20170312.models.StartInstancesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("StartInstances", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.StartInstancesResponse()
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


    def StopInstances(self, request):
        """本介面 (StopInstances) 用於關閉一個或多個實例。

        * 只有狀态爲`RUNNING`的實例才可以進行此操作。
        * 介面調用成功時，實例會進入`STOPPING`狀态；關閉實例成功時，實例會進入`STOPPED`狀态。
        * 支援強制關閉。強制關機的效果等同於關閉物理電腦的電源開關。強制關機可能會導緻數據丢失或文件系統損壞，請僅在服務器不能正常關機時使用。
        * 支援批次操作。每次請求批次實例的上限爲100。

        :param request: 調用StopInstances所需參數的結構體。
        :type request: :class:`taifucloudcloud.cvm.v20170312.models.StopInstancesRequest`
        :rtype: :class:`taifucloudcloud.cvm.v20170312.models.StopInstancesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("StopInstances", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.StopInstancesResponse()
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


    def SyncImages(self, request):
        """本介面（SyncImages）用於将自定義映像同步到其它地區。

        * 該介面每次調用只支援同步一個映像。
        * 該介面支援多個同步地域。
        * 單個帳號在每個地域最多支援存在10個自定義映像。

        :param request: 調用SyncImages所需參數的結構體。
        :type request: :class:`taifucloudcloud.cvm.v20170312.models.SyncImagesRequest`
        :rtype: :class:`taifucloudcloud.cvm.v20170312.models.SyncImagesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("SyncImages", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.SyncImagesResponse()
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


    def TerminateInstances(self, request):
        """本介面 (TerminateInstances) 用於主動退還實例。

        * 不再使用的實例，可通過本介面主動退還。
        * 按量計費的實例通過本介面可直接退還；包年包月實例如符合[退還規則](https://cloud.taifucloud.com/document/product/213/9711)，也可通過本介面主動退還。
        * 支援批次操作，每次請求批次實例的上限爲100。

        :param request: 調用TerminateInstances所需參數的結構體。
        :type request: :class:`taifucloudcloud.cvm.v20170312.models.TerminateInstancesRequest`
        :rtype: :class:`taifucloudcloud.cvm.v20170312.models.TerminateInstancesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("TerminateInstances", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.TerminateInstancesResponse()
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