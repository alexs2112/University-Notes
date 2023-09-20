### Secure Shell
 - A cryptographic network protocol for operating network services securely over an unsecured network

### Operating System
 - Collection of software that directs a computer's operations, including:
	 - Controlling and scheduling the execution of other programs
	 - Managing storage, input/output, communications
 - Facilitates sharing resources among a set of users
 - Provides access control mechanisms
	 - Authorization requires identification and authentication

### Unix users and superusers
 - Each user has a username (UID), group name (GID), password
 - `root` is an administrator/superuser (UID 0)
	 - Can read or write any file or system resource
	 - Can modify the operating system
	 - Can become any other user
		 - Execute commands on behalf of any users' ID
	 - Cannot read other users passwords as they aren't stored directly on the machine
		 - Root can change any user's password
 - `SUDO`: a Unix program that allows users to run programs with the privileges of another user (by default, the superuser)
	 - *s*uper*u*ser *do*
	 - Not to be confused with `su`
		 - `su` requires root password, `sudo` can be invoked with non-root password
	 - Sudoers are specified in `/etc/sudoers`
		 - Formatted as follows:
		 - `<username> <machine name>=(<user>:<group>) <command>`
		 - `root ALL=(ALL:ALL) ALL`
			 - Root can use sudo, on ALL hosts, to run ALL commands, as ALL users (and ALL groups)
		 - `alex localhost=(bob) cat dog`
			 - Alex can use sudo, on localhost, to run cat or dog as user bob
	 - Run `[/usr/bin/]visudo`, must be run as root

### Unix access control
 - **Everything is a file, everything**
	 - Files are laid out in a tree
	 - Each file associated with an inode data structure
 - inode holds information about the file
	 - UID and GID of the file owner
	 - Type, size, physical location on disk
	 - Time of last access (atime), last inode modification (ctime), last file content modification (mtime)
	 - Permission bits
	 - ...
 - `<filetype><owner><group><everyone> <# of hard links> <owner> <group> <size> <mtime> <filename>`
 - `-rw-r--r-- 1 alexander.stevenson cpsc525 3771 Apr  4  2018 .bashrc `
 - Filetypes:
	 - `-` regular
	 - `d` directory
	 - `b` block device
	 - `c` character file
	 - `l` symbolic link
	 - `p` pipe
	 - `s` socket
 - Permission bits:
	 - `r` read
	 - `w` write
	 - `x` execute (directories: traverse)
	 - `s` setuid, setgid (directories: files have gid of dir owner)
	 - `t` sticky bit (directories: make append only)
 - setuid/setgid/sticky bit
	 - First octet
	 - 4 (100; s) means setuid
	 - 2 (010; s) means setgid
	 - 1 (001; t) means sticky
	 - `-rwsr-sr-x`
	 - `-rwsr-xr-x 1 root root 68208 Nov 29  2022 /usr/bin/passwd`
	 - First s = setuid as owner (if owned by root, will think youre root and **runs as root**)
	 - Second s = setgid as group (will think your group is the group of this file)

### Security Mechanisms
 - `setuid` allows a system process to run with different privileges than the user who runs it
	 - Enables controlled access to system resources
	 - Each process has three user IDs
		 - real UID (`ruid`): What user started the program
		 - effective UID (`euid`): Which user determines access right
		 - saved UID (`suid`): Used to swap IDs, gaining or losing privileges
	 - `setuid` makes program run with the euid of the owner
 - Can exploit setuid-root programs to obtain root privileges
**Dropping and Acquiring Privileges**:
 - To acquire privileges, assign euid to be a privileged UID
 - To drop privileges temporarily, remove privileged UID from euid and save it in suid
	 - Can restore later from suid
 - To drop privileges permanently, remove privileged UID from both euid and suid
 - `setuid(newuid)`:
	 - if process has appropriate privileges, this will set the euid, ruid, suid all to newuid
	 - Otherwise, if newuid is same as ruid or suid, save euid to suid and then set euid to newuid
**Other Commands**:
 - `chown`: Change file owner (and group ownership)
	 - Usage: `sudo chwon user[:groupname] /path/to/file`
 - `chgrp`: Change file group ownership
	 - Usage: `[sudo] chgrp groupname /path/to/file`
 - `chmod`: Change permissions on a file
	 - Usage: `[sudo] chmod <mode> /path/to/file`
 - `umask`: View or set file create mask
	 - umask specifies which permission bits *not* to set in new files
 - `chroot` confines a user process to a portion of the filesystem by `ch`anging the apparent `root` inode
	 - Originally used to test system code safely
	 - Confines code to a limited portion of the filesystem
	 - Often used for guest accounts
