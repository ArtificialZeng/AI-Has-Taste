#!/usr/bin/env ruby
require 'json'
require 'digest'
path = File.join(__dir__, 'counterexample.json')
d = JSON.parse(File.read(path))
powmod = ->(b,e,m) { r=1; while e>0; r=r*b%m if e.odd?; b=b*b%m; e >>= 1; end; r }
a6 = d.fetch('a6')
raise 'a6 mismatch' unless ((2**171 + 1) / 9) == a6 && (2**171 + 1) % 9 == 0
raise 'mod 162 mismatch' unless (powmod.call(2,171,162)+1) % 162 == 27
raise 'a6 mod 18 mismatch' unless a6 % 18 == 3
r = (powmod.call(2,a6,171)+1) % 171
raise 'decisive remainder mismatch' unless r == 9
puts "PASS n=7 remainder=#{r} data_sha256=#{Digest::SHA256.file(path).hexdigest} code_sha256=#{Digest::SHA256.file(__FILE__).hexdigest}"
