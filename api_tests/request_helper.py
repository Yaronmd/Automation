import requests
from config.config import BASE_URL, HEADERS
from helper.logger import logger

class Request():

    def __init__(self,endpoint:str):
        self.endpoint = endpoint

    def make_get_request(self, by_id=None, **params):
        """
        Makes a GET request to the specified endpoint.

        :param by_id: Optional ID to append as a query parameter (?id=<value>).
        :param params: Additional query parameters as key-value pairs.
        :return: Response object if the request is successful, None otherwise.
        """
        query_params = params.copy()
        if by_id:
            query_params["id"] = by_id

        url = f"{BASE_URL}{self.endpoint}"
        
        try:
            response = requests.get(url=url, headers=HEADERS, params=query_params)
            
            response.raise_for_status()
            logger.info(
                f"Success making 'GET' request for:'{url}' with params:{query_params}, "
                f"response status:'{response.status_code}'",
                extra={"url": url, "params": query_params, "status_code": response.status_code}
            )
            return response
        except requests.exceptions.RequestException as e:
            logger.error(
                f"Failed making 'GET' request for:'{url}' with params:{query_params}, "
                f"exception:{e}",
                extra={"url": url, "params": query_params, "exception": str(e)}
            )
            return None

    def make_post_request(self,data, **kwargs):
        """
        Sends a POST request to the specified endpoint.

        Args:
            data (dict or str): The payload to send in the POST request.
            **kwargs: Additional arguments to pass to the `requests.post` method.

        Returns:
            requests.Response: The response object from the POST request if successful.
            None: If the request fails.

        Logs:
            - Logs success with URL, data, and response status if the request is successful.
            - Logs error with URL, response status, and exception details if the request fails.
        """
        url = f"{BASE_URL}{self.endpoint}"
        try:
            response=requests.post(url=url,data=data,**kwargs)
            response.raise_for_status()
            logger.info(f"Success making 'POST' request for:'{url}' with data:{data}, response status:'{response.status_code}'",extra=kwargs)
            return response
        except requests.exceptions.RequestException as e:
            logger.error(f"Failed making 'POST' request for:'{url}', response status:'{response.status_code}', exception:{e}",extra=kwargs)
            return None
        
    def make_delete_request(self, identifier=None, **kwargs):
        """
        Sends a DELETE request to the specified endpoint or a specific resource.

        Args:
            identifier (str or int, optional): The identifier of the resource to delete. 
                Appended to the endpoint URL if provided.
            **kwargs: Additional arguments to pass to the `requests.delete` method.

        Returns:
            requests.Response: The response object from the DELETE request if successful.
            None: If the request fails.

        Logs:
            - Logs success with URL and response status if the request is successful.
            - Logs error with URL and exception details if the request fails.
        """
        url = f"{BASE_URL}{self.endpoint}"
        if identifier:
            url = f"{url}/{identifier}"
        try:
            response = requests.delete(url=url, **kwargs)
            response.raise_for_status()
            logger.info(
                f"Success making 'DELETE' request for:'{url}', response status:'{response.status_code}'",
                extra=kwargs,
            )
            return response
        except requests.exceptions.RequestException as e:
            logger.error(
                f"Failed making 'DELETE' request for:'{url}', exception:{e}",
                extra=kwargs,
            )
            return None
