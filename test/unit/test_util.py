from BaseCase import BaseCase
import unittest
from src import util


class TestSaveUser(BaseCase):
    """
    Unit test for save_user
    """

    def test_export_to_csv(self):
        """
        given valid rows, valid headers and file path the function should generate csv
        """
        file = util.export_to_csv([["content"]], ["header"], "data/export.csv")
        assert file is not None

    def test_get_file_path(self):
        """
        given file_id check if telegram api returns file path
        """
        file_id = "some Id"
        try:
            file_path = util.get_file_path(file_id)
        except Exception as ex:
            assert False
        assert file_path is not None

    def test_generate_audio_file(self):
        """
        given file_path check if audio file is generated and saved
        """
        file_path = "some Id"
        try:
            file = util.generate_audio_file(file_path)
        except Exception as ex:
            assert False
        assert file is not None

    def test_transcribe_audio(self):
        """
        given audio file path check if transcription works correctly
        """
        file_path = "some path"
        try:
            transcription = util.transcribe_audio(file_path)
        except Exception as ex:
            assert False
        assert len(transcription) != 0
