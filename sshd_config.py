class SSHDConfig:
  # This structure holds all the setting names and permitted value
  #
  # For now, the options that are customizable are marked by 'String'
  # The eventual plan is to create their own custom type and add pattern 
  # validation
  sshd_config_opt = {
      'AcceptEnv': {'type': 'String'},
      'AddressFamily': {'type': 'Single-Option', 'options': ('any', 'inet', 'inet6')},
      'AllowAgentForwarding': {'type': 'Single-Option', 'options': ('yes', 'no')},
      'AllowGroups': ('String'),
      'AllowTcpForwarding': {'type': 'Single-Option', 'options': ('yes', 'no')},
      'AllowUsers': {'type': 'String'},
      'AuthorizedKeysFile': ('String'),
      'ChallengeResponseAuthentication': ('Single-Option', 'yes', 'no'),
      'ChrootDirectory': ('String'),
      'Compression': ('Single-Option', 'delayed', 'yes', 'no'),
      'DenyGroups': ('String'),
      'DenyUsers': ('String'),
      'ForceCommand': ('String'),
      'GatewayPorts': ('String','127.0.0.1'),
      'GSSAPIStoreCredentialsOnRekey': ('Single-Option', 'no', 'yes'),
      'HostbasedUsesNameFromPacketOnly': ('Single-Option', 'no', 'yes'),
      'HostKey': ('String','/etc/ssh/ssh_host_key'),
      'IgnoreRhosts': ('Single-Option', 'yes', 'no'),
      'IgnoreUserKnownHosts': ('Single-Option', 'no', 'yes'),
    }
  # Same as above, but this structure holds settings that are only
  # available in version 2
  sshd_config_opt_v2 = {
      'Banner', ['String', 'none'],
      'Ciphers': ('Multiple-Options', '[<array of index>]',
                  '3des-cbc', 'aes128-cbc', 'aes192-cbc', 'aes256-cbc',
                  'aes128-ctr', 'aes192-ctr', 'aes256-ctr', 'arcfour128',
                  'arcfour256', 'arcfour', 'flowfish-cbc', 'cast128-cbc'),
      'ClientAliveCountMax': ('Number', 3);
      'ClientAliveInterval': ('Number', 0);
      'GSSAPIAuthentication': ('Single-Option', 'no', 'yes'),
      'GSSAPIKeyExchange': ('Single-Option', 'no', 'yes'),
      'GSSAPICleanupCredentials': ('Single-Option', 'yes', 'no'),
      'GSSAPIStrictAcceptorCheck': ('Single-Option', 'no', 'yes'),
      'HostbasedAuthentication': ('Single-Option', 'no', 'yes'),
      'HostKey': ('String','/etc/ssh/ssh_host_key'),
  # This class holds a single configuration and its description
  def __init__(self, keyword, argument, description):
    self.key = keyword
    self.arg = argument
    self.desc = description
