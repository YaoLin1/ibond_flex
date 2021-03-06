#
#  Copyright 2020 The FLEX Authors. All Rights Reserved.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#


from flex.tools.ionic import commu
from flex.crypto.key_exchange.api import make_agreement
from flex.tools.ionic import make_variable_channel
from test.fed_config_example import fed_conf_guest


def test_key_exchange():
    commu.init(fed_conf_guest)
    var_chan = make_variable_channel('test_key_exchange', fed_conf_guest["federation"]["host"][0],
                                     fed_conf_guest["federation"]["guest"][0])

    for times in range(5):
        for each in [2048, 3072, 4096, 6144, 8192]:
            k = make_agreement(remote_id='zhibang-d-014010', key_size=each)
            k2 = var_chan.recv(tag='k')
            assert k == k2
