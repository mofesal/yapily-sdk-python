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

from yapily.models.address_details import AddressDetails  # noqa: F401,E501
from yapily.models.amount import Amount  # noqa: F401,E501
from yapily.models.balance import Balance  # noqa: F401,E501
from yapily.models.charge_details import ChargeDetails  # noqa: F401,E501
from yapily.models.currency_exchange import CurrencyExchange  # noqa: F401,E501
from yapily.models.iso_bank_transaction_code import IsoBankTransactionCode  # noqa: F401,E501
from yapily.models.merchant import Merchant  # noqa: F401,E501
from yapily.models.proprietary_bank_transaction_code import ProprietaryBankTransactionCode  # noqa: F401,E501
from yapily.models.statement_reference import StatementReference  # noqa: F401,E501


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
        'booking_date_time': 'datetime',
        'value_date_time': 'datetime',
        'status': 'str',
        'amount': 'float',
        'currency': 'str',
        'transaction_amount': 'Amount',
        'currency_exchange': 'CurrencyExchange',
        'charge_details': 'ChargeDetails',
        'reference': 'str',
        'statement_references': 'list[StatementReference]',
        'description': 'str',
        'transaction_information': 'list[str]',
        'address_details': 'AddressDetails',
        'iso_bank_transaction_code': 'IsoBankTransactionCode',
        'proprietary_bank_transaction_code': 'ProprietaryBankTransactionCode',
        'balance': 'Balance',
        'merchant': 'Merchant'
    }

    attribute_map = {
        'id': 'id',
        'date': 'date',
        'booking_date_time': 'bookingDateTime',
        'value_date_time': 'valueDateTime',
        'status': 'status',
        'amount': 'amount',
        'currency': 'currency',
        'transaction_amount': 'transactionAmount',
        'currency_exchange': 'currencyExchange',
        'charge_details': 'chargeDetails',
        'reference': 'reference',
        'statement_references': 'statementReferences',
        'description': 'description',
        'transaction_information': 'transactionInformation',
        'address_details': 'addressDetails',
        'iso_bank_transaction_code': 'isoBankTransactionCode',
        'proprietary_bank_transaction_code': 'proprietaryBankTransactionCode',
        'balance': 'balance',
        'merchant': 'merchant'
    }

    def __init__(self, id=None, date=None, booking_date_time=None, value_date_time=None, status=None, amount=None, currency=None, transaction_amount=None, currency_exchange=None, charge_details=None, reference=None, statement_references=None, description=None, transaction_information=None, address_details=None, iso_bank_transaction_code=None, proprietary_bank_transaction_code=None, balance=None, merchant=None):  # noqa: E501
        """Transaction - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._date = None
        self._booking_date_time = None
        self._value_date_time = None
        self._status = None
        self._amount = None
        self._currency = None
        self._transaction_amount = None
        self._currency_exchange = None
        self._charge_details = None
        self._reference = None
        self._statement_references = None
        self._description = None
        self._transaction_information = None
        self._address_details = None
        self._iso_bank_transaction_code = None
        self._proprietary_bank_transaction_code = None
        self._balance = None
        self._merchant = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if date is not None:
            self.date = date
        if booking_date_time is not None:
            self.booking_date_time = booking_date_time
        if value_date_time is not None:
            self.value_date_time = value_date_time
        if status is not None:
            self.status = status
        if amount is not None:
            self.amount = amount
        if currency is not None:
            self.currency = currency
        if transaction_amount is not None:
            self.transaction_amount = transaction_amount
        if currency_exchange is not None:
            self.currency_exchange = currency_exchange
        if charge_details is not None:
            self.charge_details = charge_details
        if reference is not None:
            self.reference = reference
        if statement_references is not None:
            self.statement_references = statement_references
        if description is not None:
            self.description = description
        if transaction_information is not None:
            self.transaction_information = transaction_information
        if address_details is not None:
            self.address_details = address_details
        if iso_bank_transaction_code is not None:
            self.iso_bank_transaction_code = iso_bank_transaction_code
        if proprietary_bank_transaction_code is not None:
            self.proprietary_bank_transaction_code = proprietary_bank_transaction_code
        if balance is not None:
            self.balance = balance
        if merchant is not None:
            self.merchant = merchant

    @property
    def id(self):
        """Gets the id of this Transaction.  # noqa: E501

        Transaction Id returned by the institution if present  # noqa: E501

        :return: The id of this Transaction.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Transaction.

        Transaction Id returned by the institution if present  # noqa: E501

        :param id: The id of this Transaction.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def date(self):
        """Gets the date of this Transaction.  # noqa: E501

        Transaction date as defined by the institution  # noqa: E501

        :return: The date of this Transaction.  # noqa: E501
        :rtype: datetime
        """
        return self._date

    @date.setter
    def date(self, date):
        """Sets the date of this Transaction.

        Transaction date as defined by the institution  # noqa: E501

        :param date: The date of this Transaction.  # noqa: E501
        :type: datetime
        """

        self._date = date

    @property
    def booking_date_time(self):
        """Gets the booking_date_time of this Transaction.  # noqa: E501

        Date and (if available) time that transaction is posted  # noqa: E501

        :return: The booking_date_time of this Transaction.  # noqa: E501
        :rtype: datetime
        """
        return self._booking_date_time

    @booking_date_time.setter
    def booking_date_time(self, booking_date_time):
        """Sets the booking_date_time of this Transaction.

        Date and (if available) time that transaction is posted  # noqa: E501

        :param booking_date_time: The booking_date_time of this Transaction.  # noqa: E501
        :type: datetime
        """

        self._booking_date_time = booking_date_time

    @property
    def value_date_time(self):
        """Gets the value_date_time of this Transaction.  # noqa: E501

        The actual or expected date and time transaction is cleared  # noqa: E501

        :return: The value_date_time of this Transaction.  # noqa: E501
        :rtype: datetime
        """
        return self._value_date_time

    @value_date_time.setter
    def value_date_time(self, value_date_time):
        """Sets the value_date_time of this Transaction.

        The actual or expected date and time transaction is cleared  # noqa: E501

        :param value_date_time: The value_date_time of this Transaction.  # noqa: E501
        :type: datetime
        """

        self._value_date_time = value_date_time

    @property
    def status(self):
        """Gets the status of this Transaction.  # noqa: E501

        The status of the transaction  # noqa: E501

        :return: The status of this Transaction.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Transaction.

        The status of the transaction  # noqa: E501

        :param status: The status of this Transaction.  # noqa: E501
        :type: str
        """
        allowed_values = ["ACCOUNT_CHECK", "BOOKED", "DECLINED", "PENDING", "REFUNDED", "RETRYING", "REVERSED", "UPCOMING"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def amount(self):
        """Gets the amount of this Transaction.  # noqa: E501

        Deprecated. Use the amount value in `transactionAmount` instead  # noqa: E501

        :return: The amount of this Transaction.  # noqa: E501
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this Transaction.

        Deprecated. Use the amount value in `transactionAmount` instead  # noqa: E501

        :param amount: The amount of this Transaction.  # noqa: E501
        :type: float
        """

        self._amount = amount

    @property
    def currency(self):
        """Gets the currency of this Transaction.  # noqa: E501

        Deprecated. Use the currency value in `transactionAmount` instead  # noqa: E501

        :return: The currency of this Transaction.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this Transaction.

        Deprecated. Use the currency value in `transactionAmount` instead  # noqa: E501

        :param currency: The currency of this Transaction.  # noqa: E501
        :type: str
        """

        self._currency = currency

    @property
    def transaction_amount(self):
        """Gets the transaction_amount of this Transaction.  # noqa: E501


        :return: The transaction_amount of this Transaction.  # noqa: E501
        :rtype: Amount
        """
        return self._transaction_amount

    @transaction_amount.setter
    def transaction_amount(self, transaction_amount):
        """Sets the transaction_amount of this Transaction.


        :param transaction_amount: The transaction_amount of this Transaction.  # noqa: E501
        :type: Amount
        """

        self._transaction_amount = transaction_amount

    @property
    def currency_exchange(self):
        """Gets the currency_exchange of this Transaction.  # noqa: E501


        :return: The currency_exchange of this Transaction.  # noqa: E501
        :rtype: CurrencyExchange
        """
        return self._currency_exchange

    @currency_exchange.setter
    def currency_exchange(self, currency_exchange):
        """Sets the currency_exchange of this Transaction.


        :param currency_exchange: The currency_exchange of this Transaction.  # noqa: E501
        :type: CurrencyExchange
        """

        self._currency_exchange = currency_exchange

    @property
    def charge_details(self):
        """Gets the charge_details of this Transaction.  # noqa: E501

        If present, contains details of any charges applied during this transaction  # noqa: E501

        :return: The charge_details of this Transaction.  # noqa: E501
        :rtype: ChargeDetails
        """
        return self._charge_details

    @charge_details.setter
    def charge_details(self, charge_details):
        """Sets the charge_details of this Transaction.

        If present, contains details of any charges applied during this transaction  # noqa: E501

        :param charge_details: The charge_details of this Transaction.  # noqa: E501
        :type: ChargeDetails
        """

        self._charge_details = charge_details

    @property
    def reference(self):
        """Gets the reference of this Transaction.  # noqa: E501

        Transaction reference  # noqa: E501

        :return: The reference of this Transaction.  # noqa: E501
        :rtype: str
        """
        return self._reference

    @reference.setter
    def reference(self, reference):
        """Sets the reference of this Transaction.

        Transaction reference  # noqa: E501

        :param reference: The reference of this Transaction.  # noqa: E501
        :type: str
        """

        self._reference = reference

    @property
    def statement_references(self):
        """Gets the statement_references of this Transaction.  # noqa: E501


        :return: The statement_references of this Transaction.  # noqa: E501
        :rtype: list[StatementReference]
        """
        return self._statement_references

    @statement_references.setter
    def statement_references(self, statement_references):
        """Sets the statement_references of this Transaction.


        :param statement_references: The statement_references of this Transaction.  # noqa: E501
        :type: list[StatementReference]
        """

        self._statement_references = statement_references

    @property
    def description(self):
        """Gets the description of this Transaction.  # noqa: E501

        Unstructured text containing details of the transaction. Usage varies according to the institution  # noqa: E501

        :return: The description of this Transaction.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Transaction.

        Unstructured text containing details of the transaction. Usage varies according to the institution  # noqa: E501

        :param description: The description of this Transaction.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def transaction_information(self):
        """Gets the transaction_information of this Transaction.  # noqa: E501

        Further information related to the transaction. Usage varies according to the institution  # noqa: E501

        :return: The transaction_information of this Transaction.  # noqa: E501
        :rtype: list[str]
        """
        return self._transaction_information

    @transaction_information.setter
    def transaction_information(self, transaction_information):
        """Sets the transaction_information of this Transaction.

        Further information related to the transaction. Usage varies according to the institution  # noqa: E501

        :param transaction_information: The transaction_information of this Transaction.  # noqa: E501
        :type: list[str]
        """

        self._transaction_information = transaction_information

    @property
    def address_details(self):
        """Gets the address_details of this Transaction.  # noqa: E501


        :return: The address_details of this Transaction.  # noqa: E501
        :rtype: AddressDetails
        """
        return self._address_details

    @address_details.setter
    def address_details(self, address_details):
        """Sets the address_details of this Transaction.


        :param address_details: The address_details of this Transaction.  # noqa: E501
        :type: AddressDetails
        """

        self._address_details = address_details

    @property
    def iso_bank_transaction_code(self):
        """Gets the iso_bank_transaction_code of this Transaction.  # noqa: E501


        :return: The iso_bank_transaction_code of this Transaction.  # noqa: E501
        :rtype: IsoBankTransactionCode
        """
        return self._iso_bank_transaction_code

    @iso_bank_transaction_code.setter
    def iso_bank_transaction_code(self, iso_bank_transaction_code):
        """Sets the iso_bank_transaction_code of this Transaction.


        :param iso_bank_transaction_code: The iso_bank_transaction_code of this Transaction.  # noqa: E501
        :type: IsoBankTransactionCode
        """

        self._iso_bank_transaction_code = iso_bank_transaction_code

    @property
    def proprietary_bank_transaction_code(self):
        """Gets the proprietary_bank_transaction_code of this Transaction.  # noqa: E501


        :return: The proprietary_bank_transaction_code of this Transaction.  # noqa: E501
        :rtype: ProprietaryBankTransactionCode
        """
        return self._proprietary_bank_transaction_code

    @proprietary_bank_transaction_code.setter
    def proprietary_bank_transaction_code(self, proprietary_bank_transaction_code):
        """Sets the proprietary_bank_transaction_code of this Transaction.


        :param proprietary_bank_transaction_code: The proprietary_bank_transaction_code of this Transaction.  # noqa: E501
        :type: ProprietaryBankTransactionCode
        """

        self._proprietary_bank_transaction_code = proprietary_bank_transaction_code

    @property
    def balance(self):
        """Gets the balance of this Transaction.  # noqa: E501

        Running account balance after transaction has been applied  # noqa: E501

        :return: The balance of this Transaction.  # noqa: E501
        :rtype: Balance
        """
        return self._balance

    @balance.setter
    def balance(self, balance):
        """Sets the balance of this Transaction.

        Running account balance after transaction has been applied  # noqa: E501

        :param balance: The balance of this Transaction.  # noqa: E501
        :type: Balance
        """

        self._balance = balance

    @property
    def merchant(self):
        """Gets the merchant of this Transaction.  # noqa: E501

        Merchant details  # noqa: E501

        :return: The merchant of this Transaction.  # noqa: E501
        :rtype: Merchant
        """
        return self._merchant

    @merchant.setter
    def merchant(self, merchant):
        """Sets the merchant of this Transaction.

        Merchant details  # noqa: E501

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
