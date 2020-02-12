import logging

COLLECTION_QUALIFIED_INDEX_NAME_MAX_LENGTH = 63


def fully_qualified_name(collection_name, index_name):
    return "{}${}".format(collection_name, index_name)


def length_ok(collection_name, index_name):
    return len(fully_qualified_name(collection_name, index_name)) <= COLLECTION_QUALIFIED_INDEX_NAME_MAX_LENGTH


def shorten_if_exceeds(collection_name, index_name):
    if length_ok(collection_name, index_name):
        return index_name

    return shorten(index_name)


def shorten(index_name):
    if len(index_name) <= 16:
        return index_name

    return index_name[0:4] + str(hash(index_name))[0:12]
