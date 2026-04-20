extends SequenceEvent

func trigger():
	use_highlight_tool(get_frac_shape_part(2, 2), true)
	use_select_tool(get_frac_shape(2))