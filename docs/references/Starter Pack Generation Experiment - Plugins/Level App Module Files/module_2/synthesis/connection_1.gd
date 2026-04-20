extends SequenceEvent

func trigger() -> void:
	for frac_bar in get_frac_shapes():
		use_highlight_tool(frac_bar._parts[0], true)
		await delay(1)
