#!/bin/bash

DIR_PATH="./problems"
VSCODE_SETTINGS_DIR_PATH="${HOME}/works/.vscode"
date=$1
diff=$2

if [ -z ${date} ] || [ -z ${diff} ]; then
  echo "Error: date or diff variable is not set"
  exit 1
fi

find "${VSCODE_SETTINGS_DIR_PATH}" -name "*.json.default" -print0 | while IFS= read -r -d $'\0' file; do
  new_file="${file%.json.default}.json"
  cp "${file}" "${new_file}"
done

mkdir -p ${DIR_PATH}/${date}
cp ./sample_code/init.cpp ${DIR_PATH}/${date}/${diff}.cpp
touch ${DIR_PATH}/${date}/${diff}.in
touch ${DIR_PATH}/${date}/${diff}.res
python3 ./scripts/rename.py "${date}" "${diff}"