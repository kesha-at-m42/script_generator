extends SequenceEvent

func trigger() -> void:
	var line = get_number_line()
	clear_number_line_ticks(line)
	use_place_tick_tool(line, 8)
	await delay(0.5)
	use_place_tick_tool(line, 4)
	use_place_tick_tool(line, 12)
	await delay(0.5)
	use_place_tick_tool(line, 2)
	use_place_tick_tool(line, 6)
	use_place_tick_tool(line, 10)
	use_place_tick_tool(line, 14)
