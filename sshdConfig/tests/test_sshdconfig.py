import pytest
from sshdConfig.sshd_config import SSHDConfig 

def test_validConfig():
  chrootDirSetting = SSHDConfig("ChrootDirectory", "/helloworld")
  assert chrootDirSetting.key == "ChrootDirectory"
  permitRootLoginSetting = SSHDConfig("PermitRootLogin", "yes")
  assert permitRootLoginSetting.key == "PermitRootLogin"
  cipherSetting = SSHDConfig("Ciphers", "3des-cbc, aes192-cbc, aes128-ctr") 

def test_invalidConfig():
  invalidKeyArgSetting = SSHDConfig("Invalid", "Setting")
  assert not hasattr(invalidKeyArgSetting, 'key')
  invalidArgMultiSetting = SSHDConfig("Ciphers", "3des-cbc, aes192-cbc, aes128")
  assert not hasattr(invalidArgMultiSetting, 'key')
  invalidArgSingleSetting = SSHDConfig("PermitRootLogin", "No")
  assert not hasattr(invalidArgSingleSetting, 'key')
  invalidKeySetting = SSHDConfig("PermitrootLogin", "yes")
