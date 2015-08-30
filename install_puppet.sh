brew install homebrew/versions/ruby20
gem install --no-rdoc --no-ri puppet -v 3.7.4
make dist install

# It doesn't work with ruby 2.2.2 which is what homebrew gave me by default.
# /usr/local/gems/puppet-3.7.4/lib/puppet/vendor/safe_yaml/lib/safe_yaml/syck_node_monkeypatch.rb:42:in `<top (required)>': uninitialized constant Syck (NameError)
