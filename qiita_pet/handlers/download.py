from tornado.web import authenticated

from qiita_db.data import PreprocessedData
from qiita_db.study import Study
from qiita_db.user import User
from qiita_db.util import get_filepath_from_id

from .base_handlers import BaseHandler
from .study_handlers import check_access

class DownloadHandler(BaseHandler):
    @authenticated
    def get(self, preprocessed_data_id):
        preprocessed_data = PreprocessedData(preprocessed_data_id)
        user = User(self.current_user)
        study = Study(preprocessed_data.study)
        check_access(user, study)

        file_id = [f[1] for f in preprocessed_data.get_filepaths_with_info()
                   if f[2]=='preprocessed_fasta']

        if not file_id:
            raise ValueError('User: %s tried to access preprocessed id: %s' %
                             (user.id, preprocessed_data_id))

        filepath = file_id[0][len("/Users/antoniog/Desktop/CurrentWork/largeFiles/qiita/base_dir/"):]
        filepath = '/protected/' + filepath
        print filepath, '------'


        self.set_header('X-Accel-Redirect', filepath)
        self.finish()
