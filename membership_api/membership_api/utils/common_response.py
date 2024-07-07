"""
@Author: star320129
@Email: star_320129@sina.com
@FileName: common_response.py
@DoteTime: 2024/7/7 21:46
"""

from rest_framework.response import Response


class CommonResponse(Response):
    """
    覆盖全局Response
    """
    def __init__(self, status=200, message=None, **kwargs):

        self.status = status
        self.message = message

        data = {
            'status': self.status,
            'message': self.message,
        }

        data.update(kwargs)

        super(CommonResponse, self).__init__(data)
