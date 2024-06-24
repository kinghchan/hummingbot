import aiohttp
import asyncio

from hummingbot.core.web_assistant.connections.data_types import WSJSONRequest
from hummingbot.core.web_assistant.ws_assistant import WSAssistant, WSConnection
from hummingbot.core.web_assistant.connections.connections_factory import ConnectionsFactory


EXCHANGE_NAME = "dydx_perpetual"
API_VERSION = "v3"
DYDX_REST_URL = "https://api.dydx.exchange/{}".format(API_VERSION)
DYDX_WS_URL = "wss://api.dydx.exchange/{}/ws".format(API_VERSION)
MARKETS_URL = "/markets"
TICKER_URL = "/stats"
SNAPSHOT_URL = "/orderbook/"


async def callback(msg):
    print(msg)

async def websocket(session):
    async with session.ws_connect(DYDX_WS_URL) as ws:

        subscribe_orderbook_request = {
            "type": "subscribe",
            "channel": "v3_orderbook",
            "id": "BTC-USD",
        }
        await ws.send_json(subscribe_orderbook_request)

        async for msg in ws:
            if msg.type == aiohttp.WSMsgType.TEXT:
                await callback(msg.data)
            elif msg.type in (aiohttp.WSMsgType.CLOSED, aiohttp.WSMsgType.CLOSING, aiohttp.WSMsgType.CLOSE):
                print(f"Close!")
                break
            elif msg.type == aiohttp.WSMsgType.ERROR:
                break

async def run():
    session = aiohttp.ClientSession()
    await websocket(session)

    while True:
        pass


loop = asyncio.get_event_loop()
loop.run_until_complete(run())


loop.close()

# async def run():
#     factory = ConnectionsFactory()
#     conn = await factory.get_ws_connection()
#     print(conn)
#
# loop = asyncio.get_event_loop()
# loop.run_until_complete(run())
# loop.close()
#
# from hummingbot.core.web_assistant.ws_assistant import WSAssistant, WSConnection
# import websocket
# import json
#
# EXCHANGE_NAME = "dydx_perpetual"
# API_VERSION = "v3"
# DYDX_REST_URL = "https://api.dydx.exchange/{}".format(API_VERSION)
# DYDX_WS_URL = "wss://api.dydx.exchange/{}/ws".format(API_VERSION)
# MARKETS_URL = "/markets"
# TICKER_URL = "/stats"
# SNAPSHOT_URL = "/orderbook/"
#
#
# def on_message(ws, message):
#     print(message)
#
# def on_error(ws, error):
#     print(error)
#
# def on_close(*args):
#     print(args)
#     print("### closed ###")
#
# def on_open(ws):
#     print('opened')
#     params = {
#         'type': 'subscribe',
#         'channel': 'v3_orderbook',
#         'id': 'BTC-USD'
#     }
#     ws.send(json.dumps(params))
#
# ws = websocket.WebSocketApp(DYDX_WS_URL,
#                             on_message=on_message,
#                             on_error=on_error,
#                             on_close=on_close)
# ws.on_open = on_open
#
#
# ws.run_forever()