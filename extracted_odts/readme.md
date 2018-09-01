
**This folder contains extracted (unzipped) copies of odt files, including:**

- ward_bulletin_template.odt
- automated ward bulletin scripts - what to work on next - Gabriel.odt

...and a stand-alone script to extract these .odt files, so that I can start to see incremental changes in these documents through git version control when I run `git diff` or `git difftool`. Seeing what xml file changes result from changes I make in the documents will also help give me better insight, understanding, and intuition on how the xml files work, what is their format, and how I can modify them to make them do what I want.

**PROCESS:**  
In order to reap the benefits of this new script I will need to get in the habit of running `python3 extract_odts.py` BEFORE every new `git add` and `git commit`. I can do this easiest by creating a git alias command to automatically call this every time I do `git status` or `git difftool`, since those are usually the commands I do just before doing `git add`. UPDATE: this isn't easily possible to override the built-in git commands such as `git status` or `git difftool` (see references 3 and 4 below). So, instead, just create some new, custom aliases for `git status`, such as `git s` and `git statuss`, and get in the habit of using one of them in place of `git status` when working in this repo.

**References for advanced git aliasing:**  
1. *****+https://www.atlassian.com/blog/git/advanced-git-aliases
2. https://stackoverflow.com/a/14994923/4561887
3. *****+https://stackoverflow.com/questions/5916565/define-git-alias-with-the-same-name-to-shadow-original-command/16410521#16410521
4. (my own question) - https://stackoverflow.com/questions/52123145/how-to-replace-internal-git-commands-such-as-git-status-with-custom-aliases

Ex of advanced an advanced git alias: this useless, but demonstrative, example turns `git gs` into an alias for `ls -l`
```
[alias]
    gs = "!f() { \
        ls -l; \
    }; f"
```

**To implement the above changes (as described in the "PROCESS" section), add the following to your local ".git/config" file *for this project:***

```
[alias]
    statuss = "!f() { \
        python3 ./extracted_odts/extract_odts.py && git status; \
    }; f"
    s = "!f() { \
        python3 ./extracted_odts/extract_odts.py && git status; \
    }; f"
```

Now, calling `git statuss` or `git s` actually calls `python3 ./extracted_odts/extract_odts.py && git status`.

Do this in place of just calling `git status` in order to always keep the extracted .odt files current with their source .odt files.
