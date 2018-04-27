from TencentXiangQing.settings import USER_AGENT_LIST
import random


class UserAgentMiddleware(object):

    def process_request(self,request,spider):

        user_agent = random.choice(USER_AGENT_LIST)

        request.headers['User-Agent'] = user_agent


class ProxyMiddleware(object):
    def process_request(self, request, spider):
        """
        # 免费透明代理：
        proxy = "114.67.224.167:16819"
        request.meta['proxy'] = "http://" + proxy
        """
        # 验证代理使用：
        proxy = "maozhaojun:ntkn0npx@114.67.224.167:16819"
        request.meta['proxy'] =  proxy
