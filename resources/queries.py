

class queries:

    def fetch_query(self):
        query="select * from new_schema.order;"
        return query

    def insert_query(self,order_id,order_status):
        order_id=str(order_id)
        query="INSERT INTO new_schema.order (order_id,order_status) values ("+order_id+",'"+order_status+"');"
        return query

    def update_query(self,old_order_id,new_order_id,new_order_status):
        old_order_id=str(old_order_id)
        new_order_id=str(new_order_id)
        query="UPDATE new_schema.order set order_id="+new_order_id+",order_status='"+new_order_status+"' where order_id="+old_order_id+";"
        return query

    def delete_query(self,order_id):
        order_id=str(order_id)
        query="DELETE from new_schema.order where order_id="+order_id+";"
        return query