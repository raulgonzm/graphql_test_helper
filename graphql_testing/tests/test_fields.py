# Python imports
from unittest import TestCase
import os
import sys
import inspect
import uuid
# Core Django imports

# Third-Party imports

# Apps Imports
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)
from fields import *


class GraphQLAPIHelperFieldsTestCase(TestCase):

    def test_boolean_field_construct_method_from_boolean(self):
    	new_field = BooleanField(value=True)
    	self.assertTrue(new_field.value)
    	new_field = BooleanField(value=False)
    	self.assertFalse(new_field.value)

    def test_boolean_field_construct_method_from_str(self):
    	new_field = BooleanField(value="True")
    	self.assertTrue(new_field.value)
    	new_field = BooleanField(value="False")
    	self.assertFalse(new_field.value)

    def test_to_internal_value(self):
    	new_field = BooleanField(value=True)
    	new_field.to_internal_value(value=True)
    	self.assertTrue(new_field.value)
    	new_field = BooleanField(value=False)
    	new_field.to_internal_value(value=False)
    	self.assertFalse(new_field.value)
    	new_field = BooleanField(value="True")
    	new_field.to_internal_value(value="True")
    	self.assertTrue(new_field.value)
    	new_field = BooleanField(value="False")
    	new_field.to_internal_value(value="False")
    	self.assertFalse(new_field.value)

    def test_boolean_to_str(self):
    	new_field = BooleanField(value=True)
    	self.assertEqual(new_field.to_string(), "true")
    	new_field = BooleanField(value=False)
    	self.assertEqual(new_field.to_string(), "false")

    def test_string_field_to_string(self):
    	new_field = StringField(value='miMercadona')
    	self.assertEqual(new_field.to_string(), 'miMercadona')

    def test_string_field_to_internal_value(self):
    	new_field = StringField(value='miMercadona')
    	new_field.to_internal_value(value='miMercadona')
    	self.assertEqual(new_field.value, 'miMercadona')

    def test_integer_field_to_string(self):
    	new_field = IntegerField(value=1)
    	self.assertEqual(new_field.to_string(), "1")

    def test_integer_field_to_internal_value(self):
    	new_field = IntegerField(value=1)
    	new_field.to_internal_value(value=1)
    	self.assertEqual(new_field.to_string(), "1")

    def test_uuid_field_to_string(self):
    	new_field = UUIDField(value=uuid.uuid4())
    	self.assertIsInstance(new_field.to_string(), str)

    def test_uuid_field_to_internal_value(self):
    	new_field = UUIDField(value=uuid.uuid4())
    	new_field.to_internal_value(value=uuid.uuid4())
    	self.assertIsInstance(new_field.to_string(), str)

