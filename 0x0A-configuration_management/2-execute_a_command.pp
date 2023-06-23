# Kills a process named killmenow

exec { 'pkill killmenow':
  path   => '/usr/bin/:/usr/sbin:/bin',
  onlyif => 'test `pgrep killmenow | wc -l` -gt 0',
}
