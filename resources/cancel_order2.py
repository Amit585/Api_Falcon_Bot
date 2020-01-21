
import json

class cancel_order2(object):

    def cancelOrderAsPerID(self,order_id):

        self.response = {}
        self.order_data={}
        self.order_status_flag = False
        self.order_tracking_flag=False
        self.cancellation_status=False

        with open('data/orderstatus.json', 'r') as order_status_reader:
            complete_data = order_status_reader.read()
            parsed_json = json.loads(complete_data)
            output_dict = [x for x in parsed_json if x['order_id'] == order_id and x['order_status'] !="cancelled"]
            if len(output_dict)==1:
                filtered_data=output_dict[0]
                data_index=parsed_json.index(filtered_data)
                parsed_json[data_index]['order_status']="cancelled"
                return json.dumps((parsed_json))
            else:
                return "ID Not Found"
