import os
from pprint import pprint
import json


def get_file_path(relative_paths: list[str]) -> list:
    paths = []
    for relative_path in relative_paths:
        paths.append(os.path.abspath(relative_path))

    return paths


def create_file_with_data(list_paths: list[str]):
    tests_path = list_paths[0]
    values_path = list_paths[1]
    report_path = list_paths[2]

    with open(tests_path, 'r') as tests_file:
        tests_dict = json.loads(tests_file.read())['tests']

    with open(values_path, 'r') as values_file:
        values_dict = json.loads(values_file.read())['values']

    def fill_values(tests: dict, values: dict):
        for el_tests in tests:
            for el_values in values:
                if el_tests['id'] == el_values['id']:
                    el_tests['value'] = el_values['value']
                if 'values' in el_tests:
                    fill_values(el_tests['values'], values)
        return tests

    data = {
        "tests": fill_values(tests_dict, values_dict)
    }

    with open(report_path, 'w') as report_file:
        json.dump(data, report_file, indent=2)


if __name__ == '__main__':
    file_paths = get_file_path(['tests.json', 'values.json', 'report.json'])
    create_file_with_data(file_paths)
