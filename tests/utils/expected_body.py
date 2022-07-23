class YandexDiskAPI():
    expected_body_create_folder = {
        'href': 'https://cloud-api.yandex.net/v1/disk/resources?path=disk%3A%2FTest+API',
        'method': 'GET',
        'templated': False
    }

    expected_body_copy_file = {
        'href': 'https://cloud-api.yandex.net/v1/disk/resources?path=disk%3A%2FTest+API%2F%D0%A4%D0%B0%D0%B9%D0%BB+%D0%B4%D0%BB%D1%8F+%D0%BA%D0%BE%D0%BF%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F.txt',
        'method': 'GET',
        'templated': False
    }

    expected_body_rename_file = {
        'href': 'https://cloud-api.yandex.net/v1/disk/resources?path=disk%3A%2FTest+API%2FFile+for+API.txt',
        'method': 'GET',
        'templated': False
    }
