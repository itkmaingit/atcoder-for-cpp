#!/bin/bash

CC="g++"
DIR_PATH="${HOME}/works/problems"

date=$1
diff=$2

if [ -z ${date} ] || [ -z ${diff} ]; then
  echo "Error: date or diff variable is not set"
  exit 1
fi

${CC} ${DIR_PATH}/${date}/${diff}.cpp -o ${DIR_PATH}/${date}/${diff}.out
${DIR_PATH}/${date}/${diff}.out < ${DIR_PATH}/${date}/${diff}.in | tee ${DIR_PATH}/${date}/${diff}.txt