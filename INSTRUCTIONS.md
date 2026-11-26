# Instructions

This section explains how to use nonarrate effectively **step-by-step**.

## 1.) Extract .rpa files

***This is an optional step**. If your game project does not have an `*.rpa` file located in the `game/` folder, skip
ahead.

`.rpa` files usually contain all assets to a game project. Nonarrate will _only_ operate on `.rpy` files,
which may be contained inside an `rpa` file. To get assets, you will need to extract the `rpa` file(s).

> [!TIP]
> Nonarrate only needs `rpy` files. So, extract `rpa` files that might contain `rpy` files.

There are many extractor tools you can use for this. Happy Hunting!

## 2.) Dialogue searching

Once you have access to the `.rpy` files in your `game/` folder, the next step is to search for files containing
**character definitions** and/or **dialogue**. _Keep note of these files!_

### 2a.) Character Definitions

Speaker names are most often saved to a `Character(...)` object.
**Any `.rpy` file containing character definitions are a _must_ for nonarrate.**

**Examples:**

- See [Ren'Py Docs Examples](https://www.renpy.org/doc/html/dialogue.html#example-characters)
- See [The `character` Store Examples](https://www.renpy.org/doc/html/dialogue.html#the-character-store)

```python
define h = Character("Harold")
default m = Character("Mikaeil", what_italic=True)
define character.robby = Character("Robby")
```

### 2b.) Say Dialogue

**Any `.rpy` file containing dialogue is a _must_ for nonarrate.**

**Examples:**

- See ['Say Statement' in Ren'Py's Docs](https://www.renpy.org/doc/html/dialogue.html#say-statement)

```renpy
"This is narration."

"Eileen" "This is dialogue, with an explicit character name."

elly "This is dialogue, using a character object instead."

"Bam!!" with vpunch
```

## 3.) Using nonarrate

Once you find which `.rpy` files contain **character definitions** and **dialogue**, you can now use nonarrate.

> [!TIP]
> Use `--backup` alongside your commands to create backups of modified `.rpy` files.
> If something goes wrong, you can now use `--restore` to revert back to the files' original state.

**Example:**

```bash
# Start in game/ directory
# Do not touch files named 'minigame' and 'opt'.
# Keep dialogue that match the following syntax -> "" "Here is my dialogue"
# Backup files before removing narration
nonarrate game/ --invalid-files minigame opt --keep-empty-quoted-chars --backup
```

### 3a.) Ignoring files

Take advantage of the [FILE COMMANDS](./COMMANDS.md#file-searching) options to tell nonarrate what files/folders to ignore or focus
on.

There are 2 workflows for ignoring files/folders:

- `--valid-*` --> _(`--valid-dirs`,`--valid-files`,`--valid-globs`)_
- `invalid-*` --> _(`--invalid-dirs`,`--invalid-files`,`--invalid-globs`)_

#### 3aa.) Invalid Options Workflow

Nonarrate will ignore certain files/folders by default. See [IGNORED_FILES.md](./IGNORED_FILES.md)
for list of ignored files/folders. This is also the default workflow for nonarrate if `--invalid-*` and `--valid-*` options are not used.

This workflow consists of you telling nonarrate what files/folders to ignore because there are no **character definitions** or **dialogue** present.

**Example:**

```bash
nonarrate game/ --invalid-dirs images sfx --invalid-files red_shaders minigames --backup
```

#### 3ab.) Valid Opions Workflow

Nonarrate will ignore _all_ files/folders by default.

You must explicitly tell nonarrate what files/folders it can enter/look at.

> [!TIP]
> `--valid-*` options _completely_ ignores all entries from [IGNORED_FILES.md](./IGNORED_FILES.md).
> You can validate _any_ files/folders.

**Example:**

```bash
nonarrate game/ --valid-dirs scripts dlc chapter1 chapter2 chapter3 --valid-files script outside home intro --valid-globs day_*
```

### 3b.) Adjusting Narration

Sometimes, the default settings is not enough or maybe _too_ much. Regardless, take advantage of
[Narrator Filter options](./COMMANDS.md#narrator-filters). Most often than not, simply enabling, `--keep-empty-quoted-chars` or
using `--text-tags <tags..>` to remove dialogue with certain tag names is all you need!

Additionally, pay attention to the tables provided in [COMMANDS.md](./COMMANDS.md#narrator-filters). They will help you!

## 4.) Error Fixing

***This is an optional step**. In your case, the game may run smoothly. If so, you're done! Otherwise, continue reading this section.

When launching the game, an error screen will appear showing all the issues caused by nonarrate. Don't fret! This is
normal behavior. nonarrate comes with error fixing capabilities. Not all types of errors will be fixed. Check
out [ERROR_TYPES](./ERROR_TYPES.md) for eligible types.

To fix errors, point nonarrate to Ren'Py's auto-generated `errors.txt` file.

**Example:** `nonarrate ./errors.txt`

From here, there are 2 workflows you can use to reload the game:

1. _(recommended)_ Keep error screen open and just select the `Reload` button
2. Close error screen and reopen game

Repeat these steps until the game is launched successfully!

## Final Thoughts

The key is finding files containing dialogue and adjusting nonarrate's settings to fit the current game's needs.
Every game project is different after all!
