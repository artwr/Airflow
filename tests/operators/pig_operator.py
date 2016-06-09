from __future__ import print_function

import doctest
import json
import logging
import os
import re
import unittest
import mock
from datetime import datetime, time, timedelta
from time import sleep

from dateutil.relativedelta import relativedelta

from airflow import configuration
from airflow.executors import SequentialExecutor, LocalExecutor
from airflow.models import Variable

configuration.test_mode()
from airflow import jobs, models, DAG, utils, operators, hooks, macros, settings
from airflow.hooks import BaseHook
from airflow.bin import cli
from airflow.www import app as application
from airflow.settings import Session
from airflow.utils import LoggingMixin, round_time
from lxml import html
from airflow.utils import AirflowException
from airflow.configuration import AirflowConfigException

NUM_EXAMPLE_DAGS = 9
DEV_NULL = '/dev/null'
DEFAULT_DATE = datetime(2015, 1, 1)
DEFAULT_DATE_ISO = DEFAULT_DATE.isoformat()
DEFAULT_DATE_DS = DEFAULT_DATE_ISO[:10]
TEST_DAG_ID = 'unit_tests'
configuration.test_mode()

try:
    import cPickle as pickle
except ImportError:
    # Python 3
    import pickle

class FakeDatetime(datetime):
    "A fake replacement for datetime that can be mocked for testing."
    def __new__(cls, *args, **kwargs):
        return date.__new__(datetime, *args, **kwargs)

def reset(dag_id=TEST_DAG_ID):
    session = Session()
    tis = session.query(models.TaskInstance).filter_by(dag_id=dag_id)
    tis.delete()
    session.commit()
    session.close()

reset()



import unittest

from airflow.operators.pig_operator import PigOperator

