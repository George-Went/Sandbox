#!/usr/bin/env bash
for question in Foo Bar Baz; do
    read -p "${question}? "
    replies=("${replies[@]}" "$REPLY")
done
echo "${replies[@]}"