# Creates custom HTTP response header "X-Served-By"

include stdlib

exec { 'update system':
  provider => shell,
  command  => 'apt-get update -y',
  before   => Package['nginx'],
}

Package { 'nginx':
  ensure => installed,
  before => File_line['add_header'],
  notify => Service['nginx']
}

file { '/var/www/html/index.html':
  ensure  => present,
  content => inline_template('<%= "Hello World!\n " %>'),
  require => Package['nginx'],
}

exec {'redirect_me':
  command  => 'sed -i "25i\ \trewrite ^/redirect_me https://www.youtube.com/v=QH2-TGUlwu4 permanent;\n" /etc/nginx/sites-available/default',
  provider => 'shell'
}

file_line { 'add_header':
  ensure => present,
  line   => inline_template('<%= "\n\tadd_header X-Served-By $hostname always;" %>'),
  after  => '^(\s)+server_name (.)+$',
  path   => '/etc/nginx/sites-available/default',
  notify => Service['nginx'],
}

service { 'nginx':
  ensure => running,
}
