
import json

class cancel_order(object):

    def cancelOrderAsPerID(self,order_id):

        self.response = {}
        self.order_data={}
        self.order_status_flag = False
        self.order_tracking_flag=False
        self.cancellation_status=False
        order_status_results = []
        order_tracking_results=[]

        #updating order status file
        with open('data/orderstatus.json', 'r') as order_status_reader:
            order_data = order_status_reader.read()
            parsed_json = json.loads(order_data)
            for data in parsed_json:
                if (order_id == data["order_id"]):
                    self.order_data=data
                    self.order_status_flag = True
                    if (data["order_status"] != "cancelled"):
                        data["order_status"] = "cancelled"
                        self.cancellation_status=True
                    else:
                        self.cancellation_status=False
                order_status_results.append(data)
            order_status_reader.close()
        with open('data/orderstatus.json', 'w') as order_status_writer:
            json.dump(order_status_results, order_status_writer, indent=4, sort_keys=False)
            order_status_writer.close()

        #updating order tracking file
        with open('data/ordertracking.json', 'r') as order_tracking_reader:
            order_data = order_tracking_reader.read()
            parsed_json = json.loads(order_data)
            for data in parsed_json:
                if (order_id == data["order_id"]):
                    self.order_tracking_flag = True
                    if(data["is_cancelled"]!="true"):
                        data["is_cancelled"]="true"
                order_tracking_results.append(data)
            order_tracking_reader.close()
        with open('data/ordertracking.json', 'w') as order_tracking_writer:
            json.dump(order_tracking_results,order_tracking_writer,indent=4,sort_keys=False)
            order_tracking_writer.close()

        #Returning response as per requirement
        if self.order_status_flag == True and self.order_tracking_flag == True:
            if self.cancellation_status==True:
                self.response["order_id"]=self.order_data["order_id"]
                self.response["name"]=self.order_data["name"]
                self.response["status"]="Order cancelled"
            else:
                self.response["order_id"] = self.order_data["order_id"]
                self.response["name"] = self.order_data["name"]
                self.response["status"] = "Order has already been cancelled"
        else:
            self.response["status"] = "order id not found."
        return json.dumps(self.response)