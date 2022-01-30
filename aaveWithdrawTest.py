from web3 import Web3
import web3
from web3.middleware import construct_sign_and_send_raw_middleware

#for readability
from termcolor import colored

w3 = Web3(Web3.WebsocketProvider('wss://kovan.infura.io/ws/v3/f5640519a5584ab3ac3fa0f8e2e336fc'))
account = w3.eth.account.from_key("0xa76e120651138799cd6fc2184fd34ed82ee53381a003e25d36822c980843da9b")
myPubKey = "0xb213cba22C5187637048f83594Fce3d8C7147B69"
w3.middleware_onion.add(construct_sign_and_send_raw_middleware(account))
w3.eth.default_account = account.address

ERC20ABI = [
    {
        "constant": True,
        "inputs": [],
        "name": "name",
        "outputs": [
            {
                "name": "",
                "type": "string"
            }
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": False,
        "inputs": [
            {
                "name": "_spender",
                "type": "address"
            },
            {
                "name": "_value",
                "type": "uint256"
            }
        ],
        "name": "approve",
        "outputs": [
            {
                "name": "",
                "type": "bool"
            }
        ],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [],
        "name": "totalSupply",
        "outputs": [
            {
                "name": "",
                "type": "uint256"
            }
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": False,
        "inputs": [
            {
                "name": "_from",
                "type": "address"
            },
            {
                "name": "_to",
                "type": "address"
            },
            {
                "name": "_value",
                "type": "uint256"
            }
        ],
        "name": "transferFrom",
        "outputs": [
            {
                "name": "",
                "type": "bool"
            }
        ],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [],
        "name": "decimals",
        "outputs": [
            {
                "name": "",
                "type": "uint8"
            }
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [
            {
                "name": "_owner",
                "type": "address"
            }
        ],
        "name": "balanceOf",
        "outputs": [
            {
                "name": "balance",
                "type": "uint256"
            }
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [],
        "name": "symbol",
        "outputs": [
            {
                "name": "",
                "type": "string"
            }
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": False,
        "inputs": [
            {
                "name": "_to",
                "type": "address"
            },
            {
                "name": "_value",
                "type": "uint256"
            }
        ],
        "name": "transfer",
        "outputs": [
            {
                "name": "",
                "type": "bool"
            }
        ],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [
            {
                "name": "_owner",
                "type": "address"
            },
            {
                "name": "_spender",
                "type": "address"
            }
        ],
        "name": "allowance",
        "outputs": [
            {
                "name": "",
                "type": "uint256"
            }
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "payable": True,
        "stateMutability": "payable",
        "type": "fallback"
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "name": "owner",
                "type": "address"
            },
            {
                "indexed": True,
                "name": "spender",
                "type": "address"
            },
            {
                "indexed": False,
                "name": "value",
                "type": "uint256"
            }
        ],
        "name": "Approval",
        "type": "event"
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "name": "from",
                "type": "address"
            },
            {
                "indexed": True,
                "name": "to",
                "type": "address"
            },
            {
                "indexed": False,
                "name": "value",
                "type": "uint256"
            }
        ],
        "name": "Transfer",
        "type": "event"
    }
]

### for ETH

#check ETH and aWETH bal before withdrawal
ETHDecimals = 18
aWETHDecimals = 18
print(colored("ETH balance before withdraw/burn: ", "red"), colored(w3.eth.get_balance(myPubKey) / (10 ** ETHDecimals), "magenta"))
aWETHContractAddress = "0x87b1f4cf9BD63f7BBD3eE1aD04E8F52540349347"

aWETHContract = w3.eth.contract(address = aWETHContractAddress, abi = ERC20ABI)
rawaWETHBal = aWETHContract.functions.balanceOf(myPubKey).call()
aWETHBal = rawaWETHBal / (10 ** aWETHDecimals)
print(colored("aWETH balance before withdraw/burn: ", "red"), colored(aWETHBal, "blue"))

#approve allowance of aWETH
WETHGatewayContractABI = [{"inputs":[{"internalType":"address","name":"weth","type":"address"}],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"previousOwner","type":"address"},{"indexed":True,"internalType":"address","name":"newOwner","type":"address"}],"name":"OwnershipTransferred","type":"event"},{"stateMutability":"payable","type":"fallback"},{"inputs":[{"internalType":"address","name":"lendingPool","type":"address"}],"name":"authorizeLendingPool","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"lendingPool","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"},{"internalType":"uint256","name":"interesRateMode","type":"uint256"},{"internalType":"uint16","name":"referralCode","type":"uint16"}],"name":"borrowETH","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"lendingPool","type":"address"},{"internalType":"address","name":"onBehalfOf","type":"address"},{"internalType":"uint16","name":"referralCode","type":"uint16"}],"name":"depositETH","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"emergencyEtherTransfer","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"token","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"emergencyTokenTransfer","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"getWETHAddress","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"renounceOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"lendingPool","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"},{"internalType":"uint256","name":"rateMode","type":"uint256"},{"internalType":"address","name":"onBehalfOf","type":"address"}],"name":"repayETH","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"address","name":"newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"lendingPool","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"},{"internalType":"address","name":"to","type":"address"}],"name":"withdrawETH","outputs":[],"stateMutability":"nonpayable","type":"function"},{"stateMutability":"payable","type":"receive"}]
WETHGatewayAddress = "0xA61ca04DF33B72b235a8A28CfB535bb7A5271B70"
WETHGatewayContract = w3.eth.contract(address = WETHGatewayAddress, abi = WETHGatewayContractABI)
desiredaWETHWithdrawal = 0.01
aWETHAllowance = aWETHContract.functions.approve(WETHGatewayAddress, int(desiredaWETHWithdrawal * (10 ** aWETHDecimals))).transact({"from": myPubKey})
print(colored("Approving aWETH for burning...", "yellow"))
w3.eth.wait_for_transaction_receipt(w3.toHex(aWETHAllowance), timeout = 60, poll_latency = 5)

#withdraw
withdraw = WETHGatewayContract.functions.withdrawETH("0xE0fBa4Fc209b4948668006B2bE61711b7f465bAe", int(desiredaWETHWithdrawal * (10 ** aWETHDecimals)), myPubKey).transact({"from": myPubKey, "gas": 10000000, "gasPrice": w3.eth.gas_price}) #gasPrice is waiting time, gas is the upper limit
print(colored("Burning aWETH...", "yellow"))
w3.eth.wait_for_transaction_receipt(w3.toHex(withdraw), timeout = 60, poll_latency = 5)

#check ETH and aWETH bal after burning
print(colored("ETH balance after withdraw/burn: ", "green"), colored(w3.eth.get_balance(myPubKey) / (10 ** ETHDecimals), "magenta"))
rawaWETHBal = aWETHContract.functions.balanceOf(myPubKey).call()
aWETHBal = rawaWETHBal / (10 ** aWETHDecimals)
print(colored("aWETH balance after withdraw/burn: ", "green"), colored(aWETHBal, "blue"))