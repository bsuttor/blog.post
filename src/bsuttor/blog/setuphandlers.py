# -*- coding: utf-8 -*-
def testSetup(context):
    if context.readDataFile('bsuttor.blog.txt') is None:
        return
