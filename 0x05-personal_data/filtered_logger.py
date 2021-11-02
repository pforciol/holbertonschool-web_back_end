#!/usr/bin/env python3
""" filtered_logger module """

import logging
import re
import os
import mysql.connector
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


def get_db() -> mysql.connector.connection.MySQLConnection:
    """

        Returns:
            The MySQLConnection object.

    """
    user = os.getenv("PERSONAL_DATA_DB_USERNAME") or "root"
    pswd = os.getenv("PERSONAL_DATA_DB_PASSWORD") or ""
    host = os.getenv("PERSONAL_DATA_DB_HOST") or "localhost"
    name = os.getenv("PERSONAL_DATA_DB_NAME")

    return mysql.connector.connect(
        host=host,
        user=user,
        password=pswd,
        database=name)


if __name__ == '__main__':
    db = get_db()
    cursor = db.cursor()

    query = "SELECT group_concat(COLUMN_NAME) FROM INFORMATION_SCHEMA.COLUMNS\
            WHERE TABLE_SCHEMA = 'my_db' AND TABLE_NAME = 'users';"
    cursor.execute(query)

    for row in cursor:
        keys = row[0]

    keys = keys.split(',')

    cursor.execute("SELECT * FROM users;")
    for row in cursor:
        to_join = [f'{k}={v}' for k, v in zip(keys, row)]
        message = "; ".join(to_join)
        message += ';'
        log_record = logging.LogRecord("user_data", logging.INFO, None, None,
                                       message, None, None)

        formatter = RedactingFormatter(fields=("name", "email", "phone", "ssn",
                                               "password"))

        print(formatter.format(log_record))

    cursor.close()
    db.close()
