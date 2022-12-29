from tronpy import Tron
from tronpy.keys import PrivateKey
# connect to the Tron blockchain
client = Tron()

def create_wallet():
       wallet=client.generate_address()
       print("my wallet is :%s" % wallet)
       print("Wallet address:%s" %wallet['base58check_address'])
       print("Private Key:  %s" % wallet['private_key'])
'''
my wallet is :
{'base58check_address': 'TQ6rVJ8XXbwpb7QAbVHWk1aLhMC4SzWZZd',
'hex_address': '419b03f7140fdea186a03e6794191b7f37d423dcff',
'private_key': '2ff492029acc463b108a02514d33cae931863df6da519908e9f4dbd692d1e6ab',
'public_key': '4b1fe24b0a49bdfd6d75ab8cb37f2bfb1702b5b3a9290116b21ab9973c866ed8b4483d5f25fd03ee8ffebf0d850c7694c916cc4f8b6c13f5b3073930fe6aff7c'}
'''


def is_valid(address):
    is_address = client.is_address(str(address))
    return is_address
WALLET_ADDRESS='TQ6rVJ8XXbwpb7QAbVHWk1aLhMC4SzWZZd'
PRIVATE_KEY='2ff492029acc463b108a02514d33cae931863df6da519908e9f4dbd692d1e6ab'
def send_tron(wallet,amount):
     try:
             priv_key=PrivateKey(bytes.fromhex(PRIVATE_KEY))

             txn=(client.trx.transfer(WALLET_ADDRESS,str(wallet),int(amount))
             .memo('Transaction Description')
             .build()
             .inspect()
             .sign(priv_key)
             .brodcast()
              )
             return txn.wait()
     except Exception as ex:
             return ex
def account_balance(address):
    balance = client.get_account_balance(str(address))
    return balance
create_wallet()
#print(is_valid('TQ6rVJ8XXbwpb7QAbVHWk1aLhMC4SzWZZd'))
#wallet=' TRfffNywtDL6wEamxg8V46LJfyR8Fvy7nu'
amount=5000000
transaction =send_tron(wallet,amount)
#print(transaction)
#print(account_balance(WALLET_ADDRESS))
#print(account_balance(wallet))
#account = 'TMoJMiQQgzneoGimdJjZtxcPiHJjamqRzK'
#wallet2='TPhBQKbg3WqZnxCeiDw9ZtsaYutkvHqeWS'
#print(account_balance(wallet2))
#wallet3='TRfffNywtDL6wEamxg8V46LJfyR8Fvy7nu'
#print(account_balance(wallet3))
