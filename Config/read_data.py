from configparser import ConfigParser
from csv import DictReader


def read_data_ini(list_name: str, list_value: str) -> str:
    """
    method is read data from ini file
    :param list_name: {str}
    :param list_value: {str}
    :return: {str}
    """
    config = ConfigParser()
    config.read('pytest.ini')
    data = config[list_name][list_value]
    return data


def read_csv_data(file_name: str) -> list:
    """
    method is read data from csv file
    :param file_name: {str}     file name
    :return: {list}
    """
    with open(file_name, 'r') as f:
        dict_reader = DictReader(f)
        list_of_dict = list(dict_reader)
        return list_of_dict
