#!/usr/bin/env ruby
sender = ARGV[0].scan(/(?<=from:)[+]?[a-zA-Z0-9]+/).join
receiver = ARGV[0].scan(/(?<=to:)[+]?[a-zA-Z0-9]+/).join
flags = ARGV[0].scan(/(?<=flags:)-?\d:-?\d:-?\d:-?\d:-?\d/).join

puts "#{sender},#{receiver},#{flags}"
