import json
import re
import os
import sys

DATE=""
DIFFICULTY=""



def replace_run_sh(file_path):
    """シェルスクリプト内の 変数 を置換する。

    Args:
      file_path: シェルスクリプトのファイルパス。
    """


    with open(file_path, 'r') as f:
        lines = f.readlines()

    with open(file_path, 'w') as f:
        for line in lines:
            if line.startswith('difficulty='):
                f.write(f'difficulty="{DIFFICULTY}"\n')
            elif line.startswith('date='):
                f.write(f'date="{DATE}"\n')
            else:
                f.write(line)

def replace_launch_json(file_path):
  """launch.json のプレースホルダーを標準入力で受け取った値に置換する。

  Args:
    file_path: launch.json のファイルパス。
  """

  with open(file_path, 'r') as f:
    data = json.load(f)

  # [date] と [difficulty] を置換
  data['configurations'][0]["args"][1]='${workspaceFolder}'+f"/problems/{DATE}/{DIFFICULTY}.in"
  data['configurations'][0]["args"][3]='${workspaceFolder}'+f"/problems/{DATE}/{DIFFICULTY}.txt"

  with open(file_path, 'w') as f:
    json.dump(data, f, indent=2)

def replace_tasks_json(file_path):
  """tasks.json のプレースホルダーを標準入力で受け取った値に置換する。

  Args:
    file_path: tasks.json のファイルパス。
  """

  with open(file_path, 'r') as f:
    data = json.load(f)

  # [date] と [difficulty] を置換
  data['tasks'][0]["args"][1]='${workspaceFolder}'+f"/problems/{DATE}/{DIFFICULTY}.cpp"

  with open(file_path, 'w') as f:
    json.dump(data, f, indent=2)




if __name__ == "__main__":
    HOME = os.environ['HOME']
    DATE=sys.argv[1]
    DIFFICULTY=sys.argv[2]
    replace_run_sh(f"{HOME}/works/scripts/run.sh")
    replace_tasks_json(f"{HOME}/works/.vscode/tasks.json")
    replace_launch_json(f"{HOME}/works/.vscode/launch.json")