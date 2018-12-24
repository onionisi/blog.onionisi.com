Title: Vim tips
Date: 2017-10-16
Category: Blog
Tags: api, work
Slug: vim_tips

##### vim ctrl-o

when you in insert mode,
`ctrl-o` can temporarily escape insert mode without change mode

##### vim pattern match

Other than using Macro, you deserve pattern match, which is similar with sed.

```
g/^\s*$/d             # delete empty line
g/pattern/,+nd        # delete match line and after n line
g/pattern/,-nd        # delete match line and before n line
%s/^pattern//g        # delete line head in pattern       
%s/pattern$//g        # delete line tail in pattern       
```

##### vim exmode

You can do magic things under exmode.

```
Q                   enter ex mode
d, m, t             delete, move, copy
/pattern/           the line match the pattern
0, ., 1, $, %       begin, current line, first line, last line, all line
- +                 line before, line after
, ;                 line ranger, readjust current line with first number
g, g!               global, global reverse
|                   cmd separator
```

##### YCM compilation database

YCM looks for a file named compile_commands.json in the directory of the opened file or in any directory above it in the hierarchy (recursively); when the file is found, it is loaded. 

- CMake: add -DCMAKE_EXPORT_COMPILE_COMMANDS=ON when configuring (or add set( CMAKE_EXPORT_COMPILE_COMMANDS ON ) to CMakeLists.txt) and copy or symlink the generated database to the root of your project.
- Ninja: check out the compdb tool (-t compdb) in its docs.
- GNU Make: check out Bear
- Others: check out .ycm_extra_conf.py below
