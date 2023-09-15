### Basic Concepts
 - **Version control system**:
	 - Stores source code files for a project in a central place
		 - Allows multiple developers to work on the same code base in a controlled way
	 - Keeps a record of changes made to source code files over time
		 - Recall any version of a file based on a date or version number
	 - Allows you to maintain multiple, concurrent releases of your software
		 - ie. the *mainline* (or *trunk*) plus one or more *branch releases*
 - **Repository**: Place where source code files for projects are stored
	 - Will contain *all* versions of the files (stored as differences)
	 - Is usually network accessible
	 - You should also store non-code project artifacts such as:
		 - Makefiles
		 - External documentation (analysis, design, etc)
	 - Best not to store generated artifacts
		 - Object code, executable, javadoc output, etc
 - **Workspace**: The place where you work on a copy of a project's files
	 - Files in the repository are not directly changed, you work on a local copy
 - **Checking Out**: Populates your workspace with up-to-date copies of files and directories from the repository
 - **Committing**: Saves your changes back into the repository
	 - Sometimes called *checking in*
	 - The repository keeps track of changes using revision numbers
		 - You can also comment the change
 - **Updating**: Repopulates your workspace with the latest versions of files
	 - Useful when other developers are also working concurrently on the same project
 - **Version Number**: Each version of a file (or a set of files) is given a unique *revision number*
	 - In SVN (subversion):
		 - 1 for the initial revision
		 - 2, 3, etc. for subsequent committed versions
	 - Is time stamped and can be commented
 - **Tag**: Allows you to name a particular revision of your project (or particular directories or subsets of files)
	 - Eg: `PreRelease1` might tag revision 34 of `file1.c`, revision 27 of `file2.c`, etc
	 - Checking out using the tag retrieves the same set of files despite subsequent revisions
 - **Branch**: A separate independent line of development
	 - Is like a separate repository for the same project
	 - Allows parallel development on the same code base
	 - Useful for creating a *release branch*
 - **Merging**: Allows you to apply changes made in a release branch back into the mainline (bug fixes)
 - **Conflicts**: Multiple developers editing the same file can lead to conflicts
	 - *Strict Locking* allows only one person at a time to have write access to the file
	 - SVN (usually) uses *optimistic locking*
		 - If you try to commit a shared file, you are forced to update the file first
		 - SVN merges changes from other developers into the working copy
		 - With no conflicts you can commit the file, otherwise you must manually resolve the conflicts
 - You can:
	 - Retrieve a specific revision of a file or set of files (a directory or project)
	 - List the differences between revisions
	 - Retrieve all source code as it appeared at some date in the past
 - Normally, developers work on the same shared code base for a project
	 - Called the *mainline* or *trunk*

### Working With SVN
 - Short for subversion
 - Download and manuals available at: `subversion.apache.org`
	 - `svn --version` (or `svnadmin --version`)
 - There are several GUI frontends to SVN (most are not free)
	 - May be integrated into an IDE
**Initial setup**:
 - Create a repository in your account on the local file system 
```
mkdir /home/alexste/repo
svnadmin create /home/alexste/repo
```
 - Do not directly change the files in this directory
	 - Always use `svn` or `svnadmin` commands
 - Note the repository URL
	 - `file:///home/alexste/repo`
 - Create your project:
	 - Decide on a name (in examples: `panther`)
	 - Create some initial source code files in a **temporary directory** (`file1.c`, `file2.c`)
	 - Import the files into the repository (from the temp directory):
	   `svn import -m "initial import" . file:///home/alexste/repo/panther/trunk`
	   `svn import -m <log message> <files> <repo URL>/<project name>/trunk`
**Typical Daily Workflow**:
 - Create a workspace directory:
   `mkdir ~/work && cd ~/work`
 - Check out the project:
   `svn co file:///home/alexste/repo/panther/trunk panther`
 - Change into the project subdirectory
   `cd panther`
 - Make changes to the files
	 - Use `status` to give the current state of the files
	   `svn status *.c`
	 - Should indicate they are "locally modified" (`M`)
	 - Use `diff` to show the differences between the local copy and the repository version
	   `svn diff file1.c`
 - Commit the changes to the repository
   `svn commit -m "Commit message"`
	 - Use `log` to see the history of a file
	   `svn log file2.c`
 - Use `update` to refresh the files and directories in the workspace 
   `svn update`
	 - Necessary if working in a multi-person project, or if you deleted local copies
 - Repeat the last 3 steps as needed
**Other useful commands**:
 - Use `add` to add new directories and files to the repository
   `mkdir mathlib`
   `svn add mathlib`
   `cd mathlib`
   `# create and edit file math.c`
   `svn add math.c`
   `svn commit -m "new math stuff"`
 - Use `delete` to remove directories and/or files from the repository
   `svn delete mathlib`
   `svn commit -m "deleted mathlib"`
 - Use `mv` to move and/or rename files and directories
   `svn mv file1.c main.c`
   `svn commit -m "renamed file1.c to main.c"`
 - Use `revert` to reverse unwanted changes done to working copy files and/or directories
   `# Mistakenly edit file2.c` 
   `svn revert file2.c`
   `svn commit -m "Revert edit to file2.c"`
	 - Use `-R` to apply this to an entire directory or the entire project
	   `svn revert -R directory`
	   `svn revert -R .`
 - Revert a committed revision: do a reverse merge from the latest revision to an earlier one
   `svn merge -r 5:4 .` (reverse entire project from version 5 to 4)
   `svn commit -m "reverted to r4"`
	 - This creates a revision 6, identical to revision 4
 - Release tag from a working copy:
	 - Make sure the project is up to date (`svn update`)
	 - If not done already, create a `tags` subdirectory for the project in the repository
   `svn mkdir file:///home/alexste/repo/panther/tags -m "Created tags subdirectory"`
	 - Use `copy` to create a tagged version in the newly created subdirectory in the repository
   `svn copy . file:///home/alexste/repo/panther/tags/Rev1 -m "Created Rev1 tag"`
	 - Later you can use this tag to checkout this set of files
	`svn co file:///home/alexste/repo/panther/tags/Rev1 panther`
