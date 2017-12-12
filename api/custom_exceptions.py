class GeneralException(Exception):
    """Class for lendingfront api exceptions."""

    def __init__(self, message, status_code):
        self.custom_message = message
        self.status_code = status_code

    def __str__(self):
        return repr(self.custom_message)

    @property
    def message(self):
        """
        The user friendly message property
        """
        return self.custom_message

    @property
    def get_status_code(self):
        """
        The user friendly message property
        """
        return self.status_code
