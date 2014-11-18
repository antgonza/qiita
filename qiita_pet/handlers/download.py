from tornado.web import authenticated

from qiita_db.data import PreprocessedData
from qiita_db.study import Study
from qiita_db.user import User
from qiita_db.util import get_filepath_from_id

from .base_handlers import BaseHandler
from .study_handlers import check_access

class DownloadHanderCheck(BaseHandler):
    @authenticated
    def get(self, preprocessed_data_id):
        preprocessed_data = PreprocessedData(preprocessed_data_id)
        user = User(self.current_user)
        study = Study(preprocessed_data.study)
        check_access(user, study)

        file_id = [f[1] for f in preprocessed_data.get_filepaths_with_info()
                   if f[2]=='preprocessed_fastq'][0]

#         self.redirect('/download_protected/%s' % file_id)
#
#
#         try:
#             filepath = get_filepath_from_id(file_id)
#         except:
#             print 'You can download that file'
#             self.finish()
#
#
        filepath = file_id[len("/Users/antoniog/Desktop/CurrentWork/largeFiles/qiita/base_dir/"):]
        filepath = '/download_protected/' + filepath
        print filepath, '------'


        self.set_header('X-Accel-Redirect', filepath)
        self.finish()


class DownloadHanderProtected(BaseHandler):
    @authenticated
    def get(self, file_id):
        print 'entre'
        self.set_header('X-Accel-Redirect', '/download_protected/preprocessed_data/16_seqs.fastq' )
        self.finish()
