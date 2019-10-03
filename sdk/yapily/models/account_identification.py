# coding: utf-8

"""
    Yapily API

    To access endpoints that require authentication, use your application key and secret created in the Dashboard (https://dashboard.yapily.com)  # noqa: E501

    OpenAPI spec version: 0.0.147
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class AccountIdentification(object):
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
        'type': 'str',
        'identification': 'str'
    }

    attribute_map = {
        'type': 'type',
        'identification': 'identification'
    }

    def __init__(self, type=None, identification=None):  # noqa: E501
        """AccountIdentification - a model defined in Swagger"""  # noqa: E501

        self._type = None
        self._identification = None
        self.discriminator = None

        self.type = type
        self.identification = identification

    @property
    def type(self):
        """Gets the type of this AccountIdentification.  # noqa: E501


        :return: The type of this AccountIdentification.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this AccountIdentification.


        :param type: The type of this AccountIdentification.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["SORT_CODE", "ACCOUNT_NUMBER", "IBAN", "BBAN", "SWIFT", "BIC", "PAN", "MASKED_PAN", "MSISDN", "ABA", "ABA_WIRE", "ABA_ACH"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def identification(self):
        """Gets the identification of this AccountIdentification.  # noqa: E501


        :return: The identification of this AccountIdentification.  # noqa: E501
        :rtype: str
        """
        return self._identification

    @identification.setter
    def identification(self, identification):
        """Sets the identification of this AccountIdentification.


        :param identification: The identification of this AccountIdentification.  # noqa: E501
        :type: str
        """
        if identification is None:
            raise ValueError("Invalid value for `identification`, must not be `None`")  # noqa: E501

        self._identification = identification

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
        if not isinstance(other, AccountIdentification):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
