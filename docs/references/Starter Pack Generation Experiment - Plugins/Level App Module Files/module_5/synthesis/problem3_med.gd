extends SequenceEvent

func trigger():
	var number_lines = get_num_lines()
	for line in number_lines:
		remove_number_line_points(line)
	use_arrow_tool(number_lines[0], Vector2i(0, 1), Vector2i(1, 3))
	await delay(1)
	use_arrow_tool(number_lines[0], Vector2i(1, 3), Vector2i(2, 3))
	set_number_line_arrow_label(number_lines[0], "2", 1)
	await delay(1)
	use_arrow_tool(number_lines[1], Vector2i(2, 3), Vector2i(3, 3))
	set_number_line_arrow_label(number_lines[0], "3", 2)
	await delay(1)
	use_arrow_tool(number_lines[1], Vector2i(0, 1), Vector2i(1, 4))
	await delay(1)
	use_arrow_tool(number_lines[1], Vector2i(1, 4), Vector2i(2, 4))
	set_number_line_arrow_label(number_lines[1], "2", 1)
	await delay(1)
	use_arrow_tool(number_lines[1], Vector2i(2, 4), Vector2i(3, 4))
	set_number_line_arrow_label(number_lines[1], "3", 2)
	await delay(1)
	use_arrow_tool(number_lines[1], Vector2i(3, 4), Vector2i(4, 4))
	set_number_line_arrow_label(number_lines[1], "4", 3)