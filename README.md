Okay a little explanation for the files here

I started off with `main.py` for initial extraction of the `[[]]` patterns.

Next is `clean.py` which got rid of some of the bloat from wikipedia

After `lowercase.py` was used to do what the name suggests 

Then `articles_to_dict.py` counts the words and turns in into a `txt` file

`clean_dict.py` cleans up the data a little more getting rid of the wikipedia meta links

All of these should be one file, it doesn't take much effort to do so but I can't really be bothered. If you are up for it throw up a PR and I'll accept it, if not I might come back to this and formalise it if I need to show this code to actual data scientists.
