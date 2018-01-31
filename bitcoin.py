THE_BLOCKCHAIN = [
    {
        'sender': 'alice',
        'sender_signature': 'alicesig',
        'receiver': 'bob',
        'amount': 2.50,
        'hash_previous': 53673637,
        'next_transaction': pointer,
    }
    ...
]

{}


NUM_TX_IN_BLOCK = 21

def mine():
    block = []
    while len(block) < NUM_TX_IN_BLOCK:
        tx = get_a_transaction_from_the_internet()
        # validate tx
        if tx.amount <= get_person_balance(tx.sender, THE_BLOCKCHAIN + block):
            block.append(tx)

    # Now we have a block
    # Perform proof of work for block
    nonce = random_integer_between(0, nonce_max)
    while num_leading_zeros(sha256(serialize(block + nonce))) < 30:
        nonce = random_integer_between(0, nonce_max)

    broadcast(serialize(block + nonce))


def get_person_balance(person, blockchain):
    balance = 0.0
    for historical_tx in blockchain:  # Iterating through 25 Gb of the whole blockchain
        if historical_tx.sender == person:  # really, use signature to
            balance += historical_tx.amount  # might be positive (received) or negative (spent)
    return balance
