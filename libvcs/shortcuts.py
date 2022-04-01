"""Shortcuts"""
from typing import Dict, Literal, Type, Union

from libvcs import GitRepo, MercurialRepo, SubversionRepo
from libvcs.exc import InvalidPipURL, InvalidVCS

#: Default VCS systems by string (in :data:`DEFAULT_VCS_CLASS_MAP`)
DEFAULT_VCS_LITERAL = Literal["git", "hg", "svn"]
#: Union of VCS Classes
DEFAULT_VCS_CLASS_UNION = Type[Union[GitRepo, MercurialRepo, SubversionRepo]]
#: String -> Class Map. ``DEFAULT_VCS_CLASS_MAP['git']`` -> :class:`~libvcs.git.GitRepo`
DEFAULT_VCS_CLASS_MAP: Dict[DEFAULT_VCS_LITERAL, DEFAULT_VCS_CLASS_UNION] = {
    "git": GitRepo,
    "svn": SubversionRepo,
    "hg": MercurialRepo,
}


def create_repo(
    url, vcs, progress_callback=None, *args, **kwargs
) -> Union[GitRepo, MercurialRepo, SubversionRepo]:
    r"""Return a object representation of a VCS repository.

    Examples
    --------
    >>> from libvcs.shortcuts import create_repo
    >>>
    >>> r = create_repo(
    ...     url='https://www.github.com/you/myrepo',
    ...     vcs='git',
    ...     repo_dir='/tmp/myrepo'
    ... )

    >>> r.update_repo()
    |myrepo| (git)  Repo directory for myrepo (git) does not exist @ \
        /tmp/myrepo
    |myrepo| (git)  Cloning.
    |myrepo| (git)  git clone https://www.github.com/tony/myrepo \
        /tmp/myrepo
    Cloning into '/tmp/myrepo'...
    Checking connectivity... done.
    |myrepo| (git)  git fetch
    |myrepo| (git)  git pull
    Already up-to-date.
    """
    if vcs == "git":
        return GitRepo(url, progress_callback=progress_callback, *args, **kwargs)
    elif vcs == "hg":
        return MercurialRepo(url, progress_callback=progress_callback, *args, **kwargs)
    elif vcs == "svn":
        return SubversionRepo(url, progress_callback=progress_callback, *args, **kwargs)
    else:
        raise InvalidVCS("VCS %s is not a valid VCS" % vcs)


def create_repo_from_pip_url(
    pip_url, **kwargs
) -> Union[GitRepo, MercurialRepo, SubversionRepo]:
    r"""Return a object representation of a VCS repository via pip-style url.

    Examples
    --------

    >>> from libvcs.shortcuts import create_repo_from_pip_url

    >>> r = create_repo_from_pip_url(
    ...         pip_url='git+https://www.github.com/you/myrepo',
    ...         repo_dir='/tmp/myrepo')

    >>> r.update_repo()
    |myrepo| (git)  Repo directory for myrepo (git) does not exist @ \
        /tmp/myrepo
    |myrepo| (git)  Cloning.
    |myrepo| (git)  git clone https://www.github.com/tony/myrepo \
        /tmp/myrepo
    Cloning into '/tmp/myrepo'...
    Checking connectivity... done.
    |myrepo| (git)  git fetch
    |myrepo| (git)  git pull
    Already up-to-date.
    """
    if pip_url.startswith("git+"):
        return GitRepo.from_pip_url(pip_url, **kwargs)
    elif pip_url.startswith("hg+"):
        return MercurialRepo.from_pip_url(pip_url, **kwargs)
    elif pip_url.startswith("svn+"):
        return SubversionRepo.from_pip_url(pip_url, **kwargs)
    else:
        raise InvalidPipURL(pip_url)


def create_repo_legacy(
    url, vcs, progress_callback=None, *args, **kwargs
) -> Union[GitRepo, MercurialRepo, SubversionRepo]:
    r"""Return a object representation of a VCS repository.

    Examples
    --------
    >>> from libvcs.shortcuts import create_repo_legacy
    >>>
    >>> r = create_repo_legacy(
    ...     url='https://www.github.com/you/myrepo',
    ...     vcs='git',
    ...     repo_dir='/tmp/myrepo'
    ... )

    >>> r.update_repo()
    |myrepo| (git)  Repo directory for myrepo (git) does not exist @ \
        /tmp/myrepo
    |myrepo| (git)  Cloning.
    |myrepo| (git)  git clone https://www.github.com/tony/myrepo \
        /tmp/myrepo
    Cloning into '/tmp/myrepo'...
    Checking connectivity... done.
    |myrepo| (git)  git fetch
    |myrepo| (git)  git pull
    Already up-to-date.
    """
    if vcs == "git":
        return GitRepo(url, progress_callback=progress_callback, *args, **kwargs)
    elif vcs == "hg":
        return MercurialRepo(url, progress_callback=progress_callback, *args, **kwargs)
    elif vcs == "svn":
        return SubversionRepo(url, progress_callback=progress_callback, *args, **kwargs)
    else:
        raise InvalidVCS("VCS %s is not a valid VCS" % vcs)
