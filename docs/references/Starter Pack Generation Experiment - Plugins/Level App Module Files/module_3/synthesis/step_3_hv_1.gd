extends SequenceEvent

func trigger():
	for part in get_frac_shape_parts(0, [0,1,2]):
		use_highlight_tool(part, true)