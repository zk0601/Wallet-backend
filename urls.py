from apps.helloword import HelloWorld
from apps.ETH import GetEthBalanceHandler, GetEthHourTradeHandler, GetEthHourBanlanceHandler, GetEthTradeHandler

handlers=[
    (r'/hello_world', HelloWorld),
    (r'/eth/get_balance', GetEthBalanceHandler),
    (r'/eth/get_trade', GetEthTradeHandler),
    (r'/eth/get_hourtrade', GetEthHourTradeHandler),
    (r'/eth/get_hourbalance', GetEthHourBanlanceHandler)
]