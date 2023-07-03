# Creates custom HTTP response header "X-Served-By"

include stdlib

$line = '        add_header X-Served-By $hostname always;'

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
