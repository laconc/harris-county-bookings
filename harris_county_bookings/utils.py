import hashlib
from datetime import datetime

__all__ = ['Utils']


class Utils(object):
    @staticmethod
    def filter_keys_from_dict(dictionary, keys):
        return {k: v for k, v in filter(lambda t: t[0] in keys, dictionary.items())}

    @staticmethod
    def generate_hash(string):
        hash_object = hashlib.sha1(string.encode())
        return hash_object.hexdigest()

    @staticmethod
    def standardize_date(dt, incoming_format):
        return datetime.strptime(dt, incoming_format).strftime('%m/%d/%Y')

    @staticmethod
    def strip_whitespace_from_values(dictionary):
        return {k: v.strip() for k, v in dictionary.items()}
