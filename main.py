from api_tests.request_helper import Request


if __name__ == "__main__":

    users_request = Request(endpoint="/users")
    res = users_request.make_get_request()
    res_1 = users_request.make_get_request(by_id="1")

    post_data = {
        "firstname": "yaron",
        "lastname": "mordechai",
        "email":"yaronmord@gmail.com"

    }
    res_2 = users_request.make_post_request(data=post_data)
    