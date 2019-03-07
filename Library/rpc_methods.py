from modernrpc.core import rpc_method

from Library.service import AuthorsService


@rpc_method
def get_authors():
    return AuthorsService.get_authors_brief()


@rpc_method
def get_author_by_id(id: int):
    return AuthorsService.get_author_by_id(id)


@rpc_method
def find_author_by_name(search_query: str):
    return AuthorsService.find_author_by_name(search_query)
