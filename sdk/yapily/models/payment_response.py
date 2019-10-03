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

from yapily.models.amount import Amount  # noqa: F401,E501
from yapily.models.charge_details import ChargeDetails  # noqa: F401,E501
from yapily.models.frequency_response import FrequencyResponse  # noqa: F401,E501
from yapily.models.payee import Payee  # noqa: F401,E501
from yapily.models.payment_status_details import PaymentStatusDetails  # noqa: F401,E501


class PaymentResponse(object):
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
        'payment_idempotency_id': 'str',
        'institution_consent_id': 'str',
        'payment_lifecycle_id': 'str',
        'status': 'str',
        'status_details': 'PaymentStatusDetails',
        'payee_details': 'Payee',
        'reference': 'str',
        'amount': 'float',
        'currency': 'str',
        'amount_details': 'Amount',
        'first_payment_amount_details': 'Amount',
        'first_payment_date_time': 'datetime',
        'next_payment_amount_details': 'Amount',
        'next_payment_date_time': 'datetime',
        'final_payment_amount_details': 'Amount',
        'final_payment_date_time': 'datetime',
        'created_at': 'datetime',
        'previous_payment_amount_details': 'Amount',
        'previous_payment_date_time': 'datetime',
        'charge_details': 'list[ChargeDetails]',
        'scheduled_payment_type': 'str',
        'scheduled_payment_date_time': 'datetime',
        'frequency_details': 'FrequencyResponse',
        'account_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'payment_idempotency_id': 'paymentIdempotencyId',
        'institution_consent_id': 'institutionConsentId',
        'payment_lifecycle_id': 'paymentLifecycleId',
        'status': 'status',
        'status_details': 'statusDetails',
        'payee_details': 'payeeDetails',
        'reference': 'reference',
        'amount': 'amount',
        'currency': 'currency',
        'amount_details': 'amountDetails',
        'first_payment_amount_details': 'firstPaymentAmountDetails',
        'first_payment_date_time': 'firstPaymentDateTime',
        'next_payment_amount_details': 'nextPaymentAmountDetails',
        'next_payment_date_time': 'nextPaymentDateTime',
        'final_payment_amount_details': 'finalPaymentAmountDetails',
        'final_payment_date_time': 'finalPaymentDateTime',
        'created_at': 'createdAt',
        'previous_payment_amount_details': 'previousPaymentAmountDetails',
        'previous_payment_date_time': 'previousPaymentDateTime',
        'charge_details': 'chargeDetails',
        'scheduled_payment_type': 'scheduledPaymentType',
        'scheduled_payment_date_time': 'scheduledPaymentDateTime',
        'frequency_details': 'frequencyDetails',
        'account_id': 'accountId'
    }

    def __init__(self, id=None, payment_idempotency_id=None, institution_consent_id=None, payment_lifecycle_id=None, status=None, status_details=None, payee_details=None, reference=None, amount=None, currency=None, amount_details=None, first_payment_amount_details=None, first_payment_date_time=None, next_payment_amount_details=None, next_payment_date_time=None, final_payment_amount_details=None, final_payment_date_time=None, created_at=None, previous_payment_amount_details=None, previous_payment_date_time=None, charge_details=None, scheduled_payment_type=None, scheduled_payment_date_time=None, frequency_details=None, account_id=None):  # noqa: E501
        """PaymentResponse - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._payment_idempotency_id = None
        self._institution_consent_id = None
        self._payment_lifecycle_id = None
        self._status = None
        self._status_details = None
        self._payee_details = None
        self._reference = None
        self._amount = None
        self._currency = None
        self._amount_details = None
        self._first_payment_amount_details = None
        self._first_payment_date_time = None
        self._next_payment_amount_details = None
        self._next_payment_date_time = None
        self._final_payment_amount_details = None
        self._final_payment_date_time = None
        self._created_at = None
        self._previous_payment_amount_details = None
        self._previous_payment_date_time = None
        self._charge_details = None
        self._scheduled_payment_type = None
        self._scheduled_payment_date_time = None
        self._frequency_details = None
        self._account_id = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if payment_idempotency_id is not None:
            self.payment_idempotency_id = payment_idempotency_id
        if institution_consent_id is not None:
            self.institution_consent_id = institution_consent_id
        if payment_lifecycle_id is not None:
            self.payment_lifecycle_id = payment_lifecycle_id
        if status is not None:
            self.status = status
        if status_details is not None:
            self.status_details = status_details
        if payee_details is not None:
            self.payee_details = payee_details
        if reference is not None:
            self.reference = reference
        if amount is not None:
            self.amount = amount
        if currency is not None:
            self.currency = currency
        if amount_details is not None:
            self.amount_details = amount_details
        if first_payment_amount_details is not None:
            self.first_payment_amount_details = first_payment_amount_details
        if first_payment_date_time is not None:
            self.first_payment_date_time = first_payment_date_time
        if next_payment_amount_details is not None:
            self.next_payment_amount_details = next_payment_amount_details
        if next_payment_date_time is not None:
            self.next_payment_date_time = next_payment_date_time
        if final_payment_amount_details is not None:
            self.final_payment_amount_details = final_payment_amount_details
        if final_payment_date_time is not None:
            self.final_payment_date_time = final_payment_date_time
        if created_at is not None:
            self.created_at = created_at
        if previous_payment_amount_details is not None:
            self.previous_payment_amount_details = previous_payment_amount_details
        if previous_payment_date_time is not None:
            self.previous_payment_date_time = previous_payment_date_time
        if charge_details is not None:
            self.charge_details = charge_details
        if scheduled_payment_type is not None:
            self.scheduled_payment_type = scheduled_payment_type
        if scheduled_payment_date_time is not None:
            self.scheduled_payment_date_time = scheduled_payment_date_time
        if frequency_details is not None:
            self.frequency_details = frequency_details
        if account_id is not None:
            self.account_id = account_id

    @property
    def id(self):
        """Gets the id of this PaymentResponse.  # noqa: E501


        :return: The id of this PaymentResponse.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PaymentResponse.


        :param id: The id of this PaymentResponse.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def payment_idempotency_id(self):
        """Gets the payment_idempotency_id of this PaymentResponse.  # noqa: E501


        :return: The payment_idempotency_id of this PaymentResponse.  # noqa: E501
        :rtype: str
        """
        return self._payment_idempotency_id

    @payment_idempotency_id.setter
    def payment_idempotency_id(self, payment_idempotency_id):
        """Sets the payment_idempotency_id of this PaymentResponse.


        :param payment_idempotency_id: The payment_idempotency_id of this PaymentResponse.  # noqa: E501
        :type: str
        """

        self._payment_idempotency_id = payment_idempotency_id

    @property
    def institution_consent_id(self):
        """Gets the institution_consent_id of this PaymentResponse.  # noqa: E501


        :return: The institution_consent_id of this PaymentResponse.  # noqa: E501
        :rtype: str
        """
        return self._institution_consent_id

    @institution_consent_id.setter
    def institution_consent_id(self, institution_consent_id):
        """Sets the institution_consent_id of this PaymentResponse.


        :param institution_consent_id: The institution_consent_id of this PaymentResponse.  # noqa: E501
        :type: str
        """

        self._institution_consent_id = institution_consent_id

    @property
    def payment_lifecycle_id(self):
        """Gets the payment_lifecycle_id of this PaymentResponse.  # noqa: E501


        :return: The payment_lifecycle_id of this PaymentResponse.  # noqa: E501
        :rtype: str
        """
        return self._payment_lifecycle_id

    @payment_lifecycle_id.setter
    def payment_lifecycle_id(self, payment_lifecycle_id):
        """Sets the payment_lifecycle_id of this PaymentResponse.


        :param payment_lifecycle_id: The payment_lifecycle_id of this PaymentResponse.  # noqa: E501
        :type: str
        """

        self._payment_lifecycle_id = payment_lifecycle_id

    @property
    def status(self):
        """Gets the status of this PaymentResponse.  # noqa: E501


        :return: The status of this PaymentResponse.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this PaymentResponse.


        :param status: The status of this PaymentResponse.  # noqa: E501
        :type: str
        """
        allowed_values = ["PENDING", "FAILED", "DECLINED", "COMPLETED", "EXPIRED", "UNKNOWN", "ACTIVE", "INACTIVE"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def status_details(self):
        """Gets the status_details of this PaymentResponse.  # noqa: E501


        :return: The status_details of this PaymentResponse.  # noqa: E501
        :rtype: PaymentStatusDetails
        """
        return self._status_details

    @status_details.setter
    def status_details(self, status_details):
        """Sets the status_details of this PaymentResponse.


        :param status_details: The status_details of this PaymentResponse.  # noqa: E501
        :type: PaymentStatusDetails
        """

        self._status_details = status_details

    @property
    def payee_details(self):
        """Gets the payee_details of this PaymentResponse.  # noqa: E501


        :return: The payee_details of this PaymentResponse.  # noqa: E501
        :rtype: Payee
        """
        return self._payee_details

    @payee_details.setter
    def payee_details(self, payee_details):
        """Sets the payee_details of this PaymentResponse.


        :param payee_details: The payee_details of this PaymentResponse.  # noqa: E501
        :type: Payee
        """

        self._payee_details = payee_details

    @property
    def reference(self):
        """Gets the reference of this PaymentResponse.  # noqa: E501


        :return: The reference of this PaymentResponse.  # noqa: E501
        :rtype: str
        """
        return self._reference

    @reference.setter
    def reference(self, reference):
        """Sets the reference of this PaymentResponse.


        :param reference: The reference of this PaymentResponse.  # noqa: E501
        :type: str
        """

        self._reference = reference

    @property
    def amount(self):
        """Gets the amount of this PaymentResponse.  # noqa: E501


        :return: The amount of this PaymentResponse.  # noqa: E501
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this PaymentResponse.


        :param amount: The amount of this PaymentResponse.  # noqa: E501
        :type: float
        """

        self._amount = amount

    @property
    def currency(self):
        """Gets the currency of this PaymentResponse.  # noqa: E501


        :return: The currency of this PaymentResponse.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this PaymentResponse.


        :param currency: The currency of this PaymentResponse.  # noqa: E501
        :type: str
        """

        self._currency = currency

    @property
    def amount_details(self):
        """Gets the amount_details of this PaymentResponse.  # noqa: E501


        :return: The amount_details of this PaymentResponse.  # noqa: E501
        :rtype: Amount
        """
        return self._amount_details

    @amount_details.setter
    def amount_details(self, amount_details):
        """Sets the amount_details of this PaymentResponse.


        :param amount_details: The amount_details of this PaymentResponse.  # noqa: E501
        :type: Amount
        """

        self._amount_details = amount_details

    @property
    def first_payment_amount_details(self):
        """Gets the first_payment_amount_details of this PaymentResponse.  # noqa: E501


        :return: The first_payment_amount_details of this PaymentResponse.  # noqa: E501
        :rtype: Amount
        """
        return self._first_payment_amount_details

    @first_payment_amount_details.setter
    def first_payment_amount_details(self, first_payment_amount_details):
        """Sets the first_payment_amount_details of this PaymentResponse.


        :param first_payment_amount_details: The first_payment_amount_details of this PaymentResponse.  # noqa: E501
        :type: Amount
        """

        self._first_payment_amount_details = first_payment_amount_details

    @property
    def first_payment_date_time(self):
        """Gets the first_payment_date_time of this PaymentResponse.  # noqa: E501


        :return: The first_payment_date_time of this PaymentResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._first_payment_date_time

    @first_payment_date_time.setter
    def first_payment_date_time(self, first_payment_date_time):
        """Sets the first_payment_date_time of this PaymentResponse.


        :param first_payment_date_time: The first_payment_date_time of this PaymentResponse.  # noqa: E501
        :type: datetime
        """

        self._first_payment_date_time = first_payment_date_time

    @property
    def next_payment_amount_details(self):
        """Gets the next_payment_amount_details of this PaymentResponse.  # noqa: E501


        :return: The next_payment_amount_details of this PaymentResponse.  # noqa: E501
        :rtype: Amount
        """
        return self._next_payment_amount_details

    @next_payment_amount_details.setter
    def next_payment_amount_details(self, next_payment_amount_details):
        """Sets the next_payment_amount_details of this PaymentResponse.


        :param next_payment_amount_details: The next_payment_amount_details of this PaymentResponse.  # noqa: E501
        :type: Amount
        """

        self._next_payment_amount_details = next_payment_amount_details

    @property
    def next_payment_date_time(self):
        """Gets the next_payment_date_time of this PaymentResponse.  # noqa: E501


        :return: The next_payment_date_time of this PaymentResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._next_payment_date_time

    @next_payment_date_time.setter
    def next_payment_date_time(self, next_payment_date_time):
        """Sets the next_payment_date_time of this PaymentResponse.


        :param next_payment_date_time: The next_payment_date_time of this PaymentResponse.  # noqa: E501
        :type: datetime
        """

        self._next_payment_date_time = next_payment_date_time

    @property
    def final_payment_amount_details(self):
        """Gets the final_payment_amount_details of this PaymentResponse.  # noqa: E501


        :return: The final_payment_amount_details of this PaymentResponse.  # noqa: E501
        :rtype: Amount
        """
        return self._final_payment_amount_details

    @final_payment_amount_details.setter
    def final_payment_amount_details(self, final_payment_amount_details):
        """Sets the final_payment_amount_details of this PaymentResponse.


        :param final_payment_amount_details: The final_payment_amount_details of this PaymentResponse.  # noqa: E501
        :type: Amount
        """

        self._final_payment_amount_details = final_payment_amount_details

    @property
    def final_payment_date_time(self):
        """Gets the final_payment_date_time of this PaymentResponse.  # noqa: E501


        :return: The final_payment_date_time of this PaymentResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._final_payment_date_time

    @final_payment_date_time.setter
    def final_payment_date_time(self, final_payment_date_time):
        """Sets the final_payment_date_time of this PaymentResponse.


        :param final_payment_date_time: The final_payment_date_time of this PaymentResponse.  # noqa: E501
        :type: datetime
        """

        self._final_payment_date_time = final_payment_date_time

    @property
    def created_at(self):
        """Gets the created_at of this PaymentResponse.  # noqa: E501


        :return: The created_at of this PaymentResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this PaymentResponse.


        :param created_at: The created_at of this PaymentResponse.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def previous_payment_amount_details(self):
        """Gets the previous_payment_amount_details of this PaymentResponse.  # noqa: E501


        :return: The previous_payment_amount_details of this PaymentResponse.  # noqa: E501
        :rtype: Amount
        """
        return self._previous_payment_amount_details

    @previous_payment_amount_details.setter
    def previous_payment_amount_details(self, previous_payment_amount_details):
        """Sets the previous_payment_amount_details of this PaymentResponse.


        :param previous_payment_amount_details: The previous_payment_amount_details of this PaymentResponse.  # noqa: E501
        :type: Amount
        """

        self._previous_payment_amount_details = previous_payment_amount_details

    @property
    def previous_payment_date_time(self):
        """Gets the previous_payment_date_time of this PaymentResponse.  # noqa: E501


        :return: The previous_payment_date_time of this PaymentResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._previous_payment_date_time

    @previous_payment_date_time.setter
    def previous_payment_date_time(self, previous_payment_date_time):
        """Sets the previous_payment_date_time of this PaymentResponse.


        :param previous_payment_date_time: The previous_payment_date_time of this PaymentResponse.  # noqa: E501
        :type: datetime
        """

        self._previous_payment_date_time = previous_payment_date_time

    @property
    def charge_details(self):
        """Gets the charge_details of this PaymentResponse.  # noqa: E501


        :return: The charge_details of this PaymentResponse.  # noqa: E501
        :rtype: list[ChargeDetails]
        """
        return self._charge_details

    @charge_details.setter
    def charge_details(self, charge_details):
        """Sets the charge_details of this PaymentResponse.


        :param charge_details: The charge_details of this PaymentResponse.  # noqa: E501
        :type: list[ChargeDetails]
        """

        self._charge_details = charge_details

    @property
    def scheduled_payment_type(self):
        """Gets the scheduled_payment_type of this PaymentResponse.  # noqa: E501


        :return: The scheduled_payment_type of this PaymentResponse.  # noqa: E501
        :rtype: str
        """
        return self._scheduled_payment_type

    @scheduled_payment_type.setter
    def scheduled_payment_type(self, scheduled_payment_type):
        """Sets the scheduled_payment_type of this PaymentResponse.


        :param scheduled_payment_type: The scheduled_payment_type of this PaymentResponse.  # noqa: E501
        :type: str
        """

        self._scheduled_payment_type = scheduled_payment_type

    @property
    def scheduled_payment_date_time(self):
        """Gets the scheduled_payment_date_time of this PaymentResponse.  # noqa: E501


        :return: The scheduled_payment_date_time of this PaymentResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._scheduled_payment_date_time

    @scheduled_payment_date_time.setter
    def scheduled_payment_date_time(self, scheduled_payment_date_time):
        """Sets the scheduled_payment_date_time of this PaymentResponse.


        :param scheduled_payment_date_time: The scheduled_payment_date_time of this PaymentResponse.  # noqa: E501
        :type: datetime
        """

        self._scheduled_payment_date_time = scheduled_payment_date_time

    @property
    def frequency_details(self):
        """Gets the frequency_details of this PaymentResponse.  # noqa: E501


        :return: The frequency_details of this PaymentResponse.  # noqa: E501
        :rtype: FrequencyResponse
        """
        return self._frequency_details

    @frequency_details.setter
    def frequency_details(self, frequency_details):
        """Sets the frequency_details of this PaymentResponse.


        :param frequency_details: The frequency_details of this PaymentResponse.  # noqa: E501
        :type: FrequencyResponse
        """

        self._frequency_details = frequency_details

    @property
    def account_id(self):
        """Gets the account_id of this PaymentResponse.  # noqa: E501


        :return: The account_id of this PaymentResponse.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this PaymentResponse.


        :param account_id: The account_id of this PaymentResponse.  # noqa: E501
        :type: str
        """

        self._account_id = account_id

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
        if not isinstance(other, PaymentResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
