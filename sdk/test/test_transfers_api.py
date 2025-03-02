# coding: utf-8

"""
    Yapily API

    To access endpoints that require authentication, use your application key and secret created in the Dashboard (https://dashboard.yapily.com)  # noqa: E501

    OpenAPI spec version: 0.0.155
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import yapily
from yapily.api.transfers_api import TransfersApi  # noqa: E501
from yapily.rest import ApiException


class TestTransfersApi(unittest.TestCase):
    """TransfersApi unit test stubs"""

    def setUp(self):
        self.api = yapily.api.transfers_api.TransfersApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_transfer_using_put(self):
        """Test case for transfer_using_put

        Transfer money from one account to another account accessible with the same consent  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
