property Util : script "steno-dictionaries/util"

on run
  set activeApp to Util's getActiveApp()

  if activeApp is "1Password 7" then
    perform1PasswordQuitHard(activeApp)
  else if activeApp is "iTerm2" then
    performiTerm2QuitHard(activeApp)
  else
    # Convert a "Quit Hard" into a standard "Quit" for applications that do
    # not have specific "Quit Hard" handling.
    performQuit(activeApp)
  end if
end run

on perform1PasswordQuitHard(activeApp)
  tell application "System Events" to tell process activeApp
    keystroke "q" using {control down, option down, command down}
  end tell
end perform1PasswordQuitHard

on performiTerm2QuitHard(activeApp)
  set processName to Util's getiTermProcessName()

  if processName contains "vim" then
    performQuitVimHard(activeApp)
  else if processName contains "tmux" then
    performQuitTmuxHard(activeApp)
  else
    performQuit(activeApp)
  end if
end performiTerm2QuitHard

on performQuitVimHard(activeApp)
  tell application "System Events" to tell process activeApp
    # 53 = Escape
    key code 53
    keystroke ":quit!"
    # 36 = Return
    key code 36
  end tell
end performQuitVim

on performQuitTmuxHard(activeApp)
  tell application "System Events" to tell process activeApp
    # Use tmux safe kill to shut down all sessions
    # https://github.com/jlipps/tmux-safekill
    keystroke "a" using {control down}
    keystroke "c" using {shift down}
  end tell
end performQuitTmuxHard

on performQuit(activeApp)
  tell application "System Events" to tell process activeApp
    keystroke "q" using {command down}
  end tell
end performQuit
