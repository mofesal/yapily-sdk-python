# coding: utf-8

"""
    Yapily API

    To access endpoints that require authentication, use your application key and secret created in the Dashboard (https://dashboard.yapily.com)  # noqa: E501

    OpenAPI spec version: 0.0.131
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from yapily.models.account_statement import AccountStatement  # noqa: F401,E501
from yapily.models.response_meta import ResponseMeta  # noqa: F401,E501


class ApiResponseOfAccountStatement(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'meta': 'ResponseMeta',
        'data': 'AccountStatement',
        'links': 'dict(str, str)'
    }

    attribute_map = {
        'meta': 'meta',
        'data': 'data',
        'links': 'links'
    }

    def __init__(self, meta=None, data=None, links=None):  # noqa: E501
        """ApiResponseOfAccountStatement - a model defined in Swagger"""  # noqa: E501

        self._meta = None
        self._data = None
        self._links = None
        self.discriminator = None

        if meta is not None:
            self.meta = meta
        if data is not None:
            self.data = data
        if links is not None:
            self.links = links

    @property
    def meta(self):
        """Gets the meta of this ApiResponseOfAccountStatement.  # noqa: E501


        :return: The meta of this ApiResponseOfAccountStatement.  # noqa: E501
        :rtype: ResponseMeta
        """
        return self._meta

    @meta.setter
    def meta(self, meta):
        """Sets the meta of this ApiResponseOfAccountStatement.


        :param meta: The meta of this ApiResponseOfAccountStatement.  # noqa: E501
        :type: ResponseMeta
        """

        self._meta = meta

    @property
    def data(self):
        """Gets the data of this ApiResponseOfAccountStatement.  # noqa: E501


        :return: The data of this ApiResponseOfAccountStatement.  # noqa: E501
        :rtype: AccountStatement
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this ApiResponseOfAccountStatement.


        :param data: The data of this ApiResponseOfAccountStatement.  # noqa: E501
        :type: AccountStatement
        """

        self._data = data

    @property
    def links(self):
        """Gets the links of this ApiResponseOfAccountStatement.  # noqa: E501


        :return: The links of this ApiResponseOfAccountStatement.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this ApiResponseOfAccountStatement.


        :param links: The links of this ApiResponseOfAccountStatement.  # noqa: E501
        :type: dict(str, str)
        """

        self._links = links

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ApiResponseOfAccountStatement):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
