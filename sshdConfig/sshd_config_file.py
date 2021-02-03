from sshdConfig.sshd_config import SSHDConfig

# this class contains the necessary information to build an sshd_config file
class SSHDConfigFile:
  # constructor takes a map from config key to SSHDConfigs
  def __init__(self, configurations):
    self.config = configurations

  # add a configuration to the file
  def add_config(self, configuration):
    # type check configuration
    if not isinstance(configuration, SSHDConfig):
      return False
    # configuration is invalid
    if not hasattr(configuration, 'key'):
      return False
    # add the config to a list of configurations
    self.config.update({configuration.key: configuration})

  # remove a configuration using the name of the setting
  def remove_config(self, key_to_remove):
    self.config.remove(key_to_remove)

  def write_to_file(self):
    with open('sshdConfigWrite.conf', 'x') as FILE:
      for key in self.config.keys():
        FILE.write(str(self.config[key]))
