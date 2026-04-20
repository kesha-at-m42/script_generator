extends SequenceEvent

func trigger():
	for part in get_frac_shape_parts(1, [0,2,3]):
		use_highlight_tool(part, true)