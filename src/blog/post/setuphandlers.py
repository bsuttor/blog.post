# -*- coding: utf-8 -*-
def testSetup(context):
    if context.readDataFile('blog.post.txt') is None:
        return
