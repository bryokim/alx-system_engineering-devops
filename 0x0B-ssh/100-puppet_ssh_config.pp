# Makes changes to the ssh config file
# IdentityFile => ~/.ssh/school
# PasswordAuthentication => no

include stdlib

file_line { 'Turn off passwd auth':
  ensure  => present,
  path    => '/etc/ssh/ssh_config',
  line    => '    PasswordAuthentication no',
  match   => '^[#]*[\s]*(?i)PasswordAuthentication[\s]+(yes|no)[\s]*$',
  replace => true,
}

file_line { 'Declare identity file':
  ensure  => present,
  path    => '/etc/ssh/ssh_config',
  line    => '    IdentityFile ~/.ssh/school',
  match   => '^[#]*[\s]*(?i)IdentityFile[\s]+~/.ssh/id_rsa[\s]*$',
  replace => true,
}
