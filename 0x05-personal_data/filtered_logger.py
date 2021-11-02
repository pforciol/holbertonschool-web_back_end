#!/usr/bin/env python3
""" filtered_logger module """

import logging
import re
from typing import List

PII_FIELDS = ("name", "email", "phone", "ssn", "password")


def filter_datum(
        fields: List[str],
        redaction: str,
        message: str,
        separator: str) -> str:
    """

        Args:
            fields: all fields to obfuscate
            redaction: by what the field will be obfuscated
            message: the log line
            separator: by which character separate all fields in the message

        Returns:
            The log message, obfuscated.

    """

    for field in fields:
        message = re.sub(fr'{field}=([^=]*){separator}',
                         fr'{field}={redaction}{separator}', message)
    return message


class RedactingFormatter(logging.Formatter):
    """

        Redacting Formatter class

    """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        self.fields = fields
        super(RedactingFormatter, self).__init__(self.FORMAT)

    def format(self, record: logging.LogRecord) -> str:
        """

            Args:
                record: incoming log record.

            Returns:
                String with filtered values.

        """
        return filter_datum(self.fields, self.REDACTION,
                            super().format(record), self.SEPARATOR)


def get_logger() -> logging.Logger:
    """

        Returns:
            The Logger object.

    """
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)
    ch.setFormatter(RedactingFormatter(PII_FIELDS))

    logger.addHandler(ch)

    return logger
