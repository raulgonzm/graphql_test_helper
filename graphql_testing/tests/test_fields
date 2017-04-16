# Python imports
from unittest import TestCase
# Core Django imports

# Third-Party imports

# Apps Imports


class GraphQLAPIHelperFieldsTestCase(TestCase):

    def test_boolean_field_construct_method_from_boolean(self):
    	new_field = Field(value=True)
    	self.assertTrue(new_field.value)
    	new_field = Field(value=False)
    	self.assertFalse(new_field.value)

    def test_boolean_field_construct_method_from_str(self):
    	new_field = Field(value="True")
    	self.assertTrue(new_field.value)
    	new_field = Field(value="False")
    	self.assertFalse(new_field.value)

    def test_to_internal_value(self):
    	new_field = Field(value=True).to_internal_value(value=True)
    	self.assertTrue(new_field.value)
    	new_field = Field(value=False).to_internal_value(value=False)
    	self.assertFalse(new_field.value)
    	new_field = Field(value="True").to_internal_value(value="True")
    	self.assertTrue(new_field.value)
    	new_field = Field(value="False").to_internal_value(value="False")
    	self.assertFalse(new_field.value)

    def test_boolean_to_str(self):
    	new_field = Field(value=True)
    	self.assertEqual(new_field.to_string(), "true")
    	new_field = Field(value=False)
    	self.assertEqual(new_field.to_string(), "false")
