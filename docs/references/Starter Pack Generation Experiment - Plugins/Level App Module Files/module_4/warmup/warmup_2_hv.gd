extends SequenceEvent

func trigger() -> void:
	var line = get_number_line()
	clear_number_line_ticks(line)
	use_place_tick_tool(line, 2)
