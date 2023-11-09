class StateModel:
    def __init__(self):
        pass

    @staticmethod
    def errorstate():
        error = 'ERROR'
        return error

    commonerror_set = {"plugin", "notifications"}