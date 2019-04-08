# coding: utf-8

"""
    Yapily API

    To access endpoints that require authentication, use your Application key and secret created in the Dashboard (https://dashboard.yapily.com)  # noqa: E501

    OpenAPI spec version: 0.0.100
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from yapily.models.overdraft_overdraft_fees_charges1 import OverdraftOverdraftFeesCharges1  # noqa: F401,E501
from yapily.models.overdraft_overdraft_tier_band import OverdraftOverdraftTierBand  # noqa: F401,E501


class OverdraftOverdraftTierBandSet(object):
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
        'authorised_indicator': 'bool',
        'buffer_amount': 'str',
        'identification': 'str',
        'notes': 'list[str]',
        'overdraft_fees_charges': 'list[OverdraftOverdraftFeesCharges1]',
        'overdraft_tier_band': 'list[OverdraftOverdraftTierBand]',
        'overdraft_type': 'str',
        'tier_band_method': 'str'
    }

    attribute_map = {
        'authorised_indicator': 'AuthorisedIndicator',
        'buffer_amount': 'BufferAmount',
        'identification': 'Identification',
        'notes': 'Notes',
        'overdraft_fees_charges': 'OverdraftFeesCharges',
        'overdraft_tier_band': 'OverdraftTierBand',
        'overdraft_type': 'OverdraftType',
        'tier_band_method': 'TierBandMethod'
    }

    def __init__(self, authorised_indicator=None, buffer_amount=None, identification=None, notes=None, overdraft_fees_charges=None, overdraft_tier_band=None, overdraft_type=None, tier_band_method=None):  # noqa: E501
        """OverdraftOverdraftTierBandSet - a model defined in Swagger"""  # noqa: E501

        self._authorised_indicator = None
        self._buffer_amount = None
        self._identification = None
        self._notes = None
        self._overdraft_fees_charges = None
        self._overdraft_tier_band = None
        self._overdraft_type = None
        self._tier_band_method = None
        self.discriminator = None

        if authorised_indicator is not None:
            self.authorised_indicator = authorised_indicator
        if buffer_amount is not None:
            self.buffer_amount = buffer_amount
        if identification is not None:
            self.identification = identification
        if notes is not None:
            self.notes = notes
        if overdraft_fees_charges is not None:
            self.overdraft_fees_charges = overdraft_fees_charges
        if overdraft_tier_band is not None:
            self.overdraft_tier_band = overdraft_tier_band
        if overdraft_type is not None:
            self.overdraft_type = overdraft_type
        if tier_band_method is not None:
            self.tier_band_method = tier_band_method

    @property
    def authorised_indicator(self):
        """Gets the authorised_indicator of this OverdraftOverdraftTierBandSet.  # noqa: E501


        :return: The authorised_indicator of this OverdraftOverdraftTierBandSet.  # noqa: E501
        :rtype: bool
        """
        return self._authorised_indicator

    @authorised_indicator.setter
    def authorised_indicator(self, authorised_indicator):
        """Sets the authorised_indicator of this OverdraftOverdraftTierBandSet.


        :param authorised_indicator: The authorised_indicator of this OverdraftOverdraftTierBandSet.  # noqa: E501
        :type: bool
        """

        self._authorised_indicator = authorised_indicator

    @property
    def buffer_amount(self):
        """Gets the buffer_amount of this OverdraftOverdraftTierBandSet.  # noqa: E501


        :return: The buffer_amount of this OverdraftOverdraftTierBandSet.  # noqa: E501
        :rtype: str
        """
        return self._buffer_amount

    @buffer_amount.setter
    def buffer_amount(self, buffer_amount):
        """Sets the buffer_amount of this OverdraftOverdraftTierBandSet.


        :param buffer_amount: The buffer_amount of this OverdraftOverdraftTierBandSet.  # noqa: E501
        :type: str
        """

        self._buffer_amount = buffer_amount

    @property
    def identification(self):
        """Gets the identification of this OverdraftOverdraftTierBandSet.  # noqa: E501


        :return: The identification of this OverdraftOverdraftTierBandSet.  # noqa: E501
        :rtype: str
        """
        return self._identification

    @identification.setter
    def identification(self, identification):
        """Sets the identification of this OverdraftOverdraftTierBandSet.


        :param identification: The identification of this OverdraftOverdraftTierBandSet.  # noqa: E501
        :type: str
        """

        self._identification = identification

    @property
    def notes(self):
        """Gets the notes of this OverdraftOverdraftTierBandSet.  # noqa: E501


        :return: The notes of this OverdraftOverdraftTierBandSet.  # noqa: E501
        :rtype: list[str]
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        """Sets the notes of this OverdraftOverdraftTierBandSet.


        :param notes: The notes of this OverdraftOverdraftTierBandSet.  # noqa: E501
        :type: list[str]
        """

        self._notes = notes

    @property
    def overdraft_fees_charges(self):
        """Gets the overdraft_fees_charges of this OverdraftOverdraftTierBandSet.  # noqa: E501


        :return: The overdraft_fees_charges of this OverdraftOverdraftTierBandSet.  # noqa: E501
        :rtype: list[OverdraftOverdraftFeesCharges1]
        """
        return self._overdraft_fees_charges

    @overdraft_fees_charges.setter
    def overdraft_fees_charges(self, overdraft_fees_charges):
        """Sets the overdraft_fees_charges of this OverdraftOverdraftTierBandSet.


        :param overdraft_fees_charges: The overdraft_fees_charges of this OverdraftOverdraftTierBandSet.  # noqa: E501
        :type: list[OverdraftOverdraftFeesCharges1]
        """

        self._overdraft_fees_charges = overdraft_fees_charges

    @property
    def overdraft_tier_band(self):
        """Gets the overdraft_tier_band of this OverdraftOverdraftTierBandSet.  # noqa: E501


        :return: The overdraft_tier_band of this OverdraftOverdraftTierBandSet.  # noqa: E501
        :rtype: list[OverdraftOverdraftTierBand]
        """
        return self._overdraft_tier_band

    @overdraft_tier_band.setter
    def overdraft_tier_band(self, overdraft_tier_band):
        """Sets the overdraft_tier_band of this OverdraftOverdraftTierBandSet.


        :param overdraft_tier_band: The overdraft_tier_band of this OverdraftOverdraftTierBandSet.  # noqa: E501
        :type: list[OverdraftOverdraftTierBand]
        """

        self._overdraft_tier_band = overdraft_tier_band

    @property
    def overdraft_type(self):
        """Gets the overdraft_type of this OverdraftOverdraftTierBandSet.  # noqa: E501


        :return: The overdraft_type of this OverdraftOverdraftTierBandSet.  # noqa: E501
        :rtype: str
        """
        return self._overdraft_type

    @overdraft_type.setter
    def overdraft_type(self, overdraft_type):
        """Sets the overdraft_type of this OverdraftOverdraftTierBandSet.


        :param overdraft_type: The overdraft_type of this OverdraftOverdraftTierBandSet.  # noqa: E501
        :type: str
        """
        allowed_values = ["Committed", "OnDemand", "Other"]  # noqa: E501
        if overdraft_type not in allowed_values:
            raise ValueError(
                "Invalid value for `overdraft_type` ({0}), must be one of {1}"  # noqa: E501
                .format(overdraft_type, allowed_values)
            )

        self._overdraft_type = overdraft_type

    @property
    def tier_band_method(self):
        """Gets the tier_band_method of this OverdraftOverdraftTierBandSet.  # noqa: E501


        :return: The tier_band_method of this OverdraftOverdraftTierBandSet.  # noqa: E501
        :rtype: str
        """
        return self._tier_band_method

    @tier_band_method.setter
    def tier_band_method(self, tier_band_method):
        """Sets the tier_band_method of this OverdraftOverdraftTierBandSet.


        :param tier_band_method: The tier_band_method of this OverdraftOverdraftTierBandSet.  # noqa: E501
        :type: str
        """
        allowed_values = ["Tiered", "Whole"]  # noqa: E501
        if tier_band_method not in allowed_values:
            raise ValueError(
                "Invalid value for `tier_band_method` ({0}), must be one of {1}"  # noqa: E501
                .format(tier_band_method, allowed_values)
            )

        self._tier_band_method = tier_band_method

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
        if not isinstance(other, OverdraftOverdraftTierBandSet):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
