{"changed":true,"filter":false,"title":".bashrc","tooltip":"~/.bashrc","ace":{},"value":"# .bashrc\n\nexport PATH=$PATH:$HOME/.local/bin:$HOME/bin\n\n# load nvm\nexport NVM_DIR=\"$HOME/.nvm\"\n[ \"$BASH_VERSION\" ] && npm() { \n    # hack: avoid slow npm sanity check in nvm\n    if [ \"$*\" == \"config get prefix\" ]; then which node | sed \"s/bin\\/node//\"; \n    else $(which npm) \"$@\"; fi \n}\n# [ -s \"$NVM_DIR/nvm.sh\" ] && . \"$NVM_DIR/nvm.sh\"  # This loads nvm\nrvm_silence_path_mismatch_check_flag=1 # prevent rvm complaints that nvm is first in PATH\nunset npm # end hack\n\n\n# User specific aliases and functions\nalias python=python2.7\nalias run=\"python3 ~/environment/manage.py runserver $IP:$PORT\"\n\n# modifications needed only in interactive mode\nif [ \"$PS1\" != \"\" ]; then\n    # Set default editor for git\n    git config --global core.editor /usr/bin/nano\n\n    # Turn on checkwinsize\n    shopt -s checkwinsize\n\n    # keep more history\n    shopt -s histappend\n    export HISTSIZE=100000\n    export HISTFILESIZE=100000\n    export PROMPT_COMMAND=\"history -a;\"\n\n    # Source for Git PS1 function\n    git_type=$(type -t __git_ps1)\n    if [ -z $git_type ] && [ -e \"/usr/share/git-core/contrib/completion/git-prompt.sh\" ]; then\n        . /usr/share/git-core/contrib/completion/git-prompt.sh\n    fi\n\n    # Cloud9 default prompt\n    _cloud9_prompt_user() {\n        if [ \"$C9_USER\" = root ]; then\n            echo \"$USER\"\n        else\n            echo \"$C9_USER\"\n        fi\n    }\n\n    PS1='\\[\\033[01;32m\\]$(_cloud9_prompt_user)\\[\\033[00m\\]:\\[\\033[01;34m\\]\\w\\[\\033[00m\\]$(__git_ps1 \" (%s)\" 2>/dev/null) $ '\nfi\n\n# Add RVM to PATH for scripting. Make sure this is the last PATH variable change.\nexport PATH=\"$PATH:$HOME/.rvm/bin\"\n\n","undoManager":{"mark":-1,"position":-1,"stack":[]},"timestamp":1564521623286}