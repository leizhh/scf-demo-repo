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
from taifucloudcloud.cdb.v20170320 import models


class CdbClient(AbstractClient):
    _apiVersion = '2017-03-20'
    _endpoint = 'cdb.taifucloudcloudapi.com'


    def AddTimeWindow(self, request):
        """本介面(AddTimeWindow)用於添加雲資料庫實例的維護時間視窗，以指定實例在哪些時間段可以自動執行切換訪問操作。

        :param request: 調用AddTimeWindow所需參數的結構體。
        :type request: :class:`taifucloudcloud.cdb.v20170320.models.AddTimeWindowRequest`
        :rtype: :class:`taifucloudcloud.cdb.v20170320.models.AddTimeWindowResponse`

        """
        try:
            params = request._serialize()
            body = self.call("AddTimeWindow", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AddTimeWindowResponse()
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
        """本介面(AssociateSecurityGroups)用於安全組批次綁定實例。

        :param request: 調用AssociateSecurityGroups所需參數的結構體。
        :type request: :class:`taifucloudcloud.cdb.v20170320.models.AssociateSecurityGroupsRequest`
        :rtype: :class:`taifucloudcloud.cdb.v20170320.models.AssociateSecurityGroupsResponse`

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


    def CloseWanService(self, request):
        """本介面(CloseWanService)用於關閉雲資料庫實例的外網訪問。關閉外網訪問後，外網網址将不可訪問。

        :param request: 調用CloseWanService所需參數的結構體。
        :type request: :class:`taifucloudcloud.cdb.v20170320.models.CloseWanServiceRequest`
        :rtype: :class:`taifucloudcloud.cdb.v20170320.models.CloseWanServiceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CloseWanService", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CloseWanServiceResponse()
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


    def CreateAccounts(self, request):
        """本介面(CreateAccounts)用於創建雲資料庫的帳戶，需要指定新的帳戶名和域名，以及所對應的密碼，同時可以設置賬號的備注訊息。

        :param request: 調用CreateAccounts所需參數的結構體。
        :type request: :class:`taifucloudcloud.cdb.v20170320.models.CreateAccountsRequest`
        :rtype: :class:`taifucloudcloud.cdb.v20170320.models.CreateAccountsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateAccounts", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateAccountsResponse()
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


    def CreateBackup(self, request):
        """本介面(CreateBackup)用於創建資料庫備份。

        :param request: 調用CreateBackup所需參數的結構體。
        :type request: :class:`taifucloudcloud.cdb.v20170320.models.CreateBackupRequest`
        :rtype: :class:`taifucloudcloud.cdb.v20170320.models.CreateBackupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateBackup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateBackupResponse()
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


    def CreateDBImportJob(self, request):
        """本介面(CreateDBImportJob)用於創建雲資料庫數據導入任務。

        注意，用戶進行數據導入任務的文件，必須提前上傳到Top Cloud 。用戶須在控制台進行文件導入。

        :param request: 調用CreateDBImportJob所需參數的結構體。
        :type request: :class:`taifucloudcloud.cdb.v20170320.models.CreateDBImportJobRequest`
        :rtype: :class:`taifucloudcloud.cdb.v20170320.models.CreateDBImportJobResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateDBImportJob", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateDBImportJobResponse()
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
        """本介面(CreateDBInstance)用於創建包年包月的雲資料庫實例（包括主實例、災備實例和只讀實例），可通過傳入實例規格、MySQL 版本號、購買時長和數量等訊息創建雲資料庫實例。

        該介面爲異步介面，您還可以使用[查詢實例清單](https://cloud.taifucloud.com/document/api/236/15872)介面查詢該實例的詳細訊息。當該實例的Status爲1，且TaskStatus爲0，表示實例已經發貨成功。

        1. 首先請使用[獲取雲資料庫可售賣規格](https://cloud.taifucloud.com/document/api/236/17229)介面查詢可創建的實例規格訊息，然後請使用[查詢資料庫價格](https://cloud.taifucloud.com/document/api/236/18566)介面查詢可創建實例的售賣價格；
        2. 單次創建實例最大支援 100 個，實例時長最大支援 36 個月；
        3. 支援創建 MySQL5.5 、 MySQL5.6 、 MySQL5.7 版本；
        4. 支援創建主實例、只讀實例、災備實例；
        5. 當入參指定Port或ParamList時，該實例會進行初始化操作；

        :param request: 調用CreateDBInstance所需參數的結構體。
        :type request: :class:`taifucloudcloud.cdb.v20170320.models.CreateDBInstanceRequest`
        :rtype: :class:`taifucloudcloud.cdb.v20170320.models.CreateDBInstanceResponse`

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
        """本介面(CreateDBInstanceHour)用於創建按量計費的實例，可通過傳入實例規格、MySQL 版本號和數量等訊息創建雲資料庫實例，支援主實例、災備實例和只讀實例的創建。

        該介面爲異步介面，您還可以使用[查詢實例清單](https://cloud.taifucloud.com/document/api/236/15872)介面查詢該實例的詳細訊息。當該實例的Status爲1，且TaskStatus爲0，表示實例已經發貨成功。

        1. 首先請使用[獲取雲資料庫可售賣規格](https://cloud.taifucloud.com/document/api/236/17229)介面查詢可創建的實例規格訊息，然後請使用[查詢資料庫價格](https://cloud.taifucloud.com/document/api/236/18566)介面查詢可創建實例的售賣價格；
        2. 單次創建實例最大支援 100 個，實例時長最大支援 36 個月；
        3. 支援創建 MySQL5.5、MySQL5.6和MySQL5.7 版本；
        4. 支援創建主實例、災備實例和只讀實例；
        5. 當入參指定Port或ParamList時，該實例會進行初始化操作；

        :param request: 調用CreateDBInstanceHour所需參數的結構體。
        :type request: :class:`taifucloudcloud.cdb.v20170320.models.CreateDBInstanceHourRequest`
        :rtype: :class:`taifucloudcloud.cdb.v20170320.models.CreateDBInstanceHourResponse`

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


    def CreateParamTemplate(self, request):
        """該介面（CreateParamTemplate）用於創建參數範本。

        :param request: 調用CreateParamTemplate所需參數的結構體。
        :type request: :class:`taifucloudcloud.cdb.v20170320.models.CreateParamTemplateRequest`
        :rtype: :class:`taifucloudcloud.cdb.v20170320.models.CreateParamTemplateResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateParamTemplate", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateParamTemplateResponse()
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


    def DeleteAccounts(self, request):
        """本介面(DeleteAccounts)用於删除雲資料庫的帳戶。

        :param request: 調用DeleteAccounts所需參數的結構體。
        :type request: :class:`taifucloudcloud.cdb.v20170320.models.DeleteAccountsRequest`
        :rtype: :class:`taifucloudcloud.cdb.v20170320.models.DeleteAccountsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteAccounts", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteAccountsResponse()
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


    def DeleteBackup(self, request):
        """本介面(DeleteBackup)用於删除資料庫備份。

        :param request: 調用DeleteBackup所需參數的結構體。
        :type request: :class:`taifucloudcloud.cdb.v20170320.models.DeleteBackupRequest`
        :rtype: :class:`taifucloudcloud.cdb.v20170320.models.DeleteBackupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteBackup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteBackupResponse()
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


    def DeleteParamTemplate(self, request):
        """該介面（DeleteParamTemplate）用於删除參數範本。

        :param request: 調用DeleteParamTemplate所需參數的結構體。
        :type request: :class:`taifucloudcloud.cdb.v20170320.models.DeleteParamTemplateRequest`
        :rtype: :class:`taifucloudcloud.cdb.v20170320.models.DeleteParamTemplateResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteParamTemplate", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteParamTemplateResponse()
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


    def DeleteTimeWindow(self, request):
        """本介面(DeleteTimeWindow)用於删除雲資料庫實例的維護時間視窗。删除實例維護時間視窗之後，預設的維護時間窗爲 03:00-04:00，即當選擇在維護時間視窗内切換訪問新實例時，預設會在03:00-04:00點進行切換訪問新實例。

        :param request: 調用DeleteTimeWindow所需參數的結構體。
        :type request: :class:`taifucloudcloud.cdb.v20170320.models.DeleteTimeWindowRequest`
        :rtype: :class:`taifucloudcloud.cdb.v20170320.models.DeleteTimeWindowResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteTimeWindow", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteTimeWindowResponse()
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


    def DescribeAccountPrivileges(self, request):
        """本介面(DescribeAccountPrivileges)用於查詢雲資料庫帳戶支援的權限訊息。

        :param request: 調用DescribeAccountPrivileges所需參數的結構體。
        :type request: :class:`taifucloudcloud.cdb.v20170320.models.DescribeAccountPrivilegesRequest`
        :rtype: :class:`taifucloudcloud.cdb.v20170320.models.DescribeAccountPrivilegesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAccountPrivileges", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAccountPrivilegesResponse()
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


    def DescribeAccounts(self, request):
        """本介面(DescribeAccounts)用於查詢雲資料庫的所有帳戶訊息。

        :param request: 調用DescribeAccounts所需參數的結構體。
        :type request: :class:`taifucloudcloud.cdb.v20170320.models.DescribeAccountsRequest`
        :rtype: :class:`taifucloudcloud.cdb.v20170320.models.DescribeAccountsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAccounts", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAccountsResponse()
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


    def DescribeAsyncRequestInfo(self, request):
        """本介面(DescribeAsyncRequestInfo)用於查詢雲資料庫實例異步任務的執行結果。

        :param request: 調用DescribeAsyncRequestInfo所需參數的結構體。
        :type request: :class:`taifucloudcloud.cdb.v20170320.models.DescribeAsyncRequestInfoRequest`
        :rtype: :class:`taifucloudcloud.cdb.v20170320.models.DescribeAsyncRequestInfoResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAsyncRequestInfo", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAsyncRequestInfoResponse()
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


    def DescribeBackupConfig(self, request):
        """本介面(DescribeBackupConfig)用於查詢資料庫備份配置訊息。

        :param request: 調用DescribeBackupConfig所需參數的結構體。
        :type request: :class:`taifucloudcloud.cdb.v20170320.models.DescribeBackupConfigRequest`
        :rtype: :class:`taifucloudcloud.cdb.v20170320.models.DescribeBackupConfigResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeBackupConfig", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeBackupConfigResponse()
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


    def DescribeBackupDatabases(self, request):
        """本介面(DescribeBackupDatabases)用於查詢備份資料庫清單 (将廢棄)。

        :param request: 調用DescribeBackupDatabases所需參數的結構體。
        :type request: :class:`taifucloudcloud.cdb.v20170320.models.DescribeBackupDatabasesRequest`
        :rtype: :class:`taifucloudcloud.cdb.v20170320.models.DescribeBackupDatabasesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeBackupDatabases", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeBackupDatabasesResponse()
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


    def DescribeBackupTables(self, request):
        """本介面(DescribeBackupTables)用於查詢指定的資料庫的備份數據表名 (将廢棄)。

        :param request: 調用DescribeBackupTables所需參數的結構體。
        :type request: :class:`taifucloudcloud.cdb.v20170320.models.DescribeBackupTablesRequest`
        :rtype: :class:`taifucloudcloud.cdb.v20170320.models.DescribeBackupTablesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeBackupTables", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeBackupTablesResponse()
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


    def DescribeBackups(self, request):
        """本介面(DescribeBackups)用於查詢雲資料庫實例的備份數據。

        :param request: 調用DescribeBackups所需參數的結構體。
        :type request: :class:`taifucloudcloud.cdb.v20170320.models.DescribeBackupsRequest`
        :rtype: :class:`taifucloudcloud.cdb.v20170320.models.DescribeBackupsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeBackups", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeBackupsResponse()
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


    def DescribeBinlogs(self, request):
        """本介面(DescribeBinlogs)用於查詢雲資料庫實例的二進制數據。

        :param request: 調用DescribeBinlogs所需參數的結構體。
        :type request: :class:`taifucloudcloud.cdb.v20170320.models.DescribeBinlogsRequest`
        :rtype: :class:`taifucloudcloud.cdb.v20170320.models.DescribeBinlogsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeBinlogs", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeBinlogsResponse()
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


    def DescribeDBImportRecords(self, request):
        """本介面(DescribeDBImportRecords)用於查詢雲資料庫導入任務操作日志。

        :param request: 調用DescribeDBImportRecords所需參數的結構體。
        :type request: :class:`taifucloudcloud.cdb.v20170320.models.DescribeDBImportRecordsRequest`
        :rtype: :class:`taifucloudcloud.cdb.v20170320.models.DescribeDBImportRecordsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDBImportRecords", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDBImportRecordsResponse()
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


    def DescribeDBInstanceCharset(self, request):
        """本介面(DescribeDBInstanceCharset)用於查詢雲資料庫實例的字元集，獲取字元集的名稱。

        :param request: 調用DescribeDBInstanceCharset所需參數的結構體。
        :type request: :class:`taifucloudcloud.cdb.v20170320.models.DescribeDBInstanceCharsetRequest`
        :rtype: :class:`taifucloudcloud.cdb.v20170320.models.DescribeDBInstanceCharsetResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDBInstanceCharset", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDBInstanceCharsetResponse()
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


    def DescribeDBInstanceConfig(self, request):
        """本介面(DescribeDBInstanceConfig)用於雲資料庫實例的配置訊息，包括同步模式，佈署模式等。

        :param request: 調用DescribeDBInstanceConfig所需參數的結構體。
        :type request: :class:`taifucloudcloud.cdb.v20170320.models.DescribeDBInstanceConfigRequest`
        :rtype: :class:`taifucloudcloud.cdb.v20170320.models.DescribeDBInstanceConfigResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDBInstanceConfig", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDBInstanceConfigResponse()
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


    def DescribeDBInstanceGTID(self, request):
        """本介面(DescribeDBInstanceGTID)用於查詢雲資料庫實例是否開通了GTID，不支援版本爲5.5以及以下的實例。

        :param request: 調用DescribeDBInstanceGTID所需參數的結構體。
        :type request: :class:`taifucloudcloud.cdb.v20170320.models.DescribeDBInstanceGTIDRequest`
        :rtype: :class:`taifucloudcloud.cdb.v20170320.models.DescribeDBInstanceGTIDResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDBInstanceGTID", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDBInstanceGTIDResponse()
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


    def DescribeDBInstanceRebootTime(self, request):
        """本介面(DescribeDBInstanceRebootTime)用於查詢雲資料庫實例重啓預計所需的時間。

        :param request: 調用DescribeDBInstanceRebootTime所需參數的結構體。
        :type request: :class:`taifucloudcloud.cdb.v20170320.models.DescribeDBInstanceRebootTimeRequest`
        :rtype: :class:`taifucloudcloud.cdb.v20170320.models.DescribeDBInstanceRebootTimeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDBInstanceRebootTime", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDBInstanceRebootTimeResponse()
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
        """本介面(DescribeDBInstances)用於查詢雲資料庫實例清單，支援通過項目ID、實例ID、訪問網址、實例狀态等過濾條件來篩選實例。支援查詢主實例、災備實例和只讀實例訊息清單。

        :param request: 調用DescribeDBInstances所需參數的結構體。
        :type request: :class:`taifucloudcloud.cdb.v20170320.models.DescribeDBInstancesRequest`
        :rtype: :class:`taifucloudcloud.cdb.v20170320.models.DescribeDBInstancesResponse`

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


    def DescribeDBPrice(self, request):
        """本介面(DescribeDBPrice)用於查詢雲資料庫實例的價格，支援查詢按量計費或者包年包月的價格。可傳入實例類型、購買時長、購買數量、内存大小、硬碟大小和可用區訊息等來查詢實例價格。

        注意：對某個地域進行詢價，請使用對應地域的接入點，接入點訊息請參照<a href="https://cloud.taifucloud.com/document/api/236/15832">服務網址</a>文件。例如：對 地域進行詢價，請把請求發到：cdb.ap-guangzhou.taifucloudcloudapi.com。同理對 地域詢價，把請求發到：cdb.ap-shanghai.taifucloudcloudapi.com

        :param request: 調用DescribeDBPrice所需參數的結構體。
        :type request: :class:`taifucloudcloud.cdb.v20170320.models.DescribeDBPriceRequest`
        :rtype: :class:`taifucloudcloud.cdb.v20170320.models.DescribeDBPriceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDBPrice", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDBPriceResponse()
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


    def DescribeDBSecurityGroups(self, request):
        """本介面(DescribeDBSecurityGroups)用於查詢實例的安全組詳情。

        :param request: 調用DescribeDBSecurityGroups所需參數的結構體。
        :type request: :class:`taifucloudcloud.cdb.v20170320.models.DescribeDBSecurityGroupsRequest`
        :rtype: :class:`taifucloudcloud.cdb.v20170320.models.DescribeDBSecurityGroupsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDBSecurityGroups", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDBSecurityGroupsResponse()
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


    def DescribeDBSwitchRecords(self, request):
        """本介面(DescribeDBSwitchRecords)用於查詢雲資料庫實例切換記錄。

        :param request: 調用DescribeDBSwitchRecords所需參數的結構體。
        :type request: :class:`taifucloudcloud.cdb.v20170320.models.DescribeDBSwitchRecordsRequest`
        :rtype: :class:`taifucloudcloud.cdb.v20170320.models.DescribeDBSwitchRecordsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDBSwitchRecords", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDBSwitchRecordsResponse()
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


    def DescribeDBZoneConfig(self, request):
        """本介面(DescribeDBZoneConfig)用於查詢可創建的雲資料庫各地域可售賣的規格配置。

        :param request: 調用DescribeDBZoneConfig所需參數的結構體。
        :type request: :class:`taifucloudcloud.cdb.v20170320.models.DescribeDBZoneConfigRequest`
        :rtype: :class:`taifucloudcloud.cdb.v20170320.models.DescribeDBZoneConfigResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDBZoneConfig", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDBZoneConfigResponse()
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


    def DescribeDatabases(self, request):
        """本介面(DescribeDatabases)用於查詢雲資料庫實例的資料庫訊息。

        :param request: 調用DescribeDatabases所需參數的結構體。
        :type request: :class:`taifucloudcloud.cdb.v20170320.models.DescribeDatabasesRequest`
        :rtype: :class:`taifucloudcloud.cdb.v20170320.models.DescribeDatabasesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDatabases", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDatabasesResponse()
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


    def DescribeDefaultParams(self, request):
        """該介面（DescribeDefaultParams）用於查詢預設的可設置參數清單。

        :param request: 調用DescribeDefaultParams所需參數的結構體。
        :type request: :class:`taifucloudcloud.cdb.v20170320.models.DescribeDefaultParamsRequest`
        :rtype: :class:`taifucloudcloud.cdb.v20170320.models.DescribeDefaultParamsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDefaultParams", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDefaultParamsResponse()
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


    def DescribeDeviceMonitorInfo(self, request):
        """本介面（DescribeDeviceMonitorInfo）用於查詢雲資料庫物理機當天的監控訊息，暫只支援内存488G、硬碟6T的實例查詢。

        :param request: 調用DescribeDeviceMonitorInfo所需參數的結構體。
        :type request: :class:`taifucloudcloud.cdb.v20170320.models.DescribeDeviceMonitorInfoRequest`
        :rtype: :class:`taifucloudcloud.cdb.v20170320.models.DescribeDeviceMonitorInfoResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDeviceMonitorInfo", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDeviceMonitorInfoResponse()
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


    def DescribeInstanceParamRecords(self, request):
        """該介面（DescribeInstanceParamRecords）用於查詢實例參數修改曆史。

        :param request: 調用DescribeInstanceParamRecords所需參數的結構體。
        :type request: :class:`taifucloudcloud.cdb.v20170320.models.DescribeInstanceParamRecordsRequest`
        :rtype: :class:`taifucloudcloud.cdb.v20170320.models.DescribeInstanceParamRecordsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeInstanceParamRecords", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeInstanceParamRecordsResponse()
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


    def DescribeInstanceParams(self, request):
        """該介面（DescribeInstanceParams）用於查詢實例的參數清單。

        :param request: 調用DescribeInstanceParams所需參數的結構體。
        :type request: :class:`taifucloudcloud.cdb.v20170320.models.DescribeInstanceParamsRequest`
        :rtype: :class:`taifucloudcloud.cdb.v20170320.models.DescribeInstanceParamsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeInstanceParams", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeInstanceParamsResponse()
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


    def DescribeParamTemplateInfo(self, request):
        """該介面（DescribeParamTemplateInfo）用於查詢參數範本詳情。

        :param request: 調用DescribeParamTemplateInfo所需參數的結構體。
        :type request: :class:`taifucloudcloud.cdb.v20170320.models.DescribeParamTemplateInfoRequest`
        :rtype: :class:`taifucloudcloud.cdb.v20170320.models.DescribeParamTemplateInfoResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeParamTemplateInfo", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeParamTemplateInfoResponse()
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


    def DescribeParamTemplates(self, request):
        """該介面（DescribeParamTemplates）查詢參數範本清單。

        :param request: 調用DescribeParamTemplates所需參數的結構體。
        :type request: :class:`taifucloudcloud.cdb.v20170320.models.DescribeParamTemplatesRequest`
        :rtype: :class:`taifucloudcloud.cdb.v20170320.models.DescribeParamTemplatesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeParamTemplates", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeParamTemplatesResponse()
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


    def DescribeProjectSecurityGroups(self, request):
        """本介面(DescribeProjectSecurityGroups)用於查詢項目的安全組詳情。

        :param request: 調用DescribeProjectSecurityGroups所需參數的結構體。
        :type request: :class:`taifucloudcloud.cdb.v20170320.models.DescribeProjectSecurityGroupsRequest`
        :rtype: :class:`taifucloudcloud.cdb.v20170320.models.DescribeProjectSecurityGroupsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeProjectSecurityGroups", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeProjectSecurityGroupsResponse()
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


    def DescribeRollbackRangeTime(self, request):
        """本介面(DescribeRollbackRangeTime)用於查詢雲資料庫實例可回檔的時間範圍。

        :param request: 調用DescribeRollbackRangeTime所需參數的結構體。
        :type request: :class:`taifucloudcloud.cdb.v20170320.models.DescribeRollbackRangeTimeRequest`
        :rtype: :class:`taifucloudcloud.cdb.v20170320.models.DescribeRollbackRangeTimeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeRollbackRangeTime", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeRollbackRangeTimeResponse()
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


    def DescribeSlowLogs(self, request):
        """本介面(DescribeSlowLogs)用於獲取雲資料庫實例的慢查詢日志。

        :param request: 調用DescribeSlowLogs所需參數的結構體。
        :type request: :class:`taifucloudcloud.cdb.v20170320.models.DescribeSlowLogsRequest`
        :rtype: :class:`taifucloudcloud.cdb.v20170320.models.DescribeSlowLogsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeSlowLogs", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeSlowLogsResponse()
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


    def DescribeSupportedPrivileges(self, request):
        """本介面(DescribeSupportedPrivileges)用於查詢雲資料庫的支援的權限訊息，包括全局權限，資料庫權限，表權限以及列權限。

        :param request: 調用DescribeSupportedPrivileges所需參數的結構體。
        :type request: :class:`taifucloudcloud.cdb.v20170320.models.DescribeSupportedPrivilegesRequest`
        :rtype: :class:`taifucloudcloud.cdb.v20170320.models.DescribeSupportedPrivilegesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeSupportedPrivileges", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeSupportedPrivilegesResponse()
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


    def DescribeTables(self, request):
        """本介面(DescribeTables)用於查詢雲資料庫實例的資料庫表訊息。

        :param request: 調用DescribeTables所需參數的結構體。
        :type request: :class:`taifucloudcloud.cdb.v20170320.models.DescribeTablesRequest`
        :rtype: :class:`taifucloudcloud.cdb.v20170320.models.DescribeTablesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeTables", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeTablesResponse()
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


    def DescribeTagsOfInstanceIds(self, request):
        """獲取實例綁定的標簽

        :param request: 調用DescribeTagsOfInstanceIds所需參數的結構體。
        :type request: :class:`taifucloudcloud.cdb.v20170320.models.DescribeTagsOfInstanceIdsRequest`
        :rtype: :class:`taifucloudcloud.cdb.v20170320.models.DescribeTagsOfInstanceIdsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeTagsOfInstanceIds", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeTagsOfInstanceIdsResponse()
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


    def DescribeTasks(self, request):
        """本介面(DescribeTasks)用於查詢雲資料庫實例任務清單。

        :param request: 調用DescribeTasks所需參數的結構體。
        :type request: :class:`taifucloudcloud.cdb.v20170320.models.DescribeTasksRequest`
        :rtype: :class:`taifucloudcloud.cdb.v20170320.models.DescribeTasksResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeTasks", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeTasksResponse()
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


    def DescribeTimeWindow(self, request):
        """本介面(DescribeTimeWindow)用於查詢雲資料庫實例的維護時間視窗。

        :param request: 調用DescribeTimeWindow所需參數的結構體。
        :type request: :class:`taifucloudcloud.cdb.v20170320.models.DescribeTimeWindowRequest`
        :rtype: :class:`taifucloudcloud.cdb.v20170320.models.DescribeTimeWindowResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeTimeWindow", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeTimeWindowResponse()
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


    def DescribeUploadedFiles(self, request):
        """本介面(DescribeUploadedFiles)用於查詢用戶導入的SQL文件清單。

        :param request: 調用DescribeUploadedFiles所需參數的結構體。
        :type request: :class:`taifucloudcloud.cdb.v20170320.models.DescribeUploadedFilesRequest`
        :rtype: :class:`taifucloudcloud.cdb.v20170320.models.DescribeUploadedFilesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeUploadedFiles", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeUploadedFilesResponse()
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
        """本介面(DisassociateSecurityGroups)用於安全組批次解綁實例。

        :param request: 調用DisassociateSecurityGroups所需參數的結構體。
        :type request: :class:`taifucloudcloud.cdb.v20170320.models.DisassociateSecurityGroupsRequest`
        :rtype: :class:`taifucloudcloud.cdb.v20170320.models.DisassociateSecurityGroupsResponse`

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


    def InitDBInstances(self, request):
        """本介面(InitDBInstances)用於初始化雲資料庫實例，包括初始化密碼、預設字元集、實例端口號等

        :param request: 調用InitDBInstances所需參數的結構體。
        :type request: :class:`taifucloudcloud.cdb.v20170320.models.InitDBInstancesRequest`
        :rtype: :class:`taifucloudcloud.cdb.v20170320.models.InitDBInstancesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("InitDBInstances", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.InitDBInstancesResponse()
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


    def InquiryPriceUpgradeInstances(self, request):
        """本介面(InquiryPriceUpgradeInstances)用於查詢雲資料庫實例升級的價格，支援查詢按量計費或者包年包月實例的升級價格，實例類型支援主實例、災備實例和只讀實例。

        :param request: 調用InquiryPriceUpgradeInstances所需參數的結構體。
        :type request: :class:`taifucloudcloud.cdb.v20170320.models.InquiryPriceUpgradeInstancesRequest`
        :rtype: :class:`taifucloudcloud.cdb.v20170320.models.InquiryPriceUpgradeInstancesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("InquiryPriceUpgradeInstances", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.InquiryPriceUpgradeInstancesResponse()
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


    def IsolateDBInstance(self, request):
        """本介面(IsolateDBInstance)用於銷毀雲資料庫實例，銷毀之後不能通過IP和端口訪問資料庫，按量計費實例銷毀後直接下線。

        :param request: 調用IsolateDBInstance所需參數的結構體。
        :type request: :class:`taifucloudcloud.cdb.v20170320.models.IsolateDBInstanceRequest`
        :rtype: :class:`taifucloudcloud.cdb.v20170320.models.IsolateDBInstanceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("IsolateDBInstance", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.IsolateDBInstanceResponse()
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


    def ModifyAccountDescription(self, request):
        """本介面(ModifyAccountDescription)用於修改雲資料庫帳戶的備注訊息。

        :param request: 調用ModifyAccountDescription所需參數的結構體。
        :type request: :class:`taifucloudcloud.cdb.v20170320.models.ModifyAccountDescriptionRequest`
        :rtype: :class:`taifucloudcloud.cdb.v20170320.models.ModifyAccountDescriptionResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyAccountDescription", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyAccountDescriptionResponse()
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


    def ModifyAccountPassword(self, request):
        """本介面(ModifyAccountPassword)用於修改雲資料庫帳戶的密碼。

        :param request: 調用ModifyAccountPassword所需參數的結構體。
        :type request: :class:`taifucloudcloud.cdb.v20170320.models.ModifyAccountPasswordRequest`
        :rtype: :class:`taifucloudcloud.cdb.v20170320.models.ModifyAccountPasswordResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyAccountPassword", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyAccountPasswordResponse()
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


    def ModifyAccountPrivileges(self, request):
        """本介面(ModifyAccountPrivileges)用於修改雲資料庫的帳戶的權限訊息。

        :param request: 調用ModifyAccountPrivileges所需參數的結構體。
        :type request: :class:`taifucloudcloud.cdb.v20170320.models.ModifyAccountPrivilegesRequest`
        :rtype: :class:`taifucloudcloud.cdb.v20170320.models.ModifyAccountPrivilegesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyAccountPrivileges", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyAccountPrivilegesResponse()
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


    def ModifyAutoRenewFlag(self, request):
        """本介面(ModifyAutoRenewFlag)用於修改雲資料庫實例的自動續約標記。僅支援包年包月的實例設置自動續約標記。

        :param request: 調用ModifyAutoRenewFlag所需參數的結構體。
        :type request: :class:`taifucloudcloud.cdb.v20170320.models.ModifyAutoRenewFlagRequest`
        :rtype: :class:`taifucloudcloud.cdb.v20170320.models.ModifyAutoRenewFlagResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyAutoRenewFlag", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyAutoRenewFlagResponse()
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


    def ModifyBackupConfig(self, request):
        """本介面(ModifyBackupConfig)用於修改資料庫備份配置訊息。

        :param request: 調用ModifyBackupConfig所需參數的結構體。
        :type request: :class:`taifucloudcloud.cdb.v20170320.models.ModifyBackupConfigRequest`
        :rtype: :class:`taifucloudcloud.cdb.v20170320.models.ModifyBackupConfigResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyBackupConfig", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyBackupConfigResponse()
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


    def ModifyDBInstanceName(self, request):
        """本介面(ModifyDBInstanceName)用於修改雲資料庫實例的名稱。

        :param request: 調用ModifyDBInstanceName所需參數的結構體。
        :type request: :class:`taifucloudcloud.cdb.v20170320.models.ModifyDBInstanceNameRequest`
        :rtype: :class:`taifucloudcloud.cdb.v20170320.models.ModifyDBInstanceNameResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyDBInstanceName", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyDBInstanceNameResponse()
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


    def ModifyDBInstanceProject(self, request):
        """本介面(ModifyDBInstanceProject)用於修改雲資料庫實例的所屬項目。

        :param request: 調用ModifyDBInstanceProject所需參數的結構體。
        :type request: :class:`taifucloudcloud.cdb.v20170320.models.ModifyDBInstanceProjectRequest`
        :rtype: :class:`taifucloudcloud.cdb.v20170320.models.ModifyDBInstanceProjectResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyDBInstanceProject", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyDBInstanceProjectResponse()
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


    def ModifyDBInstanceSecurityGroups(self, request):
        """本介面(ModifyDBInstanceSecurityGroups)用於修改實例綁定的安全組。

        :param request: 調用ModifyDBInstanceSecurityGroups所需參數的結構體。
        :type request: :class:`taifucloudcloud.cdb.v20170320.models.ModifyDBInstanceSecurityGroupsRequest`
        :rtype: :class:`taifucloudcloud.cdb.v20170320.models.ModifyDBInstanceSecurityGroupsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyDBInstanceSecurityGroups", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyDBInstanceSecurityGroupsResponse()
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


    def ModifyDBInstanceVipVport(self, request):
        """本介面(ModifyDBInstanceVipVport)用於修改雲資料庫實例的IP和端口號，也可進行基礎網絡轉VPC網絡和VPC網絡下的子網變更。

        :param request: 調用ModifyDBInstanceVipVport所需參數的結構體。
        :type request: :class:`taifucloudcloud.cdb.v20170320.models.ModifyDBInstanceVipVportRequest`
        :rtype: :class:`taifucloudcloud.cdb.v20170320.models.ModifyDBInstanceVipVportResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyDBInstanceVipVport", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyDBInstanceVipVportResponse()
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


    def ModifyInstanceParam(self, request):
        """本介面(ModifyInstanceParam)用於修改雲資料庫實例的參數。

        :param request: 調用ModifyInstanceParam所需參數的結構體。
        :type request: :class:`taifucloudcloud.cdb.v20170320.models.ModifyInstanceParamRequest`
        :rtype: :class:`taifucloudcloud.cdb.v20170320.models.ModifyInstanceParamResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyInstanceParam", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyInstanceParamResponse()
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


    def ModifyInstanceTag(self, request):
        """可以對實例標簽進行添加、修改或者删除

        :param request: 調用ModifyInstanceTag所需參數的結構體。
        :type request: :class:`taifucloudcloud.cdb.v20170320.models.ModifyInstanceTagRequest`
        :rtype: :class:`taifucloudcloud.cdb.v20170320.models.ModifyInstanceTagResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyInstanceTag", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyInstanceTagResponse()
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


    def ModifyParamTemplate(self, request):
        """該介面（ModifyParamTemplate）用於修改參數範本。

        :param request: 調用ModifyParamTemplate所需參數的結構體。
        :type request: :class:`taifucloudcloud.cdb.v20170320.models.ModifyParamTemplateRequest`
        :rtype: :class:`taifucloudcloud.cdb.v20170320.models.ModifyParamTemplateResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyParamTemplate", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyParamTemplateResponse()
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


    def ModifyTimeWindow(self, request):
        """本介面(ModifyTimeWindow)用於更新雲資料庫實例的維護時間視窗。

        :param request: 調用ModifyTimeWindow所需參數的結構體。
        :type request: :class:`taifucloudcloud.cdb.v20170320.models.ModifyTimeWindowRequest`
        :rtype: :class:`taifucloudcloud.cdb.v20170320.models.ModifyTimeWindowResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyTimeWindow", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyTimeWindowResponse()
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


    def OpenDBInstanceGTID(self, request):
        """本介面(OpenDBInstanceGTID)用於開啓雲資料庫實例的GTID，只支援版本爲5.6以及以上的實例。

        :param request: 調用OpenDBInstanceGTID所需參數的結構體。
        :type request: :class:`taifucloudcloud.cdb.v20170320.models.OpenDBInstanceGTIDRequest`
        :rtype: :class:`taifucloudcloud.cdb.v20170320.models.OpenDBInstanceGTIDResponse`

        """
        try:
            params = request._serialize()
            body = self.call("OpenDBInstanceGTID", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.OpenDBInstanceGTIDResponse()
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


    def OpenWanService(self, request):
        """本介面(OpenWanService)用於開通實例外網訪問。

        注意，實例開通外網訪問之前，需要先将實例進行[實例初始化](https://cloud.taifucloud.com/document/api/236/15873)操作。

        :param request: 調用OpenWanService所需參數的結構體。
        :type request: :class:`taifucloudcloud.cdb.v20170320.models.OpenWanServiceRequest`
        :rtype: :class:`taifucloudcloud.cdb.v20170320.models.OpenWanServiceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("OpenWanService", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.OpenWanServiceResponse()
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


    def RenewDBInstance(self, request):
        """本介面(RenewDBInstance)用於續約雲資料庫實例，僅支援付費模式爲包年包月的實例。按量計費實例不需要續約。

        :param request: 調用RenewDBInstance所需參數的結構體。
        :type request: :class:`taifucloudcloud.cdb.v20170320.models.RenewDBInstanceRequest`
        :rtype: :class:`taifucloudcloud.cdb.v20170320.models.RenewDBInstanceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("RenewDBInstance", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RenewDBInstanceResponse()
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


    def RestartDBInstances(self, request):
        """本介面(RestartDBInstances)用於重啓雲資料庫實例。

        注意：
        1、本介面只支援主實例進行重啓操作；
        2、實例狀态必須爲正常，並且沒有其他異步任務在執行中。

        :param request: 調用RestartDBInstances所需參數的結構體。
        :type request: :class:`taifucloudcloud.cdb.v20170320.models.RestartDBInstancesRequest`
        :rtype: :class:`taifucloudcloud.cdb.v20170320.models.RestartDBInstancesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("RestartDBInstances", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RestartDBInstancesResponse()
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


    def StartBatchRollback(self, request):
        """該介面（StartBatchRollback）用於批次回檔雲資料庫實例的庫表。

        :param request: 調用StartBatchRollback所需參數的結構體。
        :type request: :class:`taifucloudcloud.cdb.v20170320.models.StartBatchRollbackRequest`
        :rtype: :class:`taifucloudcloud.cdb.v20170320.models.StartBatchRollbackResponse`

        """
        try:
            params = request._serialize()
            body = self.call("StartBatchRollback", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.StartBatchRollbackResponse()
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


    def StopDBImportJob(self, request):
        """本介面(StopDBImportJob)用於終止數據導入任務。

        :param request: 調用StopDBImportJob所需參數的結構體。
        :type request: :class:`taifucloudcloud.cdb.v20170320.models.StopDBImportJobRequest`
        :rtype: :class:`taifucloudcloud.cdb.v20170320.models.StopDBImportJobResponse`

        """
        try:
            params = request._serialize()
            body = self.call("StopDBImportJob", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.StopDBImportJobResponse()
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


    def SwitchForUpgrade(self, request):
        """本介面(SwitchForUpgrade)用於切換訪問新實例，針對主升級中的實例處於待切換狀态時，用戶可主動發起該流程

        :param request: 調用SwitchForUpgrade所需參數的結構體。
        :type request: :class:`taifucloudcloud.cdb.v20170320.models.SwitchForUpgradeRequest`
        :rtype: :class:`taifucloudcloud.cdb.v20170320.models.SwitchForUpgradeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("SwitchForUpgrade", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.SwitchForUpgradeResponse()
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
        """本介面(UpgradeDBInstance)用於升級雲資料庫實例，實例類型支援主實例、災備實例和只讀實例

        :param request: 調用UpgradeDBInstance所需參數的結構體。
        :type request: :class:`taifucloudcloud.cdb.v20170320.models.UpgradeDBInstanceRequest`
        :rtype: :class:`taifucloudcloud.cdb.v20170320.models.UpgradeDBInstanceResponse`

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


    def UpgradeDBInstanceEngineVersion(self, request):
        """本介面(UpgradeDBInstanceEngineVersion)用於升級雲資料庫實例版本，實例類型支援主實例、災備實例和只讀實例。

        :param request: 調用UpgradeDBInstanceEngineVersion所需參數的結構體。
        :type request: :class:`taifucloudcloud.cdb.v20170320.models.UpgradeDBInstanceEngineVersionRequest`
        :rtype: :class:`taifucloudcloud.cdb.v20170320.models.UpgradeDBInstanceEngineVersionResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UpgradeDBInstanceEngineVersion", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpgradeDBInstanceEngineVersionResponse()
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


    def VerifyRootAccount(self, request):
        """本介面(VerifyRootAccount)用於校驗雲資料庫實例的ROOT賬號是否有足夠的權限進行授權操作。

        :param request: 調用VerifyRootAccount所需參數的結構體。
        :type request: :class:`taifucloudcloud.cdb.v20170320.models.VerifyRootAccountRequest`
        :rtype: :class:`taifucloudcloud.cdb.v20170320.models.VerifyRootAccountResponse`

        """
        try:
            params = request._serialize()
            body = self.call("VerifyRootAccount", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.VerifyRootAccountResponse()
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