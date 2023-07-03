# Creates custom HTTP response header "X-Served-By"

include stdlib

$line = '        add_header X-Served-By $hostname always;'

exec { 'update system':
  command => 'sudo apt-get update -y',
  before  => Package['nginx'],
}

Package { 'nginx':
  ensure => installed,
  before => File_line['add_header']
}

file_line { 'add_header':
  ensure => present,
  line   => $line,
  after  => '^http {',
  path   => '/etc/nginx/nginx.conf',
  notify => Service['nginx'],
}

service { 'nginx':
  ensure => running,
}
