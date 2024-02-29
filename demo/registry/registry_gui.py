from .registry import Registry
import pathlib


class RegistryGui(Registry):
    GUI_PATH = 'gui_path'

    def __init__(self):
        Registry.__init__(self)

    @property
    def gui_path(self):
        return self.read_reg(self.GUI_PATH, Registry.STRING, '')

    @gui_path.setter
    def gui_path(self, value=''):
        if value is None:
            value = str(pathlib.Path(__file__).parents[2].resolve())
            print(value)
        self.set_reg(self.GUI_PATH, Registry.STRING, value)


if __name__ == '__main__':
    reg_pp = RegistryGui()
    reg_pp.pp_path = None
