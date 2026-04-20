extends SequenceEvent

func trigger() -> void:
	var bar = get_frac_shape()
	clear_shaded(bar)
	use_highlight_tool(bar._parts[0], true)
	await delay(1)
	use_highlight_tool(bar._parts[0], false)
