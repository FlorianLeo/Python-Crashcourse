import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
	"""Test for the class AnonymousSurvey"""
	def test_store_single_response(self):
		"""Test that a single response is stored properly"""
		question = "What language did you first learn to speak?"
		my_survey = AnonymousSurvey(question)
		my_survey.store_response('English')
		self.assertIn('English', my_survey.responses)

	def test_store_three_responses(self):
		"""Test that thre individual responses are stored porperly."""
		question = "What language did you first learn to speak?"
		my_survey = AnonymousSurvey(question)
		responses = ['English', 'Spanish', 'Mandarin']
		for element in responses:
			my_survey.store_response(element)
		for element in responses:
			self.assertIn(element, my_survey.responses)

if __name__ == '__main__':
	unittest.main()