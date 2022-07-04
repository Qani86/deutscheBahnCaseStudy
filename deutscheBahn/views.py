import csv
import json

from django.http import HttpResponse
from rest_framework.decorators import api_view

CSV_DATA = 'csvFile/DBNetz-Betriebsstellenverzeichnis-Stand2021-10.csv'


@api_view(['GET'])
def deutscheBahn(request):
    reader = csv.DictReader(open(CSV_DATA, encoding='utf-8'), delimiter=';')
    rows = []
    for row in reader:
        rows.append(row)
    return HttpResponse(json.dumps(rows), content_type="application/json")
