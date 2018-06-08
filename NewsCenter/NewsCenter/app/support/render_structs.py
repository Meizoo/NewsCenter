class RenderDeclared(object):
	def __init__(self, bool):
		if bool:
			self.message = 'Declared'
			self.button = 'Undeclare'
		else:
			self.message = 'Undeclared'
			self.button = 'Declare'

class RenderInterest(object):
	def __init__(self, bool):
		if bool:
			self.message = 'Interested'
			self.button = 'Not interesting'
		else:
			self.message = 'Not interested'
			self.button = 'Interesting'
