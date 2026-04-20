extends SequenceEvent

func trigger():
	use_place_tool(get_num_line(), 1, 4)
	await delay(0.8)
	use_place_tool(get_num_line(), 3, 4)
