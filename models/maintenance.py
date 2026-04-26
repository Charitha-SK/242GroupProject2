from models.base_request import BaseRequest

class maintenance(BaseRequest):
    def __init__(self,sr_id,type,requester_name,location,urgency_lvl,estimated_cost,status,issue_type,days_open,):
        super().__init__(sr_id,'Maintenance',requester_name,location,urgency_lvl,estimated_cost,status)
        self.issue_type = issue_type
        self.days_open = days_open

    def to_str(self):
        return (f''
                f'│ ID : {self.sr_id: ^10} | Type : Maintenence | Requested By : {self.requester_name:^10} │'
                f'│ Location : {self.location: ^10} | Urgency Lvl : {self.urgency_lvl: ^10} | Estimated Cost : {self.estimated_cost: ^10}│'
                f'│ Status : {self.status: ^10} | Issue Type : {self.issue_type: ^10} | Days Open: {self.days_open: ^10}│'
                f'')
