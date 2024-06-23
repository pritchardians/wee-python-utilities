import os
import logging


def get_project_root(project_name: str) -> str:
    """
    Get the path of the project root, to use in relative path processing
    :param project_name: Name of the current project
    :return: Project root path
    :rtype: str
    """
    # Create a list of the path nodes i the current working directory
    full_path_list: list[str] = os.getcwd().split(os.sep)
    # Get all the path nodes from the list up to the project path, and join is by the os. sep
    # (probably \ or / depending on whether you are running on Unix or Windows)
    try:
        project_root = os.sep.join(os.getcwd().split(os.sep)[:full_path_list.index(project_name) + 1:])
        logging.info(f"Project root path: {project_root}")
        print(f"Project root path: {project_root}")
        return project_root
    except ValueError:
        err_mess: str = "Incorrect project name sent to get_project_root function. "
        err_mess += f"Argument given was {project_name}"
        logging.error(err_mess)
        # Print error to stdout in case logging ot yet set
        print(err_mess)
        raise ValueError(err_mess)


if __name__ == '__main__':
    print(get_project_root("find-best-match"))
