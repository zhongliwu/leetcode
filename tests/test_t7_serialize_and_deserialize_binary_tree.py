# -*- coding: utf-8 -*-

import pytest
from utils.Tree import (
    TreeNode, serialize, deserialize
)


class TestT7SerializeAndDeserializeBinaryTree:

    def test_serialize_official_sample(self):
        root = deserialize('{3,9,20,#,#,15,7}')
        assert root.val == 3

        tree_txt = serialize(root)
        assert tree_txt == '{3,9,20,#,#,15,7}'



