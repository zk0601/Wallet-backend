from .base import BaseHandler
from tornado.concurrent import run_on_executor
from models.ETH_model import EthBalance, EthTrade
import datetime


class GetEthBalanceHandler(BaseHandler):
    @run_on_executor
    def post(self):
        try:
            data = dict()
            date = self.get_argument("date", None)
            platform = self.get_argument("platform", 'ALL')
            if not date:
                return self.response(code=1, msg='No time')

            time_format = "%Y%m%d"
            today = datetime.datetime.strptime(date, time_format)
            tomorrow = today + datetime.timedelta(days=1)
            plat_list = ['Okex', 'huobi', '币安', 'Bitfinex', 'UpBit', 'P网', 'GATE']
            if not platform in platform and not platform == 'ALL':
                return self.response(code=1, msg='Platform error')
            if not platform == 'ALL':
                balance = self.session.query(EthBalance).filter(EthBalance.platform == platform,
                                                                EthBalance.time.between(today, tomorrow)).order_by(EthBalance.id.asc()).all()
                tmp = [0 for _ in range(24)]
                for index, item in enumerate(balance):
                    tmp[index] = str(item.balance)
                data.setdefault(platform, tmp)
            else:
                for plat in plat_list:
                    balance = self.session.query(EthBalance).filter(EthBalance.platform == plat,
                                                                    EthBalance.time.between(today, tomorrow)).order_by(EthBalance.id.asc()).all()
                    tmp = [0 for _ in range(24)]
                    for index, item in enumerate(balance):
                        tmp[index] = str(item.balance)
                    data.setdefault(plat, tmp)

            return self.response(code=0, msg='success', data=data)

        except Exception as e:
            return self.response(code=1, msg='ERROR')
        finally:
            self.session.remove()


class GetEthTradeHandler(BaseHandler):
    @run_on_executor
    def post(self):
        try:
            time = self.get_argument("time", None)
            platform = self.get_argument("platform", None)
            value_level = self.get_argument("value_level", None)
            if not time or not platform:
                return self.response(code=1, msg='arg error')
            time_format = "%Y%m%d %H"
            current_hour = datetime.datetime.strptime(time, time_format)
            next_hour = current_hour + datetime.timedelta(hours=1)
            if not value_level:
                trade = self.session.query(EthTrade).filter(EthTrade.platform == platform,
                                                            EthTrade.trade_time.between(current_hour, next_hour)).order_by(EthTrade.id.asc()).all()
            else:
                trade = self.session.query(EthTrade).filter(EthTrade.platform == platform, EthTrade.value > value_level,
                                                            EthTrade.trade_time.between(current_hour,next_hour)).order_by(EthTrade.id.asc()).all()

            datetime_format = "%Y%m%d %H:%M:%S"
            data = list()
            for item in trade:
                tmp = dict()
                tmp['platform_address'] = item.platform_address
                tmp['trade_time'] = item.trade_time.strftime(datetime_format)
                tmp['from_address'] = item.from_address
                tmp['to_address'] = item.to_address
                tmp['value'] = str(item.value)
                data.append(tmp)

            return self.response(code=0, msg='success', data=data)

        except Exception as e:
            return self.response(code=1, msg='ERROR')
        finally:
            self.session.remove()


class GetEthHourBanlanceHandler(BaseHandler):
    @run_on_executor
    def post(self):
        try:
            data = dict()
            date_str = self.get_argument("date", None)
            platform = self.get_argument("platform", 'ALL')

            if not date_str:
                return self.response(code=1, msg='arg error')

            date_format = "%Y%m%d %H"
            now = datetime.datetime.strptime(date_str, date_format)
            next_hour = now + datetime.timedelta(hours=1)
            if not platform == 'ALL':
                balance = self.session.query(EthBalance).filter(EthBalance.platform == platform,
                                                                EthBalance.time.between(now, next_hour)).order_by(EthBalance.id.asc()).first()
                data.setdefault(platform, str(balance.balance))
            else:
                balance = self.session.query(EthBalance).filter(EthBalance.time.between(now, next_hour)).order_by(EthBalance.id.asc()).all()
                for item in balance:
                    data.setdefault(item.platform, str(item.balance))
            return self.response(code=0, msg='success', data=data)

        except Exception as e:
            return self.response(code=1, msg='ERROR')
        finally:
            self.session.remove()