import falcon
import json
from resources.cancel_order2 import cancel_order2

class calls(object):

    def on_get(self,req,resp):
        with open('data/orderstatus.json','r') as f:
            resp.body=f.read()
            resp.status=falcon.HTTP_200

    def on_put(self,req,resp,id):
        # data = req.stream.read()
        response=cancel_order2.cancelOrderAsPerID(self,id)
        if response:
            resp.body=response
            resp.status=falcon.HTTP_200
        else:
            resp.status=falcon.HTTP_404





