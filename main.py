from github import Github
import rich
from rich.console import Console
from rich.tree import Tree
console = Console(width=100, record=True)
username  = input("Please enter your github username: ")
gh = Github()
userdata = gh.get_user(username)
pythontreeexists = False
jstreeexists = False
javatreeexists = False
htmltreeexists = False
ctreeexists = False
cpptreeexists = False
for repo in userdata.get_repos():
    if repo.language == 'Python':
        pythontreeexists = True
    if repo.language == 'JavaScript':
        jstreeexists = True
    if repo.language == 'Java':
        javatreeexists = True
    if repo.language == 'HTML':
        htmltreeexists = True
    if repo.language == 'C':
        ctreeexists = True
    if repo.language == 'C++':
        cpptreeexists = True
roottree = Tree(f":bust_in_silhouette: {username}")
projecttree = roottree.add(":file_folder: projects")
if pythontreeexists:
    pythontree = projecttree.add(":snake: Python")
if jstreeexists:
    jstree = projecttree.add("[black on yellow]JS[/black on yellow] Javascript")
if javatreeexists:
    javatree = projecttree.add(":coffee: Java")
if htmltreeexists:
    htmltree = projecttree.add("[white on red]5[/white on red] HTML")
if ctreeexists:
    ctree = projecttree.add("[white on blue]C[/white on blue] C")
if cpptreeexists:
    cpptree = projecttree.add("[white on blue]C++[/white on blue] C++")
for repo in userdata.get_repos():
    repostring = f"{repo.name} - {repo.description}"
    if repo.language == 'Python':
        pythontree.add(repostring)
    elif repo.language == 'JavaScript':
        jstree.add(repostring)
    elif repo.language == 'Java':
        javatree.add(repostring)
    elif repo.language == 'HTML':
        htmltree.add(repostring)
    elif repo.language == 'C':
        ctree.add(repostring)
    elif repo.language == 'C++':
        cpptree.add(repostring)
    else:
        projecttree.add(repostring)
console.print(roottree)
console.save_html("README.md", inline_styles=True)