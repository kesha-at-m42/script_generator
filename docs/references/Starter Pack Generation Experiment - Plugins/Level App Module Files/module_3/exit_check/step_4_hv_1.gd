extends SequenceEvent

func trigger():
	clear_selected()
	use_highlight_tool(get_frac_shape_part(0, 0), true)
