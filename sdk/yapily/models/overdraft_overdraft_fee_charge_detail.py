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

from yapily.models.other_application_frequency import OtherApplicationFrequency  # noqa: F401,E501
from yapily.models.other_calculation_frequency import OtherCalculationFrequency  # noqa: F401,E501
from yapily.models.other_fee_rate_type import OtherFeeRateType  # noqa: F401,E501
from yapily.models.other_fee_type import OtherFeeType  # noqa: F401,E501
from yapily.models.overdraft_overdraft_fee_charge_cap import OverdraftOverdraftFeeChargeCap  # noqa: F401,E501


class OverdraftOverdraftFeeChargeDetail(object):
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
        'application_frequency': 'str',
        'calculation_frequency': 'str',
        'fee_amount': 'str',
        'fee_rate': 'str',
        'fee_rate_type': 'str',
        'fee_type': 'str',
        'incremental_borrowing_amount': 'str',
        'notes': 'list[str]',
        'other_application_frequency': 'OtherApplicationFrequency',
        'other_calculation_frequency': 'OtherCalculationFrequency',
        'other_fee_rate_type': 'OtherFeeRateType',
        'other_fee_type': 'OtherFeeType',
        'overdraft_control_indicator': 'bool',
        'overdraft_fee_charge_cap': 'OverdraftOverdraftFeeChargeCap'
    }

    attribute_map = {
        'application_frequency': 'ApplicationFrequency',
        'calculation_frequency': 'CalculationFrequency',
        'fee_amount': 'FeeAmount',
        'fee_rate': 'FeeRate',
        'fee_rate_type': 'FeeRateType',
        'fee_type': 'FeeType',
        'incremental_borrowing_amount': 'IncrementalBorrowingAmount',
        'notes': 'Notes',
        'other_application_frequency': 'OtherApplicationFrequency',
        'other_calculation_frequency': 'OtherCalculationFrequency',
        'other_fee_rate_type': 'OtherFeeRateType',
        'other_fee_type': 'OtherFeeType',
        'overdraft_control_indicator': 'OverdraftControlIndicator',
        'overdraft_fee_charge_cap': 'OverdraftFeeChargeCap'
    }

    def __init__(self, application_frequency=None, calculation_frequency=None, fee_amount=None, fee_rate=None, fee_rate_type=None, fee_type=None, incremental_borrowing_amount=None, notes=None, other_application_frequency=None, other_calculation_frequency=None, other_fee_rate_type=None, other_fee_type=None, overdraft_control_indicator=None, overdraft_fee_charge_cap=None):  # noqa: E501
        """OverdraftOverdraftFeeChargeDetail - a model defined in Swagger"""  # noqa: E501

        self._application_frequency = None
        self._calculation_frequency = None
        self._fee_amount = None
        self._fee_rate = None
        self._fee_rate_type = None
        self._fee_type = None
        self._incremental_borrowing_amount = None
        self._notes = None
        self._other_application_frequency = None
        self._other_calculation_frequency = None
        self._other_fee_rate_type = None
        self._other_fee_type = None
        self._overdraft_control_indicator = None
        self._overdraft_fee_charge_cap = None
        self.discriminator = None

        if application_frequency is not None:
            self.application_frequency = application_frequency
        if calculation_frequency is not None:
            self.calculation_frequency = calculation_frequency
        if fee_amount is not None:
            self.fee_amount = fee_amount
        if fee_rate is not None:
            self.fee_rate = fee_rate
        if fee_rate_type is not None:
            self.fee_rate_type = fee_rate_type
        if fee_type is not None:
            self.fee_type = fee_type
        if incremental_borrowing_amount is not None:
            self.incremental_borrowing_amount = incremental_borrowing_amount
        if notes is not None:
            self.notes = notes
        if other_application_frequency is not None:
            self.other_application_frequency = other_application_frequency
        if other_calculation_frequency is not None:
            self.other_calculation_frequency = other_calculation_frequency
        if other_fee_rate_type is not None:
            self.other_fee_rate_type = other_fee_rate_type
        if other_fee_type is not None:
            self.other_fee_type = other_fee_type
        if overdraft_control_indicator is not None:
            self.overdraft_control_indicator = overdraft_control_indicator
        if overdraft_fee_charge_cap is not None:
            self.overdraft_fee_charge_cap = overdraft_fee_charge_cap

    @property
    def application_frequency(self):
        """Gets the application_frequency of this OverdraftOverdraftFeeChargeDetail.  # noqa: E501


        :return: The application_frequency of this OverdraftOverdraftFeeChargeDetail.  # noqa: E501
        :rtype: str
        """
        return self._application_frequency

    @application_frequency.setter
    def application_frequency(self, application_frequency):
        """Sets the application_frequency of this OverdraftOverdraftFeeChargeDetail.


        :param application_frequency: The application_frequency of this OverdraftOverdraftFeeChargeDetail.  # noqa: E501
        :type: str
        """
        allowed_values = ["AccountClosing", "AccountOpening", "AcademicTerm", "ChargingPeriod", "Daily", "PerItem", "Monthly", "OnAccountAnniversary", "Other", "PerHour", "PerOccurrence", "PerSheet", "PerTransaction", "PerTransactionAmount", "PerTransactionPercentage", "Quarterly", "SixMonthly", "StatementMonthly", "Weekly", "Yearly"]  # noqa: E501
        if application_frequency not in allowed_values:
            raise ValueError(
                "Invalid value for `application_frequency` ({0}), must be one of {1}"  # noqa: E501
                .format(application_frequency, allowed_values)
            )

        self._application_frequency = application_frequency

    @property
    def calculation_frequency(self):
        """Gets the calculation_frequency of this OverdraftOverdraftFeeChargeDetail.  # noqa: E501


        :return: The calculation_frequency of this OverdraftOverdraftFeeChargeDetail.  # noqa: E501
        :rtype: str
        """
        return self._calculation_frequency

    @calculation_frequency.setter
    def calculation_frequency(self, calculation_frequency):
        """Sets the calculation_frequency of this OverdraftOverdraftFeeChargeDetail.


        :param calculation_frequency: The calculation_frequency of this OverdraftOverdraftFeeChargeDetail.  # noqa: E501
        :type: str
        """
        allowed_values = ["AccountClosing", "AccountOpening", "AcademicTerm", "ChargingPeriod", "Daily", "PerItem", "Monthly", "OnAccountAnniversary", "Other", "PerHour", "PerOccurrence", "PerSheet", "PerTransaction", "PerTransactionAmount", "PerTransactionPercentage", "Quarterly", "SixMonthly", "StatementMonthly", "Weekly", "Yearly"]  # noqa: E501
        if calculation_frequency not in allowed_values:
            raise ValueError(
                "Invalid value for `calculation_frequency` ({0}), must be one of {1}"  # noqa: E501
                .format(calculation_frequency, allowed_values)
            )

        self._calculation_frequency = calculation_frequency

    @property
    def fee_amount(self):
        """Gets the fee_amount of this OverdraftOverdraftFeeChargeDetail.  # noqa: E501


        :return: The fee_amount of this OverdraftOverdraftFeeChargeDetail.  # noqa: E501
        :rtype: str
        """
        return self._fee_amount

    @fee_amount.setter
    def fee_amount(self, fee_amount):
        """Sets the fee_amount of this OverdraftOverdraftFeeChargeDetail.


        :param fee_amount: The fee_amount of this OverdraftOverdraftFeeChargeDetail.  # noqa: E501
        :type: str
        """

        self._fee_amount = fee_amount

    @property
    def fee_rate(self):
        """Gets the fee_rate of this OverdraftOverdraftFeeChargeDetail.  # noqa: E501


        :return: The fee_rate of this OverdraftOverdraftFeeChargeDetail.  # noqa: E501
        :rtype: str
        """
        return self._fee_rate

    @fee_rate.setter
    def fee_rate(self, fee_rate):
        """Sets the fee_rate of this OverdraftOverdraftFeeChargeDetail.


        :param fee_rate: The fee_rate of this OverdraftOverdraftFeeChargeDetail.  # noqa: E501
        :type: str
        """

        self._fee_rate = fee_rate

    @property
    def fee_rate_type(self):
        """Gets the fee_rate_type of this OverdraftOverdraftFeeChargeDetail.  # noqa: E501


        :return: The fee_rate_type of this OverdraftOverdraftFeeChargeDetail.  # noqa: E501
        :rtype: str
        """
        return self._fee_rate_type

    @fee_rate_type.setter
    def fee_rate_type(self, fee_rate_type):
        """Sets the fee_rate_type of this OverdraftOverdraftFeeChargeDetail.


        :param fee_rate_type: The fee_rate_type of this OverdraftOverdraftFeeChargeDetail.  # noqa: E501
        :type: str
        """
        allowed_values = ["LinkedBaseRate", "Gross", "Net", "Other"]  # noqa: E501
        if fee_rate_type not in allowed_values:
            raise ValueError(
                "Invalid value for `fee_rate_type` ({0}), must be one of {1}"  # noqa: E501
                .format(fee_rate_type, allowed_values)
            )

        self._fee_rate_type = fee_rate_type

    @property
    def fee_type(self):
        """Gets the fee_type of this OverdraftOverdraftFeeChargeDetail.  # noqa: E501


        :return: The fee_type of this OverdraftOverdraftFeeChargeDetail.  # noqa: E501
        :rtype: str
        """
        return self._fee_type

    @fee_type.setter
    def fee_type(self, fee_type):
        """Sets the fee_type of this OverdraftOverdraftFeeChargeDetail.


        :param fee_type: The fee_type of this OverdraftOverdraftFeeChargeDetail.  # noqa: E501
        :type: str
        """
        allowed_values = ["ArrangedOverdraft", "EmergencyBorrowing", "BorrowingItem", "OverdraftRenewal", "AnnualReview", "OverdraftSetup", "Surcharge", "TempOverdraft", "UnauthorisedBorrowing", "UnauthorisedPaidTrans", "Other", "UnauthorisedUnpaidTrans"]  # noqa: E501
        if fee_type not in allowed_values:
            raise ValueError(
                "Invalid value for `fee_type` ({0}), must be one of {1}"  # noqa: E501
                .format(fee_type, allowed_values)
            )

        self._fee_type = fee_type

    @property
    def incremental_borrowing_amount(self):
        """Gets the incremental_borrowing_amount of this OverdraftOverdraftFeeChargeDetail.  # noqa: E501


        :return: The incremental_borrowing_amount of this OverdraftOverdraftFeeChargeDetail.  # noqa: E501
        :rtype: str
        """
        return self._incremental_borrowing_amount

    @incremental_borrowing_amount.setter
    def incremental_borrowing_amount(self, incremental_borrowing_amount):
        """Sets the incremental_borrowing_amount of this OverdraftOverdraftFeeChargeDetail.


        :param incremental_borrowing_amount: The incremental_borrowing_amount of this OverdraftOverdraftFeeChargeDetail.  # noqa: E501
        :type: str
        """

        self._incremental_borrowing_amount = incremental_borrowing_amount

    @property
    def notes(self):
        """Gets the notes of this OverdraftOverdraftFeeChargeDetail.  # noqa: E501


        :return: The notes of this OverdraftOverdraftFeeChargeDetail.  # noqa: E501
        :rtype: list[str]
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        """Sets the notes of this OverdraftOverdraftFeeChargeDetail.


        :param notes: The notes of this OverdraftOverdraftFeeChargeDetail.  # noqa: E501
        :type: list[str]
        """

        self._notes = notes

    @property
    def other_application_frequency(self):
        """Gets the other_application_frequency of this OverdraftOverdraftFeeChargeDetail.  # noqa: E501


        :return: The other_application_frequency of this OverdraftOverdraftFeeChargeDetail.  # noqa: E501
        :rtype: OtherApplicationFrequency
        """
        return self._other_application_frequency

    @other_application_frequency.setter
    def other_application_frequency(self, other_application_frequency):
        """Sets the other_application_frequency of this OverdraftOverdraftFeeChargeDetail.


        :param other_application_frequency: The other_application_frequency of this OverdraftOverdraftFeeChargeDetail.  # noqa: E501
        :type: OtherApplicationFrequency
        """

        self._other_application_frequency = other_application_frequency

    @property
    def other_calculation_frequency(self):
        """Gets the other_calculation_frequency of this OverdraftOverdraftFeeChargeDetail.  # noqa: E501


        :return: The other_calculation_frequency of this OverdraftOverdraftFeeChargeDetail.  # noqa: E501
        :rtype: OtherCalculationFrequency
        """
        return self._other_calculation_frequency

    @other_calculation_frequency.setter
    def other_calculation_frequency(self, other_calculation_frequency):
        """Sets the other_calculation_frequency of this OverdraftOverdraftFeeChargeDetail.


        :param other_calculation_frequency: The other_calculation_frequency of this OverdraftOverdraftFeeChargeDetail.  # noqa: E501
        :type: OtherCalculationFrequency
        """

        self._other_calculation_frequency = other_calculation_frequency

    @property
    def other_fee_rate_type(self):
        """Gets the other_fee_rate_type of this OverdraftOverdraftFeeChargeDetail.  # noqa: E501


        :return: The other_fee_rate_type of this OverdraftOverdraftFeeChargeDetail.  # noqa: E501
        :rtype: OtherFeeRateType
        """
        return self._other_fee_rate_type

    @other_fee_rate_type.setter
    def other_fee_rate_type(self, other_fee_rate_type):
        """Sets the other_fee_rate_type of this OverdraftOverdraftFeeChargeDetail.


        :param other_fee_rate_type: The other_fee_rate_type of this OverdraftOverdraftFeeChargeDetail.  # noqa: E501
        :type: OtherFeeRateType
        """

        self._other_fee_rate_type = other_fee_rate_type

    @property
    def other_fee_type(self):
        """Gets the other_fee_type of this OverdraftOverdraftFeeChargeDetail.  # noqa: E501


        :return: The other_fee_type of this OverdraftOverdraftFeeChargeDetail.  # noqa: E501
        :rtype: OtherFeeType
        """
        return self._other_fee_type

    @other_fee_type.setter
    def other_fee_type(self, other_fee_type):
        """Sets the other_fee_type of this OverdraftOverdraftFeeChargeDetail.


        :param other_fee_type: The other_fee_type of this OverdraftOverdraftFeeChargeDetail.  # noqa: E501
        :type: OtherFeeType
        """

        self._other_fee_type = other_fee_type

    @property
    def overdraft_control_indicator(self):
        """Gets the overdraft_control_indicator of this OverdraftOverdraftFeeChargeDetail.  # noqa: E501


        :return: The overdraft_control_indicator of this OverdraftOverdraftFeeChargeDetail.  # noqa: E501
        :rtype: bool
        """
        return self._overdraft_control_indicator

    @overdraft_control_indicator.setter
    def overdraft_control_indicator(self, overdraft_control_indicator):
        """Sets the overdraft_control_indicator of this OverdraftOverdraftFeeChargeDetail.


        :param overdraft_control_indicator: The overdraft_control_indicator of this OverdraftOverdraftFeeChargeDetail.  # noqa: E501
        :type: bool
        """

        self._overdraft_control_indicator = overdraft_control_indicator

    @property
    def overdraft_fee_charge_cap(self):
        """Gets the overdraft_fee_charge_cap of this OverdraftOverdraftFeeChargeDetail.  # noqa: E501


        :return: The overdraft_fee_charge_cap of this OverdraftOverdraftFeeChargeDetail.  # noqa: E501
        :rtype: OverdraftOverdraftFeeChargeCap
        """
        return self._overdraft_fee_charge_cap

    @overdraft_fee_charge_cap.setter
    def overdraft_fee_charge_cap(self, overdraft_fee_charge_cap):
        """Sets the overdraft_fee_charge_cap of this OverdraftOverdraftFeeChargeDetail.


        :param overdraft_fee_charge_cap: The overdraft_fee_charge_cap of this OverdraftOverdraftFeeChargeDetail.  # noqa: E501
        :type: OverdraftOverdraftFeeChargeCap
        """

        self._overdraft_fee_charge_cap = overdraft_fee_charge_cap

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
        if not isinstance(other, OverdraftOverdraftFeeChargeDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
