import xlsxwriter

def create_workbook(filename):
    work_book = xlsxwriter.Workbook(filename)
    return work_book

