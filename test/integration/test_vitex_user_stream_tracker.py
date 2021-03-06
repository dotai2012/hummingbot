#!/usr/bin/env python
import sys
import asyncio
import logging
import unittest
from os.path import join, realpath
from hummingbot.connector.exchange.vitex.vitex_user_stream_tracker import VitexUserStreamTracker
from hummingbot.core.utils.async_utils import safe_ensure_future

sys.path.insert(0, realpath(join(__file__, "../../../")))
logging.basicConfig(level=logging.DEBUG)


class UserStreamTrackerUnitTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.ev_loop: asyncio.BaseEventLoop = asyncio.get_event_loop()
        cls.user_stream_tracker: VitexUserStreamTracker = VitexUserStreamTracker()
        cls.user_stream_tracker_task: asyncio.Task = safe_ensure_future(cls.user_stream_tracker.start())

    def test_user_stream(self):
        # Wait process some msgs.
        self.ev_loop.run_until_complete(asyncio.sleep(120.0))
        print(self.user_stream_tracker.user_stream)


def main():
    unittest.main()


if __name__ == "__main__":
    main()
