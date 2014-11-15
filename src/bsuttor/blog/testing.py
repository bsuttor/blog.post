# -*- coding: utf-8 -*-
from plone.testing import z2
from plone.app.testing import PloneWithPackageLayer
from plone.app.testing import IntegrationTesting
from plone.app.testing import FunctionalTesting

from plone.app.robotframework.testing import AUTOLOGIN_LIBRARY_FIXTURE

import bsuttor.blog


BSUTTOR_BLOG = PloneWithPackageLayer(
    zcml_package=bsuttor.blog,
    zcml_filename='testing.zcml',
    gs_profile_id='bsuttor.blog:testing',
    name='BSUTTOR_BLOG'
)

BSUTTOR_BLOG_INTEGRATION = IntegrationTesting(
    bases=(BSUTTOR_BLOG, ),
    name="BSUTTOR_BLOG_INTEGRATION"
)

BSUTTOR_BLOG_FUNCTIONAL = FunctionalTesting(
    bases=(BSUTTOR_BLOG, ),
    name="BSUTTOR_BLOG_FUNCTIONAL"
)

BSUTTOR_BLOG_ROBOT_TESTING = FunctionalTesting(
    bases=(BSUTTOR_BLOG, AUTOLOGIN_LIBRARY_FIXTURE, z2.ZSERVER_FIXTURE),
    name="BSUTTOR_BLOG_ROBOT_TESTING")


