from .utils.api_utils import YandexDiskApi


def test_API_Copy_file_to_previously_created_folder():
    print('\nЗапуск теста')
    disk_api = YandexDiskApi()
    disk_api.create_folder()
    disk_api.copy_file()
    disk_api.rename_file()
