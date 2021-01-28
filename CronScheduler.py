# -*- coding: utf-8 -*-
"""
Created on Wed Mar 06 10:00:44 2019

@author: Lucas
"""

import os
import getpass
from crontab import CronTab

my_cron = CronTab(user=getpass.getuser())
pulldatajob = my_cron.new(
    command='python ' +
    os.path.join(os.getcwd(), 'PullCurrentData' + '.' + 'py'))
pulldatajob.minute.every(1)
my_cron.write()