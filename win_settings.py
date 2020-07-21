from Forms import dlgSettings
from general_functions import set_layout
from configobj import ConfigObj
import wx.propgrid


class SettingsDlg(dlgSettings):
    def __init__(self, parent):
        super().__init__(parent)
        set_layout(self)

        # adding application properties
        self.pgSettings.Append(wx.propgrid.StringProperty('Company', 'company'))
        self.pgSettings.Append(wx.propgrid.StringProperty('Connection String', 'conn_str'))
        self.pgSettings.Append(wx.propgrid.StringProperty('Owner', 'owner'))
        self.pgSettings.Append(wx.propgrid.DirProperty('Default Snapshot Path', 'snp_dir'))

    def onSettingsLoad(self, event):
        config = ConfigObj('misc/settings.ini')
        for prop in self.pgSettings.Properties:
            prop.SetValue(config[prop.GetLabel()])

    def onSettingsSave(self, event):
        config = ConfigObj('misc/settings.ini')
        for prop in self.pgSettings.Properties:
            config[prop.GetLabel()] = prop.GetValue()
        config.write()
        self.Destroy()

