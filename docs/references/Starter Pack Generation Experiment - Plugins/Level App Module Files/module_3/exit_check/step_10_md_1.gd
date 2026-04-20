extends SequenceEvent

func trigger():
	for part in get_frac_shape()._parts:
		use_highlight_tool(part, true)
	use_write_tool(get_frac_shape_part(0,0), "1")
	use_write_tool(get_frac_shape_part(0,1), "2")
	use_write_tool(get_frac_shape_part(0,2), "3")
