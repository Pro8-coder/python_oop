import re


class CardCheck:
    CARD_NUMBER_PATTERN = re.compile(r'^\d{4}-\d{4}-\d{4}-\d{4}$')
    NAME_PATTERN = re.compile(r'^[A-Z0-9]+ [A-Z0-9]+$')

    @staticmethod
    def check_card_number(number):
        return bool(CardCheck.CARD_NUMBER_PATTERN.match(number))

    @staticmethod
    def check_name(name):
        return bool(CardCheck.NAME_PATTERN.match(name))

