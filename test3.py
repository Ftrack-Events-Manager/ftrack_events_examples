# -*- coding: utf-8 -*-
"""
@author: LiaoKong
@time: 2021/08/29 17:28 
"""
from ftrack_events_helper import EventBase, subscribe


@subscribe()
class Test3(EventBase):
    event_name = 'test3'

    def run(self, event):
        self.logger.error('这是test3的log')
