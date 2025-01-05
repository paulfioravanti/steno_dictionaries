# Code Dictionary

This dictionary contains code- and programming-related outlines that _result in
text output_, as apposed to some side effect like a script running, which does
not result in any text output.

Plover's default dictionary already contains a lot of tech-related outlines,
including [shell][] commands. This dictionary does not repeat them, but only
contains new general code-related entries, as well as entries for programming
languages I use frequently.

I have found that coding with steno is _greatly_ enhanced by liberal use of
snippets. I code with [Vim][] (see my [vim commands dictionary][] for
vim-related outlines), and hence use [Ultisnips][] for all my snippets.
You find all the Ultisnips snippets I use in [Vim Snippets][] repo.

If you want to see an example of coding with steno in action, check out my
[steno coding YouTube playlist][].

<!-- vim-markdown-toc GFM -->

* [Code](#code)
* [Elixir](#elixir)
* [Elm](#elm)
* [Git](#git)
* [Heroku](#heroku)
* [HTML](#html)
* [Markdown](#markdown)
* [Ruby](#ruby)
* [Shell](#shell)

<!-- vim-markdown-toc -->

## Code

These are general code-related entries that are either not specific to a
particular language, or if they are, I don't have enough entries for them to
justify a new subheading yet.

```yaml
"*EUPLG": "img"                 # IMG
"*PGS": "{^px}"                 # PX
"*RL": "erl"                    # eRL
"-PGS": "px"                    # PX
"34*9": ">"                     # More Than
"34*9S": ">="                   # More Than or equalS
"4R*9": "<"                     # Less Than
"4R*9S": "<="                   # Less Than or equalS
"A*BG": "acc"                   # [overrides Arkansas]
"A*EPL/SKR*EUPT": "applescript" # APPLESCRIPT
"A*FBG": "asc"                  # ASC
"A*FD": "asdf"                  # [overrides avid]
"AO*ULTS": "utils"              # UTiLS (inverted L)
"AP/*L/SKR*EUPT": "applescript" # APPLESCRIPT
"AP/-L/SKR*EUPT": "applescript" # APPLESCRIPT
"EPL/EPL": "{^em}"              # EM
"EUPBG": "inc"                  # INC [override]
"H*PT": "{^http://^}"           # HTtP (inverted P) [alt]
"H-PT": "http"                  # HTtP (inverted P)
"K-PLD": "cmd"                  # CMD
"KH*R": "chr"                   # CHaRacter
"KHRAOEBLG": ":="               # CoLon EQuaL (aka walrus operator)
"KO*PBD": "cond"                # COND
"KOPBTS": "const"               # CONST (inverted T)
"KPEUFPL": "exercism"           # eXercISM
"KPREUFPL": "exercism"          # eXeRcISM
"KPWH*BG": "QMK"                # qmk
"KPWH-BG": "qmk"                # qmk
"KR*SZ": "CSS"                  # CSS
"KR-PLD": "cmd"                 # CMD
"KR-SZ": "css"                  # CSS [override]
"KW*LS": "==="                  # eQUALS
"KW-RP": "{^=\\{\\}^}{#LEFT}"   # eQUals PRop/PaRam
"KWA*EPBG": "=>"                # eQuals ANGle bracket
"KWR*PL": "yml"                 # YML (merged M&L)
"KWR*TD": "yt-dlp"              # YouTube Download (yt-dlp tool)
"KWR-TD": "yt-dlp"              # YouTube Download (yt-dlp tool)
"KWRAPL/*L": "yaml"             # YAML
"KWROEUP": "IO"                 # IO (inverted)
"O*RLS": "||="                  # OR-equaLS
"O*RLZ": "||="                  # OR-equaLS
"O*RZ": "||"                    # OR
"P*BG": "pkg"                   # PacKaGe
"P-BGS": "px"                   # [overrides People's Exhibit#G]          
"PEU": "py"                     # P(y) [overrides pi]
"PROBG": "proc"                 # PROC
"PUB/S*UB": "PubSub"            # PUBSUB
"PWRAO*UFL": "Brewfile"         # BREWFiLe
"PWRAOUFL": "Brewfile"          # BREWFiLe
"R*PL": "repl"                  # RePL
"R-PBLG": "rgba"                # RGba
"RO*BGT": "=>"                  # hashROCKeT
"S-FG": "svg"                   # [overrides SVG]
"S-FGS": "svgs"                 # [overrides SVGs]
"S-RBG": "src"                  # SRC
"SKR*SZ": "scss"                # SCSS
"SKR-SZ": "scss"                # SCSS
"SKW*L": "sql"                  # SQL
"SKWR-SZ": "js"                 # JS
"SKWRAFPB": "json"              # JSoN
"SKWROFPB": "json"              # JSON (inverted O)
"SO*EUFPB": "assign-value"      # ASSIGN Value (inverted V)
"SPH*PT": "{^smtp://^}"         # SMTP (inverted TP)
"SPH-PT": "smtp"                # SMTP (inverted TP)
"SR*BG": "src"                  # SRC
"ST*R": "str"                   # STR
"STA*RS": "**"                  # STARS (power of)
"STK*L": "DSL"                  # DSL (inverted S)
"STKWR-S": "ts"                 # TYpeScript
"STKWR-SZ": "tsx"               # TYpeScript (Z for X)
"STO*P": "tabstop"              # TabSTOP
"STP-PLT": "{^&.^}"             # (lonely operator)
"T*GT": "txt"
"T-FRP": "tmp"                  # TMP
"TA*BS": "tabstop"              # TABStop
"TAO*EUFP": "typeof"            # TYPEOF (inverted OF)
"TK*EFBG": "desc"               # DESC [override]
"TKPHRAGS": "cflags"            # CFLAGS
"TKPW*/SUB": "gsub"             # GSUB
"TPAO*E": "IIFE"                # iIFE (immediately invoked function expression) [override]
"TPH*FPB": "ENV"                # eNV (double N)
"TPH*PL": "npm"                 # [overrides New Mexico]                  
"TPH-FPB": "env"                # eNV (double N)
"TPHA*EUBGS": "¬"               # NegATION
```

## Elixir

[Elixir][]-related entries that produce straight text output. For more complex
entries, see my [Vim Snippets][] repo, specifically:

- [`elixir.snippets`][]
- [`eelixir.snippets`][]
- All the library-specific snippets under the [`elixir` directory][]

You can see some of these entries in action in:

- _[Build a real-time Twitter clone with steno using LiveView and Phoenix
  1.6][]_

```yaml
"AO*EBGS": "eex"                                                                      # [overrides objection]
"AO*EBGS/AO*EBGS": "EEx"
"AO*EBGSZ": "EEx"
"AO*EBGZ": "EEx"
"AOEBGZ": "eex"
"HAO*EBGS": "heex"
"HAOEBGZ": "heex"
"HR*EUF": "--live"
"HREUF/SRAO*U": "LiveView"
"O*EUBGS": "iex"
"O*EUBGS/PHEUBGS": "{^iex -S mix^}"                                                   # IEX MIX
"O*EUBGS/PHEUBGS/TP*GS": "{^iex -S mix phx^}"                                         # IEX MIX PHoeniX
"O*EUBGS/PHEUBGS/TP*GS/S-FR": "{^iex -S mix phx.server^}"                             # IEX MIX PHoeniX SERVER
"O*EUBGS/PHEUBGS/TP*GS/SR-FR": "{^iex -S mix phx.server^}"                            # IEX MIX PHoeniX SERVER
"O*EUBGS/PHEUBGS/TPAOEPBGS": "{^iex -S mix phx^}"                                     # IEX MIX PHOENIX
"O*EUBGS/PHEUBGS/TPAOEPBGS/S-FR": "{^iex -S mix phx.server^}"                         # IEX MIX PHOENIX SERVER
"O*EUBGS/PHEUBGS/TPAOEPBGS/SR-FR": "{^iex -S mix phx.server^}"                        # IEX MIX PHOENIX SERVER
"O*EUBGS/TP*GS": "{^iex -S mix phx^}"                                                 # IEX PHoeniX
"O*EUBGS/TP*GS/S-FR": "{^iex -S mix phx.server^}"                                     # IEX PHoeniX SerVeR
"O*EUBGS/TP*GS/SR-FR": "{^iex -S mix phx.server^}"                                    # IEX PHoeniX SerVeR
"O*EUBGS/TPAOEPBGS": "{^iex -S mix phx^}"                                             # IEX PHOENIX
"O*EUBGS/TPAOEPBGS/S-FR": "{^iex -S mix phx.server^}"                                 # IEX PHOENIX SerVeR
"O*EUBGS/TPAOEPBGS/SR-FR": "{^iex -S mix phx.server^}"                                # IEX PHOENIX SerVeR
"PHEUBGS/*EBGT/HRAOD": "{^mix ecto.load^}"
"PHEUBGS/*EBGT/HRAOD/ROEUP": "{^mix ecto.load --repo ^}{-|}"
"PHEUBGS/*EBGT/HROD": "{^mix ecto.load^}"
"PHEUBGS/*EBGT/HROD/ROEUP": "{^mix ecto.load --repo ^}{-|}"
"PHEUBGS/*EBGT/KRAET": "{^mix ecto.create^}"
"PHEUBGS/*EBGT/KRAET/ROEUP": "{^mix ecto.create --repo ^}{-|}"
"PHEUBGS/*EBGT/PHAO*EUG": "{^mix ecto.migrate^}"
"PHEUBGS/*EBGT/PHAO*EUG/ROEUP": "{^mix ecto.migrate --repo ^}{-|}"
"PHEUBGS/*EBGT/PHAO*EUG/STEP": "{^mix ecto.migrate --step ^}"
"PHEUBGS/*EBGT/PHAO*EUG/TO": "{^mix ecto.migrate --to ^}"
"PHEUBGS/*EBGT/PHAOEU/TKPWRAEUGSZ": "{^mix ecto.migrations^}"
"PHEUBGS/*EBGT/PHAOEU/TKPWRAEUGSZ/ROEUP": "{^mix ecto.migrations --repo ^}{-|}"
"PHEUBGS/*EBGT/PHAOEUG": "{^mix ecto.migrate^}"
"PHEUBGS/*EBGT/PHAOEUG/RAEUGSZ": "{^mix ecto.migrations^}"
"PHEUBGS/*EBGT/PHAOEUG/RAEUGSZ/ROEUP": "{^mix ecto.migrations --repo ^}{-|}"
"PHEUBGS/*EBGT/PHAOEUG/ROEUP": "{^mix ecto.migrate --repo ^}{-|}"
"PHEUBGS/*EBGT/PHAOEUG/STEP": "{^mix ecto.migrate --step ^}"
"PHEUBGS/*EBGT/PHAOEUG/TO": "{^mix ecto.migrate --to ^}"
"PHEUBGS/*EBGT/RAOE/SET": "{^mix ecto.reset^}"
"PHEUBGS/*EBGT/RE/SET": "{^mix ecto.reset^}"
"PHEUBGS/*EBGT/ROL/PWA*BG": "{^mix ecto.rollback^}"
"PHEUBGS/*EBGT/ROL/PWA*BG/ROEUP": "{^mix ecto.rollback --repo ^}{-|}"
"PHEUBGS/*EBGT/ROL/PWA*BG/STEP": "{^mix ecto.rollback --step ^}"
"PHEUBGS/*EBGT/ROL/PWA*BG/TO": "{^mix ecto.rollback --to ^}"
"PHEUBGS/*EBGT/SKWR*EPB": "{^mix ecto.gen^}"
"PHEUBGS/*EBGT/SKWR*EPB/PHAOEU/TKPWRAEUGS": "{^mix ecto.gen.migration ^}{MODE:SNAKE}"
"PHEUBGS/*EBGT/SKWR*EPB/PHAOEUG/RAEUGS": "{^mix ecto.gen.migration ^}{MODE:SNAKE}"
"PHEUBGS/*EBGT/SKWR*EPB/ROEUP": "{^mix ecto.gen.repo --repo ^}{-|}"
"PHEUBGS/*EBGT/SR*ET": "{^mix ecto.reset^}"
"PHEUBGS/*EBGT/TK*UPL": "{^mix ecto.dump^}"
"PHEUBGS/*EBGT/TK*UPL/ROEUP": "{^mix ecto.dump --repo ^}{-|}"
"PHEUBGS/*EBGT/TKROP": "{^mix ecto.drop^}"
"PHEUBGS/*EBGT/TKROP/ROEUP": "{^mix ecto.drop --repo ^}{-|}"
"PHEUBGS/HEBGS/OUTD": "{^mix hex.outdated^}"
"PHEUBGS/HEP/TP*GS/TPHU": "{^mix help phx.new^}"
"PHEUBGS/HEP/TPAOEPBGS/TPHU": "{^mix help phx.new^}"
"PHEUBGS/HROEL/HEBGS": "{^mix local.hex^}"
"PHEUBGS/HROEL/TP*GS": "{^mix local.phx^}"
"PHEUBGS/HROEL/TPAOEPBGS": "{^mix local.phx^}"
"PHEUBGS/KRAOEUF/STPHAUL": "{^mix archive.install}"
"PHEUBGS/KRAOEUF/STPHAUL/HEBGS/TP*GS": "{^mix archive.install hex phx_new^}"          # MIX ARCHIVE INSTALL HEX PHoeniX
"PHEUBGS/KRAOEUF/STPHAUL/HEBGS/TPAOEPBGS": "{^mix archive.install hex phx_new^}"      # MIX ARCHIVE INSTALL HEX PHOENIX
"PHEUBGS/KRAOEUF/STPHAUL/TP*GS": "{^mix archive.install hex phx_new^}"                # MIX ARCHIVE INSTALL PHoeniX
"PHEUBGS/KRAOEUF/STPHAUL/TPAOEPBGS": "{^mix archive.install hex phx_new^}"            # MIX ARCHIVE INSTALL PHOENIX
"PHEUBGS/TKEPS": "{^mix deps^}"
"PHEUBGS/TKEPS/AUPTD": "{^mix deps.update --all^}"
"PHEUBGS/TKEPS/TKPWET": "{^mix deps.get^}"
"PHEUBGS/TP*GS/ROUTS": "{^mix phx.routes}{-|}"
"PHEUBGS/TP*GS/S-FR": "{^mix phx.server^}" # PHOENIX SerVeR
"PHEUBGS/TP*GS/SKWR*EFT": "{^mix phx.digest}"
"PHEUBGS/TP*GS/SKWR*EFT/KHRAOEPB": "{^mix phx.digest.clean}"
"PHEUBGS/TP*GS/SKWR*EPB": "{^mix phx.gen^}"
"PHEUBGS/TP*GS/SKWR*EPB/A*UT": "{^mix phx.gen.auth}{-|}"
"PHEUBGS/TP*GS/SKWR*EPB/EPL/PWRED/-D": "{^mix phx.gen.embedded}{-|}"
"PHEUBGS/TP*GS/SKWR*EPB/HAOEPLT": "{^mix phx.gen.html}{-|}"
"PHEUBGS/TP*GS/SKWR*EPB/HREUF": "{^mix phx.gen.live}{-|}"
"PHEUBGS/TP*GS/SKWR*EPB/KEGT": "{^mix phx.gen.context}{-|}"
"PHEUBGS/TP*GS/SKWR*EPB/KHAPBL": "{^mix phx.gen.channel}{-|}"
"PHEUBGS/TP*GS/SKWR*EPB/PREPBS": "{^mix phx.gen.presence}{-|}"
"PHEUBGS/TP*GS/SKWR*EPB/RE/HRAOES": "{^mix phx.gen.release^}"
"PHEUBGS/TP*GS/SKWR*EPB/SERT": "{^mix phx.gen.cert}"
"PHEUBGS/TP*GS/SKWR*EPB/SKAOEPL/KWRA": "{^mix phx.gen.schema}{-|}"
"PHEUBGS/TP*GS/SKWR*EPB/SKOEUPL": "{^mix phx.gen.schema}{-|}"
"PHEUBGS/TP*GS/SKWR*EPB/SKRET": "{^mix phx.gen.secret}"
"PHEUBGS/TP*GS/SKWR*EPB/SKWRAFPB": "{^mix phx.gen.json}{-|}"
"PHEUBGS/TP*GS/SKWR*EPB/SKWROFPB": "{^mix phx.gen.json}{-|}"
"PHEUBGS/TP*GS/SKWR*EPB/SOBGT": "{^mix phx.gen.socket}{-|}"
"PHEUBGS/TP*GS/SKWR*EPB/TPHOEFR": "{^mix phx.gen.notifier}{-|}"
"PHEUBGS/TP*GS/SKWR*EPB/TPHOEUFR": "{^mix phx.gen.notifier}{-|}"
"PHEUBGS/TP*GS/SR-FR": "{^mix phx.server^}" # PHOENIX SerVeR
"PHEUBGS/TP*GS/TPHU": "{^mix phx.new}"
"PHEUBGS/TP*GS/TPHU/*EBGT": "{^mix phx.new.ecto}"
"PHEUBGS/TP*GS/TPHU/WEB": "{^mix phx.new.web}"
"PHEUBGS/TPAOEPBGS/ROUTS": "{^mix phx.routes}{-|}"
"PHEUBGS/TPAOEPBGS/S-FR": "{^mix phx.server^}" # PHOENIX SerVeR
"PHEUBGS/TPAOEPBGS/SKWR*EFT": "{^mix phx.digest}"
"PHEUBGS/TPAOEPBGS/SKWR*EFT/KHRAOEPB": "{^mix phx.digest.clean}"
"PHEUBGS/TPAOEPBGS/SKWR*EPB": "{^mix phx.gen^}"
"PHEUBGS/TPAOEPBGS/SKWR*EPB/A*UT": "{^mix phx.gen.auth}{-|}"
"PHEUBGS/TPAOEPBGS/SKWR*EPB/EPL/PWRED/-D": "{^mix phx.gen.embedded}{-|}"
"PHEUBGS/TPAOEPBGS/SKWR*EPB/HAOEPLT": "{^mix phx.gen.html}{-|}"
"PHEUBGS/TPAOEPBGS/SKWR*EPB/HREUF": "{^mix phx.gen.live}{-|}"
"PHEUBGS/TPAOEPBGS/SKWR*EPB/KEGT": "{^mix phx.gen.context}{-|}"
"PHEUBGS/TPAOEPBGS/SKWR*EPB/KHAPBL": "{^mix phx.gen.channel}{-|}"
"PHEUBGS/TPAOEPBGS/SKWR*EPB/PREPBS": "{^mix phx.gen.presence}{-|}"
"PHEUBGS/TPAOEPBGS/SKWR*EPB/RE/HRAOES": "{^mix phx.gen.release^}"
"PHEUBGS/TPAOEPBGS/SKWR*EPB/SERT": "{^mix phx.gen.cert}"
"PHEUBGS/TPAOEPBGS/SKWR*EPB/SKAOEPL/KWRA": "{^mix phx.gen.schema}{-|}"
"PHEUBGS/TPAOEPBGS/SKWR*EPB/SKOEUPL": "{^mix phx.gen.schema}{-|}"
"PHEUBGS/TPAOEPBGS/SKWR*EPB/SKRET": "{^mix phx.gen.secret}"
"PHEUBGS/TPAOEPBGS/SKWR*EPB/SKWRAFPB": "{^mix phx.gen.json}{-|}"
"PHEUBGS/TPAOEPBGS/SKWR*EPB/SKWROFPB": "{^mix phx.gen.json}{-|}"
"PHEUBGS/TPAOEPBGS/SKWR*EPB/SOBGT": "{^mix phx.gen.socket}{-|}"
"PHEUBGS/TPAOEPBGS/SKWR*EPB/TPHOEFR": "{^mix phx.gen.notifier}{-|}"
"PHEUBGS/TPAOEPBGS/SKWR*EPB/TPHOEUFR": "{^mix phx.gen.notifier}{-|}"
"PHEUBGS/TPAOEPBGS/SR-FR": "{^mix phx.server^}"                                       # PHOENIX SerVeR
"PHEUBGS/TPAOEPBGS/TPHU": "{^mix phx.new}"
"PHEUBGS/TPAOEPBGS/TPHU/*EBGT": "{^mix phx.new.ecto}"
"PHEUBGS/TPAOEPBGS/TPHU/WEB": "{^mix phx.new.web}"
"PHRAOEUP": "{^|>}"                                                                   # eLixir PIPE (plipe)
"POEUP": "{^|>}"                                                                      # elixir P(o)IPe
"TK-FP": "defp"
"TP*GS": "phx"
"TP*GSZ": "{^phx-^}"
```

## Elm

[Elm][]-related entries that produce straight text output.

```yaml
"HR*PL/AP/PHAEUBG": "{^elm-app make}"
"HR*PL/AP/PHR*EURB": "{^elm-app publish^}"
"HR*PL/AP/PW*UPL": "{^elm-app bump^}"
"HR*PL/AP/PWEULD": "{^elm-app build}"
"HR*PL/AP/R*PL": "{^elm-app repl^}"
"HR*PL/AP/RAOERBGT": "{^elm-app reactor^}"
"HR*PL/AP/SKWRAOEBGT": "{^elm-app eject}"
"HR*PL/AP/START": "{^elm-app start^}"
"HR*PL/AP/STPHAUL": "{^elm-app install^}"
"HR*PL/AP/T*ES": "{^elm-app test}"
"HR*PL/AP/TEFT": "{^elm-app test}"
"HR*PL/AP/TKEUF": "{^elm-app diff}"
"HR*PL/AP/TPH*EUPBT": "{^elm-app init^}"
"HREPL/AP/PHAEUBG": "{^elm-app make}"
"HREPL/AP/PHR*EURB": "{^elm-app publish^}"
"HREPL/AP/PW*UPL": "{^elm-app bump^}"
"HREPL/AP/PWEULD": "{^elm-app build}"
"HREPL/AP/R*PL": "{^elm-app repl^}"
"HREPL/AP/RAOERBGT": "{^elm-app reactor^}"
"HREPL/AP/SKWRAOEBGT": "{^elm-app eject}"
"HREPL/AP/START": "{^elm-app start^}"
"HREPL/AP/STPHAUL": "{^elm-app install^}"
"HREPL/AP/T*ES": "{^elm-app test}"
"HREPL/AP/TEFT": "{^elm-app test}"
"HREPL/AP/TKEUF": "{^elm-app diff}"
"HREPL/AP/TPH*EUPBT": "{^elm-app init^}"
"KR*EPL": "create-elm-app"                # CReate ElM app
"PH-FPBLG": "msg"                         # MSG
"SPH-PBLG": "msg"                         # MSG (inverted M and S)
```

## Git

[Git][] command-related entries.

```yaml
"TKPW*EUD": "{^git diff --ignore-all-space}"                                                                                      # GIt Diff
"TKPW*EUFP": "{^git add --patch}"                                                                                                 # GIt add patCH [override]
"TKPW*EUFPT": "{^git checkout --force}"                                                                                           # GIt CHeckouT (force)
"TKPW*EUFRB": "{^git stash}"                                                                                                      # GIt StaSH
"TKPW*EUFRPB": "{^git branch --delete}"                                                                                           # GIt braNCH (delete)
"TKPW*EUL": "{^git log --oneline --decorate --all --graph}"                                                                       # GIt Log
"TKPW*EULG": "{^git log --oneline --decorate --all --graph}"                                                                      # GIt LoG
"TKPW*EUP": "{^git push --force}"                                                                                                 # GIt Push (force) [override]
"TKPW*EUP/O*RPBLG/PWRA*FRPB": "{^git push --force origin $(git symbolic-ref HEAD --short)}"                                       # GIt Push (force) ORIGIN (current BRANCH name)
"TKPW*EUPL": "{^git pull --rebase}"                                                                                               # GIt PuLL (rebase) [override]
"TKPW*EUPL/O*RPBLG/PHAEUPB": "{^git pull --rebase origin main}"                                                                   # GIT PULL (rebase) ORIGIN MAIN
"TKPW*EUPL/O*RPBLG/PHAFRT": "{^git pull --rebase origin master}"                                                                  # GIT PULL (rebase) ORIGIN MASTER
"TKPW*EUPL/O*RPBLG/PWRAFRPB": "{^git pull --rebase origin $(git symbolic-ref HEAD --short)}"                                      # GIT PULL (rebase) ORIGIN (current BRANCH name)
"TKPW*EUPL/STPRAOEPL/PHAEUPB": "{^git pull --rebase upstream main}"                                                               # GIT PULL (rebase) uPSTREAM MAIN
"TKPW*EUPL/STPRAOEPL/PHAFRT": "{^git pull --rebase upstream master}"                                                              # GIT PULL (rebase) uPSTREAM MASTER
"TKPW*EUPL/STPRAOEPL/PWRAFRPB": "{^git pull --rebase upstream $(git symbolic-ref HEAD --short)}"                                  # GIT PULL (rebase) uPSTREAM (current BRANCH name)
"TKPW*EUPLT": "{^git commit --amend}"                                                                                             # GIt coMMiT (amend)
"TKPW*EUPLTD": "{^git commit --amend --no-edit}"                                                                                  # GIt coMMiT (amend) no-eDit
"TKPW*EURBS": "{^git rebase --interactive}"                                                                                       # Git ReBaSe (interactive)
"TKPW*EURPL": "{^git rm --force}"                                                                                                 # GIt RM (force)
"TKPW*EURPLT": "{^git remote --verbose}"                                                                                          # GIt ReMoTe (verbose)
"TKPW*EUTD": "{^git add .}"                                                                                                       # GIT aDD (current pathspec)
"TKPW*EUTS": "{^git status --short}"                                                                                              # GIT Status (short)
"TKPW*URB": "{^git stash push}"                                                                                                   # Git stash pUSH
"TKPWA*FP": "{^git add --patch}"                                                                                                  # Git Add patCH
"TKPWAO*EB": "{^git rebase --abort}"                                                                                              # Git rEBase abort
"TKPWAOEB": "{^git rebase}"                                                                                                       # Git rEBase
"TKPWAOEBT": "{^git rebase --continue}"                                                                                           # Git rEBase conTinue
"TKPWEUD": "{^git diff}"                                                                                                          # GIt Diff
"TKPWEUFP": "{^git add --patch}"                                                                                                  # GIt add patCH [override]
"TKPWEUFPT": "{^git checkout}"                                                                                                    # GIt CHeckouT
"TKPWEUFPT/PW*": "{^git checkout -b ^}{MODE:LOWER}{MODE:SET_SPACE:-}}"                                                            # GIt CHeckouT Branch
"TKPWEUFPT/PWRAFRPB": "{^git checkout -b ^}{MODE:LOWER}{MODE:SET_SPACE:-}"                                                        # GIt CHeckouT BRANCH
"TKPWEUFPTD": "{^git checkout -b ^}{MODE:LOWER}{MODE:SET_SPACE:-}"                                                                # GIt CHeckouT (branch)
"TKPWEUFRB": "{^git stash}"                                                                                                       # GIt StaSH
"TKPWEUFRPB": "{^git branch --list --verbose}"                                                                                    # GIt braNCH
"TKPWEUP": "{^git push}"                                                                                                          # GIt Push
"TKPWEUP/TAGS": "{^git push --tags}"                                                                                              # GIt Push TAGS
"TKPWEUP/O*RPBLG/PWRAFRPB": "{^git push origin $(git symbolic-ref HEAD --short)}"                                                 # GIT PUSH ORIGIN (current BRANCH name)
"TKPWEUPBT": "{^git init}"                                                                                                        # GIt iNiT
"TKPWEUPL": "{^git pull}"                                                                                                         # GIt PuLL [override]
"TKPWEUPL/O*RPBLG/PHAEUPB": "{^git pull origin main}"                                                                             # GIt PuLL ORIGIN MAIN
"TKPWEUPL/O*RPBLG/PHAFRT": "{^git pull origin master}"                                                                            # GIt PuLL ORIGIN MASTER
"TKPWEUPL/O*RPBLG/PWRAFRPB": "{^git pull origin $(git symbolic-ref HEAD --short)}"                                                # GIt PuLL ORIGIN (current BRANCH name)
"TKPWEUPL/STPRAOEPL/PHAEUPB": "{^git pull upstream main}"                                                                         # GIt PuLL uPSTREAM MAIN
"TKPWEUPL/STPRAOEPL/PHAFRT": "{^git pull upstream master}"                                                                        # GIt PuLL uPSTREAM MASTER
"TKPWEUPL/STPRAOEPL/PWRAFRPB": "{^git pull upstream $(git symbolic-ref HEAD --short)}"                                            # GIt PuLL uPSTREAM (current BRANCH name)
"TKPWEUPLT": "{^git commit --message=\"\"^}{#LEFT}{-|}"                                                                           # GIt coMMiT (message)
"TKPWEUPLTD": "{^git commit --all --message=\"\"^}{#LEFT}{-|}"                                                                    # GIt coMMiT (all, message)
"TKPWEURBS": "{^git rebase}"                                                                                                      # Git ReBaSe
"TKPWEURBS/PWORT": "{^git rebase --abort}"                                                                                        # Git ReBaSe ABORT
"TKPWEURBS/T-PB": "{^git rebase --continue}"                                                                                      # Git ReBaSe CONTINUE
"TKPWEURPBLG": "{^git merge}"                                                                                                     # GIt meRGe
"TKPWEURPL": "{^git rm}"                                                                                                          # GIt RM
"TKPWEURPLT": "{^git remote}"                                                                                                     # GIt ReMoTe
"TKPWEUT/A*D": "{^git add .}"                                                                                                     # GIT ADd (current pathspec)
"TKPWEUT/AD/AD": "{^git add .}"                                                                                                   # GIT ADD (current pathspec)
"TKPWEUT/AD/PAFP": "{^git add --patch}"                                                                                           # GIT ADD PATCH
"TKPWEUT/HRO*G": "{^git log --oneline --decorate --all --graph}"                                                                  # GIT LOG (oneline decorate all graph)
"TKPWEUT/HROG": "{^git log}"                                                                                                      # GIT LOG
"TKPWEUT/KHO*UT": "{^git checkout --force}"                                                                                       # GIT CHECKOUT force
"TKPWEUT/KHOUT/PW*": "{^git checkout -b ^}{MODE:LOWER}{MODE:SET_SPACE:-}"                                                         # GIT CHECKOUT Branch
"TKPWEUT/KHOUT/PWRAFRPB": "{^git checkout -b ^}{MODE:LOWER}{MODE:SET_SPACE:-}"                                                    # GIT CHECKOUT BRANCH
"TKPWEUT/KHOUT/TPORS": "{^git checkout --force}"                                                                                  # GIT CHECKOUT FORCE
"TKPWEUT/KHR*UP": "{^git branch --merged | grep --invert-match '\\*\\|master\\|develop\\|main' | xargs -n 1 git branch --delete}" # GIT CLEANUP
"TKPWEUT/KPH*EUPLT": "{^git commit --message=\"\"^}{#LEFT}{-|}"                                                                   # GIT CoMMIT Message
"TKPWEUT/KPH*EUT": "{^git commit --amend}"                                                                                        # GIT CoMMIT (amend)
"TKPWEUT/KPH*EUTD": "{^git commit --amend --no-edit}"                                                                             # GIT CoMMIT (amend) no-eDit
"TKPWEUT/KPHEUFPLT": "{^git commit --message=\"\"^}{#LEFT}{-|}"                                                                   # GIT CoMMIT Message
"TKPWEUT/KPHEUPLT": "{^git commit --message=\"\"^}{#LEFT}{-|}"                                                                    # GIT CoMMIT Message
"TKPWEUT/KPHEUT": "{^git commit}"                                                                                                 # GIT CoMMIT
"TKPWEUT/KPHEUT/APLD": "{^git commit --amend}"                                                                                    # GIT CoMMIT AMEND
"TKPWEUT/KPHEUT/APLD/TPHO*ETD": "{^git commit --amend --no-edit}"                                                                 # GIT CoMMIT AMEND NO EDIT
"TKPWEUT/KPHEUT/APLD/TPHO/ETD": "{^git commit --amend --no-edit}"                                                                 # GIT CoMMIT AMEND NO EDIT
"TKPWEUT/KPHEUT/PHEPBLG": "{^git commit --message=\"\"^}{#LEFT}{-|}"                                                              # GIT CoMMIT MESSAGE
"TKPWEUT/KWREUT": "{^git init}"                                                                                                   # GIT InIT
"TKPWEUT/P*UL": "{^git pull --rebase}"                                                                                            # GIT PULL (rebase)
"TKPWEUT/P*UL/O*RPBLG/PHAEUPB": "{^git pull --rebase origin main}"                                                                # GIT PULL (rebase) ORIGIN MAIN
"TKPWEUT/P*UL/O*RPBLG/PHAFRT": "{^git pull --rebase origin master}"                                                               # GIT PULL (rebase) ORIGIN MASTER
"TKPWEUT/P*UL/O*RPBLG/PWRAFRPB": "{^git pull --rebase origin $(git symbolic-ref HEAD --short)}"                                   # GIT PULL (rebase) ORIGIN (current BRANCH name)
"TKPWEUT/P*UL/STPRAOEPL/PHAEUPB": "{^git pull --rebase upstream main}"                                                            # GIT PULL (rebase) uPSTREAM MAIN
"TKPWEUT/P*UL/STPRAOEPL/PHAFRT": "{^git pull --rebase upstream master}"                                                           # GIT PULL (rebase) uPSTREAM MASTER
"TKPWEUT/P*UL/STPRAOEPL/PWRAFRPB": "{^git pull --rebase upstream $(git symbolic-ref HEAD --short)}"                               # GIT PULL (rebase) uPSTREAM (current BRANCH name)
"TKPWEUT/P*URB": "{^git push --force}"                                                                                            # GIT PUSH (force)
"TKPWEUT/P*URB/O*RPBLG/PWRAFRPB": "{^git push --force origin $(git symbolic-ref HEAD --short)}"                                   # GIT PUSH (force) ORIGIN (current BRANCH name)
"TKPWEUT/PHERPBLG/STPRAOEPL/PHAEUPB": "{^git merge upstream/main}"                                                                # GIT MERGE uPSTREAM MAIN
"TKPWEUT/PHERPBLG/STPRAOEPL/PHAFRT": "{^git merge upstream/master}"                                                               # GIT MERGE uPSTREAM MASTER
"TKPWEUT/PUL": "{^git pull}"                                                                                                      # GIT PULL
"TKPWEUT/PUL/O*RPBLG/PHAEUPB": "{^git pull origin main}"                                                                          # GIT PULL ORIGIN MAIN
"TKPWEUT/PUL/O*RPBLG/PHAFRT": "{^git pull origin master}"                                                                         # GIT PULL ORIGIN MASTER
"TKPWEUT/PUL/O*RPBLG/PWRAFRPB": "{^git pull origin $(git symbolic-ref HEAD --short)}"                                             # GIT PULL ORIGIN (current BRANCH name)
"TKPWEUT/PUL/STPRAOEPL/PHAEUPB": "{^git pull upstream main}"                                                                      # GIT PULL uPSTREAM MAIN
"TKPWEUT/PUL/STPRAOEPL/PHAFRT": "{^git pull upstream master}"                                                                     # GIT PULL uPSTREAM MASTER
"TKPWEUT/PUL/STPRAOEPL/PWRAFRPB": "{^git pull upstream $(git symbolic-ref HEAD --short)}"                                         # GIT PULL uPSTREAM (current BRANCH name)
"TKPWEUT/PURB": "{^git push}"                                                                                                     # GIT PUSH
"TKPWEUT/PURB/O*RPBLG/PWRA*FRPB": "{^git push --force origin $(git symbolic-ref HEAD --short)}"                                   # GIT PUSH (force) ORIGIN (current BRANCH name)
"TKPWEUT/PURB/O*RPBLG/PWRAFRPB": "{^git push origin $(git symbolic-ref HEAD --short)}"                                            # GIT PUSH ORIGIN (current BRANCH name)
"TKPWEUT/PWHRA*EUPL": "{^git blame -wM}"                                                                                          # GIT BLAME (-w ignore whitespace, -M find line movements)
"TKPWEUT/PWRA*FRPB": "{^git branch --verbose}"                                                                                    # GIT BRANCH (verbose)
"TKPWEUT/PWRAFRPB/SROEBS": "{^git branch --verbose}"                                                                              # GIT BRANCH VERBOSE
"TKPWEUT/R*PL": "{^git rm --force}"                                                                                               # GIT RM (force)
"TKPWEUT/R-PL": "{^git rm}"                                                                                                       # GIT RM
"TKPWEUT/RAOEBS": "{^git rebase}"                                                                                                 # GIT REBase
"TKPWEUT/RAOEBS/PWORT": "{^git rebase --abort}"                                                                                   # GIT REBase ABORT
"TKPWEUT/RAOEBS/T-PB": "{^git rebase --continue}"                                                                                 # GIT REBase CONTINUE
"TKPWEUT/RAOEBS/TPHRAF": "{^git rebase --interactive}"                                                                            # GIT REBase INTERACTIVE
"TKPWEUT/RAOEPLT": "{^git remote --verbose}"                                                                                      # GIT REMOTE verbose
"TKPWEUT/ST*TS": "{^git status}"                                                                                                  # GIT STATUS
"TKPWEUT/ST-TS": "{^git status --short}"                                                                                          # GIT STATUS (short)
"TKPWEUT/STARB": "{^git stash}"                                                                                                   # GIT STASH
"TKPWEUT/STARB/POP": "{^git stash pop}"                                                                                           # GIT STASH POP
"TKPWEUT/STARB/PURB": "{^git stash push}"                                                                                         # GIT STASH PUSH
"TKPWEUT/TK*EUF": "{^git diff --ignore-all-space}"                                                                                # GIT DIFF (ignore all space)
"TKPWEUT/TKEUF": "{^git diff}"                                                                                                    # GIT DIFF
"TKPWEUT/TKPEUG/HR*EUS": "{^git config --list}"                                                                                   # GIT CONFIG LIST
"TKPWEUT/TPH*EUT": "{^git init}"                                                                                                  # GIT iNIT
"TKPWEUTD": "{^git add}"                                                                                                          # GIT aDD
"TKPWO*P": "{^git stash pop}"                                                                                                     # Git stash pOP
"TKPWOP": "{^git stash pop}"                                                                                                      # Git stash pOP
```

## Heroku

Entries for [Heroku][]-related commands.

```yaml
"HERBG/AD/RE/TKEUS": "{^heroku addons:create heroku-redis:hobby-dev^}"
"HERBG/RUPB/RAEUBG/TK-B/PHAO*EUG": "{^heroku run rake db:migrate^}"
"HERBG/RUPB/RAEUBG/TK-B/PHAOEUG": "{^heroku run rake db:migrate^}"
``` 

## HTML

[HTML][]-related entries that produce straight text output. See [my HTML
snippets][] for more complex tag usage.

```yaml
"H-R": "{^<hr />^}"
"KPW-D": "kbd"
"PWR*": "{^<br />^}"
```

## Markdown

Entries related to [Markdown][].

```yaml
"-6G": "{^###### ^}{-|}"
"1-G": "{^# ^}{-|}"
"2-G": "{^## ^}{-|}"
"3-G": "{^### ^}{-|}"
"4-G": "{^#### ^}{-|}"
"5G": "{^##### ^}{-|}"
"KH*FG": "{^`}"
"KH-FG": "{^`^}"
"KW*T": "{^> ^}{-|}"
"PR*FB": "{^`}"
"PR-FB": "{^`^}"
"PWHR*T": "{^+ ^}{-|}" # BuLLeT
"PWHR-T": "{^- ^}{-|}" # BuLLeT
"SKH*FGS": "{^```^}"
"SKH-FGS": "{^```^}"
"SKPH": "{^\\^}"
"SKPH*": "{^\\^}"
"SKPR*FBGS": "{^```^}"
"SKPR-FBGS": "{^```^}"
"WH*FB": "{^`}"
"WH-FB": "{^`^}"
```

## Ruby

[Ruby][]-related entries that produce straight text output. For more complex
entries, see my [Vim Snippets][] repo, specifically:

- [`ruby.snippets`][]
- [`eruby.snippets`][]
- [`rails.snippets`][]
- All the other specific snippets under the [`ruby` directory][]

You can see some of these entries in action in:

- _[Rails 7: The Steno Demo][]_

```yaml
"*ERB": "erb"
"*ERB/KHROES": "{^%>^}"                           # ERB CLOSE
"*ERB/KPEBG/OEP": "{^<%=^}"                       # ERB EXEC OPEN
"*ERB/OEP": "{^<%}"                               # ERB OPEN
"*ERB/TA*G": "{^<%=  %>^}{#LEFT LEFT LEFT}{^}"
"EUPL/PORT/PHA*P": "{^bin/importmap}"             # imPORTMAP (Rails)
"KW-P": "{^= _^}"                                 # eQUals Previous statement (use in rails console)
"KWUPBD": "{^= _^}"                               # eQUals UNDerscore (use in rails console)
"PRO*RT/PHA*P": "{^bin/importmap}"                # imPORTMAP (rails)
"PWUPBLD/HROBG/AD/PHRORPL": "{^bundle lock --add-platform^}"
"PWUPBLD/HROBG/AD/PHRORPL/HROEUPBGS": "{^bundle lock --add-platform x86_64-linux^}"
"R-B": "rb"
"RA*RT": "attr"                                   # (r)ATTR
"RA*RT/RAERD": "attr_reader"
"RA*RT/SESZ": "attr_accessor"
"RA*RT/WREUR": "attr_writer"
"RAEUBG/TA*EFBGS": "{^bin/rake --tasks^}"
"RAEULS/*BGS/TEGT/STPHAUL": "{^bin/rails action_text:install^}"
"RAEULS/ROUTS": "{^bin/rails routes^}"
"RAEULS/S-FR": "{^bin/rails server^}"
"RAEULS/SKO*EL": "{^bin/rails console^}"          # COnSOLE
"RAEULS/SKO*L": "{^bin/rails console^}"           # COnSOLE
"RAEULS/SKWRAEUT": "{^bin/rails generate}"
"RAEULS/SR-GS": "{^rails --version^}"             # RAILS VerSION
"RAEULS/STKO*EL": "{^bin/rails dbconsole^}"       # DbCOnSOLE
"RAEULS/TEFT": "{^bin/rails test^}"
"RAEULS/TK-B/KRAET": "{^bin/rails db:create}"
"RAEULS/TK-B/PHAO*EUG": "{^bin/rails db:migrate}" # MIGrate
"RAEULS/TK-B/PHAOEUG": "{^bin/rails db:migrate}"  # MIGrate
"RAEULS/TK-B/S-PL/KHAEUPBG": "{^bin/rails db:system:change --to=^}{>}"
"RAEULS/TK-B/SAOED": "{^bin/rails db:seed^}"
"RAEULS/TK-B/STUP": "{^bin/rails db:setup^}"
"RAEULS/TPHU": "{^rails new}"                     # RAILS NEW
"RAO*UB/SR-GS": "{^ruby --version^}"              # RUBY VerSION
"SKWREFL": "Gemfile"                              # GEmFile
"SKWREFPL": "Gemfile"                             # GEMFile
"SKWREPL/TPAO*EUL": "Gemfile"
"SPREBG": "rspec"
"TKA*EUBS": "{--database=^}"                      # DAtaBaSe
"TKPWA*EUS": "{--database=^}"                     # DataBASE [override]
"TR*": "attr"                                     # atTR
```

## Shell

[Shell Script][]-related entries that produce straight text output.

```yaml
"A*FD/HR*EUS/AUL": "{^asdf list-all}"
"EPBD/*F": "endif"
"HRES/TAEUP/TAEUP": "less +F ~/Library/Application\\ Support/plover/tapey_tape.txt" # LESS TAPEy TAPE (realtime feed)
"KR*D/PR-PB": "{^cd ..^}"                                                           # Change Directory to PareNt
"KR*D/PR-PBT": "{^cd ..^}"                                                          # Change Directory to PareNT
"KR*D/UP": "{^cd ..^}"                                                              # Change Directory UP a level
"KR-P/R*": "{^cp -r}"                                                               # CP -R
"KR-RP": "{^cp -r}"                                                                 # CP -R (r inverted)
"KRAO*EBGT": "create-react-app"                                                     # CReate rEaCT app
"KRAOEBGT": "create-react-app"                                                      # CReate rEaCT app
"PHUBGS": "mux"                                                                     # MUX
"PW*G": "{^bg^}"                                                                    # BG
"R*/KUP": "rcup"                                                                    # RCUP
"R-PL/R-F": "{^rm -rf}"
"R-PL/TK*EUR": "{^rmdir}"
"S*ED": "sed"                                                                       # sed [override]
"S*RB": "zsh"
"TKHR*": "--download"
"TKPWH": "gh"                                                                       # (GitHub CLI)
"TP-G": "{^fg^}"
"TPH*PGS": "npx"                                                                    # NPX (GS to make X)
"TPH*PGS/KRAO*EBGT": "{^npx create-react-app}"                                      # NPX CReate rEaCT app
"TPH*PGS/KRAOEBGT": "{^npx create-react-app}"                                       # NPX CReate rEaCT app
"TPHUBGS": "tmux"
"W*GT": "wget"
```

[Build a real-time Twitter clone with steno using LiveView and Phoenix 1.6]: https://www.youtube.com/watch?v=T_kMd7rxYU0
[Elixir]: https://elixir-lang.org/
[Elm]: https://elm-lang.org/
[`eelixir.snippets`]: https://github.com/paulfioravanti/vim-snippets/blob/main/vim/UltiSnips/eelixir.snippets
[`eruby.snippets`]: https://github.com/paulfioravanti/vim-snippets/blob/main/vim/UltiSnips/eruby.snippets
[`elixir` directory]: https://github.com/paulfioravanti/vim-snippets/blob/main/vim/UltiSnips/elixir
[`elixir.snippets`]: https://github.com/paulfioravanti/vim-snippets/blob/main/vim/UltiSnips/elixir.snippets
[Git]: https://git-scm.com/
[Heroku]: https://www.heroku.com/
[HTML]: https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/HTML_basics
[Markdown]: https://daringfireball.net/projects/markdown/syntax
[my dotfiles]: https://github.com/paulfioravanti/dotfiles/tree/master/vim/UltiSnips
[my HTML snippets]: https://github.com/paulfioravanti/dotfiles/blob/master/vim/UltiSnips/html.snippets
[`rails.snippets`]: https://github.com/paulfioravanti/vim-snippets/blob/main/vim/UltiSnips/rails.snippets
[Rails 7: The Steno Demo]: https://www.youtube.com/watch?v=q7g0ml60LGY
[Ruby]: https://www.ruby-lang.org/en/
[`ruby` directory]: https://github.com/paulfioravanti/vim-snippets/blob/main/vim/UltiSnips/ruby
[`ruby.snippets`]: https://github.com/paulfioravanti/vim-snippets/blob/main/vim/UltiSnips/ruby.snippets
[shell]: https://en.wikipedia.org/wiki/Shell_(computing)
[Shell Script]: https://en.wikipedia.org/wiki/Shell_script
[steno coding YouTube playlist]: https://www.youtube.com/playlist?list=PLNN5NpKrqwAMRA5uRGtGzwUDgzHFDk8Z4
[Ultisnips]: https://github.com/SirVer/ultisnips
[Vim]: https://www.vim.org/
[vim commands dictionary]: ./commands.md#vim
[Vim Snippets]: https://github.com/paulfioravanti/vim-snippets
