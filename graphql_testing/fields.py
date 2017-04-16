# Python imports

# Core Django imports

# Third-Party imports

# Apps Imports


class Field(object):

	def __init__(self, value)
		self.value = self.to_internal_value(value)
	
	def to_string(self):
		return self.value

	def to_internal_value(self, value):
		raise NotImplementedError("")


class BooleanField(Field):

	def to_string(self):
		return str(self.value).lower()

	def to_internal_value(self, value):
		if isinstance(value, str):
			self.value = True if value == 'True' else False
		else:
			self.value = value


class StringField(Field):

	def to_internal_value(self, value):
		self.value = str(value)


class IntegerField(Field):

	def to_internal_value(self, value):
		self.value = str(value)


class UUIDField(Field):

	def to_internal_value(self, value):
		self.value = str(value)