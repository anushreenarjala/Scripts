#!/bin/bash - 
#===============================================================================
#
#          FILE: create_archive_for_labnote_upload.sh
# 
#         USAGE: ./create_archive_for_labnote_upload.sh 
# 
#   DESCRIPTION:  This script needs to be run the same directory which is
#   to be uploaded on labnotes.
# 
#       OPTIONS: ---
#  REQUIREMENTS: ---
#          BUGS: ---
#         NOTES: ---
#        AUTHOR: Dilawar Singh (), dilawars@ncbs.res.in
#  ORGANIZATION: NCBS Bangalore
#       CREATED: 05/17/2017 05:50:43 PM
#      REVISION:  ---
#===============================================================================

set -o nounset                              # Treat unset variables as an error

TOTALSIZE=0
NOW=$(date +"%Y_%m_%d__%H_%M_%S")
LABNOTE="LABNOTE_${NOW}"
DIR="/tmp/${LABNOTE}"
mkdir -p ${DIR}
FILES=`find . -type f -size 1M`
for f in ${FILES}; do
    cp $f ${DIR}/
done
echo "Total size of labnote archive "
du -sh ${DIR}

# create archive file.
tar -cvzf ${LABNOTE}.tar.gz ${DIR}
