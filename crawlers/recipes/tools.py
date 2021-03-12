import os


def get_filepath(path_from_module: str, file_name: str) -> str:
    """
    We use this method to find the files that in many cases we need but are not visible.
    :param path_from_module: string, required
    -The path from the central repo to the folder we want.
    :param file_name: string, required
    -The file we want from the folder.
    :return: The actual path to file
    """
    fn = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__))).split('src')[0]
    return '{0}/{1}/{2}'.format(fn, path_from_module, file_name)


def get_folder_path(path_from_module: str) -> str:
    """
    We use this method to find the folders that in many cases we need but are not visible.
    :param path_from_module: string, required
    -The path from the central repo to the folder we want.
    :return: string
    -The actual path to folder
    """
    fn = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__))).split('src')[0]
    return '{0}/{1}/'.format(fn, path_from_module)
