
import requests
import time

from zb.crawlers.utils import get_header

# stations


class TicketQuery:
    """余票查询"""
    def __init__(self, from_station, to_station, date):
        self.api = "https://kyfw.12306.cn/otn/leftTicket/queryA?leftTicketDTO." \
                   "train_date={date}&leftTicketDTO.from_station={from_station}&" \
                   "leftTicketDTO.to_station={to_station}&purpose_codes=ADULT"
        self.url = self.api.format(date=date,
                                   from_station=from_station,
                                   to_station=to_station)
        self.raw = (date, from_station, to_station)

        self.response = None
        self.left_ticket = None

    def _get_response(self):
        response = requests.get(self.url, headers=get_header())
        if response.status_code != 200:
            raise requests.exceptions.RequestException
        else:
            self.response = response

    def _parser(self):
        data = self.response.json()['data']
        stations = data['map']
        result = data['result']

    def run(self):
        self._get_response()
        self._parser()

    def __repr__(self):
        return "< query ticket: %s - %s - %s >" % self.raw



