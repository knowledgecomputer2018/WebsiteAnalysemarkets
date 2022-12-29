from cardano.wallet import WalletService
from cardano.backends.walletrest import WalletREST
from cardano.wallet import Wallet

#ws=WalletService(WalletREST(port=8090))
#wal=ws.create_wallet(name="test wallet", mnemonic="resist render west spin antique wild gossip thing syrup network risk gospel seek drop receive",passphrase="xxx",)
wallet='DdzFFzCqrhsqLwgodP95C9jZtViNsLVXFL7FgoTncRT8zGjW32hzWNK5PGWNSNZmQJGEdy8vNRcpAF9ZP6yQ4zbHbUNeaCrm6eqenKUE'

wal = Wallet(wallet, backend=WalletREST(port=8090))

print(wal)
