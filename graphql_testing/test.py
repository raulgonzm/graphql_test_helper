# Python imports
import json
# Core Django imports

# Third-Party imports

# Apps Imports


class GraphQLAPIHelper(object):

    def __init__(self, node, fields, filters=None):
        self.node = node
        self.fields = fields
        self.filters = filters

    def __clean_query(self):
        return self.query.replace("\n", "").replace(" ", "")

    def _build_node_fields_list(self):
        return ', '.join(map(str, self.fields))

    def _build_node_filter_list(self):
        return str({filter_key: filter.value for k, v in d.items()})

    def _build_graphql_query(self):
        if self.filters:
            return self._build_graphql_query_with_lookups()
        return self._build_graphql_query_without_lookups()

    def _build_graphql_query_without_lookups(self):
        self.query = '''{{
          {} {{
                edges {{
                    node {{
                        {}
                    }}
                }}
            }}
        }}'''.format(self.node, self._build_node_fields_list())
        return self.__clean_query()

    def _build_graphql_query_with_lookups(self):
        self.query = '''{{
                  {}({}) {{
                        edges {{
                            node {{
                                {}
                            }}
                        }}
                    }}
                }}'''.format(self.node, self.filters, self._build_node_fields_list())
        return self.__clean_query()

    def get_body_query(self):
        return json.dumps({'query': self._build_graphql_query()})