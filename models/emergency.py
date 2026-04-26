from models.base_request import BaseRequest

class emergency(BaseRequest):

    def __init__(self,sr_id,type,requester_name,location,urgency_lvl,estimated_cost,status,hazard_lvl,response_time):
        super().__init__(sr_id,'Emergency',requester_name,location,urgency_lvl,estimated_cost,status)
        self.hazard_lvl = hazard_lvl
        self.response_time = response_time

    def to_str(self):
        return (f''
                f'│ ID : {self.sr_id: ^10} | Type : Emergency | Requested By : {self.requester_name:^10} │'
                f'│ Location : {self.location: ^10} | Urgency Lvl : {self.urgency_lvl: ^10} | Estimated Cost : {self.estimated_cost: ^10}│'
                f'│ Status : {self.status: ^10} | Hazard Lvl : {self.hazard_lvl: ^10} | Response Time (mins): {self.response_time: ^10}│'
                f'')