from p2pool.bitcoin import networks

PARENT = networks.nets['myriad_scrypt']
SHARE_PERIOD = 15 # seconds
CHAIN_LENGTH = 24*60*60//10 # shares
REAL_CHAIN_LENGTH = 24*60*60//10 # shares
TARGET_LOOKBEHIND = 200 # shares
SPREAD = 60 # blocks
IDENTIFIER = '27392307bca64c44'.decode('hex')
PREFIX = '27392307bca64c44'.decode('hex')
P2P_PORT = 5555
MIN_TARGET = 0
MAX_TARGET = 2**256//2**20 - 1
PERSIST = True
WORKER_PORT = 5556
BOOTSTRAP_ADDRS = 'birdspool.no-ip.org nz.p2pool.geek.nz uk.p2pool.geek.nz'.split(' ')
VERSION_CHECK = lambda v: True
