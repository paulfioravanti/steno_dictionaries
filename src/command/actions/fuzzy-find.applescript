property System : script "steno-dictionaries/system"
property Terminal : script "steno-dictionaries/terminal"

on run
  set activeApp to System's getActiveApp()

  if activeApp is not contained by Terminal's Apps then
    System's displayError("Fuzzy find not supported with", activeApp)
  end if

  set processName to Terminal's getProcessName(activeApp)

  if processName contains "vim" then
    performVimFuzzyFind(activeApp)
  else
    performCommandLineFuzzyFind(activeApp)
  end
end run

on performVimFuzzyFind(activeApp)
  tell application "System Events" to tell process activeApp
    # 53 = Escape
    key code 53
    # Currently using Ctrl-P for fuzzy finding in Vim.
    # https://github.com/kien/ctrlp.vim
    keystroke "p" using {control down}
  end tell
end performVimFuzzyFind

on performCommandLineFuzzyFind(activeApp)
  tell application "System Events" to tell process activeApp
    # Currently using fzf for fuzzy finding on the command line.
    # https://github.com/junegunn/fzf
    keystroke "$(fzf)"
  end tell
end performCommandLineFuzzyFind
