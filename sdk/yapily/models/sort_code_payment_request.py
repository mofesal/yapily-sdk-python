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

from yapily.models.merchant_info import MerchantInfo  # noqa: F401,E501


class SortCodePaymentRequest(object):
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
        'sender_account_id': 'str',
        'name': 'str',
        'amount': 'float',
        'currency': 'str',
        'reference': 'str',
        'country': 'str',
        'type': 'str',
        'account_number': 'str',
        'sort_code': 'str',
        'merchant_info': 'MerchantInfo'
    }

    attribute_map = {
        'sender_account_id': 'senderAccountId',
        'name': 'name',
        'amount': 'amount',
        'currency': 'currency',
        'reference': 'reference',
        'country': 'country',
        'type': 'type',
        'account_number': 'accountNumber',
        'sort_code': 'sortCode',
        'merchant_info': 'merchantInfo'
    }

    def __init__(self, sender_account_id=None, name=None, amount=None, currency=None, reference=None, country=None, type=None, account_number=None, sort_code=None, merchant_info=None):  # noqa: E501
        """SortCodePaymentRequest - a model defined in Swagger"""  # noqa: E501

        self._sender_account_id = None
        self._name = None
        self._amount = None
        self._currency = None
        self._reference = None
        self._country = None
        self._type = None
        self._account_number = None
        self._sort_code = None
        self._merchant_info = None
        self.discriminator = None

        if sender_account_id is not None:
            self.sender_account_id = sender_account_id
        self.name = name
        self.amount = amount
        self.currency = currency
        self.reference = reference
        self.country = country
        if type is not None:
            self.type = type
        self.account_number = account_number
        self.sort_code = sort_code
        if merchant_info is not None:
            self.merchant_info = merchant_info

    @property
    def sender_account_id(self):
        """Gets the sender_account_id of this SortCodePaymentRequest.  # noqa: E501


        :return: The sender_account_id of this SortCodePaymentRequest.  # noqa: E501
        :rtype: str
        """
        return self._sender_account_id

    @sender_account_id.setter
    def sender_account_id(self, sender_account_id):
        """Sets the sender_account_id of this SortCodePaymentRequest.


        :param sender_account_id: The sender_account_id of this SortCodePaymentRequest.  # noqa: E501
        :type: str
        """

        self._sender_account_id = sender_account_id

    @property
    def name(self):
        """Gets the name of this SortCodePaymentRequest.  # noqa: E501


        :return: The name of this SortCodePaymentRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SortCodePaymentRequest.


        :param name: The name of this SortCodePaymentRequest.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def amount(self):
        """Gets the amount of this SortCodePaymentRequest.  # noqa: E501


        :return: The amount of this SortCodePaymentRequest.  # noqa: E501
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this SortCodePaymentRequest.


        :param amount: The amount of this SortCodePaymentRequest.  # noqa: E501
        :type: float
        """
        if amount is None:
            raise ValueError("Invalid value for `amount`, must not be `None`")  # noqa: E501

        self._amount = amount

    @property
    def currency(self):
        """Gets the currency of this SortCodePaymentRequest.  # noqa: E501


        :return: The currency of this SortCodePaymentRequest.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this SortCodePaymentRequest.


        :param currency: The currency of this SortCodePaymentRequest.  # noqa: E501
        :type: str
        """
        if currency is None:
            raise ValueError("Invalid value for `currency`, must not be `None`")  # noqa: E501

        self._currency = currency

    @property
    def reference(self):
        """Gets the reference of this SortCodePaymentRequest.  # noqa: E501


        :return: The reference of this SortCodePaymentRequest.  # noqa: E501
        :rtype: str
        """
        return self._reference

    @reference.setter
    def reference(self, reference):
        """Sets the reference of this SortCodePaymentRequest.


        :param reference: The reference of this SortCodePaymentRequest.  # noqa: E501
        :type: str
        """
        if reference is None:
            raise ValueError("Invalid value for `reference`, must not be `None`")  # noqa: E501

        self._reference = reference

    @property
    def country(self):
        """Gets the country of this SortCodePaymentRequest.  # noqa: E501


        :return: The country of this SortCodePaymentRequest.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this SortCodePaymentRequest.


        :param country: The country of this SortCodePaymentRequest.  # noqa: E501
        :type: str
        """
        if country is None:
            raise ValueError("Invalid value for `country`, must not be `None`")  # noqa: E501

        self._country = country

    @property
    def type(self):
        """Gets the type of this SortCodePaymentRequest.  # noqa: E501


        :return: The type of this SortCodePaymentRequest.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this SortCodePaymentRequest.


        :param type: The type of this SortCodePaymentRequest.  # noqa: E501
        :type: str
        """
        allowed_values = ["BILL", "GOODS", "SERVICES", "OTHER", "PERSON_TO_PERSON"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def account_number(self):
        """Gets the account_number of this SortCodePaymentRequest.  # noqa: E501


        :return: The account_number of this SortCodePaymentRequest.  # noqa: E501
        :rtype: str
        """
        return self._account_number

    @account_number.setter
    def account_number(self, account_number):
        """Sets the account_number of this SortCodePaymentRequest.


        :param account_number: The account_number of this SortCodePaymentRequest.  # noqa: E501
        :type: str
        """
        if account_number is None:
            raise ValueError("Invalid value for `account_number`, must not be `None`")  # noqa: E501

        self._account_number = account_number

    @property
    def sort_code(self):
        """Gets the sort_code of this SortCodePaymentRequest.  # noqa: E501


        :return: The sort_code of this SortCodePaymentRequest.  # noqa: E501
        :rtype: str
        """
        return self._sort_code

    @sort_code.setter
    def sort_code(self, sort_code):
        """Sets the sort_code of this SortCodePaymentRequest.


        :param sort_code: The sort_code of this SortCodePaymentRequest.  # noqa: E501
        :type: str
        """
        if sort_code is None:
            raise ValueError("Invalid value for `sort_code`, must not be `None`")  # noqa: E501

        self._sort_code = sort_code

    @property
    def merchant_info(self):
        """Gets the merchant_info of this SortCodePaymentRequest.  # noqa: E501


        :return: The merchant_info of this SortCodePaymentRequest.  # noqa: E501
        :rtype: MerchantInfo
        """
        return self._merchant_info

    @merchant_info.setter
    def merchant_info(self, merchant_info):
        """Sets the merchant_info of this SortCodePaymentRequest.


        :param merchant_info: The merchant_info of this SortCodePaymentRequest.  # noqa: E501
        :type: MerchantInfo
        """

        self._merchant_info = merchant_info

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
        if not isinstance(other, SortCodePaymentRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
