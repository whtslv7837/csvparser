import argparse
from utils import csv_reader
from reports.average_rating import AverageRatingReport
from tabulate import tabulate

REPORTS = {
    'average-rating': AverageRatingReport
}


def main():
    parser = argparse.ArgumentParser(description='Анализ Рейтинга Брендов')
    parser.add_argument('--files', nargs='+', required=True, help='Файлы csv')
    parser.add_argument('--report', required=True, choices=REPORTS.keys(), help='Тип отчета')
    args = parser.parse_args()

    report_class = REPORTS[args.report]
    data = csv_reader(args.files)
    report = report_class(data)
    result = report.generate()

    print(tabulate(result, headers=['Brand', 'Average Rating'], tablefmt='grid'))


if __name__ == '__main__':
    main()