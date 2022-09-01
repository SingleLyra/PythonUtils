# need pip install xlrd == 1.2.0
import xlrd
def READ_EXCEL(filename, remove_excel_head=False):
    xlsx_data = xlrd.open_workbook(filename)
    sheet1 = xlsx_data.sheets()[0]
    nrows = sheet1.nrows
    ncols = sheet1.ncols

    print(nrows, ncols)
    li = []
    for i in range(nrows):
        if remove_excel_head and i == 0:
            i = i + 1
        li.append(sheet1.row_values(i))
        print(sheet1.row_values(i))
    return nrows, ncols, li
def MakeGraph(point_all):
    graph = {}
    def addedge(x: str, y: str, dic: dict):
        dic[(x,y)] = True
    for point_x in point_all:
        Output_x = point_x[2]
        for point_y in point_all:
            Input_y = point_y[1]
            flag_x2y = False
            for op in Input_y.split(" "):
                if op in Output_x:
                    flag_x2y = True
            if flag_x2y:
                addedge(point_x[0], point_y[0], graph)
    print(len(point_all))
    return graph

if __name__ == "__main__":
    point_all = []
    nrows, ncols, li = READ_EXCEL(filename='data/05-07-规则输入输出与联系.xlsx',remove_excel_head=True)
    for rowid in range(len(li)):
        row = li[rowid]
        rule_name = ""
        Input = ""
        Output = ""
        for colid in range(ncols):
            if colid == 0:
                rule_name = row[colid]
            if colid == 2:
                Input = row[colid]
            if colid == 3:
                Output = row[colid]
        temp = (rule_name, Input, Output)
        point_all.append(temp)
    print(point_all)
    graph = MakeGraph(point_all)
    print(len(graph))