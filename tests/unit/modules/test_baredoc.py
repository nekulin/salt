# -*- coding: utf-8 -*-

# Import Python libs
from __future__ import absolute_import

# Import module
import salt.modules.baredoc as baredoc

# Import Salt Testing Libs
from tests.support.unit import TestCase


class BaredocTest(TestCase):
    """
    Validate baredoc module
    """

    def test_baredoc_list_states(self):
        """
        Test baredoc state module listing
        """
        ret = baredoc.list_states(names_only=True)
        assert "value_present" in ret["xml"][0]

    def test_baredoc_list_states_args(self):
        """
        Test baredoc state listing with args
        """
        ret = baredoc.list_states()
        assert "value_present" in ret["xml"][0]
        assert "xpath" in ret["xml"][0]["value_present"]

    def test_baredoc_list_states_single(self):
        """
        Test baredoc state listing single state module
        """
        ret = baredoc.list_states("xml")
        assert "value_present" in ret["xml"][0]
        assert "xpath" in ret["xml"][0]["value_present"]

    def test_baredoc_list_modules(self):
        """
        test baredoc executiion module listing
        """
        ret = baredoc.list_modules(names_only=True)
        assert "get_value" in ret["xml"][0]

    def test_baredoc_list_modules_args(self):
        """
        test baredoc execution module listing with args
        """
        ret = baredoc.list_modules()
        assert "get_value" in ret["xml"][0]
        assert "file" in ret["xml"][0]["get_value"]

    def test_baredoc_list_modules_single(self):
        """
        test baredoc single module listing
        """
        ret = baredoc.list_modules("xml")
        assert "get_value" in ret["xml"][0]
        assert "file" in ret["xml"][0]["get_value"]
