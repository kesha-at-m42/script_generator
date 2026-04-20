extends SequenceEvent

func trigger() -> void:
	var bars = get_frac_shapes()
	for bar in bars:
		clear_shaded(bar)
	for bar in bars:
		use_highlight_tool(bar._parts[0], true)
		await delay(1)
		use_highlight_tool(bar._parts[0], false)
