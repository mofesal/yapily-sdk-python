# coding: utf-8

"""
    Yapily API

    To access endpoints that require authentication, use your Application key and secret created in the Dashboard (https://dashboard.yapily.com)  # noqa: E501

    OpenAPI spec version: 0.0.29
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class AgeEligibility(object):
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
        'maximum_age': 'float',
        'minimum_age': 'float',
        'notes': 'list[str]'
    }

    attribute_map = {
        'maximum_age': 'MaximumAge',
        'minimum_age': 'MinimumAge',
        'notes': 'Notes'
    }

    def __init__(self, maximum_age=None, minimum_age=None, notes=None):  # noqa: E501
        """AgeEligibility - a model defined in Swagger"""  # noqa: E501

        self._maximum_age = None
        self._minimum_age = None
        self._notes = None
        self.discriminator = None

        if maximum_age is not None:
            self.maximum_age = maximum_age
        if minimum_age is not None:
            self.minimum_age = minimum_age
        if notes is not None:
            self.notes = notes

    @property
    def maximum_age(self):
        """Gets the maximum_age of this AgeEligibility.  # noqa: E501


        :return: The maximum_age of this AgeEligibility.  # noqa: E501
        :rtype: float
        """
        return self._maximum_age

    @maximum_age.setter
    def maximum_age(self, maximum_age):
        """Sets the maximum_age of this AgeEligibility.


        :param maximum_age: The maximum_age of this AgeEligibility.  # noqa: E501
        :type: float
        """

        self._maximum_age = maximum_age

    @property
    def minimum_age(self):
        """Gets the minimum_age of this AgeEligibility.  # noqa: E501


        :return: The minimum_age of this AgeEligibility.  # noqa: E501
        :rtype: float
        """
        return self._minimum_age

    @minimum_age.setter
    def minimum_age(self, minimum_age):
        """Sets the minimum_age of this AgeEligibility.


        :param minimum_age: The minimum_age of this AgeEligibility.  # noqa: E501
        :type: float
        """

        self._minimum_age = minimum_age

    @property
    def notes(self):
        """Gets the notes of this AgeEligibility.  # noqa: E501


        :return: The notes of this AgeEligibility.  # noqa: E501
        :rtype: list[str]
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        """Sets the notes of this AgeEligibility.


        :param notes: The notes of this AgeEligibility.  # noqa: E501
        :type: list[str]
        """

        self._notes = notes

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
        if not isinstance(other, AgeEligibility):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
