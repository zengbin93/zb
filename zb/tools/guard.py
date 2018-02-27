# -*- coding:utf-8 -*-
import os
import time
import requests
from retrying import retry
import click

@retry(stop_max_attempt_number=6)
def push_sms(title, content, key='SCU10748T12f471f07094648d297222fc649e374d598bf38bc81fd'):
    """使用server酱推送消息到微信"""
    # post方法推送
    url = 'https://sc.ftqq.com/%s.send' % key
    requests.post(url, data={'text': title, 'desp': content})


class Guard:
    alive = "I am still running"
    dead = "I got an Exception, please save me"
    stop = "I stopped myself, leave me alone"
    file = "state.txt"

    def write_state(self, state):
        with open(self.file, 'w', encoding='utf8') as f:
            if state == "alive":
                f.write(self.alive)
            elif state == "dead":
                f.write(self.dead)
            elif state == "stop":
                f.write(self.stop)

    def response_state(self, response_cmd):
        if not os.path.exists(self.file):
            print("执行cmd：%s" % response_cmd)
            os.system(response_cmd)
            time.sleep(100)
            return "first run"
        with open(self.file, 'r', encoding='utf8') as f:
            state = f.readline()
            if state == self.dead:
                push_sms(title="程序死掉了", content=state)
                os.system(response_cmd)
                push_sms(title="程序复活", content="执行命令：%s" % response_cmd)
            # elif state == self.alive:
            #     print(state)
            elif state == self.stop:
                push_sms(title="程序关机提醒", content=state)
        return state



@click.command()
@click.option('--cmd', help="程序死掉之后的响应命令")
@click.option('--sleep', default=10, help="休眠时间")
def guard(cmd, sleep):
    guard = Guard()
    while True:
        state = guard.response_state(response_cmd=cmd)
        if state == guard.stop:
            break
        time.sleep(sleep)


if __name__ == "__main__":
    guard()
