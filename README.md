# Steno Dictionaries

This repository contains my personal stenography dictionaries, and
some non-dictionary steno-related source code for [Plover][].

Details regarding the dictionaries and source code can be found under their
respective directories (`dictionaries` and `src`).

The dictionaries are mostly in [Markdown][] format, with a bit of [JSON][] (see
[Plover Plugins section](#add-plover-plugins) for how to use Markdown
dictionaries). They either use, or are intended to supplement, Plover theory,
and _generally_ not be in conflict with
[Plover's default `main.json` dictionary][Plover main.json].

## Blog Posts

More information about these dictionaries and what led to their creation can
be found in the following blog posts I wrote:

- _[Going Platinum][]_
- _[Plover For the Record][]_

Persistent steno practice using [Typey Type][] was a massive factor in gaining
the confidence to be able to feel like I could supplement Plover entries with my
own content. I wrote about working with Typey Type here:

- _[I Completed Typey Type][]_

You can read all about the formulation of the [Doom Typist][] dictionary, and
how steno gaming is possible, here:

- _[Steno Gaming: Doom Typist][]_

## Sibling Repositories

In order to make coding a more joyous experience with steno, I take advantage of
snippets to help me write code boilerplate more quickly and flexibly. My
snippets are made with [Ultisnips][], and the repo containing them can be found
here:

-  [Vim Snippets][]

I am currently working on a Japanese language theory that can be used with
Plover, which I call _Chidori_. Some outlines in these dictionaries reference
it, and so the repo containing the dictionary can be found here:

- [Chidori][]

## Setup

### Clone repository

In your terminal program, use [Git][] to clone the repository from its home on
[Github][]:

```sh
git clone git@github.com:paulfioravanti/steno-dictionaries.git
```

### Import Dictionaries

Use Plover's Open Dictionaries functionality to choose one or more dictionaries
to import into your dictionaries list.

### Add Plover Plugins

In order for some dictionaries to work, particular [Plover Plugins][] will
need to be installed. Click the Plover Plugins Manager button on the Plover
user interface to show the list of installable plugins.

Install a plugin by selecting the plugin name from the list and clicking the
"Install/Update" button.

- [Plover 1Password][]: Needed in order to use outlines that reference secret
  entries contained in [1Password][] password vaults (translations start with
  `{:1PASSWORD:...}`)
- [Plover Cycle Translations][]: Needed in order to use outlines that enable
  multiple cycleable translations using a "selector stroke" (translations start
  with `{:CYCLE:...}`)
- [Plover Dict Commands][]: Needed in order to use outlines that enable typing
  raw steno (see my [Plover Control Commands][] dictionary)
- [Plover Layout Display][]: Needed in order to use my [Georgi][]-inspired
  [layout config][]
- [Plover Local Env Var][]: Needed in order to use personal outlines that
  contain semi-private information (translations start with `{:ENV_VAR:...}`)
- [Plover Markdown Dictionary][]: Needed in order to use any of the dictionary
  entries that are embedded in [Markdown][] files (`.md`)
- [Plover Platform Specific Translation][]: Needed in order to use outlines that
  contain multiple platform (OS) specific translations in a single outline
  definition (translations start with `{:PLATFORM:...}`)
- [Plover Q&A][]: Needed in order to use my Q&A-related outlines (translations
  start with `{:Q_AND_A:...}`)
- [Plover Run AppleScript][]: Needed in order to use commands that use
  [AppleScript][] files (translations start with `{:COMMAND:APPLESCRIPT:...}`)
- [Plover Run Shell][]: Needed to use the outlines that can control applications
  on your computer (see [`commands.md`][] for examples)
- [Plover Stitching][]: Needed to use my custom [stitching][]-related dictionary
  outlines (ie [`stitching.md`][])
- [Plover Emoji][]: Aside from the occasional few I have made custom briefs for
  in my [`emoji.md`][] dictionary, I leverage this plugin for every other
  emoji, and can recommend installing it

### Create Environment Variable

In order to use many of the outlines in [`commands.md`][], you will need to
define a `STENO_DICTIONARIES` environment variable in your `~/.bashrc` file (or
`~/.zshrc`, or whatever [configuration file][] your [shell][] uses) containing
the value of the path that this directory is in.

For example, I have my `steno-dictionaries/` directory located inside a
`steno/` directory under my user account's home directory. So, in my
`~/.bashrc` file, I have an entry that looks like:

**`~/.bashrc`**

```sh
# Enable call outs to scripts in steno command dictionaries.
export STENO_DICTIONARIES="$HOME/steno/steno-dictionaries"
```

Change the path value to wherever you have cloned this directory, and the
commands should work as expected.

### Compile Applescript Files

Outlines in dictionaries containing commands that run an [AppleScript][] file
reference compiled `.scpt` versions of the `.applescript` files contained in
this repository.

Those compiled `.scpt` files are not contained in this repository by default.
If you are using these scripts for the first time, in order to generate the
`.scpt` files, run the following script in the root directory of this repository
which will do it for you:

```sh
./bin/bootstrap
```

If you decide to make changes to the logic in the Applescript files, remember to
re-generate the `.scpt` files by running the command below to recompile them.

```sh
./bin/compile-applescript-files
```

If you want to just remove all the `.scpt` files for whatever reason, run the
following script:

```sh
./bin/remove-scpt-files
```

> For more details about the whats and whys regarding the AppleScript files in
> this repo than you would probably ever care to know about (and the pain
> suffered during their creation), see the following blog posts:
>
> - _[Sharing AppleScript Handlers][]_
> - _[AppleScript Records: Strings as Keys]_

## Hat Tips :tophat:

Inspiration for additions have been:

- [Di's steno dictionaries][]
- [Platinum Steno][] video course

## License

This project is licensed under the terms of the GNU General Public License v3.0.

See [`LICENSE.txt`][] for details.

[1Password]: https://1password.com/
[AppleScript]: https://en.wikipedia.org/wiki/AppleScript
[AppleScript Records: Strings as Keys]: https://www.paulfioravanti.com/blog/applescript-records-string-keys/
[Chidori]: https://github.com/paulfioravanti/plover-chidori
[`commands.md`]: ./dictionaries/commands.md
[configuration file]: https://en.wikipedia.org/wiki/Configuration_file
[Di's steno dictionaries]: https://github.com/didoesdigital/steno-dictionaries
[Doom Typist]: https://github.com/mmaulwurff/typist.pk3
[`emoji.md`]: ./dictionaries/emoji.md
[Georgi]: https://www.gboards.ca/product/georgi
[Going Platinum]: https://www.paulfioravanti.com/blog/going-platinum/
[Git]: https://git-scm.com/
[GitHub]: https://github.com/
[I Completed Typey Type]: https://www.paulfioravanti.com/blog/completed-typey-type/
[JSON]: https://en.wikipedia.org/wiki/JSON
[layout config]: ./etc/plover-layout-display.json
[`LICENSE.txt`]: ./LICENSE.txt
[Markdown]: https://daringfireball.net/projects/markdown/
[Platinum Steno]: https://www.youtube.com/channel/UC-bfgyMjBdFuzhuL4Ff6XqA
[Plover]: http://www.openstenoproject.org/plover/
[Plover 1Password]: https://github.com/paulfioravanti/plover-1password
[Plover Control Commands]: ./dictionaries/commands.md#plover-control-commands
[Plover Cycle Translations]: https://github.com/paulfioravanti/plover-cycle-translations
[Plover Dict Commands]: https://github.com/KoiOates/plover_dict_commands
[Plover Emoji]: https://github.com/morinted/plover_emoji
[Plover For the Record]: https://www.paulfioravanti.com/blog/plover-for-the-record/
[Plover Layout Display]: https://github.com/morinted/plover_layout_display
[Plover Local Env Var]: https://github.com/paulfioravanti/plover-local-env-var
[Plover main.json]: https://github.com/openstenoproject/plover/blob/master/plover/assets/main.json
[Plover Markdown Dictionary]: https://github.com/antistic/plover_markdown_dictionary
[Plover Platform Specific Translation]: https://github.com/paulfioravanti/plover-platform-specific-translation
[Plover Plugins]: https://github.com/openstenoproject/plover/wiki/Plugins
[Plover Q&A]: https://github.com/paulfioravanti/plover-q-and-a
[Plover Run AppleScript]: https://github.com/paulfioravanti/plover-run-applescript
[Plover Run Shell]: https://github.com/user202729/plover_run_shell
[Plover Stitching]: https://github.com/morinted/plover_stitching
[Python]: https://www.python.org/
[Sharing AppleScript Handlers]: https://www.paulfioravanti.com/blog/sharing-applescript-handlers/
[shell]: https://en.wikipedia.org/wiki/Shell_(computing)
[Steno Gaming: Doom Typist]: https://www.paulfioravanti.com/blog/steno-gaming-doom-typist/
[stitching]: http://ilovesteno.com/2015/03/12/theory-thursday-stitching/
[`stitching.md`]: ./dictionaries/stitching.md
[Typey Type]: https://didoesdigital.com/typey-type/
[Ultisnips]: https://github.com/SirVer/ultisnips
[Vim Snippets]: https://github.com/paulfioravanti/vim-snippets
