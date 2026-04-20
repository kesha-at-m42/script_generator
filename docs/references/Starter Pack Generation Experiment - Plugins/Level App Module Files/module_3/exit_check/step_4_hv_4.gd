extends SequenceEvent

func trigger():
	clear_highlights(get_frac_shape(1))
	use_highlight_tool(get_frac_shape_part(2, 0), true)
