extends SequenceEvent

func trigger():
	var part := get_frac_shape_part()
	use_highlight_tool(part, true)
	use_write_tool(part, "1")
