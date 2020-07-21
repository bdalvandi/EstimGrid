from Forms import dlgAbout
from win_infobox import InfoBox
from general_functions import set_layout


class AboutDlg(dlgAbout):
    def __init__(self, parent):
        super().__init__(parent)
        set_layout(self)

    def onCredit(self, event):
        dlg = InfoBox(self,'Credit', 'misc/credit')
        dlg.ShowModal()
        dlg.Destroy()

    def onLicense(self, event):
        dlg = InfoBox(self, 'License', 'misc/license')
        dlg.ShowModal()
        dlg.Destroy()

