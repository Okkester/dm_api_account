from requests import Response
from restclient.restclient import Restclient
from dm_api_account.utilities import validate_request_json, validate_status_code
import allure
from dm_api_account.models import *


class LoginApi:
    def __init__(self, host, headers=None):
        self.host = host
        self.client = Restclient(host=host, headers=headers)
        if headers:
            self.client.session.headers.update(headers)

    def post_v1_account_login(self, json: LoginCredentials, status_code: int = 200) -> Response:
        """
        Authenticate via credentials
        :param status_code:
        :param json: login_credentials_model
        :return:
        """
        with allure.step("Авторизация пользователя"):
            response = self.client.post(
                path=f"/v1/account/login",
                json=validate_request_json(json)
            )
        validate_status_code(response, status_code)
        if response.status_code == 200:
            UserEnvelope(**response.json())
        return response

    # def post_v1_account_login(
    #         self,
    #         json: LoginCredentials,
    #         status_code: int = 200,
    #         **kwargs
    # ) -> Response | UserEnvelope:
    #     """
    #     Authenticate via credentials
    #     :param status_code:
    #     :param json: login_credentials_model
    #     :return:
    #     """
    #
    #     response = self.client.post(
    #         path=f"/v1/account/login",
    #         json=validate_request_json(json),
    #         **kwargs
    #     )
    #     validate_status_code(response, status_code)
    #     # if response.status_code == 200:   # убрал по комментарию к домашке "проверки"
    #     #     return UserEnvelope(**response.json())
    #     return response

    def delete_v1_account_login(
            self,
            status_code: int = 204,
            **kwargs
    ) -> Response:
        """
        Logout as current user
        :return:
        """
        with allure.step("Логаут пользователя"):
            response = self.client.delete(
                path=f"/v1/account/login",
                **kwargs
            )
        validate_status_code(response, status_code)
        return response

    def delete_v1_account_login_all(
            self,
            status_code: int = 204,
            **kwargs
    ) -> Response:
        """
        Logout from every device
        :return:
        """
        with allure.step("Логаут пользователя на всех устройствах"):
            response = self.client.delete(
                path=f"/v1/account/login/all",
                **kwargs
            )
        validate_status_code(response, status_code)
        return response
