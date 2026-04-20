extends SequenceEvent

func trigger():
	use_place_tool(get_num_line(0), 1, 4)
	await delay(1)
	use_place_tool(get_num_line(0), 3, 4)
