import json

class Transactions:
    """
    This class is used to keep transactions
    """

    def __init__(self) -> None:
        # contains transaction in list
        self.__transactions = []


    def toString(self) -> str:
        """
        returns <str> : transactions in string format
        """

        # d = ""
        # for txn in self.__transactions:
        #     d += f"--{txn['sender']}--{txn['receiver']}--{txn['txn_amount']}--{txn['txn_time']}--{txn['txn_hash']}"

        return json.dumps(self.__transactions)

    
    def transactions(self) -> list:
        """
        returns <list> : returns transactions in list format
        """

        return self.__transactions


    def add(self, transaction) -> None:
        """
        Add transaction to list

        args:
        transaction <dict> : transaction in dictionary format
        """
        self.__transactions.append(transaction)