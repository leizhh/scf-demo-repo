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
from taifucloudcloud.mongodb.v20180408 import models


class MongodbClient(AbstractClient):
    _apiVersion = '2018-04-08'
    _endpoint = 'mongodb.taifucloudcloudapi.com'


    def AssignProject(self, request):
        """本介面(AssignProject)用於指定雲資料庫實例的所屬項目。


        :param request: Request instance for AssignProject.
        :type request: :class:`taifucloudcloud.mongodb.v20180408.models.AssignProjectRequest`
        :rtype: :class:`taifucloudcloud.mongodb.v20180408.models.AssignProjectResponse`

        """
        try:
            params = request._serialize()
            body = self.call("AssignProject", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AssignProjectResponse()
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


    def CreateDBInstance(self, request):
        """本介面(CreateDBInstance)用於創建包年包月的MongoDB雲資料庫實例。

        :param request: Request instance for CreateDBInstance.
        :type request: :class:`taifucloudcloud.mongodb.v20180408.models.CreateDBInstanceRequest`
        :rtype: :class:`taifucloudcloud.mongodb.v20180408.models.CreateDBInstanceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateDBInstance", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateDBInstanceResponse()
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


    def CreateDBInstanceHour(self, request):
        """本介面(CreateDBInstanceHour)用於創建按量計費的MongoDB雲資料庫實例（包括主實例、災備實例和只讀實例），可通過傳入實例規格、實例類型、MongoDB版本、購買時長和數量等訊息創建雲資料庫實例。

        :param request: Request instance for CreateDBInstanceHour.
        :type request: :class:`taifucloudcloud.mongodb.v20180408.models.CreateDBInstanceHourRequest`
        :rtype: :class:`taifucloudcloud.mongodb.v20180408.models.CreateDBInstanceHourResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateDBInstanceHour", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateDBInstanceHourResponse()
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


    def DescribeClientConnections(self, request):
        """本介面(DescribeClientConnections)用於查詢實例用戶端連接訊息，包括連接IP和連接數量。目前只支援3.2版本的MongoDB實例。

        :param request: Request instance for DescribeClientConnections.
        :type request: :class:`taifucloudcloud.mongodb.v20180408.models.DescribeClientConnectionsRequest`
        :rtype: :class:`taifucloudcloud.mongodb.v20180408.models.DescribeClientConnectionsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeClientConnections", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeClientConnectionsResponse()
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


    def DescribeDBInstances(self, request):
        """本介面(DescribeDBInstances)用於查詢雲資料庫實例清單，支援通過項目ID、實例ID、實例狀态等過濾條件來篩選實例。支援查詢主實例、災備實例和只讀實例訊息清單。

        :param request: Request instance for DescribeDBInstances.
        :type request: :class:`taifucloudcloud.mongodb.v20180408.models.DescribeDBInstancesRequest`
        :rtype: :class:`taifucloudcloud.mongodb.v20180408.models.DescribeDBInstancesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDBInstances", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDBInstancesResponse()
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


    def DescribeSlowLog(self, request):
        """本介面(DescribeSlowLogs)用於獲取雲資料庫實例的慢查詢日志。

        :param request: Request instance for DescribeSlowLog.
        :type request: :class:`taifucloudcloud.mongodb.v20180408.models.DescribeSlowLogRequest`
        :rtype: :class:`taifucloudcloud.mongodb.v20180408.models.DescribeSlowLogResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeSlowLog", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeSlowLogResponse()
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


    def DescribeSpecInfo(self, request):
        """本介面(DescribeSpecInfo)用於查詢實例的售賣規格。

        :param request: Request instance for DescribeSpecInfo.
        :type request: :class:`taifucloudcloud.mongodb.v20180408.models.DescribeSpecInfoRequest`
        :rtype: :class:`taifucloudcloud.mongodb.v20180408.models.DescribeSpecInfoResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeSpecInfo", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeSpecInfoResponse()
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


    def RenameInstance(self, request):
        """本介面(RenameInstance)用於修改雲資料庫實例的名稱。

        :param request: Request instance for RenameInstance.
        :type request: :class:`taifucloudcloud.mongodb.v20180408.models.RenameInstanceRequest`
        :rtype: :class:`taifucloudcloud.mongodb.v20180408.models.RenameInstanceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("RenameInstance", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RenameInstanceResponse()
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


    def SetAutoRenew(self, request):
        """本介面(SetAutoRenew)用於設置包年包月雲資料庫實例的續約選項。

        :param request: Request instance for SetAutoRenew.
        :type request: :class:`taifucloudcloud.mongodb.v20180408.models.SetAutoRenewRequest`
        :rtype: :class:`taifucloudcloud.mongodb.v20180408.models.SetAutoRenewResponse`

        """
        try:
            params = request._serialize()
            body = self.call("SetAutoRenew", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.SetAutoRenewResponse()
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


    def SetPassword(self, request):
        """本介面(SetPassword)用於設置雲資料庫帳戶的密碼。


        :param request: Request instance for SetPassword.
        :type request: :class:`taifucloudcloud.mongodb.v20180408.models.SetPasswordRequest`
        :rtype: :class:`taifucloudcloud.mongodb.v20180408.models.SetPasswordResponse`

        """
        try:
            params = request._serialize()
            body = self.call("SetPassword", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.SetPasswordResponse()
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


    def TerminateDBInstance(self, request):
        """本介面(TerminateDBInstance)用於銷毀按量計費的MongoDB雲資料庫實例

        :param request: Request instance for TerminateDBInstance.
        :type request: :class:`taifucloudcloud.mongodb.v20180408.models.TerminateDBInstanceRequest`
        :rtype: :class:`taifucloudcloud.mongodb.v20180408.models.TerminateDBInstanceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("TerminateDBInstance", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.TerminateDBInstanceResponse()
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


    def UpgradeDBInstance(self, request):
        """本介面(UpgradeDBInstance)用於升級包年包月的MongoDB雲資料庫實例，可以擴容内存、儲存以及Oplog

        :param request: Request instance for UpgradeDBInstance.
        :type request: :class:`taifucloudcloud.mongodb.v20180408.models.UpgradeDBInstanceRequest`
        :rtype: :class:`taifucloudcloud.mongodb.v20180408.models.UpgradeDBInstanceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UpgradeDBInstance", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpgradeDBInstanceResponse()
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


    def UpgradeDBInstanceHour(self, request):
        """本介面(UpgradeDBInstanceHour)用於升級按量計費的MongoDB雲資料庫實例，可以擴容内存、儲存以及oplog

        :param request: Request instance for UpgradeDBInstanceHour.
        :type request: :class:`taifucloudcloud.mongodb.v20180408.models.UpgradeDBInstanceHourRequest`
        :rtype: :class:`taifucloudcloud.mongodb.v20180408.models.UpgradeDBInstanceHourResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UpgradeDBInstanceHour", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpgradeDBInstanceHourResponse()
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