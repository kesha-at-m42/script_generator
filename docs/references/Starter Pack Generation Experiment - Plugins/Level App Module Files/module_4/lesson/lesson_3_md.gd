extends SequenceEvent

func trigger() -> void:
	var line = get_number_line()
	clear_number_line_tick_highlights(line)
	for tick in line._ticks:
		if tick.is_read_only:
			continue
		use_highlight_tool(tick, true)
		await delay(0.5)
		use_highlight_tool(tick, false)
	
