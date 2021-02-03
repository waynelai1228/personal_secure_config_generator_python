from definitions import ROOT_DIR  # the root directory of this project
import json

# this class stores a single sshd configuration
class SSHDConfig:
  # constructor takes a configuration keyword and its corresponding argument
  def __init__(self, keyword, argument):
    sshd_config_json = open(ROOT_DIR + "/sshdConfig/sshd_config_opt.json", "r")
    sshd_config_v2_json = open(ROOT_DIR + "/sshdConfig/sshd_config_opt_v2.json", "r")
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
      setting_type = self.sshd_config_opt[keyword]["type"]

      # if type is string, then argument can be anything
      if setting_type == "String":
        self.key = keyword
        self.arg = argument

      # if type is single value, then argument must be on of the options
      if setting_type == "Single-Option":
        if argument in self.sshd_config_opt[keyword]["options"]:
          self.key = keyword
          self.arg = argument

      # if type is multi option, split the argument using delimiter ','
      # and check that each individual value is valid
      if setting_type == "Multi-Option":
        arguments = argument.split(", ")
        argument_valid = True 
        while option in arguments:
          if option not in self.sshd_config_opt[keyword]["options"]:
            argument_valid = False
            break
        if argument_valid:
          self.key = keyword
          self.arg = argument

  def __str__(self):
    return self.key + " " + self.arg + "\n"
