from apps.helloword import HelloWorld
from apps.ETH import GetEthBalanceHandler, GetEthTradeHandler, GetEthHourBanlanceHandler

handlers=[
    (r'/hello_world', HelloWorld),
    (r'/eth/get_balance', GetEthBalanceHandler),
    (r'/eth/get_trade', GetEthTradeHandler),
    (r'/eth/get_hourbalance', GetEthHourBanlanceHandler)
]