from mycoin.functions import hash_me

class Block:
    """
    This class will be used as block in blockchain.

    args:
    transactions <Transactions> : a list of transactions containing as fixed value in chain
    txn_time <float> : time of adding block
    prev_hash <str> : previous block hash
    """
    nonce = 0

    def __init__(self, transactions, txn_time) -> None:
        self.transactions = transactions
        self.txn_time = txn_time
        self.prev_hash = ""

    def calculate_hash(self) -> str:
        """
        returns <str> : hashed value of string(transactions, transaction time, previous hash, nonce)
        """
        return hash_me(f"{self.transactions.toString()} --- {self.txn_time} --- {self.prev_hash} --- {self.nonce}")


    def mine(self, diff, max_nonce):
        """
        Mine the block using passed information

        diff <int> : difficulty of leading zeros
        max_nonce <int> : maximum nonce limit
        """

        while not self.calculate_hash().startswith("0"*diff) and self.nonce < max_nonce:
            self.nonce += 1
