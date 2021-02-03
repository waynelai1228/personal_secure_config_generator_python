import pytest
from sshdConfig.sshd_config import SSHDConfig
from sshdConfig.sshd_config_file import SSHDConfigFile

def test_addconfig():
  sshdfile = SSHDConfigFile({})

  chrootDirSetting = SSHDConfig("ChrootDirectory", "/helloworld")
  permitRootLoginSetting = SSHDConfig("PermitRootLogin", "yes")
  cipherSetting = SSHDConfig("Ciphers", "3des-cbc, aes192-cbc, aes128-ctr") 

  sshdfile.add_config(chrootDirSetting)
  sshdfile.add_config(permitRootLoginSetting)
  sshdfile.add_config(cipherSetting)
  sshdfile.write_to_file()
