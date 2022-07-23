from .utils.api_utils import YandexDiskApi


def test_API_Copy_file_to_previously_created_folder():
    """Проверка копирования файла в созданную папку, с последующим переименовыванием этого файла
    ОР_1: Файл успешно переименован
    ОР_2: Код ответа соответствует требованиям
    ОР_3: Тело ответа соответствует требованиям
    """
    disk_api = YandexDiskApi()
    disk_api.create_folder()
    disk_api.copy_file()
    disk_api.rename_file()
    disk_api.check_file_name()
