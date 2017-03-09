# -*- coding: utf-8 -*-
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import odo

from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults


class SimpleOdoOperator(BaseOperator):
    """
    Use Odo to transfer data from the source to the destination
    """
    template_fields = ('source', 'target',)
    ui_color = '#2980B9'

    @apply_defaults
    def __init__(self,
                 source,
                 target,
                 *args,
                 **kwargs):
        super(SimpleOdoOperator, self).__init__(*args, **kwargs)
        self.source = source
        self.target = target

    def execute(self, context):
        odo.odo(self.source, self.target)


class OdoOperator(BaseOperator):
    """
    Use Odo to transfer data from the source to the destination.
    This will use conn_ids to setup Odo URIs.
    """
    template_fields = ('source', 'target',)
    ui_color = '#2980B9'

    @apply_defaults
    def __init__(self,
                 source,
                 target,
                 source_conn_id,
                 target_conn_id,
                 *args,
                 **kwargs):
        super(OdoOperator, self).__init__(*args, **kwargs)
        self.source = source
        self.target = target
        self.source_conn_id = source_conn_id
        self.target_conn_id = target_conn_id

    def execute(self, context):
        odo.odo(self.source, self.target)
