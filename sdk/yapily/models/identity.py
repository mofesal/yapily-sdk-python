# coding: utf-8

"""
    Yapily API

    To access endpoints that require authentication, use your application key and secret created in the Dashboard (https://dashboard.yapily.com)  # noqa: E501

    OpenAPI spec version: 0.0.141
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from yapily.models.identity_address import IdentityAddress  # noqa: F401,E501


class Identity(object):
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
        'first_name': 'str',
        'last_name': 'str',
        'gender': 'str',
        'birthdate': 'str',
        'email': 'str',
        'phone': 'str',
        'addresses': 'list[IdentityAddress]'
    }

    attribute_map = {
        'id': 'id',
        'first_name': 'firstName',
        'last_name': 'lastName',
        'gender': 'gender',
        'birthdate': 'birthdate',
        'email': 'email',
        'phone': 'phone',
        'addresses': 'addresses'
    }

    def __init__(self, id=None, first_name=None, last_name=None, gender=None, birthdate=None, email=None, phone=None, addresses=None):  # noqa: E501
        """Identity - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._first_name = None
        self._last_name = None
        self._gender = None
        self._birthdate = None
        self._email = None
        self._phone = None
        self._addresses = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if first_name is not None:
            self.first_name = first_name
        if last_name is not None:
            self.last_name = last_name
        if gender is not None:
            self.gender = gender
        if birthdate is not None:
            self.birthdate = birthdate
        if email is not None:
            self.email = email
        if phone is not None:
            self.phone = phone
        if addresses is not None:
            self.addresses = addresses

    @property
    def id(self):
        """Gets the id of this Identity.  # noqa: E501


        :return: The id of this Identity.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Identity.


        :param id: The id of this Identity.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def first_name(self):
        """Gets the first_name of this Identity.  # noqa: E501


        :return: The first_name of this Identity.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this Identity.


        :param first_name: The first_name of this Identity.  # noqa: E501
        :type: str
        """

        self._first_name = first_name

    @property
    def last_name(self):
        """Gets the last_name of this Identity.  # noqa: E501


        :return: The last_name of this Identity.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this Identity.


        :param last_name: The last_name of this Identity.  # noqa: E501
        :type: str
        """

        self._last_name = last_name

    @property
    def gender(self):
        """Gets the gender of this Identity.  # noqa: E501


        :return: The gender of this Identity.  # noqa: E501
        :rtype: str
        """
        return self._gender

    @gender.setter
    def gender(self, gender):
        """Sets the gender of this Identity.


        :param gender: The gender of this Identity.  # noqa: E501
        :type: str
        """

        self._gender = gender

    @property
    def birthdate(self):
        """Gets the birthdate of this Identity.  # noqa: E501


        :return: The birthdate of this Identity.  # noqa: E501
        :rtype: str
        """
        return self._birthdate

    @birthdate.setter
    def birthdate(self, birthdate):
        """Sets the birthdate of this Identity.


        :param birthdate: The birthdate of this Identity.  # noqa: E501
        :type: str
        """

        self._birthdate = birthdate

    @property
    def email(self):
        """Gets the email of this Identity.  # noqa: E501


        :return: The email of this Identity.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this Identity.


        :param email: The email of this Identity.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def phone(self):
        """Gets the phone of this Identity.  # noqa: E501


        :return: The phone of this Identity.  # noqa: E501
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this Identity.


        :param phone: The phone of this Identity.  # noqa: E501
        :type: str
        """

        self._phone = phone

    @property
    def addresses(self):
        """Gets the addresses of this Identity.  # noqa: E501


        :return: The addresses of this Identity.  # noqa: E501
        :rtype: list[IdentityAddress]
        """
        return self._addresses

    @addresses.setter
    def addresses(self, addresses):
        """Sets the addresses of this Identity.


        :param addresses: The addresses of this Identity.  # noqa: E501
        :type: list[IdentityAddress]
        """

        self._addresses = addresses

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
        if not isinstance(other, Identity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
