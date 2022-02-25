from mycoin.block import Block
from mycoin.functions import hash_me
from mycoin.transactions import Transactions
import time
import random
import string

class Blockchain:
    """
    This class is used to add transactions, keeping blocks, verifies the chain, 
    """

    # chain of verified blocks
    _chain = []
    # chain of unverified blocks
    _unverified_chain = []

    # in unverified chain transaction will be stored as {id:id, diff:diff, block:block}

    # transactions
    _txns = Transactions()

    # maximum transactions to be added
    MAX_TRANSACTIONS = 5

    # used to keep transaction in line format.
    _transaction_lock = False

    # chain lock
    _chain_lock = False

    # difficulty level
    _difficulty = 4
    _max_diff = 10
    _min_diff = 2


    # maximum nonce to limited
    MAX_NONCE = 0XFFFFFFFF

    # difficulty time is used to measure if last block and new block between time is greater than DIFFICULTY_TIME
    # then difficulty is reduce(decreased)
    # and if less than this then difficulty will be increased.
    # default 30 seconds
    DIFFICULTY_TIME = 30


    def __init__(self) -> None:
        """
        """


    def _adjust_difficulty(self):
        """
        Adjust difficulty
        """
        if len(self._chain) > 1:
            last = self._chain[-2]
            new = self._chain[-1]
            if (new.txn_time-last.txn_time) > self.DIFFICULTY_TIME:
                self._difficulty -= 1

                if self._difficulty < self._min_diff:
                    self._difficulty = self._min_diff
            else:
                self._difficulty += 1

                if self._difficulty > self._max_diff:
                    self._difficulty = self._max_diff



    def add_block(self, transactions):
        """
        Add block to the chain(unverified)

        args:
        transactions <Transactions> : all transactions[class]
        """
        
        self._unverified_chain.append(
            {
                "id":"".join([str(random.choice(string.ascii_letters)) for _ in range(15)]),
                "diff" : self._difficulty,
                "block" : Block(transactions, time.time())
            }
        )
        self._unverified_chain[0]["block"].prev_hash = self.last_block_hash

    

    def add_verified_block(self, object) -> bool:
        """
        Add verified block to the main chain

        args:
        object <dict> : block data object as received from mineblock : {id,diff,block}

        returns <bool> : True means block is added to the chain , False means it is not added to the chain 
        
        False reasons:
            *object is not in chain,
            *hash is not equal to leading zeros as passed difficulty,
            *wrong hash
        """

        if object not in self._unverified_chain:
            return False

        id = object["id"]
        diff = object["diff"]
        block = object["block"]

        hash = block.calculate_hash()

        if(block.calculate_hash() != hash or not hash.startswith("0"*diff)):
            return False

        self._chain.append(block)

        self._adjust_difficulty()

        self._unverified_chain.remove(object)

        if len(self._unverified_chain) > 0:
            self._unverified_chain[0]["block"].prev_hash = self.last_block_hash

        return True




    def genesis_block(self, address, amount) -> None:
        """
        Create a genesis block in chain

        args:
        address <str> : address to store all coins
        amount <float> : total amount to be added
        """

        # local transactions
        local_txns = Transactions()

        # new transaction
        txn = {
            "sender" : "GENESIS_BLOCK",
            "receiver" : address,
            "txn_amount" : amount,
            "txn_time" : time.time()
        }

        # adding to the all transactions
        local_txns.add(txn)

        b = Block(local_txns, time.time())
        b.prev_hash = ""
        b.mine(self._difficulty,self.MAX_NONCE)

        self._chain.append(b)


    
    def add_transaction(self,sender, receiver, txn_amount, txn_time) -> None:
        """
        add transaction

        args:
        sender <str> : sender address
        receiver <str> : receiver address
        txn_amount <float> : transaction amount
        txn_time <float> : transaction time

        """

        # wait while lock is acquired
        while self._transaction_lock:
            pass

        self._transaction_lock = True

        # adding transaction to list
        self._txns.add({
            "sender" : sender,
            "receiver" : receiver,
            "txn_amount" : txn_amount,
            "txn_time" : txn_time,
            "txn_hash" : hash_me(f"{sender}--{receiver}--{txn_amount}--{txn_time}")
        })

        # checking for maximum transactions
        if(len(self._txns.transactions()) == self.MAX_TRANSACTIONS):
            # adding to block
            self.add_block(self._txns)

            # empty transactions
            self._txns = Transactions()

        self._transaction_lock = False



    def block_to_mine(self) -> dict:
        """
        get block to mine

        returns <dict> : containing is block available and if available then block
        """

        # exception occured/list change(if) then status will be false
        # else block id and block data will be returned
        try:
            if len(self._unverified_chain) > 0:
                return {
                    "status" : True,
                    "block" : self._unverified_chain[0]
                }
        except IndexError:
            return {
                "status" : False,
            }
            


    @property
    def last_block_hash(self):
        """
        returns last block
        """
        return self._chain[-1].calculate_hash()


    
    def verify_chain(self):
        i = 0
        while i < len(self._chain)-1:
            if self._chain[i].txn_time > self._chain[i+1].txn_time:
                return False
            elif self._chain[i].calculate_hash() != self._chain[i+1].prev_hash:
                return False
            
            i += 1

        return True
