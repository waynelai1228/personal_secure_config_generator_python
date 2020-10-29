class SSHDConfig:
  def __init__(self):
    # This structure holds all the setting names and permitted value
    # The first element of the tuple specifies the type
    # The second element of the tuple specifies the default value
    #
    # For now, the options that are customizable are marked by 'String'
    # The eventual plan is to create their own custom type and add pattern 
    # validation
    self.sshd_config_opt = {
        'AcceptEnv': ('String'),
        'AddressFamily': ('Single-Option', 'any', 'inet', 'inet6'),
        'AllowAgentForwarding': ('Single-Option', 'yes', 'no'),
        'AllowTcpForwarding': ('Single-Option', 'yes', 'no'),
        'AllowUsers': ('String'),
        'DenyUsers': ('String'),
        'AllowGroups': ('String'),
        'DenyGroups': ('String'),
        'AuthorizedKeysFile': ('String'),
        'ChallengeResponseAuthentication': ('Single-Option', 'yes', 'no'),
        'ChrootDirectory': ('String'),
        'Compression': ('Single-Option', 'delayed', 'yes', 'no'),
        'ForceCommand': ('String'),
        'GatewayPorts': ('String','127.0.0.1'),
        'HostKey': ('String','/etc/ssh/ssh_host_key'),
        'IgnoreRhosts': ('Single-Option', 'yes', 'no'),
        'IgnoreUserKnownHosts': ('Single-Option', 'no', 'yes'),
        'GSSAPIStoreCredentialsOnRekey': ('Single-Option', 'no', 'yes'),
        'HostbasedUsesNameFromPacketOnly': ('Single-Option', 'no', 'yes'),
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
        }
