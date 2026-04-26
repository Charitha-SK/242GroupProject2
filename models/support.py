from models.base_request import BaseRequest

class support(BaseRequest):

    def __init__(self,sr_id,type,requester_name,location,urgency_lvl,estimated_cost,status,attendees,event_date='########'):
        super().__init__(sr_id,'Support',requester_name,location,urgency_lvl,estimated_cost,status)
        self.attendees = attendees
        self.event_date = event_date


    def to_str(self):
        return (f''
                f'│ ID : {self.sr_id: ^10} | Type : Support | Requested By : {self.requester_name:^10} │'
                f'│ Location : {self.location: ^10} | Urgency Lvl : {self.urgency_lvl: ^10} | Estimated Cost : {self.estimated_cost: ^10}│'
                f'│ Status : {self.status: ^10} | Attendees : {self.attendees: ^10} | Event Date: {self.event_date: ^10}│'
                f'')
