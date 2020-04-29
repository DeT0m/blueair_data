from pydrive.drive import GoogleDrive
from pydrive.auth import GoogleAuth


class GoogleDriveSession():
    """Defining Google Drive session"""

    def __init__(self, folder_id):
        self.folder_id = folder_id
        self.gauth = GoogleAuth()
        self.drive = GoogleDrive(self.gauth)

    def get_file_list(self):
        """Gets sorted file list from Google Drive."""
        # Get all files from specific folder on Google Drive as list
        query = f"'{self.folder_id}' in parents and trashed=false"
        file_list = self.drive.ListFile({'q': query}).GetList()
        # Sort file list by date of file creation
        self.file_list = sorted(file_list, key=lambda i: i['createdDate'])
        return self.file_list

    def download_temp_file(self, file_id):
        """Downloads file from Google Drive as temporary file."""
        file_download = self.drive.CreateFile({'id': file_id})
        file_download.GetContentFile('temp.csv', mimetype='text/csv')

    # TODO: delete temp file
