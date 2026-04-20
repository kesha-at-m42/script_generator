extends SequenceEvent

func trigger():
	use_arrow_tool(get_num_line(0), Vector2i(0, 1), Vector2i(1, 3))
	await delay(1)
	use_arrow_tool(get_num_line(0), Vector2i(1, 3), Vector2i(2, 3))
	set_number_line_arrow_label(get_num_line(0), "2", 1)
	await delay(1)
	use_arrow_tool(get_num_line(0), Vector2i(2, 3), Vector2i(3, 3))
	set_number_line_arrow_label(get_num_line(0), "3", 2)
