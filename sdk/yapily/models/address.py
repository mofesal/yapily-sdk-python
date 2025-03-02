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


class Address(object):
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
        'address_lines': 'list[str]',
        'street_name': 'str',
        'building_number': 'str',
        'post_code': 'str',
        'town_name': 'str',
        'county': 'list[str]',
        'address_type': 'str',
        'country': 'str',
        'department': 'str',
        'sub_department': 'str'
    }

    attribute_map = {
        'address_lines': 'addressLines',
        'street_name': 'streetName',
        'building_number': 'buildingNumber',
        'post_code': 'postCode',
        'town_name': 'townName',
        'county': 'county',
        'address_type': 'addressType',
        'country': 'country',
        'department': 'department',
        'sub_department': 'subDepartment'
    }

    def __init__(self, address_lines=None, street_name=None, building_number=None, post_code=None, town_name=None, county=None, address_type=None, country=None, department=None, sub_department=None):  # noqa: E501
        """Address - a model defined in Swagger"""  # noqa: E501

        self._address_lines = None
        self._street_name = None
        self._building_number = None
        self._post_code = None
        self._town_name = None
        self._county = None
        self._address_type = None
        self._country = None
        self._department = None
        self._sub_department = None
        self.discriminator = None

        if address_lines is not None:
            self.address_lines = address_lines
        if street_name is not None:
            self.street_name = street_name
        if building_number is not None:
            self.building_number = building_number
        if post_code is not None:
            self.post_code = post_code
        if town_name is not None:
            self.town_name = town_name
        if county is not None:
            self.county = county
        if address_type is not None:
            self.address_type = address_type
        if country is not None:
            self.country = country
        if department is not None:
            self.department = department
        if sub_department is not None:
            self.sub_department = sub_department

    @property
    def address_lines(self):
        """Gets the address_lines of this Address.  # noqa: E501


        :return: The address_lines of this Address.  # noqa: E501
        :rtype: list[str]
        """
        return self._address_lines

    @address_lines.setter
    def address_lines(self, address_lines):
        """Sets the address_lines of this Address.


        :param address_lines: The address_lines of this Address.  # noqa: E501
        :type: list[str]
        """

        self._address_lines = address_lines

    @property
    def street_name(self):
        """Gets the street_name of this Address.  # noqa: E501


        :return: The street_name of this Address.  # noqa: E501
        :rtype: str
        """
        return self._street_name

    @street_name.setter
    def street_name(self, street_name):
        """Sets the street_name of this Address.


        :param street_name: The street_name of this Address.  # noqa: E501
        :type: str
        """

        self._street_name = street_name

    @property
    def building_number(self):
        """Gets the building_number of this Address.  # noqa: E501


        :return: The building_number of this Address.  # noqa: E501
        :rtype: str
        """
        return self._building_number

    @building_number.setter
    def building_number(self, building_number):
        """Sets the building_number of this Address.


        :param building_number: The building_number of this Address.  # noqa: E501
        :type: str
        """

        self._building_number = building_number

    @property
    def post_code(self):
        """Gets the post_code of this Address.  # noqa: E501


        :return: The post_code of this Address.  # noqa: E501
        :rtype: str
        """
        return self._post_code

    @post_code.setter
    def post_code(self, post_code):
        """Sets the post_code of this Address.


        :param post_code: The post_code of this Address.  # noqa: E501
        :type: str
        """

        self._post_code = post_code

    @property
    def town_name(self):
        """Gets the town_name of this Address.  # noqa: E501


        :return: The town_name of this Address.  # noqa: E501
        :rtype: str
        """
        return self._town_name

    @town_name.setter
    def town_name(self, town_name):
        """Sets the town_name of this Address.


        :param town_name: The town_name of this Address.  # noqa: E501
        :type: str
        """

        self._town_name = town_name

    @property
    def county(self):
        """Gets the county of this Address.  # noqa: E501


        :return: The county of this Address.  # noqa: E501
        :rtype: list[str]
        """
        return self._county

    @county.setter
    def county(self, county):
        """Sets the county of this Address.


        :param county: The county of this Address.  # noqa: E501
        :type: list[str]
        """

        self._county = county

    @property
    def address_type(self):
        """Gets the address_type of this Address.  # noqa: E501


        :return: The address_type of this Address.  # noqa: E501
        :rtype: str
        """
        return self._address_type

    @address_type.setter
    def address_type(self, address_type):
        """Sets the address_type of this Address.


        :param address_type: The address_type of this Address.  # noqa: E501
        :type: str
        """
        allowed_values = ["BUSINESS", "CORRESPONDENCE", "DELIVERY_TO", "MAIL_TO", "PO_BOX", "POSTAL", "RESIDENTIAL", "STATEMENT", "UNKNOWN"]  # noqa: E501
        if address_type not in allowed_values:
            raise ValueError(
                "Invalid value for `address_type` ({0}), must be one of {1}"  # noqa: E501
                .format(address_type, allowed_values)
            )

        self._address_type = address_type

    @property
    def country(self):
        """Gets the country of this Address.  # noqa: E501


        :return: The country of this Address.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this Address.


        :param country: The country of this Address.  # noqa: E501
        :type: str
        """

        self._country = country

    @property
    def department(self):
        """Gets the department of this Address.  # noqa: E501


        :return: The department of this Address.  # noqa: E501
        :rtype: str
        """
        return self._department

    @department.setter
    def department(self, department):
        """Sets the department of this Address.


        :param department: The department of this Address.  # noqa: E501
        :type: str
        """

        self._department = department

    @property
    def sub_department(self):
        """Gets the sub_department of this Address.  # noqa: E501


        :return: The sub_department of this Address.  # noqa: E501
        :rtype: str
        """
        return self._sub_department

    @sub_department.setter
    def sub_department(self, sub_department):
        """Sets the sub_department of this Address.


        :param sub_department: The sub_department of this Address.  # noqa: E501
        :type: str
        """

        self._sub_department = sub_department

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
        if not isinstance(other, Address):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
