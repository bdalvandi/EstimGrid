import wx.grid
from general_functions import ttr


# Extended Grid class with more functions
class ExGrid(wx.grid.Grid):
    def __init__(self, parent, readonly_cols=()):
        super().__init__(parent)
        self.__minimal = False
        self.__readonly_cols = readonly_cols
        self.Bind(wx.grid.EVT_GRID_CELL_CHANGED, self.onGridCellChanged)


    def __set_readonly_cols(self):
        for i in range(self.GetNumberCols()):
            if i in self.__readonly_cols:
                attr = wx.grid.GridCellAttr()
                attr.SetReadOnly(True)
                self.SetColAttr(i, attr)

    # fill the grid with data as tuple of tuple
    # each internal tuple is considered as a row
    def FillValues(self, rows):
        r=0
        for row in rows:
            if len(row) > self.GetNumberCols():
                raise GridBookError('Number of items is grater than number of columns.')
            self.AppendRows()
            c=0
            for cell in row:
                if cell is not None:
                    self.SetCellValue(r, c, str(cell))
                c += 1
            r += 1
        self.AutoSizeColumns()
        self.__set_readonly_cols()

    # return column header labels as tuple
    @property
    def ColumnLabels(self):
        labels = []
        for i in range(self.GetNumberCols()):
            labels.append(self.GetColLabelValue(i))
        return tuple(labels)

    # return values as tuple of tuple
    # each internal tuple is considered as a row
    @property
    def CellValues(self):
        values = []
        for r in range(self.GetNumberRows()):
            row = []
            for c in range(self.GetNumberCols()):
                row.append(self.GetCellValue(r, c))
            values.append(tuple(row))
        return values

    # replace object codes with values from snap dict made from snap file
    # return codes not found in snap dict as tuple
    # [column]: list of col index whose cell values are codes to be replaced
    # [snap]: dict of object codes made by [read_snap()]
    def ApplySnap(self, snap):
        invalid_codes = []
        for c in range(self.GetNumberCols()):
            if c in self.__readonly_cols:
                continue
            for r in range(self.GetNumberRows()):
                self.SetCellEditor(r, c, wx.grid.GridCellFloatEditor())
                code = self.GetCellValue(r, c)
                try:
                    snp_value = snap[code][0]
                    snp_validity = snap[code][1]
                except KeyError:
                    if self.GetColLabelValue(self.NumberCols-1) == 'Ratio':
                        continue
                    if code != '':
                        invalid_codes.append(code)
                        snp_value = ''
                        snp_validity = 11
                    else:
                        snp_value = ''
                        snp_validity = 10

                self.SetCellRenderer(r, c, wx.grid.GridCellFloatRenderer(precision=2))
                self.SetCellValue(r, c, str(snp_value))
                if snp_validity == 0:  # invalid
                    self.SetCellTextColour(r, c, 'RED')
                elif snp_validity == 2 or snp_validity == 3:  # manual
                    self.SetCellTextColour(r, c, 'BLUE')
                elif snp_validity == 10:  # None
                    self.SetCellBackgroundColour(r, c, 'GOLDENROD')
                elif snp_validity == 11:  # Object not found
                    self.SetCellBackgroundColour(r, c, 'LIGHT BLUE')

        if self.GetColLabelValue(self.NumberCols - 1) == 'Ratio':
            for r in range(self.NumberRows):
                self.SetCellValue(r, self.NumberCols - 1, str(self.RecalcCol(r)))

        return tuple(invalid_codes)

    def onGridCellChanged(self, event):
        r = event.GetRow()
        c = event.GetCol()
        f = self.GetCellFont(r, c)
        f.MakeBold()
        f.MakeItalic()
        self.SetCellFont(r, c, font=f)

        # calculate TTR column
        if self.GetColLabelValue(self.NumberCols-1) == 'TTR':
            t = float(self.GetCellValue(r, self.NumberCols - 2))
            mv = float(self.GetCellValue(r, self.NumberCols - 3))
            Mv = float(self.GetCellValue(r, self.NumberCols - 4))
            mt = float(self.GetCellValue(r, self.NumberCols - 5))
            Mt = float(self.GetCellValue(r, self.NumberCols - 6))
            self.SetCellValue(r, self.NumberCols-1, str(ttr((Mt, mt, Mv, mv, t))))
