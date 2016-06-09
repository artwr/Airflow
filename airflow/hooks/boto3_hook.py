from future import standard_library
standard_library.install_aliases()
import logging
import re
import fnmatch
import math
import os
from urllib.parse import urlparse
import warnings

import boto3
boto3.set_stream_logger('hooks.boto3', logging.INFO)

from airflow.exceptions import AirflowException
from airflow.hooks.base_hook import BaseHook


class Boto3Hook(BaseHook):
    """
    Abstract base class for boto3 AWS hooks.
    """
    # Override to provide the connection name.
    conn_name_attr = None
    # Override to have a default connection id for a particular boto3 based Hook
    default_conn_name = 'boto3_default_conn_id'

    def __init__(self, *args, **kwargs):
        if not self.conn_name_attr:
            raise AirflowException("conn_name_attr is not defined")
        elif len(args) == 1:
            setattr(self, self.conn_name_attr, args[0])
        elif self.conn_name_attr not in kwargs:
            setattr(self, self.conn_name_attr, self.default_conn_name)
        else:
            setattr(self, self.conn_name_attr, kwargs[self.conn_name_attr])

    def get_boto3_session(**kwargs):
        """
        Get a boto3 session. Useful
        """
        return boto3.session.Session(**kwargs)

    def get_conn(self):
        """Returns a connection object
        """
        raise NotImplementedError()
