#!/bin/sh

BACKUP_PATH='/tmp'
DATE=`date +%m-%d` # keep backups for 30 days
DB_NAME='your_db_name'
HOST=${MYSQL_HOST:-localhost}
PASS=${MYSQL_PASS:-""}
USER=${MYSQL_USER:-root}

# ----------------------------------------------------------------------------
# No need to edit after this line
# ----------------------------------------------------------------------------
[ -d "${BACKUP_PATH}/${DB_NAME}" ] ||  mkdir -p "${BACKUP_PATH}/${DB_NAME}"

echo "\033[0;33mStarting to backing up...\033[0m"

# ----------------------------------------------------------------------------
# check if mysqldump and dump
# ----------------------------------------------------------------------------
hash mysqldump > /dev/null 2>&1 && mysqldump -h ${HOST} --user=${USER} --password=${PASS} --events --compress --hex-blob --opt --skip-comments ${DB_NAME} | bzip2 > /${BACKUP_PATH}/${DB_NAME}/${DATE}.sql.bz2 || {
    echo 'mysqldump not installed'
    exit
}
