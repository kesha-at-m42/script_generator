extends SequenceEvent

func trigger():
	var part = get_frac_shape_part(0, 1)
	use_highlight_tool(part, true)
	use_write_tool(part, "2")
