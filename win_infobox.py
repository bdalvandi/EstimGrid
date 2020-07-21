from Forms import dlgInfoBox
from general_functions import set_layout


class InfoBox(dlgInfoBox):
    def __init__(self, parent, title, text_file_path):
        super().__init__(parent)
        set_layout(self)
        with open(text_file_path) as f:
            self.txtInfo.SetValue(f.read())
            self.SetTitle(title)

    def onCopy(self, event):
        pass

    def onPrint(self, event):
        pass
