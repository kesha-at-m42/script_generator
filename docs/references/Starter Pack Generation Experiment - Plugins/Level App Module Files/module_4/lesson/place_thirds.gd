extends SequenceEvent

func trigger() -> void:
	var line = get_number_line()
	use_place_tick_tool(line, 1)
	await delay(0.5)
	use_place_tick_tool(line, 2)
