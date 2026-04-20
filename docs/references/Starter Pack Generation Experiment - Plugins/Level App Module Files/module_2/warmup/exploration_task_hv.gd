extends SequenceEvent

func trigger() -> void:
	var bars = get_frac_shapes()
	for bar in bars:
		clear_shaded(bar)
	for bar in bars:
		use_paint_tool(bar._parts[0])
		await delay(1.25)
