# VSCode 

On any variable to have reference preview:
Cmd + Click 

For python command line arguments:
Paste following in .vscode > settings.json
"code-runner.executorMap": { "python": "$pythonPath -u $fullFileName abc 1 2 3" }

import sys
print(sys.argv)
