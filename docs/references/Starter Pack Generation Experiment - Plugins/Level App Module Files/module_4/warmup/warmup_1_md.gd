extends SequenceEvent

func trigger() -> void:
	var bar = get_frac_shape()
	var line = get_number_line()
	clear_number_line_tick_highlights(line)
	for i in range(bar._parts.size()):
		use_write_tool(bar._parts[i], var_to_str(i+1))
		use_highlight_tool(bar._parts[i], true)
		await delay(0.25)
		if !line._ticks[i+1].is_read_only:
			use_highlight_tool(line._ticks[i+1], true)
		await delay(0.25)
		use_write_tool(bar._parts[i], "")
		use_highlight_tool(bar._parts[i], false)
		await delay(0.25)
		if !line._ticks[i+1].is_read_only:
			use_highlight_tool(line._ticks[i+1], false)
