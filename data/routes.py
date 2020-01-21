import falcon
from .calls import calls

app=calls()

api=falcon.API()
api.add_route('/order',app)
api.add_route('/cancel/{id}',app)

