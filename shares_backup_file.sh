#!/bin/bash - 
#===============================================================================
#
#          FILE: shares_backup_file
# 
#         USAGE: ./shares_backup_file.sh
# 
#   DESCRIPTION: 
# 
#       OPTIONS: ---
#  REQUIREMENTS: ---
#          BUGS: ---
#         NOTES: ---
#        AUTHOR: Dilawar Singh (), dilawars@ncbs.res.in
#  ORGANIZATION: NCBS Bangalore
#       CREATED: 07/09/2016 01:59:51 PM
#      REVISION:  ---
#===============================================================================

set -o nounset                              # Treat unset variables as an error
if [[ $# -lt 1 ]]; then
    echo "USAGE: $0 filepath"
    exit
fi
FILENAME="$1"
sshpass -e rsync -azv --progress $FILENAME dilawars@shares.ncbs.res.in:~/archives/
echo "Here is the path of the file on shares"
sshpass -e ssh dilawars@shares.ncbs.res.in find /home/bhalla/dilawars/archives/ -type f -name "*${FILENAME}"
notify-send "Done backing up $FILENAME"
