extends SequenceEvent

func trigger():
	clear_highlights(get_frac_shape(0))
	use_highlight_tool(get_frac_shape_part(1, 0), true)
