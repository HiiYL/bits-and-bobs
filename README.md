# Bits and Bobs

Random snippets of code for making your life easier.

## Create Project Shorcuts

Create project shortcuts is a simple util for generating command line shortcuts to your project folders.

### Example Output

* Carousell-Django will be accessible by `_cd`
* Trust will be accessible by `_tr`
* CarouGroup will be accessible by `_cg`.

The script splits project names by capital letters and underscores `_`.

### Usage

1. Edit the `project_roots` array in the script to point to the folders containing your projects.
2. Run the script `python create_project_shortcuts.py`
3. Load the generated shortcuts into your shell using `source ~/.project_shortcuts`.
4. (optional) have it added at every launch by adding `source ~/.project_shortcuts` to your `~/.bash_profile`.
