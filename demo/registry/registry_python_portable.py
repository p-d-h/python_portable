from .registry import Registry
import pathlib


class RegistryPythonPortable(Registry):
    PP_PATH = 'pp_path'

    def __init__(self):
        Registry.__init__(self)

    @property
    def pp_path(self):
        return self.read_reg(self.PP_PATH, Registry.STRING, '')

    @pp_path.setter
    def pp_path(self, value=''):
        if value is None:
            value = str(pathlib.Path(__file__).parents[2].resolve())
            print(value)
        self.set_reg(self.PP_PATH, Registry.STRING, value)


if __name__ == '__main__':
    reg_pp = RegistryPythonPortable()
    reg_pp.pp_path = None
