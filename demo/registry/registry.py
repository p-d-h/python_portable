import winreg


class Registry:
    BOOL = 'BOOL'
    STRING = 'STRING'
    INTEGER = 'INTEGER'
    FLOAT = 'FLOAT'

    def __init__(self, reg_path=None):
        if reg_path is None:
            self.reg_path = f'Software\\xemax\\python_portable'
        else:
            self.reg_path = reg_path
        self.value_reg = None

    def set_reg(self, name, data_type, value):
        try:
            if data_type == Registry.BOOL:
                if value:
                    _value = 'True'
                else:
                    _value = 'False'
            elif data_type == Registry.STRING:
                _value = str(value)[:1000]  # Beschränkung auf 1000 Zeichen
            elif data_type == Registry.INTEGER:
                _value = str(int(value))
            elif data_type == Registry.FLOAT:
                _value = str(float(value))
            else:
                _value = '#_None_#'

            winreg.CreateKey(winreg.HKEY_CURRENT_USER, self.reg_path)
            registry_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, self.reg_path, 0,
                                          winreg.KEY_WRITE)
            winreg.SetValueEx(registry_key, name, 0, winreg.REG_SZ, _value)
            winreg.CloseKey(registry_key)
            return True
        except WindowsError:
            print('error_set_reg')
            return False

    def get_reg(self, name, data_type, default):
        try:
            registry_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, self.reg_path, 0,
                                          winreg.KEY_READ)
            self.value_reg, regtype = winreg.QueryValueEx(registry_key, name)
            winreg.CloseKey(registry_key)
        except WindowsError:
            self.set_reg(name, data_type, default)
            self.value_reg = None

    def read_reg(self, name, data_type, default):
        self.get_reg(name, data_type, default)
        value = None
        if self.value_reg is not None:
            if data_type == Registry.BOOL:
                if self.value_reg == 'True':
                    value = True
                else:
                    value = False
            elif data_type == Registry.STRING:
                value = str(self.value_reg)
            elif data_type == Registry.INTEGER:
                value = int(self.value_reg)
            elif data_type == Registry.FLOAT:
                value = float(self.value_reg)
        else:
            value = default
            self.set_reg(name, data_type, value)
        return value
