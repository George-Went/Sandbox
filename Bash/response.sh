#!/usr/bin/env expect
spawn -noecho /tmp/foo.sh
expect "Foo? " { send -- "1\r" }
expect "Bar? " { send -- "2\r" }
expect "Baz? " { send -- "3\r" }
interact