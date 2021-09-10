# -----------------------------------------------------------------------------
# Copyright (c) 2014--, The Qiita Development Team.
#
# Distributed under the terms of the BSD 3-clause License.
#
# The full license is in the file LICENSE, distributed with this software.
# -----------------------------------------------------------------------------

from unittest import main

from mock import Mock

from qiita_db.user import User
from qiita_pet.handlers.base_handlers import BaseHandler
from qiita_pet.test.tornado_test_base import TestHandlerBase
from qiita_pet.handlers.admin_processing_job import (
    AdminProcessingJob, AJAXAdminProcessingJobListing)


class TestAdminProcessingJob(TestHandlerBase):
    def test_get(self):
        BaseHandler.get_current_user = Mock(return_value=User("admin@foo.bar"))

        response = self.get('/admin/processing_jobs/')
        self.assertEqual(response.code, 200)
        self.assertIn("Available Commands", response.body.decode('ascii'))

class TestAJAXAdminProcessingJobListing(TestHandlerBase):
    def test_get(self):
        self.fail()

if __name__ == "__main__":
    main()
