


#abstract parent class for request objects
from abc import *
class BaseRequest(ABC):
    @abstractmethod
    def __init__(self,sr_id,type,requester_name,location,urgency_lvl,estimated_cost,status):
        """defines minimum reqs for a Request OBJ"""
        self.sr_id = sr_id
        self.type = type
        self.requester_name = requester_name
        self.location = location
        self.urgency_lvl = urgency_lvl
        self.estimated_cost = estimated_cost
        self.status = status

    #here for all child class incse of debugging or menu build method idk
    def get_status(self):
        return f'current status : {self.status}'

    @abstractmethod
    def to_str(self):
        return ''

    #each one uses this as is to update status so just call this
    def status_change(self,new_status:str):
        self.status = new_status