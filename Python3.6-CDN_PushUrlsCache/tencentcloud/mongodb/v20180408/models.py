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

from taifucloudcloud.common.abstract_model import AbstractModel


class AssignProjectRequest(AbstractModel):
    """AssignProject請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceIds: 實例ID清單，格式如：cmgo-p8vnipr5。與雲資料庫控制台頁面中顯示的實例ID相同
        :type InstanceIds: list of str
        :param ProjectId: 項目ID
        :type ProjectId: int
        """
        self.InstanceIds = None
        self.ProjectId = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")
        self.ProjectId = params.get("ProjectId")


class AssignProjectResponse(AbstractModel):
    """AssignProject返回參數結構體

    """

    def __init__(self):
        """
        :param FlowIds: 返回的異步任務ID清單
        :type FlowIds: list of int non-negative
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.FlowIds = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FlowIds = params.get("FlowIds")
        self.RequestId = params.get("RequestId")


class ClientConnection(AbstractModel):
    """用戶端連接訊息，包括用戶端IP和連接數

    """

    def __init__(self):
        """
        :param IP: 連接的用戶端IP
        :type IP: str
        :param Count: 對應用戶端IP的連接數
        :type Count: int
        """
        self.IP = None
        self.Count = None


    def _deserialize(self, params):
        self.IP = params.get("IP")
        self.Count = params.get("Count")


class CreateDBInstanceHourRequest(AbstractModel):
    """CreateDBInstanceHour請求參數結構體

    """

    def __init__(self):
        """
        :param Memory: 實例内存大小，單位：GB
        :type Memory: int
        :param Volume: 實例硬碟大小，單位：GB
        :type Volume: int
        :param ReplicateSetNum: 副本集個數，1爲單副本集實例，大於1爲分片集群實例，最大不超過10
        :type ReplicateSetNum: int
        :param SecondaryNum: 每個副本集内從節點個數，目前只支援從節點數爲2
        :type SecondaryNum: int
        :param EngineVersion: MongoDB引擎版本，值包括MONGO_3_WT 、MONGO_3_ROCKS和MONGO_36_WT
        :type EngineVersion: str
        :param Machine: 實例類型，GIO：高IO版；TGIO：高IO萬兆
        :type Machine: str
        :param GoodsNum: 實例數量，預設值爲1, 最小值1，最大值爲10
        :type GoodsNum: int
        :param Zone: 可用區訊息，格式如：ap-guangzhou-2
        :type Zone: str
        :param InstanceRole: 實例角色，支援值包括：MASTER-表示主實例，DR-表示災備實例，RO-表示只讀實例
        :type InstanceRole: str
        :param InstanceType: 實例類型，REPLSET-副本集，SHARD-分片集群
        :type InstanceType: str
        :param Encrypt: 數據是否加密，當且僅當引擎版本爲MONGO_3_ROCKS，可以選擇加密
        :type Encrypt: int
        :param VpcId: 私有網絡ID，如果不傳則預設選擇基礎網絡
        :type VpcId: str
        :param SubnetId: 私有網絡下的子網ID，如果設置了 VpcId，則 SubnetId必填
        :type SubnetId: str
        :param ProjectId: 項目ID，不填爲預設項目
        :type ProjectId: int
        :param SecurityGroup: 安全組參數
        :type SecurityGroup: list of str
        """
        self.Memory = None
        self.Volume = None
        self.ReplicateSetNum = None
        self.SecondaryNum = None
        self.EngineVersion = None
        self.Machine = None
        self.GoodsNum = None
        self.Zone = None
        self.InstanceRole = None
        self.InstanceType = None
        self.Encrypt = None
        self.VpcId = None
        self.SubnetId = None
        self.ProjectId = None
        self.SecurityGroup = None


    def _deserialize(self, params):
        self.Memory = params.get("Memory")
        self.Volume = params.get("Volume")
        self.ReplicateSetNum = params.get("ReplicateSetNum")
        self.SecondaryNum = params.get("SecondaryNum")
        self.EngineVersion = params.get("EngineVersion")
        self.Machine = params.get("Machine")
        self.GoodsNum = params.get("GoodsNum")
        self.Zone = params.get("Zone")
        self.InstanceRole = params.get("InstanceRole")
        self.InstanceType = params.get("InstanceType")
        self.Encrypt = params.get("Encrypt")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.ProjectId = params.get("ProjectId")
        self.SecurityGroup = params.get("SecurityGroup")


class CreateDBInstanceHourResponse(AbstractModel):
    """CreateDBInstanceHour返回參數結構體

    """

    def __init__(self):
        """
        :param DealId: 訂單ID
        :type DealId: str
        :param InstanceIds: 創建的實例ID清單
        :type InstanceIds: list of str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.DealId = None
        self.InstanceIds = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DealId = params.get("DealId")
        self.InstanceIds = params.get("InstanceIds")
        self.RequestId = params.get("RequestId")


class CreateDBInstanceRequest(AbstractModel):
    """CreateDBInstance請求參數結構體

    """

    def __init__(self):
        """
        :param SecondaryNum: 每個副本集内從節點個數
        :type SecondaryNum: int
        :param Memory: 實例内存大小，單位：GB
        :type Memory: int
        :param Volume: 實例硬碟大小，單位：GB
        :type Volume: int
        :param MongoVersion: 版本號，當前支援 MONGO_3_WT、MONGO_3_ROCKS、MONGO_36_WT
        :type MongoVersion: str
        :param MachineCode: 機器類型，GIO：高IO版；TGIO：高IO萬兆
        :type MachineCode: str
        :param GoodsNum: 實例數量，預設值爲1, 最小值1，最大值爲10
        :type GoodsNum: int
        :param Zone: 實例所屬區域名稱，格式如：ap-guangzhou-2
        :type Zone: str
        :param TimeSpan: 時長，購買月數
        :type TimeSpan: int
        :param Password: 實例密碼
        :type Password: str
        :param ProjectId: 項目ID，不填爲預設項目
        :type ProjectId: int
        :param SecurityGroup: 安全組參數
        :type SecurityGroup: list of str
        :param UniqVpcId: 私有網絡ID，如果不傳則預設選擇基礎網絡
        :type UniqVpcId: str
        :param UniqSubnetId: 私有網絡下的子網ID，如果設置了 VpcId，則 SubnetId必填
        :type UniqSubnetId: str
        """
        self.SecondaryNum = None
        self.Memory = None
        self.Volume = None
        self.MongoVersion = None
        self.MachineCode = None
        self.GoodsNum = None
        self.Zone = None
        self.TimeSpan = None
        self.Password = None
        self.ProjectId = None
        self.SecurityGroup = None
        self.UniqVpcId = None
        self.UniqSubnetId = None


    def _deserialize(self, params):
        self.SecondaryNum = params.get("SecondaryNum")
        self.Memory = params.get("Memory")
        self.Volume = params.get("Volume")
        self.MongoVersion = params.get("MongoVersion")
        self.MachineCode = params.get("MachineCode")
        self.GoodsNum = params.get("GoodsNum")
        self.Zone = params.get("Zone")
        self.TimeSpan = params.get("TimeSpan")
        self.Password = params.get("Password")
        self.ProjectId = params.get("ProjectId")
        self.SecurityGroup = params.get("SecurityGroup")
        self.UniqVpcId = params.get("UniqVpcId")
        self.UniqSubnetId = params.get("UniqSubnetId")


class CreateDBInstanceResponse(AbstractModel):
    """CreateDBInstance返回參數結構體

    """

    def __init__(self):
        """
        :param DealId: 訂單ID
        :type DealId: str
        :param InstanceIds: 創建的實例ID清單
        :type InstanceIds: list of str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.DealId = None
        self.InstanceIds = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DealId = params.get("DealId")
        self.InstanceIds = params.get("InstanceIds")
        self.RequestId = params.get("RequestId")


class DescribeClientConnectionsRequest(AbstractModel):
    """DescribeClientConnections請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 實例ID，格式如：cmgo-p8vnipr5。與雲資料庫控制台頁面中顯示的實例ID相同
        :type InstanceId: str
        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")


class DescribeClientConnectionsResponse(AbstractModel):
    """DescribeClientConnections返回參數結構體

    """

    def __init__(self):
        """
        :param Clients: 用戶端連接訊息，包括用戶端IP和對應IP的連接數量
注意：此欄位可能返回 null，表示取不到有效值。
        :type Clients: list of ClientConnection
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Clients = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Clients") is not None:
            self.Clients = []
            for item in params.get("Clients"):
                obj = ClientConnection()
                obj._deserialize(item)
                self.Clients.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDBInstancesRequest(AbstractModel):
    """DescribeDBInstances請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceIds: 實例ID清單，格式如：cmgo-p8vnipr5。與雲資料庫控制台頁面中顯示的實例ID相同
        :type InstanceIds: list of str
        :param InstanceType: 實例類型，取值範圍：0-所有實例,1-正式實例，2-臨時實例, 3-只讀實例，-1-正式實例+只讀+災備實例
        :type InstanceType: int
        :param ClusterType: 集群類型，取值範圍：0-副本集實例，1-分片實例，-1-所有實例
        :type ClusterType: int
        :param Status: 實例狀态，取值範圍：0-待初始化，1-流程執行中，2-實例有效，-2-實例已過期
        :type Status: list of int
        :param VpcId: 私有網絡的ID，基礎網絡則不傳該參數
        :type VpcId: str
        :param SubnetId: 私有網絡的子網ID，基礎網絡則不傳該參數。入參設置該參數的同時，必須設置相應的VpcId
        :type SubnetId: str
        :param PayMode: 付費類型，取值範圍：0-按量計費，1-包年包月，-1-按量計費+包年包月
        :type PayMode: int
        :param Limit: 單次請求返回的數量，最小值爲1，最大值爲100，預設值爲20
        :type Limit: int
        :param Offset: 偏移量，預設值爲0
        :type Offset: int
        :param OrderBy: 返回結果集排序的欄位，目前支援："ProjectId", "InstanceName", "CreateTime"，預設爲升序排序
        :type OrderBy: str
        :param OrderByType: 返回結果集排序方式，目前支援："ASC"或者"DESC"
        :type OrderByType: str
        """
        self.InstanceIds = None
        self.InstanceType = None
        self.ClusterType = None
        self.Status = None
        self.VpcId = None
        self.SubnetId = None
        self.PayMode = None
        self.Limit = None
        self.Offset = None
        self.OrderBy = None
        self.OrderByType = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")
        self.InstanceType = params.get("InstanceType")
        self.ClusterType = params.get("ClusterType")
        self.Status = params.get("Status")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.PayMode = params.get("PayMode")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.OrderBy = params.get("OrderBy")
        self.OrderByType = params.get("OrderByType")


class DescribeDBInstancesResponse(AbstractModel):
    """DescribeDBInstances返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 符合查詢條件的實例總數
        :type TotalCount: int
        :param InstanceDetails: 實例詳細訊息
        :type InstanceDetails: list of MongoDBInstanceDetail
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.InstanceDetails = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("InstanceDetails") is not None:
            self.InstanceDetails = []
            for item in params.get("InstanceDetails"):
                obj = MongoDBInstanceDetail()
                obj._deserialize(item)
                self.InstanceDetails.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeSlowLogRequest(AbstractModel):
    """DescribeSlowLog請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 實例ID，格式如：cmgo-p8vnipr5。與雲資料庫控制台頁面中顯示的實例ID相同
        :type InstanceId: str
        :param StartTime: 慢日志起始時間，格式：yyyy-mm-dd hh:mm:ss，如：2019-06-01 10:00:00。查詢起止時間間隔不能超過24小時，只允許查詢最近7天内慢日志。
        :type StartTime: str
        :param EndTime: 慢日志終止時間，格式：yyyy-mm-dd hh:mm:ss，如：2019-06-02 12:00:00。查詢起止時間間隔不能超過24小時，只允許查詢最近7天内慢日志。
        :type EndTime: str
        :param SlowMS: 慢日志執行時間阈值，返回執行時間超過該阈值的慢日志，單位爲毫秒(ms)，最小爲100毫秒。
        :type SlowMS: int
        :param Offset: 偏移量，最小值爲0，最大值爲10000，預設值爲0。
        :type Offset: int
        :param Limit: 分頁大小，最小值爲1，最大值爲100，預設值爲20。
        :type Limit: int
        """
        self.InstanceId = None
        self.StartTime = None
        self.EndTime = None
        self.SlowMS = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.SlowMS = params.get("SlowMS")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeSlowLogResponse(AbstractModel):
    """DescribeSlowLog返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 符合查詢條件的慢查詢日志總數。
        :type TotalCount: int
        :param SlowLogList: 符合查詢條件的慢查詢日志詳情。
        :type SlowLogList: list of str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.SlowLogList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        self.SlowLogList = params.get("SlowLogList")
        self.RequestId = params.get("RequestId")


class DescribeSpecInfoRequest(AbstractModel):
    """DescribeSpecInfo請求參數結構體

    """

    def __init__(self):
        """
        :param Zone: 可用區
        :type Zone: str
        """
        self.Zone = None


    def _deserialize(self, params):
        self.Zone = params.get("Zone")


class DescribeSpecInfoResponse(AbstractModel):
    """DescribeSpecInfo返回參數結構體

    """

    def __init__(self):
        """
        :param SpecInfoList: 實例售賣規格訊息清單
        :type SpecInfoList: list of SpecificationInfo
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.SpecInfoList = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("SpecInfoList") is not None:
            self.SpecInfoList = []
            for item in params.get("SpecInfoList"):
                obj = SpecificationInfo()
                obj._deserialize(item)
                self.SpecInfoList.append(obj)
        self.RequestId = params.get("RequestId")


class MongoDBInstance(AbstractModel):
    """實例訊息

    """

    def __init__(self):
        """
        :param InstanceId: 實例ID
        :type InstanceId: str
        :param Region: 地域訊息
        :type Region: str
        """
        self.InstanceId = None
        self.Region = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Region = params.get("Region")


class MongoDBInstanceDetail(AbstractModel):
    """實例詳情

    """

    def __init__(self):
        """
        :param InstanceId: 實例ID
        :type InstanceId: str
        :param InstanceName: 實例名稱
        :type InstanceName: str
        :param PayMode: 付費類型，可能的返回值：1-包年包月；0-按量計費
        :type PayMode: int
        :param ProjectId: 項目ID
        :type ProjectId: int
        :param ClusterType: 集群類型，可能的返回值：0-副本集實例，1-分片實例，
        :type ClusterType: int
        :param Region: 地域訊息
        :type Region: str
        :param Zone: 可用區訊息
        :type Zone: str
        :param NetType: 網絡類型，可能的返回值：0-基礎網絡，1-私有網絡
        :type NetType: int
        :param VpcId: 私有網絡的ID
        :type VpcId: str
        :param SubnetId: 私有網絡的子網ID
        :type SubnetId: str
        :param Status: 實例狀态，可能的返回值：0-待初始化，1-流程處理中，2-運作中，-2-實例已過期
        :type Status: int
        :param Vip: 實例IP
        :type Vip: str
        :param Vport: 端口號
        :type Vport: int
        :param CreateTime: 實例創建時間
        :type CreateTime: str
        :param DeadLine: 實例到期時間
        :type DeadLine: str
        :param MongoVersion: 實例版本訊息
        :type MongoVersion: str
        :param Memory: 實例内存規格，單位爲MB
        :type Memory: int
        :param Volume: 實例磁盤規格，單位爲MB
        :type Volume: int
        :param CpuNum: 實例CPU核心數
        :type CpuNum: int
        :param MachineType: 實例機器類型
        :type MachineType: str
        :param SecondaryNum: 實例從節點數
        :type SecondaryNum: int
        :param ReplicationSetNum: 實例分片數
        :type ReplicationSetNum: int
        :param AutoRenewFlag: 實例自動續約標志，可能的返回值：0-手動續約，1-自動續約，2-确認不續約
        :type AutoRenewFlag: int
        :param UsedVolume: 已用容量，單位MB
        :type UsedVolume: int
        :param MaintenanceStart: 維護視窗起始時間
        :type MaintenanceStart: str
        :param MaintenanceEnd: 維護視窗結束時間
        :type MaintenanceEnd: str
        :param ReplicaSets: 分片訊息
        :type ReplicaSets: list of MongodbShardInfo
        :param ReadonlyInstances: 只讀實例訊息
注意：此欄位可能返回 null，表示取不到有效值。
        :type ReadonlyInstances: list of MongoDBInstance
        :param StandbyInstances: 災備實例訊息
注意：此欄位可能返回 null，表示取不到有效值。
        :type StandbyInstances: list of MongoDBInstance
        :param CloneInstances: 臨時實例訊息
注意：此欄位可能返回 null，表示取不到有效值。
        :type CloneInstances: list of MongoDBInstance
        :param RelatedInstance: 關聯實例訊息，對於正式實例，該欄位表示它的臨時實例訊息；對於臨時實例，則表示它的正式實例訊息;如果爲只讀/災備實例,則表示他的主實例訊息
注意：此欄位可能返回 null，表示取不到有效值。
        :type RelatedInstance: :class:`taifucloudcloud.mongodb.v20180408.models.MongoDBInstance`
        :param Tags: 實例標簽訊息集合
注意：此欄位可能返回 null，表示取不到有效值。
        :type Tags: list of TagInfo
        :param InstanceVer: 實例標記
        :type InstanceVer: int
        :param ClusterVer: 實例標記
        :type ClusterVer: int
        :param Protocol: 協議訊息，可能的返回值：1-mongodb，2-dynamodb
        :type Protocol: int
        :param InstanceType: 實例類型，可能的返回值，1-正式實例，2-臨時實例，3-只讀實例，4-災備實例
        :type InstanceType: int
        :param InstanceStatusDesc: 實例狀态描述
        :type InstanceStatusDesc: str
        :param RealInstanceId: 實例對應的物理實例ID，回檔並替換過的實例有不同的InstanceId和RealInstanceId，從barad獲取監控數據等場景下需要用物理id獲取
        :type RealInstanceId: str
        """
        self.InstanceId = None
        self.InstanceName = None
        self.PayMode = None
        self.ProjectId = None
        self.ClusterType = None
        self.Region = None
        self.Zone = None
        self.NetType = None
        self.VpcId = None
        self.SubnetId = None
        self.Status = None
        self.Vip = None
        self.Vport = None
        self.CreateTime = None
        self.DeadLine = None
        self.MongoVersion = None
        self.Memory = None
        self.Volume = None
        self.CpuNum = None
        self.MachineType = None
        self.SecondaryNum = None
        self.ReplicationSetNum = None
        self.AutoRenewFlag = None
        self.UsedVolume = None
        self.MaintenanceStart = None
        self.MaintenanceEnd = None
        self.ReplicaSets = None
        self.ReadonlyInstances = None
        self.StandbyInstances = None
        self.CloneInstances = None
        self.RelatedInstance = None
        self.Tags = None
        self.InstanceVer = None
        self.ClusterVer = None
        self.Protocol = None
        self.InstanceType = None
        self.InstanceStatusDesc = None
        self.RealInstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.InstanceName = params.get("InstanceName")
        self.PayMode = params.get("PayMode")
        self.ProjectId = params.get("ProjectId")
        self.ClusterType = params.get("ClusterType")
        self.Region = params.get("Region")
        self.Zone = params.get("Zone")
        self.NetType = params.get("NetType")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.Status = params.get("Status")
        self.Vip = params.get("Vip")
        self.Vport = params.get("Vport")
        self.CreateTime = params.get("CreateTime")
        self.DeadLine = params.get("DeadLine")
        self.MongoVersion = params.get("MongoVersion")
        self.Memory = params.get("Memory")
        self.Volume = params.get("Volume")
        self.CpuNum = params.get("CpuNum")
        self.MachineType = params.get("MachineType")
        self.SecondaryNum = params.get("SecondaryNum")
        self.ReplicationSetNum = params.get("ReplicationSetNum")
        self.AutoRenewFlag = params.get("AutoRenewFlag")
        self.UsedVolume = params.get("UsedVolume")
        self.MaintenanceStart = params.get("MaintenanceStart")
        self.MaintenanceEnd = params.get("MaintenanceEnd")
        if params.get("ReplicaSets") is not None:
            self.ReplicaSets = []
            for item in params.get("ReplicaSets"):
                obj = MongodbShardInfo()
                obj._deserialize(item)
                self.ReplicaSets.append(obj)
        if params.get("ReadonlyInstances") is not None:
            self.ReadonlyInstances = []
            for item in params.get("ReadonlyInstances"):
                obj = MongoDBInstance()
                obj._deserialize(item)
                self.ReadonlyInstances.append(obj)
        if params.get("StandbyInstances") is not None:
            self.StandbyInstances = []
            for item in params.get("StandbyInstances"):
                obj = MongoDBInstance()
                obj._deserialize(item)
                self.StandbyInstances.append(obj)
        if params.get("CloneInstances") is not None:
            self.CloneInstances = []
            for item in params.get("CloneInstances"):
                obj = MongoDBInstance()
                obj._deserialize(item)
                self.CloneInstances.append(obj)
        if params.get("RelatedInstance") is not None:
            self.RelatedInstance = MongoDBInstance()
            self.RelatedInstance._deserialize(params.get("RelatedInstance"))
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = TagInfo()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.InstanceVer = params.get("InstanceVer")
        self.ClusterVer = params.get("ClusterVer")
        self.Protocol = params.get("Protocol")
        self.InstanceType = params.get("InstanceType")
        self.InstanceStatusDesc = params.get("InstanceStatusDesc")
        self.RealInstanceId = params.get("RealInstanceId")


class MongodbShardInfo(AbstractModel):
    """實例分片詳情

    """

    def __init__(self):
        """
        :param UsedVolume: 分片已使用容量
        :type UsedVolume: float
        :param ReplicaSetId: 分片ID
        :type ReplicaSetId: str
        :param ReplicaSetName: 分片名
        :type ReplicaSetName: str
        :param Memory: 分片内存規格，單位爲MB
        :type Memory: int
        :param Volume: 分片磁盤規格，單位爲MB
        :type Volume: int
        :param OplogSize: 分片Oplog大小，單位爲MB
        :type OplogSize: int
        :param SecondaryNum: 分片從節點數
        :type SecondaryNum: int
        :param RealReplicaSetId: 分片物理ID
        :type RealReplicaSetId: str
        """
        self.UsedVolume = None
        self.ReplicaSetId = None
        self.ReplicaSetName = None
        self.Memory = None
        self.Volume = None
        self.OplogSize = None
        self.SecondaryNum = None
        self.RealReplicaSetId = None


    def _deserialize(self, params):
        self.UsedVolume = params.get("UsedVolume")
        self.ReplicaSetId = params.get("ReplicaSetId")
        self.ReplicaSetName = params.get("ReplicaSetName")
        self.Memory = params.get("Memory")
        self.Volume = params.get("Volume")
        self.OplogSize = params.get("OplogSize")
        self.SecondaryNum = params.get("SecondaryNum")
        self.RealReplicaSetId = params.get("RealReplicaSetId")


class RenameInstanceRequest(AbstractModel):
    """RenameInstance請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 實例ID，格式如：cmgo-p8vnipr5。與雲資料庫控制台頁面中顯示的實例ID相同
        :type InstanceId: str
        :param NewName: 實例名稱
        :type NewName: str
        """
        self.InstanceId = None
        self.NewName = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.NewName = params.get("NewName")


class RenameInstanceResponse(AbstractModel):
    """RenameInstance返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class SetAutoRenewRequest(AbstractModel):
    """SetAutoRenew請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceIds: 實例ID清單，格式如：cmgo-p8vnipr5。與雲資料庫控制台頁面中顯示的實例ID相同
        :type InstanceIds: list of str
        :param AutoRenewFlag: 續約選項，取值範圍：0-手動續約，1-自動續約，2-确認不續約
        :type AutoRenewFlag: int
        """
        self.InstanceIds = None
        self.AutoRenewFlag = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")
        self.AutoRenewFlag = params.get("AutoRenewFlag")


class SetAutoRenewResponse(AbstractModel):
    """SetAutoRenew返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class SetPasswordRequest(AbstractModel):
    """SetPassword請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 實例ID，格式如：cmgo-p8vnipr5。與雲資料庫控制台頁面中顯示的實例ID相同
        :type InstanceId: str
        :param UserName: 實例帳戶名稱
        :type UserName: str
        :param Password: 實例新密碼，至少包含字母、數字和字元（!@#%^*()）中的兩種，長度爲8-16個字元
        :type Password: str
        """
        self.InstanceId = None
        self.UserName = None
        self.Password = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.UserName = params.get("UserName")
        self.Password = params.get("Password")


class SetPasswordResponse(AbstractModel):
    """SetPassword返回參數結構體

    """

    def __init__(self):
        """
        :param FlowId: 返回的異步任務ID
        :type FlowId: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.FlowId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        self.RequestId = params.get("RequestId")


class SpecItem(AbstractModel):
    """mongodb售賣規格

    """

    def __init__(self):
        """
        :param SpecCode: 規格訊息標識
        :type SpecCode: str
        :param Status: 規格有效標志，取值：0-停止售賣，1-開放售賣
        :type Status: int
        :param MachineType: 機器類型，取值：0-HIO，4-HIO10G
        :type MachineType: str
        :param Cpu: cpu核心數
        :type Cpu: int
        :param Memory: 内存規格，單位爲MB
        :type Memory: int
        :param DefaultStorage: 預設磁盤規格，單位MB
        :type DefaultStorage: int
        :param MaxStorage: 最大磁盤規格，單位MB
        :type MaxStorage: int
        :param MinStorage: 最小磁盤規格，單位MB
        :type MinStorage: int
        :param Qps: 可承載qps訊息
        :type Qps: int
        :param Conns: 連接數限制
        :type Conns: int
        :param MongoVersionCode: 實例mongodb版本訊息
        :type MongoVersionCode: str
        :param MongoVersionValue: 實例mongodb版本號
        :type MongoVersionValue: int
        :param Version: 實例mongodb版本號（短）
        :type Version: str
        :param EngineName: 儲存引擎
        :type EngineName: str
        :param ClusterType: 集群類型，取值：1-分片集群，0-副本集集群
        :type ClusterType: int
        :param MinNodeNum: 最小副本集從節點數
        :type MinNodeNum: int
        :param MaxNodeNum: 最大副本集從節點數
        :type MaxNodeNum: int
        :param MinReplicateSetNum: 最小分片數
        :type MinReplicateSetNum: int
        :param MaxReplicateSetNum: 最大分片數
        :type MaxReplicateSetNum: int
        :param MinReplicateSetNodeNum: 最小分片從節點數
        :type MinReplicateSetNodeNum: int
        :param MaxReplicateSetNodeNum: 最大分片從節點數
        :type MaxReplicateSetNodeNum: int
        """
        self.SpecCode = None
        self.Status = None
        self.MachineType = None
        self.Cpu = None
        self.Memory = None
        self.DefaultStorage = None
        self.MaxStorage = None
        self.MinStorage = None
        self.Qps = None
        self.Conns = None
        self.MongoVersionCode = None
        self.MongoVersionValue = None
        self.Version = None
        self.EngineName = None
        self.ClusterType = None
        self.MinNodeNum = None
        self.MaxNodeNum = None
        self.MinReplicateSetNum = None
        self.MaxReplicateSetNum = None
        self.MinReplicateSetNodeNum = None
        self.MaxReplicateSetNodeNum = None


    def _deserialize(self, params):
        self.SpecCode = params.get("SpecCode")
        self.Status = params.get("Status")
        self.MachineType = params.get("MachineType")
        self.Cpu = params.get("Cpu")
        self.Memory = params.get("Memory")
        self.DefaultStorage = params.get("DefaultStorage")
        self.MaxStorage = params.get("MaxStorage")
        self.MinStorage = params.get("MinStorage")
        self.Qps = params.get("Qps")
        self.Conns = params.get("Conns")
        self.MongoVersionCode = params.get("MongoVersionCode")
        self.MongoVersionValue = params.get("MongoVersionValue")
        self.Version = params.get("Version")
        self.EngineName = params.get("EngineName")
        self.ClusterType = params.get("ClusterType")
        self.MinNodeNum = params.get("MinNodeNum")
        self.MaxNodeNum = params.get("MaxNodeNum")
        self.MinReplicateSetNum = params.get("MinReplicateSetNum")
        self.MaxReplicateSetNum = params.get("MaxReplicateSetNum")
        self.MinReplicateSetNodeNum = params.get("MinReplicateSetNodeNum")
        self.MaxReplicateSetNodeNum = params.get("MaxReplicateSetNodeNum")


class SpecificationInfo(AbstractModel):
    """實例規格訊息

    """

    def __init__(self):
        """
        :param Region: 地域訊息
        :type Region: str
        :param Zone: 可用區訊息
        :type Zone: str
        :param SpecItems: 售賣規格訊息
        :type SpecItems: list of SpecItem
        """
        self.Region = None
        self.Zone = None
        self.SpecItems = None


    def _deserialize(self, params):
        self.Region = params.get("Region")
        self.Zone = params.get("Zone")
        if params.get("SpecItems") is not None:
            self.SpecItems = []
            for item in params.get("SpecItems"):
                obj = SpecItem()
                obj._deserialize(item)
                self.SpecItems.append(obj)


class TagInfo(AbstractModel):
    """實例標簽訊息

    """

    def __init__(self):
        """
        :param TagKey: 標簽Key值
        :type TagKey: str
        :param TagValue: 標簽值
        :type TagValue: str
        """
        self.TagKey = None
        self.TagValue = None


    def _deserialize(self, params):
        self.TagKey = params.get("TagKey")
        self.TagValue = params.get("TagValue")


class TerminateDBInstanceRequest(AbstractModel):
    """TerminateDBInstance請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 實例ID，格式如：cmgo-p8vnipr5。
        :type InstanceId: str
        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")


class TerminateDBInstanceResponse(AbstractModel):
    """TerminateDBInstance返回參數結構體

    """

    def __init__(self):
        """
        :param AsyncRequestId: 訂單ID，表示注銷實例成功
        :type AsyncRequestId: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.AsyncRequestId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AsyncRequestId = params.get("AsyncRequestId")
        self.RequestId = params.get("RequestId")


class UpgradeDBInstanceHourRequest(AbstractModel):
    """UpgradeDBInstanceHour請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 實例ID，格式如：cmgo-p8vnipr5
        :type InstanceId: str
        :param Memory: 升級後的内存大小，單位：GB
        :type Memory: int
        :param Volume: 升級後的硬碟大小，單位：GB
        :type Volume: int
        :param OplogSize: 升級後oplog的大小，單位：GB，預設爲磁盤空間的10%，允許設置的最小值爲磁盤的10%，最大值爲磁盤的90%
        :type OplogSize: int
        """
        self.InstanceId = None
        self.Memory = None
        self.Volume = None
        self.OplogSize = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Memory = params.get("Memory")
        self.Volume = params.get("Volume")
        self.OplogSize = params.get("OplogSize")


class UpgradeDBInstanceHourResponse(AbstractModel):
    """UpgradeDBInstanceHour返回參數結構體

    """

    def __init__(self):
        """
        :param DealId: 訂單ID
        :type DealId: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.DealId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DealId = params.get("DealId")
        self.RequestId = params.get("RequestId")


class UpgradeDBInstanceRequest(AbstractModel):
    """UpgradeDBInstance請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 實例ID，格式如：cmgo-p8vnipr5。與雲資料庫控制台頁面中顯示的實例ID相同
        :type InstanceId: str
        :param Memory: 升級後的内存大小，單位：GB
        :type Memory: int
        :param Volume: 升級後的硬碟大小，單位：GB
        :type Volume: int
        :param OplogSize: 升級後oplog的大小，單位：GB，預設爲磁盤空間的10%，允許設置的最小值爲磁盤的10%，最大值爲磁盤的90%
        :type OplogSize: int
        """
        self.InstanceId = None
        self.Memory = None
        self.Volume = None
        self.OplogSize = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Memory = params.get("Memory")
        self.Volume = params.get("Volume")
        self.OplogSize = params.get("OplogSize")


class UpgradeDBInstanceResponse(AbstractModel):
    """UpgradeDBInstance返回參數結構體

    """

    def __init__(self):
        """
        :param DealId: 訂單ID
        :type DealId: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.DealId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DealId = params.get("DealId")
        self.RequestId = params.get("RequestId")