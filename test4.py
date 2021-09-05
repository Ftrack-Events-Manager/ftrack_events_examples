# -*- coding: utf-8 -*-
"""
@author: LiaoKong
@time: 2021/08/29 17:28 
"""
from ftrack_events_helper import EventBase, subscribe


@subscribe()
class Test4(EventBase):
    def run(self, event):
        self.logger.warning('这是test4的log')


@subscribe()
class Test7(EventBase):
    event_name = '牛逼777'

    def run(self, event):
        self.logger.warning('这是牛逼777的log')
