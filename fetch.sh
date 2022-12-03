#!/bin/bash

function main {
    local session_file
    local date

    declare -i date
    date="$1"

    session_file="aoc-session"

    if [[ $date -gt 25 ]]; then
        echo "End of AOC-2022"
        exit 0
    fi

    if [[ ! -f $session_file ]]; then
      echo "[-] Missing session"
      exit 1
    fi

    cookie="$(cat ${session_file})"

    pushd $PWD
    dir="day$(date +%d)"
    if [[ -d $dir ]]; then
        echo "Directory already exists"
        exit 0
    fi

    mkdir -p $dir && cd $dir
    curl -s -O "https://adventofcode.com/2022/day/$date/input" -b "$cookie"
    cp ../template.py main.py
    popd
}

main "$(date +%d | sed 's/^0*//')"
