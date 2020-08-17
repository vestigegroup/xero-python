# coding: utf-8

"""
    Xero Payroll AU

    This is the Xero Payroll API for orgs in Australia region.  # noqa: E501

    OpenAPI spec version: 2.2.12
    Contact: api@xero.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero_python.models import BaseModel


class ReimbursementLines(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {"reimbursement_lines": "list[ReimbursementLine]"}

    attribute_map = {"reimbursement_lines": "ReimbursementLines"}

    def __init__(self, reimbursement_lines=None):  # noqa: E501
        """ReimbursementLines - a model defined in OpenAPI"""  # noqa: E501

        self._reimbursement_lines = None
        self.discriminator = None

        if reimbursement_lines is not None:
            self.reimbursement_lines = reimbursement_lines

    @property
    def reimbursement_lines(self):
        """Gets the reimbursement_lines of this ReimbursementLines.  # noqa: E501


        :return: The reimbursement_lines of this ReimbursementLines.  # noqa: E501
        :rtype: list[ReimbursementLine]
        """
        return self._reimbursement_lines

    @reimbursement_lines.setter
    def reimbursement_lines(self, reimbursement_lines):
        """Sets the reimbursement_lines of this ReimbursementLines.


        :param reimbursement_lines: The reimbursement_lines of this ReimbursementLines.  # noqa: E501
        :type: list[ReimbursementLine]
        """

        self._reimbursement_lines = reimbursement_lines