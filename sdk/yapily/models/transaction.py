# coding: utf-8

"""
    Yapily API

    To access endpoints that require authentication, use your Application key and secret created in the Dashboard (https://dashboard.yapily.com)  # noqa: E501

    OpenAPI spec version: 0.0.110
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from yapily.models.merchant import Merchant  # noqa: F401,E501


class Transaction(object):
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
        'id': 'str',
        'date': 'datetime',
        'amount': 'float',
        'currency': 'str',
        'description': 'str',
        'merchant': 'Merchant'
    }

    attribute_map = {
        'id': 'id',
        'date': 'date',
        'amount': 'amount',
        'currency': 'currency',
        'description': 'description',
        'merchant': 'merchant'
    }

    def __init__(self, id=None, date=None, amount=None, currency=None, description=None, merchant=None):  # noqa: E501
        """Transaction - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._date = None
        self._amount = None
        self._currency = None
        self._description = None
        self._merchant = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if date is not None:
            self.date = date
        if amount is not None:
            self.amount = amount
        if currency is not None:
            self.currency = currency
        if description is not None:
            self.description = description
        if merchant is not None:
            self.merchant = merchant

    @property
    def id(self):
        """Gets the id of this Transaction.  # noqa: E501


        :return: The id of this Transaction.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Transaction.


        :param id: The id of this Transaction.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def date(self):
        """Gets the date of this Transaction.  # noqa: E501


        :return: The date of this Transaction.  # noqa: E501
        :rtype: datetime
        """
        return self._date

    @date.setter
    def date(self, date):
        """Sets the date of this Transaction.


        :param date: The date of this Transaction.  # noqa: E501
        :type: datetime
        """

        self._date = date

    @property
    def amount(self):
        """Gets the amount of this Transaction.  # noqa: E501


        :return: The amount of this Transaction.  # noqa: E501
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this Transaction.


        :param amount: The amount of this Transaction.  # noqa: E501
        :type: float
        """

        self._amount = amount

    @property
    def currency(self):
        """Gets the currency of this Transaction.  # noqa: E501


        :return: The currency of this Transaction.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this Transaction.


        :param currency: The currency of this Transaction.  # noqa: E501
        :type: str
        """

        self._currency = currency

    @property
    def description(self):
        """Gets the description of this Transaction.  # noqa: E501


        :return: The description of this Transaction.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Transaction.


        :param description: The description of this Transaction.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def merchant(self):
        """Gets the merchant of this Transaction.  # noqa: E501


        :return: The merchant of this Transaction.  # noqa: E501
        :rtype: Merchant
        """
        return self._merchant

    @merchant.setter
    def merchant(self, merchant):
        """Sets the merchant of this Transaction.


        :param merchant: The merchant of this Transaction.  # noqa: E501
        :type: Merchant
        """

        self._merchant = merchant

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
        if not isinstance(other, Transaction):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
