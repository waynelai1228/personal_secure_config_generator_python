import json

class SSHDConfig:
  def __init__(self, keyword, argument, description):
    sshd_config_json = open("sshd_config_opt.json", "r")
    sshd_config_v2_json = open("sshd_config_opt_v2.json", "r")
    # This structure holds all the setting names and permitted value
    #
    # For now, the options that are customizable are marked by 'String'
    # The eventual plan is to create their own custom type and add pattern 
    # validation
    self.sshd_config_opt = json.loads(sshd_config_json.read())
    # Same as above, but this structure holds settings that are only
    # available in version 2
    # This class holds a single configuration and its description
    self.sshd_config_opt_v2 = json.loads(sshd_config_v2_json.read())

    # first check that the keyword is a valid setting
    if keyword in self.sshd_config_opt:
      # use the key to get to the type

      # if type is string, then argument can be anything

      # if type is single value, then argument must be on of the options

      # if type is multi option, split the argument using delimiter ','
      # and check that each individual value is valid
      self.key = keyword
    self.arg = argument
    self.desc = description
