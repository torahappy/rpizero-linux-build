#!/bin/bash

if [[ ! -f "$HOME/wifi-check-pid" ]]; then
  # if no pid file, create one
  echo "no pid file; continuing"
  echo -n $$ > $HOME/wifi-check-pid
else
  # if pid file exists, check validity

  # no newline (the file consists of exactly one line)
  rg -U '\n' $HOME/wifi-check-pid
  if [[ $? -eq 1 ]]; then
    # the file consists of digits only. (excludes empty files)
    rg -U '^\d+$' $HOME/wifi-check-pid
    if [[ $? -eq 0 ]]; then
      ps -Ao pid,args | rg "^\s*$(cat $HOME/wifi-check-pid)\s.+wifi-check.sh\$"
      if [[ $? -eq 0 ]]; then
        echo "process already exists; quitting"
        exit
      fi
    fi
  fi

  echo "invalid pid file; regen and continuing"
  echo -n $$ > $HOME/wifi-check-pid
fi

PRIORITY_CONNECT=0

function checkfor_priority () {
  if [ -z "$2" ]; then
    echo "invalid args"
    return 1
  fi

  if [ -z "$1" ]; then
    echo "invalid args"
    return 1
  fi

  if [[ $PRIORITY_CONNECT -eq 0 ]]; then
    sudo nmcli c show | rg "^$1\s.+--\s*\$"
    if [ $? -ne 0 ]; then
      echo "the priority connection is already up"
      PRIORITY_CONNECT=1
      return 0
    fi

    sudo nmcli device wifi list | rg "^\s*([A-F0-9]{2}:){5}[A-F0-9]{2}\s*$2\s"

    if [ $? -eq 0 ]; then
      sudo nmcli d set wlan0 autoconnect yes managed yes
      sudo nmcli d connect wlan0
      sudo nmcli c up $1
      PRIORITY_CONNECT=1
    else
      PRIORITY_CONNECT=0
    fi

  fi
}

function checkfor () {
  if [ -z "$1" ]; then
    echo "invalid args"
    return 1
  fi

  if [[ $PRIORITY_CONNECT -eq 0 ]]; then

    curl -m 60 1.1.1.1 1>/dev/null 2>&1

    if [[ $? -ne 0 ]]; then
      sudo nmcli d set wlan0 autoconnect yes managed yes
      sudo nmcli d connect wlan0
      sudo nmcli c up $1
    fi

    sleep 10

  fi

}

# checkfor_priority preconfigured my_ssid
# checkfor preconfigured2
# checkfor preconfigured3
# .
# .
# .

checkfor preconfigured

rm $HOME/wifi-check-pid
