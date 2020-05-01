from pydrive.drive import GoogleDrive
from pydrive.auth import GoogleAuth


class GoogleDriveSession():
    """Defining Google Drive session"""

    def __init__(self, folder_id):
        """
        Logs in to Google Drive and authenticates.
        Settings for Goole authentication are in settings.yaml file.
        """
        self.folder_id = folder_id  # Set folder id
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
        """
        Downloads file from Google Drive as temporary file.
        Takes one argument with file id.
        """
        # Set temporary filename. Should be unique.
        self.filename = 'temp_gd_file.csv'
        file_download = self.drive.CreateFile({'id': file_id})
        file_download.GetContentFile(self.filename, mimetype='text/csv')
