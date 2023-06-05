def displayed_msgs(list_of_messages_to_be_displayed, list_of_messages_that_were_displayed):
	"""Display messages and move them to another list"""
	while list_of_messages_to_be_displayed:
		msg_on_display = list_of_messages_to_be_displayed.pop()
		print(f"Current Message: '{msg_on_display}'")
		list_of_messages_that_were_displayed.append(msg_on_display)

various_msgs = [
				'this is message 1',
				'this is message 2',
				'this is message 3'
]
sent_msgs = []

displayed_msgs(various_msgs[:], sent_msgs)
print(various_msgs)
print(sent_msgs)

displayed_msgs(various_msgs, sent_msgs)
print(various_msgs)
print(sent_msgs)