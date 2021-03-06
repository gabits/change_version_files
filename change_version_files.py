class VersionFileEditor:
    """Opens all __init__.py files in a defined set of paths that contain a controlled version and bulk
    edits their version number according to user's input.
    """

    paths = [('Sample Core System', 'path/to/folder'),
            ('Sample App', 'path/to/folder'),
            ('Sample Website', 'path/to/folder')]

    def _open_file(self, path, mode):
        """Private method that returns the content of a file according to the path provided.
        This method doesn't close files, so whenever used would require a .close() method call after.
        """
        file_path = "{}/__init__.py".format(path)
        file = open(file_path, mode)
        return file

    def get_current_versions(self):
        """Rtetrieves the current version running on each one of the websites.
        """
        print("\n\n\nCurrent version for each website is: \n\n")
        for website, path in self.paths:
            with self._open_file(path, 'r') as file:
                version = file.readline()[13:]         # All content after "__version__ = " in the file
                print("{}: {}".format(website, version))

    def _change_file_name(self, file, new_version):
        """Private method to changes each file's name individually and it's called inside a loop by
        change_all_version_files().
        """
        changed_line = "__version__ = '{}'".format(new_version)
        file.write(changed_line)
        file.write("\n")            # Guarantees an empty line at the end of the file
        file.close()

    def change_all_version_files(self):
        """"Bulk edits all version files according to the paths declared in the self.paths dictionary.
        """"
        new_version = input("\n\nType new version number: ")
        for website, path in self.paths:
            with self._open_file(path, 'w') as file:
                self._change_file_name(file, new_version)


if __name__ == '__main__':
    """This is only ran if the script is directly called from the command line by its file name.
    It first displays all current versions of the websites/apps, then prompts user for the new version number, and at
    last it'll print back to the console the current version files numbers (which should be updated according to
    provided input).
    """
    VersionFileEditor().get_current_versions()
    VersionFileEditor().change_all_version_files()
    VersionFileEditor().get_current_versions()
