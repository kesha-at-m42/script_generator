extends SequenceEvent

func trigger():
	#style module 5 e 2 mr
	use_arrow_tool(get_num_line(0), Vector2i(0, 1), Vector2i(1, 4))
	await delay(1.5)
	extend_number_line_arrow(get_num_line(0), Vector2i(2, 4))
	await delay(1.5)
	extend_number_line_arrow(get_num_line(0), Vector2i(3, 4))
	await delay(1.5)
	extend_number_line_arrow(get_num_line(0), Vector2i(4, 4))
