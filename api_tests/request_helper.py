import requests
from config.config import BASE_URL, HEADERS
from helper.logger import logger

class Request():

    def __init__(self,endpoint:str):
        self.endpoint = endpoint

    def make_get_request(self,by_id="", **kwargs):
        if by_id:
            by_id = f"?id={by_id}"
        url = f"{BASE_URL}{self.endpoint}{by_id}"
        
        try:
            response = requests.get(url=url,headers=HEADERS,**kwargs)
            
            response.raise_for_status()
            logger.info(f"Success making 'GET' request for:'{url}', response status:'{response.status_code}'",extra=kwargs)
            return response
        except requests.exceptions.RequestException as e:
            logger.error(f"Failed making 'GET' request for:'{url}', response status:'{response.status_code}', exception:{e}",extra=kwargs)
            return None

    def make_post_request(self,data, **kwargs):
        url = f"{BASE_URL}{self.endpoint}"
        try:
            response=requests.post(url=url,data=data,**kwargs)
            response.raise_for_status()
            logger.info(f"Success making 'POST' request for:'{url}' with data:{data}, response status:'{response.status_code}'",extra=kwargs)
            return response
        except requests.exceptions.RequestException as e:
            logger.error(f"Failed making 'POST' request for:'{url}', response status:'{response.status_code}', exception:{e}",extra=kwargs)
            return None
    
