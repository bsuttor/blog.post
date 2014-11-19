# -*- coding: utf-8 -*-
from Products.Five.browser import BrowserView
from plone.app.discussion.interfaces import IConversation


class BlogsView(BrowserView):
    """Blogs View class for collection or folder"""

    def get_articles(self):
        articles = []
        return articles

    def get_total_comments(self, context):
        try:
            conversation = IConversation(context)
            return conversation.total_comments
        except TypeError:
            return 0
