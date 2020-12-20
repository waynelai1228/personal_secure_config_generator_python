import pytest
import ../sshd_config

def test_validConfig():
  chrootDirSetting = SSHDConfig("ChrootDirectory", "/helloworld")
  assert chrootDirSetting.keyword == "ChrootDirectory"
  permitRootLoginSetting = SSHDConfig("PermitRootLogin", "yes")
  assert permitRootLoginSetting == "PermitRootLogin"
