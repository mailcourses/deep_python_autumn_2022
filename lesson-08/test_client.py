from unittest import mock

from aiohttp.test_utils import AioHTTPTestCase, TestServer, make_mocked_coro
from aiohttp import web

from client import fetch_url


class ClientTestCase(AioHTTPTestCase):

    async def get_application(self):
        """
        Override the get_app method to return your application.
        """
        async def hello(request):
            return web.Response(text='Hello, world')

        app = web.Application()
        app.router.add_get('/', hello)
        return app

    async def test_hello(self):
        async with self.client.request("GET", "/") as resp:
            self.assertEqual(resp.status, 200)
            text = await resp.text()
        self.assertIn("Hello, world", text)

    async def test_client_fetch(self):
        with mock.patch("client.aiohttp.ClientSession") as ms:
            sess = mock.MagicMock()
            ms.return_value.__aenter__.return_value = sess

            mget = mock.MagicMock()
            mget.return_value.__aenter__.return_value.status = 200
            mget.return_value.__aenter__.return_value.text = make_mocked_coro("12345")

            sess.get = mget

            resp_len = await fetch_url("any")

        self.assertEqual(resp_len, 5)

