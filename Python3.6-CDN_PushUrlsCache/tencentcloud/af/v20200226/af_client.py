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
from taifucloudcloud.af.v20200226 import models


class AfClient(AbstractClient):
    _apiVersion = '2020-02-26'
    _endpoint = 'af.taifucloudcloudapi.com'


    def QueryAntiFraud(self, request):
        """天禦反欺詐服務，主要應用於銀行、證券、保險、P2P等金融行業客戶，通過 的大數據風控能力，
        可以準确識别惡意用戶訊息，解決客戶在支付、活動、理财，風控等業務環節遇到的欺詐威脅，降低企業
        的損失。

        :param request: Request instance for QueryAntiFraud.
        :type request: :class:`taifucloudcloud.af.v20200226.models.QueryAntiFraudRequest`
        :rtype: :class:`taifucloudcloud.af.v20200226.models.QueryAntiFraudResponse`

        """
        try:
            params = request._serialize()
            body = self.call("QueryAntiFraud", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.QueryAntiFraudResponse()
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