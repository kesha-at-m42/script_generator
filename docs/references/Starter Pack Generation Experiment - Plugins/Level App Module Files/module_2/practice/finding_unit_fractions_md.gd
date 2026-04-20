extends SequenceEvent

func trigger() -> void:
	var frac_bar = get_frac_shape(2)
	use_highlight_tool(frac_bar._parts[0], true)
	use_write_tool(frac_bar._parts[0], "1")
	await delay(1)
	use_highlight_tool(frac_bar._parts[1], true)
	use_write_tool(frac_bar._parts[1], "2")
