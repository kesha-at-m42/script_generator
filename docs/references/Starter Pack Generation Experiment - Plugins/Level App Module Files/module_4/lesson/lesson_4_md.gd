extends SequenceEvent

func trigger() -> void:
	var line = get_number_line()
	clear_number_line_tick_highlights(line)
	use_highlight_tool(line.bar._parts[0], true)
	await delay(0.5)
	use_highlight_tool(line.bar._parts[0], false)
	use_highlight_tool(line._ticks[1], true)
	
