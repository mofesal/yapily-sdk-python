# coding: utf-8

"""
    Yapily API

    To access endpoints that require authentication, use your application key and secret created in the Dashboard (https://dashboard.yapily.com)  # noqa: E501

    OpenAPI spec version: 0.0.155
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class UserDeleteRequest(object):
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
        'user_uuids': 'list[str]',
        'application_user_ids': 'list[str]'
    }

    attribute_map = {
        'user_uuids': 'userUuids',
        'application_user_ids': 'applicationUserIds'
    }

    def __init__(self, user_uuids=None, application_user_ids=None):  # noqa: E501
        """UserDeleteRequest - a model defined in Swagger"""  # noqa: E501

        self._user_uuids = None
        self._application_user_ids = None
        self.discriminator = None

        if user_uuids is not None:
            self.user_uuids = user_uuids
        if application_user_ids is not None:
            self.application_user_ids = application_user_ids

    @property
    def user_uuids(self):
        """Gets the user_uuids of this UserDeleteRequest.  # noqa: E501


        :return: The user_uuids of this UserDeleteRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._user_uuids

    @user_uuids.setter
    def user_uuids(self, user_uuids):
        """Sets the user_uuids of this UserDeleteRequest.


        :param user_uuids: The user_uuids of this UserDeleteRequest.  # noqa: E501
        :type: list[str]
        """

        self._user_uuids = user_uuids

    @property
    def application_user_ids(self):
        """Gets the application_user_ids of this UserDeleteRequest.  # noqa: E501


        :return: The application_user_ids of this UserDeleteRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._application_user_ids

    @application_user_ids.setter
    def application_user_ids(self, application_user_ids):
        """Sets the application_user_ids of this UserDeleteRequest.


        :param application_user_ids: The application_user_ids of this UserDeleteRequest.  # noqa: E501
        :type: list[str]
        """

        self._application_user_ids = application_user_ids

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
        if not isinstance(other, UserDeleteRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
