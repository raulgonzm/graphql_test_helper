# Python imports
from unittest import TestCase
# Core Django imports

# Third-Party imports

# Apps Imports
from mimercadona_api.core.graphql.test import GraphQLAPIHelper


class GraphQLAPIHelperTestCase(TestCase):

    def setUp(self):
        self.graphql_helper = GraphQLAPIHelper(node='miMercadona', fields=['id', 'name', 'email'])
        self.ok_query = '''{miMercadona{edges{node{id,name,email}}}}'''
        self.ok_query_with_lookups = '''{miMercadona(name:"mercadona"){edges{node{id,name,email}}}}'''

    def test_build_node_fields_list(self):
        self.assertEqual(self.graphql_helper._build_node_fields_list(), "id, name, email")

    def test_build_node_fields_list_empty_list(self):
        graphql_helper = GraphQLAPIHelper(node='miMercadona', fields=[])
        self.assertEqual(graphql_helper._build_node_fields_list(), "")

    def test_build_node_fields_list_only_one_field(self):
        graphql_helper = GraphQLAPIHelper(node='miMercadona', fields=['id', ])
        self.assertEqual(graphql_helper._build_node_fields_list(), "id")

    def test_build_graphql_query_with_lookups(self):
        graphql_helper = GraphQLAPIHelper(
            node='miMercadona',
            fields=['id', 'name', 'email'],
            filters='name: "mercadona"'
        )
        self.assertEqual(graphql_helper._build_graphql_query_with_lookups(), self.ok_query_with_lookups)

    def test_build_graphql_query_without_lookups(self):
        self.assertEqual(self.graphql_helper._build_graphql_query_without_lookups(), self.ok_query)

    def test_build_graphql_query(self):
        self.assertEqual(self.graphql_helper._build_graphql_query(), self.ok_query)

    def test_build_graphql_query_lookups(self):
        graphql_helper = GraphQLAPIHelper(
            node='miMercadona',
            fields=['id', 'name', 'email'],
            filters='name: "mercadona"'
        )
        self.assertEqual(graphql_helper._build_graphql_query(), self.ok_query_with_lookups)

    def test_get_body_query(self):
        body_query = self.graphql_helper.get_body_query()
        self.assertIn('query', body_query)
        self.assertIn('miMercadona', body_query)
        self.assertIn('edges', body_query)
        self.assertIn('node', body_query)
        self.assertIn('id', body_query)
        self.assertIn('name', body_query)
        self.assertIn('email', body_query)

