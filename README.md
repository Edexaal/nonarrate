# No Narrate - Ren'Py Mod

Removes narration and thoughts from Ren'Py visual novel games.

This is a Ren'Py tool for removing the narrator from visual novel games. It will also remove what characters are
thinking about.

## Idea

A story should unfold organically. The characters' actions, environment, and scenarios should carry the
narrative, without the need of an inner voice or overt explanation. Players are encouraged to draw their own
interpretations of the events unfolding in the story thus far.

## Types of Narration

There are 2 places to identify narration in Ren'Py:

- *Character/Speaker*
- *Dialogue*

<details>
    <summary>Ren'Py Narrator Example</summary>
    <img src="./assets/content-box.png" alt="Ren'Pys dialogue box with a narrator speaker" width="1010" height="224">
</details>

## Requirements

- Python 3.12+
- Ren'Py game with *.rpy* files

## Installation

There are multiple ways to install.

### From GitHub

```bash
> python -m pip install "nonarrate @ git+https://github.com/Edexaal/nonarrate.git"
```

### From Source Code

```bash
> git clone https://github.com/Edexaal/nonarrate.git && cd nonarrate
> python -m pip install .
```

## Usage

To use *nonarrate* check out [COMMANDS.md](./COMMANDS.md)!

## License

**nonarrate** is subject under the [Unlicense](./UNLICENSE) license.
