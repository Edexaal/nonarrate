# Command Arguments

## Positional

**(folder of .rpy OR *'errors.txt'* file)**

**Accepts**:

- The folder containing your `.rpy` files. **Recommend:** `game/` folder
- The `errors.txt` file

```
MyRenpyProject/
├── game/
├── renpy/
├── launcher/
├── log.txt
├── errors.txt
├── saves/
```

**Notes:**

- If a `folder` is provided, No Narrate will operate on `.rpy` files located in subdirectories. 
- If `errors.txt` file is provided, No Narrate will attempt to fix the errors mentioned in the file.
- If `errors.txt` file is provided, **all options will be ignored!**

**Examples:**

This removes narration from *mycoolgame*

```
python nonarrate C:\mycoolgame\game
```

This fixes the errors caused by the tool.

```
python nonarrate C:\mycoolgame\errors.txt
```

- - -

## Options

### General

***—no-pauses***

Do now show narrated scenes stripped of narration.

By default, No Narrate replaces a narration with a
 [￼`pause`￼ statement](https://www.renpy.org/doc/html/quickstart.html#pause-statement). 
This allows you to see narrated scenes. To disable this feature, use this option.

***-b, --backup***

Creates a backup folder

Backup the folder before removing narration from `.rpy` files.

### Filters

#### Character/Speaker

| Commands                         | Script Example                                             | Description                                                         |
|----------------------------------|------------------------------------------------------------|---------------------------------------------------------------------|
| —no-basic-char-obj               | n = Character(“Narrator”, …)                               | Narrator saved to character object.                                 |
| —custom-basic-char-obj,<br>—cbco | d = Character(“Developer”, …)                              | Custom speaker, who acts like a narrator, saved to character object |
| —basic-char                      | “Narrator” “It was a sunny day.”                           | Simple narrator speaker                                             |
| —custom-basic-char,<br>—cbc      | “My Mind” “It would be a good idea to distract them first” | Speaker who acts like a narrator                                    |

***—no-basic-char-obj***

Do **not** remove default narrators saved to a `Character` object.

In Ren’Py, it’s recommended to define speakers in a [
`Character()`](https://www.renpy.org/doc/html/dialogue.html#defining-character-objects) object. By default, No Narrate
will remove all [[Command Arguments/Default Narrators]]. Use this option to disable this filter.

***—custom-basic-char-obj***, ***—cbco*** `<speaker name>`

Removes a speaker saved to a `Character` object.

This option completely removes the character/speaker from the game. **Multiple uses allowed!**

Sometimes, the narrator takes on the form of a character in the game. Instead of being explicitly named *Narrator*, the
narrator can introduce itself as *Emily*, *Dev* ,*The Chosen One*, or anything else…

**Example:**

This removes speakers, *Developer* & *Conscience*, from the game:

```
python nonarrate --cbco Developer --cbco Conscience C:\mycoolgame\game
```

***—basic-char***

Removes default narrators **not** in a Character object

This removes all [[Command Arguments/Default Narrators]] explicitly written alongside their dialogue. These types of
narrators are **not** saved to a `Character` object.

***—custom-basic-char***, ***—cbc*** `<speaker name>`

Removes a speaker

Removes a speaker explicitly written alongside their dialogue and**not** saved to a `Character` object. **Multiple uses
allowed!**

**Example:**

This removes speakers, *Dev* & *DaGuy*, from the game:

```
python nonarrate --cbc Dev --cbc DaGuy C:\mycoolgame\game
```

- - -

#### Dialogue

| Commands             | Script Example                                 | Description                                                                                                  |
|----------------------|------------------------------------------------|--------------------------------------------------------------------------------------------------------------|
| —no-basic-narr       | “I’m the narrator of this game”                | Dialogues without a speaker                                                                                  |
| —no-italic-narr      | mc “{i}Maybe there’s food left over.{/i}       | Italics. Thinking dialogue.                                                                                  |
| —no-parenthesis-narr | mc “(It’s got to be here somewhere.)”          | `()`. Thinking/Narrator dialogue                                                                             |
| —custom-tag, —ct     | mc “{fzs}This is a small bold font tag.{/fzs}” | [Custom text tag.](https://www.renpy.org/doc/html/custom_text_tags.html) Can be used for thoughts/narrative. |

***—no-basic-narr***

Do **not** remove dialogues that do not have a speaker

Dialogues without a speaker (blank) are a clear indication of narration. Use this option if you want to keep this form
of narration.

***—no-italic-narr***

Do **not** remove dialogues that are fully italic

Developers tend to use italics to indicate what a person is thinking about. Use this option to allow this feature.

***—no-parenthesis-narr***

Do **not** remove dialogue wrapped entirely in a parenthesis

Parentheses are used to indicate thoughts. Sometimes, it’s used for narration. Use this option to allow this feature.

***—custom-tag***, ***—ct*** `<tag name>`

Removes dialogue wrapped entirely a custom text tag

Developers can create their own [custom text tags](https://www.renpy.org/doc/html/custom_text_tags.html), providing
custom style properties to them. Use this option to remove dialogue completely surrounded by a custom text tag. *
*Multiple uses allowed!**

**Example:**

This removes dialogues wrapped with the custom text tags, `{t}` & `{fz=20}`, from the game:

```
python nonarrate --ct t --ct fz C:\mycoolgame\game
```

- - -

## Default Narrators

- thought
- thinking
- my mind
- narrator