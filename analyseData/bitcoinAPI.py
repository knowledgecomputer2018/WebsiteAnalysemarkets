from bitcoin import *
my_private_key = random_key()
print(my_private_key)
my_public_key=privtopub(my_private_key)
print(my_public_key)
my_bitcoin_address=pubtoaddr(my_public_key)
print(my_bitcoin_address)

my_private_key1 = random_key()
print('Private Key 1:' + my_private_key1)
my_public_key1 = privtopub(my_private_key1)
print('Public Key 1: ' + my_public_key1)

my_private_key2 = random_key()
print('Private Key 2:' + my_private_key2)
my_public_key2 = privtopub(my_private_key2)
print('Public Key 2:' + my_public_key2)


my_private_key3 = random_key()
print('Private Key 3:' + my_private_key3)
my_public_key3 = privtopub(my_private_key3)
print('Public Key 3: ' + my_public_key3)


my_multi_sig = mk_multisig_script(my_private_key1, my_private_key2, my_private_key3, 2,3)
my_multi_address = scriptaddr(my_multi_sig)

print('Multi-Address: ' + my_multi_address)


